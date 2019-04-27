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

    https://favi.codes

This will return a transparent, 256x256 PNG.

.. image:: https://favi.codes/

You cant see it, but its just above this sentence. 


How to make a Favicode
======================

Maybe you just want a simple letter or two. (No more than 2 glyphs are allowed 
because the letters look too cramped when there are 3 or more). 


.. code-block::

    https://favi.codes/JS

This will return a favicon with "JS" in black letters on a transparent background, like this:

.. image:: https://favi.codes/JS

You can also do background colors:

.. code-block::

    https://favi.codes/JS?bgcolor=gold

.. image:: https://favi.codes/JS?bgcolor=gold

It you're familiar with the Javascript logo, you may recognize where this is heading. 
Let's see how close we can get it. Maybe make the text bold, and offset the X and Y
to put the "JS" in the bottom right corner

.. code-block::

    https://favi.codes/JS?&bgcolor=gold&y=35&x=65&fontsize=128&style=bold

.. image:: https://favi.codes/JS?&bgcolor=gold&y=35&x=65&fontsize=128&style=bold

Now, if you're *really* familiar with the JavaScript logo, you may be irked that the
J extends below the line. This is because the only fonts supported by Favicodes at the moment are
Google Noto Sans and FontAwesome, and that's just how capital J's look in both of those fonts. 

There is a workaround for this logo, since it is included with FontAwesome Free.
To use FontAwesome icons in your favicode, you have 2 options. The first option is if you know the
proper name of the icon, such as "paper-plane" or "js", you can use it the url after
the path, /fa/, like this:

.. code-block::

    https://favi.codes/fa/js

.. image:: https://favi.codes/fa/js

Obviously, this doesn't match either. After some fiddling, I came up with this:

.. code-block::

    https://favi.codes/fa/js?color=gold&bgcolor=black&fontsize=256&y=-8&size=224

.. image:: https://favi.codes/fa/js?color=gold&bgcolor=black&fontsize=256&y=-8&size=224

Alternatively, that same FontAwesome icon can be referenced by it's Unicode code point instead, so long
as FontAwesome is specified as the font. And, because the font is being specified, you'll have
to specify the style for this code point as well. `The code point is f3b8 and the style is 'brands' for this icon <https://fontawesome.com/icons/js?style=brands>`_. Like this:

.. code-block::

    https://favi.codes/f3b8?color=gold&bgcolor=black&fontsize=256&y=-8&size=224&font=fontawesome&style=brands


Advanced usage
==============

We just touched on Unicode code points in the URL. You can actually specify any character input this way, 
including UTF-32LE characters, although I doubt any of the fonts supported have glyphs in that range. Any input
past the root slash '/' that is longer than 2 characters (because Favicodes can only have 2 characters) is expected
to be valid hex representing a character in the font. 

So, suppose you wanted to make Slashdot's favicon. You can't use '/' or '.' in the URL bar, and 
URL encoding wont work for the slash, because to webserver will eat the slash. All you need to
know is the Unicode values for slash and dot, 002F and 002E:

.. code-block::

    https://favi.codes/02f/02e?color=white&style=extrabolditalic&x=10&y=-25&bgcolor=104f4e&fontsize=224

.. image:: https://favi.codes/02f/02e?color=white&style=extrabolditalic&x=10&y=-25&bgcolor=104f4e&fontsize=224

