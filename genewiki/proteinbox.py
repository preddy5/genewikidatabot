'''
Created on Apr 12, 2013

@author: pradyumna
'''


class ProteinBox(object):
    dicts = [ 'aliases',
              'claims',
              'description',
              'label',
              'links' ]
    def __init__(self):
        self.fieldsdict = {}
        for i in self.dicts:
            self.fieldsdict[i] = {}

    def setField(self,field_name,field_value,value = 'en'):
        fieldsdict = self.fieldsdict
        if field_name in self.dicts:
            if isinstance(field_value,dict):
                fieldsdict[field_name] = field_value
            elif isinstance(field_value,str):
                fieldsdict[field_name][value] = field_value
            elif isinstance(field_value,unicode):
                fieldsdict[field_name][value] = field_value.encode('utf8')
        else:
            raise NameError("Specified field does not exist")
        self.fieldsdict = fieldsdict
        return fieldsdict
    
    def UpdateWith(self,target):
        src = self.fieldsdict
        tgt = target.fieldsdict
        new = ProteinBox()
        for key in tgt:
            for value in tgt[key]:
                if src[key].has_key(value):
                    if src[key][value] != tgt[key][value]:
                        new.setField(key, tgt[key][value],value)
                else:
                    try:
                        new.setField(key, tgt[key][value],value)
                    except Exception:
                        #update logger
                        pass
        return new
