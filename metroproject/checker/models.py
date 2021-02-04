from django.db import models

# Create your models here.

class Rota(models.Model):
    saturday = models.CharField(max_length=10)
    sunday = models.CharField(max_length=10)
    monday = models.CharField(max_length=10)
    tuesday = models.CharField(max_length=10)
    wednesday = models.CharField(max_length=10)
    thursday = models.CharField(max_length=10)
    friday = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.saturday} {self.sunday} {self.monday} {self.tuesday}' \
               f' {self.wednesday} {self.thursday} {self.friday}'


class Driver(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return f'{self.name}'


class Duty(models.Model):
    number = models.CharField(max_length=10, primary_key=True, default=True)
    route = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.number}'


class MondayThursday(models.Model):
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE)
    start_time = models.TimeField(blank=True, null=True)
    finish_time = models.TimeField(blank=True, null=True)
    card = models.FileField(blank=True)

    def __str__(self):
        return f'{self.duty} {self.start_time} - {self.finish_time}'


class Friday(models.Model):
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE)
    start_time = models.TimeField(blank=True, null=True)
    finish_time = models.TimeField(blank=True, null=True)
    card = models.FileField(blank=True)

    def __str__(self):
        return f'{self.duty} {self.start_time} - {self.finish_time}'


class Saturday(models.Model):
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE)
    start_time = models.TimeField(blank=True, null=True)
    finish_time = models.TimeField(blank=True, null=True)
    card = models.FileField(blank=True)

    def __str__(self):
        return f'{self.duty} {self.start_time} - {self.finish_time}'


class Sunday(models.Model):
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE)
    start_time = models.TimeField(blank=True, null=True)
    finish_time = models.TimeField(blank=True, null=True)
    card = models.FileField(blank=True)

    def __str__(self):
        return f'{self.duty} {self.start_time} - {self.finish_time}'



