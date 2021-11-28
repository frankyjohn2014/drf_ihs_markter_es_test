from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from blog_ihs.models import Article,User

@registry.register_document
class UserDocument(Document):
    class Index:
        name = 'user'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = User
        fields = [
            'full_name',
        ]


@registry.register_document
class ArticleDocument(Document):
    author = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'full_name': fields.TextField(),

    })
    class Index:
        name = 'article'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
    class Django:
        model = Article
        fields = [
            'paragraph',
            'created_datetime',
        ]

