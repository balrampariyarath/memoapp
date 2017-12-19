from django.db import models


class Memos(models.Model):
    desc = models.TextField()
    image = models.ImageField(upload_to='photos', max_length=254, blank=True, null=True)
    date = models.DateField()
    person = models.CharField(max_length=255, blank=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.desc)