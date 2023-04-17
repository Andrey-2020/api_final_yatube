from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = (
            'author',
            'post',
        )


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    comment = CommentSerializer(many=True, required=False)
    publication_date = serializers.DateTimeField(source='pub_date',
                                                 read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'description', 'title', 'slug')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(read_only=True,
                            slug_field='username',
                            default=serializers.CurrentUserDefault())
    following = SlugRelatedField(queryset=User.objects.all(),
                                 slug_field='username')

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = (UniqueTogetherValidator(queryset=Follow.objects.all(),
                                              fields=('user', 'following'),
                                              message='Вы уже подписаны'),)

    def validate_following(self, value):
        user = self.context.get('request').user
        following = value
        if user == following:
            raise serializers.ValidationError(
                'Невозможно подписаться на самого себя!')
        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError('Вы уже подписаны')
        return value
