kite-string
===================

kite-string(凧糸) is Python(2.6-3.4) command-line HTTP request wrapper for `takosan <https://github.com/kentaro/takosan>`_ .

Installing
-----------------

For Users
~~~~~~~~~~~~~~~

from PyPI

.. sourcecode:: bash

    $ pip install kite-string

from Github

.. sourcecode:: bash

    $ pip install git+https://github.com/laughk/kite-string.git


Usage
-----------------

.. sourcecode:: bash

    $ kite -h
    Usage: kite [OPTIONS] TAKOSAN_URL

    Options:
      --version           show the version and exit
      --channel TEXT      Name of notice channel, or id (e.g. #example, @id)
                          [required]
      --name TEXT         set botname
      --color TEXT        set color border along the left side of the message
                          attachment [good|warning|danger|<hex color code>]  (e.g.
                          #439FE0)
      --message TEXT      Simple post messages
      --icon TEXT         set image url or emoji (e.g. :shachikun:)
      --pretext TEXT      This is optional text that appears above the message
                          attachment block
      --author-name TEXT  Small text used to display the author's name
      --author-icon TEXT  A valid URL that displays a small 16x16px image to the
                          left of the author_name text. Will only work if
                          author_name is present
      --author-link TEXT  A valid URL that will hyperlink the `author_name` text
                          mentioned above. Will only work if `author_name` is
                          present
      --title TEXT        The title is displayed as larger, bold text near the top
                          of a message attachment
      --title-link TEXT   By passing a valid URL. the `title` text will be
                          hyperlinked
      --text TEXT         This is the main text in a message attachment, and can
                          contain standard message markup
      --image-url TEXT    A valid URL to an image file that will be displayed
                          inside a message attachment (Slack currently support the
                          following formats: GIF, JPEG, PNG, and BMP.)
      -h, --help          Show this message and exit.


example
~~~~~~~~~

Simple Post

.. sourcecode:: bash

    $ kite \
    > --name 'laugh_k' \
    > --icon 'https://pbs.twimg.com/profile_images/498392311491883010/If0DOLYq.jpeg' \
    > --channel '@laughk' \
    > --text 'hello' \
    > http://takosan.example.com:4979


Multi channel Post

.. sourcecode:: bash

    $ kite \
    > --name 'laugh_k' \
    > --icon 'https://pbs.twimg.com/profile_images/498392311491883010/If0DOLYq.jpeg' \
    > --channel '#notice_channel1' \
    > --channel '#notice_channel2' \
    > --text 'hello' \
    > http://takosan.example.com:4979
