from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    drive_id = models.CharField(max_length=255, blank=True, null=True)
    public_url = models.URLField(max_length=500, blank=True, null=True)
    def __str__(self):
        return self.title or self.image.name
