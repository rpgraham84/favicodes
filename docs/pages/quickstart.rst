==========
Quickstart
==========

Making simple favicons with Favicodes is designed to be extremely straightforward. The
service is hosted on Google App Engine and is available at http://favi.codes.


First do no harm
================

The simplest favicode of all is one made from no Unicode at all. You may want a blank,
transparent favicon as your default (instead of the dog-eared-page icon that seems to
be the default for sites without a favicon). That's easy:

.. code-block::

    http://favi.codes

This will return a transparent, 256x256 PNG.

.. image:: https://favi.codes/

You cant see it, but its just above this sentence. 


How to make a Favicode
======================

Maybe you just want a simple letter or two. (No more than 2 glyphs are allowed 
because the letters look too cramped when there are 3 or more). 


.. code-block::

    http://favi.codes/JS

This will return a favicon with "JS" in black letters on a transparent background, like this:

.. image:: https://favi.codes/JS

You can also do background colors:

.. code-block::

    http://favi.codes/JS?bgcolor=yellow

.. image:: https://favi.codes/JS?bgcolor=yellow

