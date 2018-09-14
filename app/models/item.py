from django.db import models

from app.models.todo import Todo


class Item(models.Model):
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a human readable representation of the model instance.
        """
        return f"{self.name}"

    class Meta:
        ordering = ("created",)
