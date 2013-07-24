'''
Created on Apr 15, 2013

@author: pradyumna
'''

import pywikibot
from proteinbox import ProteinBox
from exceptions import ParseError
def prase_property(info):
    if info[2] == 'string':
        return info[3]
    elif info[2] == 'wikibase-entityid':
        return 'q'+str(info[3]['numeric-id'])
    else:
        raise ParseError('Property value is not String on ITEM')
    
def _claims(json):
    result = {}
    for prop in json:
        _property = 'p'+str(prop['m'][1])
        result[_property] = prase_property(prop['m'])
    return result
    
def parse_json(json):
    box = ProteinBox()
    for i in box.fieldsdict:
        if i == 'claims':
            box.setField(i,_claims(json[i]))
        else:
            box.setField(i,json[i])
    return box

def parse(data):
    return parse_json(data.get())
