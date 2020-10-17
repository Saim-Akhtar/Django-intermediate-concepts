from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.

class PostQuerySet(models.QuerySet):
    def valid(self):
        return self.filter(valid=True)

    def invalid(self):
        return self.filter(valid=False)


class PostManager(models.Manager):
    def get_queryset(self):
        # return super().get_query_set()
        return PostQuerySet(self.model,using = self._db)

    def valid(self):
        return self.get_queryset().valid()

    def invalid(self):
        return self.get_queryset().invalid()

class Post(models.Model):
    title = models.CharField(max_length=20)
    valid = models.BooleanField(default=False)

    objects = PostManager()

    def __str__(self):
        return self.title

def post_save_receiver(sender, *args, **kwargs):
    # print(args)
    # print(kwargs)
    print("Post save method is called")

post_save.connect(post_save_receiver, sender = Post)

@receiver(post_delete)
def post_delete_receiver(sender, *args, **kwargs):
    print("Post Delete method is called")
