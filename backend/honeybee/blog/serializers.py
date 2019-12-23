from rest_framework import serializers
from .models import Post, Comment, ReplyComment, Hitslike

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title', 'slug', 'author','content','status','created_on')
        
class CommentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','author','body','created_on','post')

class ReplyCommentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = ReplyComment
        fields = ('id','author','body','created_on','post','comment')
class HitsLikeSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Hitslike
        fields = ('id','hitcount','viewcount','post')