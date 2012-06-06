# -*- coding: utf-8 -*-
import logging
from Products.CMFCore.utils import getToolByName

TRANSFORMS = [
  "kml_to_html"
]


def installTransform(portal, logger=None):
    """Install ppt to html and excel to html transforms"""
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
    installTransform(portal, logger)
    logger.info('installed collective.transform.kml')
