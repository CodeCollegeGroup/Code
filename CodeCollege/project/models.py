from django.db import models
from django.db import models
from user.models import User
from comment.models import Comment,CommentBase,CommentDecorator,CommentImage

class Project(models.Model):

    recorder = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=50, null= False)

    description = models.CharField(max_length=200, null= False)

    repository = models.CharField(max_length=100, null= False)

    deploy = models.CharField(max_length=100)

    colaborator = models.ManyToManyField(User, related_name='contributed_projects')

    university_class = models.CharField(max_length=150)

    def comentar(Self, User, text, image):

        comment = Comment()

        base = CommentBase()
        base.text = text
        base.save()

        if( image ):
            imageX = CommentImage(text)
            imageX.image = image

        comment = image

        comment.save

class Image(models.Model):

    image = models.ImageField(null=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
