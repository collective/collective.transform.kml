# -*- coding: utf-8 -*-
from zope.interface import implements
import tempfile
import zipfile

from Products.PortalTransforms.interfaces import itransform
try:
    from Products.PortalTransforms.interfaces import ITransform
    HAS_PLONE3 = False
except ImportError:
    from Products.PortalTransforms.z3.interfaces import ITransform
    HAS_PLONE3 = True

import kml_to_html


class KMZ_to_HTML():
    """Transform which converts from KML to HTML"""

    if HAS_PLONE3:
        __implements__ = itransform
    else:
        implements(ITransform)

    __name__ = "kmz_to_html"
    inputs   = ("application/vnd.google-earth.kmz",)
    output   = "text/html"

    def __init__(self,name=None):
        if name:
            self.__name__=name

    def name(self):
        return self.__name__

    def convert(self, data, cache, **kwargs):
        tmp = tempfile.NamedTemporaryFile()
        tmp.file.write(data)
        tmp.file.flush()
        text = u''
        if zipfile.is_zipfile(tmp.name):
            tmpzip = zipfile.ZipFile(tmp.file)
            for zi in tmpzip.infolist():
                if zi.filename.endswith('.kml'):
                    tz = tmpzip.open(zi)
                    id = tz.name
                    text = tz.read().decode('utf-8', 'replace')
                    transform = kml_to_html.KML_to_HTML()
                    cache = transform.convert(text, cache, **kwargs)
                    tz.close()
                    break
        tmp.close()
        return cache



def register():
    return KMZ_to_HTML()
