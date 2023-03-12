from django.db import models
from .validators import validate_file_extension,file_size


class Image(models.Model):
    photo = models.FileField(upload_to='myimage', validators=[validate_file_extension, file_size])
    date = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=200, default='', null=True, blank=True)
    # category = models.CharField(max_length=150, null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.photo.storage.delete(self.photo.name)
        super().delete()