from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return a human readable representation of the model instance.
        """
        return f"{self.title}"

    class Meta:
        ordering = ('created', )