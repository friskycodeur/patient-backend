from django.db import models

gender_choice_list = (("M", "male"), ("F", "female"), ("O", "other"))


class Patient(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    gender = models.CharField(max_length=2, choices=gender_choice_list)
    age = models.IntegerField(null=False, blank=False)
    problem = models.TextField()
    doctor_name = models.CharField(max_length=150, null=False, blank=False)
    doctor_fees = models.IntegerField(default=500, null=False, blank=False)
    meds_start_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
