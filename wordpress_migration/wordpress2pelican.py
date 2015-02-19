#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Export a Wordpress blog to Pelican format

    If everything worked right, this will create a _posts directory with your converted posts.
"""

import codecs
import os
import re
import sys

import html2text
import yaml
from html2rest import html2rest
from peewee import *

database = MySQLDatabase('blog2', **{'password': 'PASSWORD', 'user': 'root'})


class UnknownField(object):
    pass


class BaseModel(Model):

    class Meta:
        database = database


class Users(BaseModel):
    id = BigIntegerField(db_column='ID', primary_key=True)
    display_name = CharField()
    user_activation_key = CharField()
    user_email = CharField()
    user_login = CharField(index=True)
    user_nicename = CharField(index=True)
    user_pass = CharField()
    user_registered = DateTimeField()
    user_status = IntegerField()
    user_url = CharField()

    class Meta:
        db_table = 'wp_users'


class Posts(BaseModel):
    id = BigIntegerField(db_column='ID', primary_key=True)
    comment_count = BigIntegerField()
    comment_status = CharField()
    guid = CharField()
    menu_order = IntegerField()
    ping_status = CharField()
    pinged = TextField()
    author = ForeignKeyField(Users, related_name='authors', db_column='post_author')
    post_category = IntegerField()
    post_content = TextField()
    post_content_filtered = TextField()
    post_date = DateTimeField()
    post_date_gmt = DateTimeField()
    post_excerpt = TextField()
    post_mime_type = CharField()
    post_modified = DateTimeField()
    post_modified_gmt = DateTimeField()
    post_name = CharField(index=True)
    post_parent = BigIntegerField(index=True)
    post_password = CharField()
    post_status = CharField()
    post_title = TextField()
    post_type = CharField()
    to_ping = TextField()

    class Meta:
        db_table = 'wp_posts'

    def __repr__(self):
        return u"<Post '{0}' id={1} status='{2}'>".format(
            self.post_title, self.id, self.post_status)


class TermRelationships(BaseModel):
    object = BigIntegerField(db_column='object_id')
    term_order = IntegerField()
    term_taxonomy = BigIntegerField(db_column='term_taxonomy_id', index=True)

    class Meta:
        db_table = 'wp_term_relationships'
        primary_key = CompositeKey('object', 'term_taxonomy')


class TermTaxonomy(BaseModel):
    count = BigIntegerField()
    description = TextField()
    parent = BigIntegerField()
    taxonomy = CharField(index=True)
    term = BigIntegerField(db_column='term_id')
    term_taxonomy = BigIntegerField(db_column='term_taxonomy_id', primary_key=True)

    class Meta:
        db_table = 'wp_term_taxonomy'


class Terms(BaseModel):
    name = CharField(index=True)
    slug = CharField(unique=True)
    term_group = BigIntegerField()
    term = BigIntegerField(db_column='term_id', primary_key=True)

    class Meta:
        db_table = 'wp_terms'


def get_published_posts(blog_id=0):
    return Posts.select().where(Posts.post_status == "publish", Posts.post_type == "post")


def get_blog_url(blog_id=0):
    return 'http://anotaciones.es'


class RestructuredTextConverter(object):
    def get_extension(self):
        return '.rst'

    def fill(self, data, html_content, output):
        title = data['title']
        output.write(title)
        output.write("\n{}\n".format('#'*len(title)))
        output.write(yaml.safe_dump(data, default_flow_style=False, allow_unicode=True).decode("utf-8"))
        output.write("\n")

        html2rest(html_content, writer=output, encoding='utf8')


class MarkdownConverter(object):
    def get_extension(self):
        return 'md'

    def fill(self, data, html_content, output):
        for k, v in data.iteritems():
            output.write(k.capitalize())
            output.write(": ")
            output.write(v)
            output.write("\n")
        output.write("\n")
        # output.write(html_content)
        output.write(html2text.html2text(html_content))

if __name__ == '__main__':
    # Output textile files in ./_posts
    if os.path.isdir("content"):
        print "There's already a content directory here, "\
            "I'm not going to overwrite it."
        sys.exit(1)
    else:
        os.mkdir("content")
    converter = MarkdownConverter()

    post_num = 1
    for post in get_published_posts():
        data = {
            "title": post.post_title,
            "date": post.post_date.strftime("%Y-%m-%d %H:%M"),
            # "categories": ", ".join(post.categories()),
            # "tags": ", ".join(post.tags()),
            "guid": post.guid
        }
        fn = u"{0}-{1}.{2}".format(
            str(post_num).zfill(4),
            re.sub(r'[/!:?\-,\']', '', post.post_title.strip().lower().replace(' ', '_')),
            converter.get_extension())
        print "writing _posts/" + fn
        try:
            f = codecs.open(os.path.join("content", fn), "w", "utf-8")
            converter.fill(data, post.post_content.replace(u"\r\n", u"\n"), f)
            f.close()
        except:
            import ipdb; ipdb.set_trace()
        post_num += 1
