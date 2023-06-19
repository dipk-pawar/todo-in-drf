from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=250)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["id"]
