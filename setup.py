from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.transform.kml',
      version=version,
      description="Transform KML to HTML",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Programming Language :: Python",
        "Topic :: Text Processing"
        ],
      keywords='',
      author='Christian Ledermann',
      author_email='christian.ledermann@gmail.com',
      url='https://github.com/collective/collective.transform.kml',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.transform'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'htmllaundry',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
