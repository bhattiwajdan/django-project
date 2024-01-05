from django.db import models

class ExampleModel(models.Model):
    # Create a CharField with max length 200
    title = models.CharField(max_length=200)

    # Create a TextField
    content = models.TextField()

    # Create a DateTimeField
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
