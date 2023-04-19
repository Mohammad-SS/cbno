from django.db import models


class ContactForm(models.Model):
    """
    Model class for storing contact form data.

    first_name: CharField for storing first name of the contact.
    last_name: CharField for storing last name of the contact.
    phone_number: CharField for storing phone number of the contact.
    email: EmailField for storing email address of the contact.
    message: TextField for storing message entered by the contact.

    full_name: Property method to return the full name of the contact.

    __str__: Method to return the email address of the contact.
    """

    first_name = models.CharField(max_length=31)
    last_name = models.CharField(max_length=31)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    message = models.TextField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email
