from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_joining = models.DateField()
    address = models.TextField(max_length=255)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    father_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    pass_out_year = models.DateField()
    stream = models.CharField(max_length=100)
    course_type = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)


    BLOOD_GROUP_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    GRADUATION_TYPE_CHOICES = (
        ('Degree', 'Degree'),
        ('B.Tech', 'B.Tech'),
    )
    graduation_type = models.CharField(max_length=10, choices=GRADUATION_TYPE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
