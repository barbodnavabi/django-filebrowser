from django.db import models

# Create your models here.
class File(models.Model):
    title=models.CharField(("tile"), max_length=100)
    image=models.ImageField(("image"), upload_to='images',)
    file=models.FileField(("file"), upload_to='files',)

    

    class Meta:
        verbose_name = ("File")
        verbose_name_plural = ("Files")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):-
    #     return reverse("File_detail", kwargs={"pk": self.pk})
