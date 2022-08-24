from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Usemail(models.Model):

    emaillist = models.EmailField(max_length=254)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # verbose_name = _("user email")
        # verbose_name_plural = _("s")
        # ordering = ('-email')
        pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})