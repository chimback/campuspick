from rest_framework import viewsets
from .models import Board, Comment
from .serializers import BoardSerializer,CommentSerializer

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer