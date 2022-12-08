from django.db import models


class Link(models.Model):
    url = models.URLField(unique=True)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        self.score = self.upvotes - self.downvotes
        super(Link, self).save(*args, **kwargs)
