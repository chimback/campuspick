from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=20)
    contents = models.TextField()
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board_no = models.ForeignKey(Board, on_delete=models.CASCADE)