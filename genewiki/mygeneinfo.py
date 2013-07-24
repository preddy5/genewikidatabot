
'''
Created on Apr 10, 2013

@author: pradyumna
'''
import urllib,json
from proteinbox import ProteinBox
from pygenewiki.exceptions import *
import uniprot
#imported from settings.py
base_url = "http://mygene.info/gene/"

def getJson(url):
    ufile = None
    try:
        ufile = urllib.urlopen(url)
        contents = ufile.read()
        if not isinstance(contents, unicode):
            contents = contents.decode('utf-8')
        return json.loads(contents)
    except ValueError as e:
        raise GeneDataNotFound("Gene Data Not found")
    except IOError as e:
        print("Network error: are you connected to the internet?")
        raise NoNetworkError('Unable to reach network')
        
def _queryUniprot(entrez):
    return uniprot.uniprotAccForEntrezId(entrez)        
        
def get(json, key):
    result = u''
    if isinstance(json, dict):
        result = json[key] if key in json else u''
    elif isinstance(json, list):
        result = get(json[0], key) if (len(json)>0) else u''
    elif isinstance(json, unicode):
        result = json
    elif isinstance(json, str):
        result = json.decode('utf8')
    return result

def findReviewedUniprotEntry(entries, entrez):
    if not isinstance(entries, dict) and not entrez:
        return u''
    elif entrez:
        return _queryUniprot(entrez)

    if 'Swiss-Prot' in entries:
        entry = entries['Swiss-Prot']
    else:
        entry = entries['TrEMBL']

    if isinstance(entry, list):
        for acc in entry: 
            if uniprot.isReviewed(acc): return acc
        # if no reviewed entries, check Uniprot directly
        canonical = _queryUniprot(entrez)
        if canonical: return canonical
        else: return entry[0] 
    else: 
        canonical = _queryUniprot(entrez)
        if canonical: return canonical
        else: return entry 
        
def get_title(entrez):
    annotation = getJson(base_url+str(entrez))
    return get(annotation,'name')

def get_claims(annotation):
    claims = {}
    claims['p351'] = str(get(annotation,'entrezgene'))
    uniprot = findReviewedUniprotEntry(get(annotation, 'uniprot'), claims['p351'])
    claims['p352'] = uniprot
    claims['p353'] = get(annotation,'symbol')
    claims['p354'] = get(annotation,'HGNC')
    return claims

def parse_json(entrez):
    annotation = getJson(base_url+str(entrez))
    mygene = ProteinBox()
    mygene.setField('description',get(annotation,'summary').split('.')[0])
    mygene.setField('claims',get_claims(annotation))
    return mygene

def parse(entrez):
    return parse_json(entrez)
