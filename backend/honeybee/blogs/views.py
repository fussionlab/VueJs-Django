from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.
from rest_framework import viewsets          # add this
from .serializers import BlogSerializer, CommentSerilaizer, ReplyCommentSerilaizer, HitsLikeSerilaizer    # add this
from .models import Post, Comment, ReplyComment, Hitslike             # add this

class PostView(viewsets.ModelViewSet): 
    serializer_class = BlogSerializer
    queryset = Post.objects.all()

    def get_object(self):
        lookup_value = self.kwargs.get('pk')

        if lookup_value is None:
            raise Http404("No Post matches the given query.")

        if lookup_value.isnumeric():
            return get_object_or_404(Post, id=lookup_value)
        else:
            return get_object_or_404(Post, slug=lookup_value)
        
class CommentView(viewsets.ModelViewSet):
    serializer_class =  CommentSerilaizer       # add this
    queryset = Comment.objects.all()  
    
    def get_queryset(self):
        qs = Comment.objects.all()  
        posts = self.request.query_params.get('post_id',None)
        if posts  is not None:
            return qs.filter(post=posts)
        return qs
    
class ReplyCommentView(viewsets.ModelViewSet):
    serializer_class =  ReplyCommentSerilaizer       # add this
    queryset = ReplyComment.objects.all()  
    
    def get_queryset(self):
        qs = ReplyComment.objects.all()  
        com = self.request.query_params.get('comment',None)
        pos = self.request.query_params.get('post', None)
        
        if pos is not None and com is not None:
            return qs.filter(post=pos,comment=com)
        elif pos is not None or com is not None:
            return qs.filter(post=pos)  
        return qs
class HitsLikesCountView(viewsets.ModelViewSet):
    serializer_class =  HitsLikeSerilaizer       # add this
    queryset = Hitslike.objects.all()  
    
    def get_queryset(self):
        qs = Hitslike.objects.all()  
        pos = self.request.query_params.get('post',None)
        if pos is not None:
            return qs.filter(post=pos)
        return qs