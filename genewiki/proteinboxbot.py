'''
Created on Apr 7, 2013

@author: pradyumna
'''

import pywikibot
import mygeneinfo,wikidata 
from pygenewiki.exceptions import *
class ProteinBoxBot(object):
    """
    Present bot is still in experimental stage it will only create 
    a wikidata page if particular Gene doesnt have a wikidata page
    """
    # imported from settings.py
    site = pywikibot.Site("en","wikipedia")
    
    def update(self,page,entrez):
        data = pywikibot.DataPage(page)
        def check():
            if not data.exists():
                data.createitem(u"%s page has been created"% (page.title()))
                # updating logger
        check()
        annotations = mygeneinfo.parse(entrez)
        wiki = wikidata.parse(data)
        return wiki.UpdateWith(annotations)
        #
        #updating gene annotations with mygene.info data
        #
        
    def _description(self,page,lang,desc):
        data = pywikibot.DataPage(page)
        if data.exists():
            #pywikibot.output(data)
            data.setitem(summary=u"ProteinBoxBot Update",items={'type': u'description', 'language': lang, 'value': desc.split('.')[0]})
        #updating logger
        else:
            pass
	def _claims(self,page,property,value):
        data = pywikibot.DataPage(page)
        if data.exists():
            import urllib2
            main_url = r'http://www.wikidata.org/w/api.php?action=wbgetclaims&entity={0}&format=json'
            create_url = r'http://www.wikidata.org/w/api.php?action=wbcreateclaim&entity={0}&property={1}&snaktype=value&value=%22{2}%22&token=foobar'
            update_url = r'http://www.wikidata.org/w/api.php?action=wbsetclaimvalue&claim={0}&snaktype=value&value=%22{1}%22&token=foobar'
            content_json = getJson(main_url.format(str(data.title())))
            if property in content_json['claims']:
                pywikibot.output('Updating {0}'.format(data.title()))
                urllib2.urlopen(update_url.format(content_json['claims'][property][0]['id'],value))
            else:
                pywikibot.output('Updating {0}'.format(data.title()))
                urllib2.urlopen(create_url.format(str(data.title()),property,value))
        else:
            pass

        
    def run(self,run_only=None, skip=[], verbose=True, debug=True):
        
        def run_only_generator():
            for page in run_only:
                title = (mygeneinfo.get_title(page) 
                        if isinstance(page, int) else page)
                yield {'page':pywikibot.Page(self.site ,title),'entrez':page}
                
        source = (self.genewiki.infoboxes 
                  if not run_only else run_only_generator)
        
        for gene in source():
            if debug:
                if verbose:
                    pywikibot.output(u"Updating %s" % (gene['page'].title()))
            try:
                update = self.update(gene['page'],gene['entrez'])
                #print update.fieldsdict
            except Exception as err:
                pass
                #print err
                # updating logger
            #updating wikidata database
            try:
                dic = update.fieldsdict #dic contains the data that is to be updated 
                for field in dic:
                    for lang in dic[field]:
                        eval('self._'+field+"(gene['page'],lang,dic[field][lang])")
                        
            except Exception as err:
                #updating logger
                ProteinBoxBotError(err.message)
                #print err
		#updating logger
                pass
            
                
                
                
                
