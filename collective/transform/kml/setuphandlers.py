# -*- coding: utf-8 -*-
import logging
from zope.app.component.hooks import getSite
from Products.CMFCore.utils import getToolByName

TRANSFORMS = [
  "kml_to_html",
  "kmz_to_html",
]

MIMETYPES = [
    {'name': 'application/vnd.google-earth.kml+xml',
    'extensions': ('kml',),
    'globs': ('*.kml',),
    'icon_path': 'text.png',
    'binary': True,
    'mimetypes': ('application/vnd.google-earth.kml+xml',)},
    {'name': 'application/vnd.google-earth.kmz',
    'extensions': ('kmz',),
    'globs': ('*.kmz',),
    'icon_path': 'text.png',
    'binary': True,
    'mimetypes': ('application/vnd.google-earth.kmz',)},
    {'name': 'application/gpx+xml',
    'extensions': ('gpx',),
    'globs': ('*.gpx',),
    'icon_path': 'text.png',
    'binary': True,
    'mimetypes': ('application/gpx+xml',)}
]


def add_mimetypes(context, logger=None):
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger('collective.transform.kml')
    portal = getSite()
    mimetypes_registry = getToolByName(portal, 'mimetypes_registry')
    all_mimetypes = mimetypes_registry.list_mimetypes()

    for mtype in MIMETYPES:
        if mtype['name'] not in all_mimetypes:
            logger.info('Registering mimetype %s' % mtype['name'])
            mimetypes_registry.register(MimeTypeItem(**mtype))


def uninstallTransform(portal):
    """Uninstall kml to html transform"""
    transforms = getToolByName(portal, 'portal_transforms')
    for transform in TRANSFORMS:
        transforms.unregisterTransform(transform)



def installTransform(portal, logger=None):
    """Install kml to html transforms"""
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger('collective.transform.kml')
    transforms = getToolByName(portal, 'portal_transforms')
    for transform in TRANSFORMS:
        if transform not in transforms.objectIds():
            transforms.manage_addTransform(
                transform,
                'collective.transform.kml.%s' % transform
            )
            logger.info("installed %s transform" % transform)

def importVarious(context):
    """Various import step code"""
    logger = logging.getLogger('collective.transform.kml')
    marker_file = 'collective.transform.kml.txt'
    if context.readDataFile(marker_file) is None:
        return
    portal = context.getSite()
    add_mimetypes(portal, logger)
    installTransform(portal, logger)
    logger.info('installed collective.transform.kml')
