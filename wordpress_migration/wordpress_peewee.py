from peewee import *

database = MySQLDatabase('blog2', **{'password': 'PASSWORD', 'user': 'root'})


class UnknownField(object):
    pass


class BaseModel(Model):

    class Meta:
        database = database


class Options(BaseModel):
    autoload = CharField()
    option = BigIntegerField(db_column='option_id', primary_key=True)
    option_name = CharField(unique=True)
    option_value = TextField()

    class Meta:
        db_table = 'wp_options'


class Postmeta(BaseModel):
    meta = BigIntegerField(db_column='meta_id', primary_key=True)
    meta_key = CharField(index=True, null=True)
    meta_value = TextField(null=True)
    post = BigIntegerField(db_column='post_id', index=True)

    class Meta:
        db_table = 'wp_postmeta'


class Posts(BaseModel):
    id = BigIntegerField(db_column='ID', primary_key=True)
    comment_count = BigIntegerField()
    comment_status = CharField()
    guid = CharField()
    menu_order = IntegerField()
    ping_status = CharField()
    pinged = TextField()
    post_author = BigIntegerField(index=True)
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

    def permalink(self):
        site_url = get_blog_url()
        structure = '/%year%/%monthnum%/%post_id%/%postname%'
        structure = structure.replace("%year%", str(self.post_date.year))
        structure = structure.replace("%monthnum%",
                                      str(self.post_date.month).zfill(2))
        structure = structure.replace("%day%", str(self.post_date.day).zfill(2))
        structure = structure.replace("%hour%",
                                      str(self.post_date.hour).zfill(2))
        structure = structure.replace("%minute%",
                                      str(self.post_date.minute).zfill(2))
        structure = structure.replace("%second%",
                                      str(self.post_date.second).zfill(2))
        structure = structure.replace("%postname%", self.post_name)
        structure = structure.replace("%post_id%", str(self.id))
        # try:
        #     structure = structure.replace("%category%", self.categories()[0])
        # except IndexError:
        #     pass
        # try:
        #     structure = structure.replace("%tag%", self.tags()[0])
        # except IndexError:
        #     pass
        structure = structure.replace("%author%", self.author.user_nicename)
        return site_url.rstrip("/") + "/" + structure.lstrip("/")


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


class Usermeta(BaseModel):
    meta_key = CharField(index=True, null=True)
    meta_value = TextField(null=True)
    umeta = BigIntegerField(db_column='umeta_id', primary_key=True)
    user = BigIntegerField(db_column='user_id', index=True)

    class Meta:
        db_table = 'wp_usermeta'


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
