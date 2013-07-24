from genewiki import mygeneinfo
from json import loads
import urllib
import pytest
requires_network = pytest.mark.requires_network

class TestMyGeneInfoParser:
    '''JSON info may be in an unexpected format or may be missing. These 
    tests should cover the possibility that the element we want is not there,
    or that it may be part of a list or dictionary.'''

    @requires_network
    def test_getJson(self):
        '''Checks that we can retrieve and parse a JSON document successfully.
        Also does a sanity check on mygene.info's available species.
        '''

        metadata =  mygeneinfo.getJson("http://mygene.info/metadata")
        assert 'human' in metadata['AVAILABLE_SPECIES']
        assert 'mouse' in metadata['AVAILABLE_SPECIES']
        
	@requires_network
    def test_get_title(self):
		title = mygeneinfo.get_title(5649)
		assert title = 'reelin'
