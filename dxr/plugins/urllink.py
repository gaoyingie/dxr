import re

import dxr.indexers
from dxr.lines import Ref
from dxr.menus import SingleDatumMenuMaker


# From http://stackoverflow.com/a/1547940
url_re = re.compile("https?://[A-Za-z0-9\-\._~:\/\?#[\]@!\$&'()*\+,;=%]+\.[A-Za-z0-9\-\._~:\/\?#[\]@!\$&'()*\+,;=%]+")


class FileToIndex(dxr.indexers.FileToIndex):
    def refs(self):
        for m in url_re.finditer(self.contents):
            url = m.group(0)
            yield m.start(0), m.end(0), Ref([UrlMenuMaker(self.tree, url)])


class UrlMenuMaker(SingleDatumMenuMaker):
    plugin = 'urllink'

    def menu_items(self):
        yield {'html': 'Follow link',
               'title': 'Visit %s' % self.data,
               'href': self.data,
               'icon': 'external_link'}
