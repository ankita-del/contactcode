from django.db import models

class ContactDetails(models.Model):
    phone = models.CharField(max_length=15)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Interest(models.Model):
    contact = models.ForeignKey(ContactDetails, on_delete=models.CASCADE)
    interest = models.CharField(max_length=100)

    def __str__(self):
        return self.interest
