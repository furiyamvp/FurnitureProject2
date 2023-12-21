from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.email}"

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


