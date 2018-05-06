from django.db import models


class Comment(models.Model):

    class Meta:
        abstract = True

    def returnComment(self):
        pass

class CommentBase(Comment):

    text = models.CharField(max_length= 500)

    def returnComment(self):
        print(self.text)

class CommentDecorator(Comment):

    comment = models.OneToOneField(Comment, on_delete=models.CASCADE, primary_key=True)

    # comment = models.OneToOneField(Comment, on_delete=models.CASCADE, primary_key=True)

    def returnComment(self):
        comment.returnComment()

class CommentImage(CommentDecorator):

    image = models.CharField(max_length= 30)

    # image = models.ImageField()

    def returnComment(self):
        comment.returnComment()
        print(self.image)


# class Componentes(models.Model):
#
#
# class Texto(Componentes):
#
#         text = models.CharField(max_length= 500, null= False)
#         comment = models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='texts')
#
#
# class Image(Componentes):
#
#     # image = models.ImageField(null=True)
#
#     text = models.CharField(max_length= 500, null= False)
#
#     project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='images', null=True)
#
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='images', null=True)
#
# class Comment(Componentes):
