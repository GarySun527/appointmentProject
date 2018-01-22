from django.db import models
# Create your models here.
class PersonModel(models.Model):
    prsn_fname = models.CharField(max_length=20, verbose_name="First Name")
    prsn_lname = models.CharField(max_length=20, verbose_name="Last Name")
    prsn_phone = models.CharField(max_length=20, verbose_name="Phone")
    prsn_email = models.EmailField(max_length=60, verbose_name="Email")
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = verbose_name
    def __str__(self):
        name = self.prsn_fname + ' ' + self.prsn_lname
        return name

class AddressModel(models.Model):
    prsn_id = models.ForeignKey(PersonModel, verbose_name="ID")
    prsn_line = models.CharField(max_length=40, verbose_name="Line")
    prsn_city = models.CharField(max_length=40, verbose_name="City")
    prsn_state = models.CharField(max_length=2, verbose_name="Sate")
    prsn_zip = models.CharField(max_length=5, verbose_name="Zip")
    class Meta:
        verbose_name = 'Adress'
        verbose_name_plural = verbose_name

class AppointmentModel(models.Model):
    prsn_id = models.ForeignKey(PersonModel)
    appt_title = models.CharField(max_length=60, verbose_name="Title")
    appt_descr = models.TextField()
    appt_date_time = models.DateField()
    appt_last_changed = models.DateField()

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = verbose_name