#!/usr/bin/env python
# -*- coding:utf-8 -*-

def get_help_message(option):

    help_messages = {
        'version':
            'show the version and exit',
        'channel':
            'Name of notice channel, or id (e.g. #example, @id)',
        'name':
            'set botname',
        'color':
            'set color border along the left side of the message attachment [good|warning|danger|<hex color code>]  (e.g. #439FE0)',
        'message':
            'Simple post messages',
        'icon':
            'set image url or emoji (e.g. :shachikun:)',
        'pretext':
            'This is optional text that appears above the message attachment block',
        'author-name':
            'Small text used to display the author\'s name',
        'author-icon':
            'A valid URL that displays a small 16x16px image to the left of the author_name text. Will only work if author_name is present',
        'author-link':
            'A valid URL that will hyperlink the `author_name` text mentioned above. Will only work if `author_name` is present',
        'title':
            'The title is displayed as larger, bold text near the top of a message attachment',
        'title-link':
            'By passing a valid URL. the `title` text will be hyperlinked',
        'text':
            'This is the main text in a message attachment, and can contain standard message markup',
        'image-url':
            'A valid URL to an image file that will be displayed inside a message attachment (Slack currently support the following formats: GIF, JPEG, PNG, and BMP.)',
    }

    if option in help_messages.keys():
        return help_messages.get(option)
    else:
        return None

