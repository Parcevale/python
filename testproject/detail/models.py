from django.db import models

class  Category(models.Model):

    name = models.CharField(max_length=150)

    crated = models.DateTimeField(auto_now_add=True)

    def __str__()str:
        return self.name

