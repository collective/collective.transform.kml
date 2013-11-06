Introduction
============

Transform KMZ and KML to HTML. It extracts the name and descrition from
the placemarks and constructs a simple html document from this.

Installation
============

Add ``collective.transform.kml`` to the list of eggs to install, e.g.:

::

    [buildout]
    ...
    eggs =
        ...
        collective.transform.kml

Re-run buildout, e.g. with:

::

    $ ./bin/buildout
