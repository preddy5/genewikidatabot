
class GeneWikiError(Exception):
    """Base class for exceptions raised by PBB"""
    
    
class ProteinBoxBotError(GeneWikiError):
    """Exception for ProteinBoxBot errors."""
    def __init__(self,message = None,code = None):
        self.message = message
        self.code = code
        if self.code:
            message = '[%s] %s'%(self.code,self.message)
        super(GeneWikiError,self).__init__(message)


class GeneDataNotFound(GeneWikiError):
    """Exception for data not found"""
    def __init__(self,message = None):
        super(GeneWikiError,self).__init__(message)

class NoNetworkError(GeneWikiError):
    """Exception for GeneWiki errors specifically related to network."""
    def __init__(self,message = None):
        super(GeneWikiError,self).__init__(message)
        
class ParseError(GeneWikiError):
    """Exception for GeneWiki errors specifically related to parsing."""
    def __init__(self,message = None):
        super(GeneWikiError,self).__init__(message)
    
