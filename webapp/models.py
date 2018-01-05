from django.db import models
from django.contrib.auth.models import User


TICKET_STATUS_CHOICES = (
    ('open', 'Open'),
    ('closed', 'Closed')
)

TICKET_PRIORITY_CHOICES = (
    (3, 'High'),
    (2, 'Medium'),
    (1, 'Low')
)


# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=128)
    address = models.TextField()
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=128)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.fullname

    __str__ = __repr__


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=128)
    address = models.TextField()
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=128)
    specialty = models.CharField(max_length=128)
    department = models.CharField(max_length=128)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.fullname

    __str__ = __repr__


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=128)
    department = models.CharField(max_length=128)

    class Meta:
        abstract = True


class Clinic(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    phone = models.CharField(max_length=32)
    email = models.EmailField(max_length=128)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.name

    __str__ = __repr__


class ClinicEmployee(Employee):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)


class Lab(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=128)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.name

    __str__ = __repr__


class LabEmployee(Employee):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)


class Pharmacy(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=128)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.name

    __str__ = __repr__


class PharmacyEmployee(Employee):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)


class ClinicTickets(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    assigned_to = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    assigned_on = models.DateTimeField()
    description = models.TextField()
    status = models.CharField(max_length=16, choices=TICKET_STATUS_CHOICES)
    priority = models.PositiveSmallIntegerField(choices=TICKET_PRIORITY_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.status

    __str__ = __repr__


class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    assigned_on = models.DateTimeField()
    symptoms = models.TextField()
    diagnosis = models.TextField()
    note = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.patient.fullname

    __str__ = __repr__


class LabTickets(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    referrer = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    assigned_on = models.DateTimeField()
    test = models.TextField()
    result = models.TextField()
    status = models.CharField(max_length=16, choices=TICKET_STATUS_CHOICES)
    priority = models.PositiveSmallIntegerField(choices=TICKET_PRIORITY_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.test

    __str__ = __repr__


class FarmacyTickets(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    referrer = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    assigned_on = models.DateTimeField()
    medicines = models.TextField()
    status = models.CharField(max_length=16, choices=TICKET_STATUS_CHOICES)
    priority = models.PositiveSmallIntegerField(choices=TICKET_PRIORITY_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.test

    __str__ = __repr__
