#!/usr/bin/env python
# -*- coding:utf-8 -*-

import click
from kite.takosan import Tako
from kite.version import get_version
from kite.help_messages import get_help_message


@click.command(context_settings={'help_option_names':['-h', '--help']})
@click.version_option(version=get_version(), prog_name='kite',
        help=get_help_message('version'))
@click.option('--channel','channels',
        nargs=1, required=True, multiple=True,
        help=get_help_message('channel'))
@click.option('--name', nargs=1, default='takosan',
        help=get_help_message('name'))
@click.option('--color', nargs=1,
        help=get_help_message('color'))
@click.option('--message',
        help=get_help_message('message'))
@click.option('--icon', nargs=1,
        help=get_help_message('icon'))
@click.option('--pretext', nargs=1,
        help=get_help_message('pretext'))
@click.option('--author-name', nargs=1,
        help=get_help_message('author-name'))
@click.option('--author-icon', nargs=1,
        help=get_help_message('author-icon'))
@click.option('--author-link', nargs=1,
        help=get_help_message('author-link'))
@click.option('--title', nargs=1,
        help=get_help_message('title'))
@click.option('--title-link', nargs=1,
        help=get_help_message('title-link'))
@click.option('--text', nargs=1,
        help=get_help_message('text'))
@click.option('--image-url', nargs=1,
        help=get_help_message('image-url'))
@click.argument('takosan_url',
        nargs=1, required=True,)
def main(takosan_url, channels,
        name,
        color,
        message,
        icon,
        pretext,
        author_name,
        author_icon,
        author_link,
        title,
        title_link,
        text,
        image_url,
        ):

    payload_base = {
        'name'         : name,
        'color'        : color,
        'message'      : message,
        'icon'         : icon,
        'pretext'      : pretext,
        'author_name'  : author_name,
        'author_icon'  : author_icon,
        'author_link'  : author_link,
        'title'        : title,
        'title_link'   : title_link,
        'text'         : text,
        'image_url'    : image_url,
    }
    tako = Tako(takosan_url, channels, payload_base)
    tako.flying()

if __name__ == '__main__':
    main()
