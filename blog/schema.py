import graphene
from graphene_django import DjangoListField, DjangoObjectType
from graphene import Field

from .models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("title", "body")


class Query(graphene.ObjectType):
    posts = DjangoListField(PostType)
    post = Field(PostType, id=graphene.Int(required=True))

    def resolve_post(self, info, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None


class PostMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, title, body):
        post = Post(title=title, body=body)
        post.save()
        return PostMutation(post=post)


class Mutation(graphene.ObjectType):
    add_post = PostMutation.Field()
