# -*- coding: utf-8 -*-
from zope.interface import implements

from elementtree.ElementTree import XML, tostring, Element

from htmllaundry import sanitize

from Products.PortalTransforms.interfaces import itransform
try:
    from Products.PortalTransforms.interfaces import ITransform
    HAS_PLONE3 = False
except ImportError:
    from Products.PortalTransforms.z3.interfaces import ITransform
    HAS_PLONE3 = True


class KML_to_HTML():
    """Transform which converts from KML to HTML"""

    if HAS_PLONE3:
        __implements__ = itransform
    else:
        implements(ITransform)

    __name__ = "kml_to_html"
    inputs   = ("application/vnd.google-earth.kml+xml",)
    output   = "text/html"

    def __init__(self,name=None):
        if name:
            self.__name__=name

    def name(self):
        return self.__name__

    def convert(self, data, cache, **kwargs):
        bodydom = Element('div')
        kmldom = XML(data)
        ns = kmldom.tag.strip('kml')
        placemarks = kmldom.findall('.//%sPlacemark' % ns)
        for placemark in placemarks:
            titles = placemark.findall(ns + 'name')
            for title in titles:
                t = Element('h2')
                t.text = title.text
                bodydom.append(t)

            descriptions = placemark.findall(ns+'description')
            for desc in descriptions:
                if desc.text:
                    text = sanitize(desc.text.strip())
                    d = XML('<div>' + text + '</div>')
                    bodydom.append(d)

        body = tostring(bodydom)
        cache.setData(body)
        return cache

def register():
    return KML_to_HTML()
