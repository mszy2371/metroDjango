from django.db import models

# Create your models here.


class Driver(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Duty(models.Model):
    number = models.CharField(max_length=10, primary_key=True, default=True, unique=True)
    route = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.number}'


class MondayThursday(models.Model):
    duty = models.OneToOneField(Duty, on_delete=models.CASCADE, primary_key=True,
                                related_name='mon_thu_duties', unique=True)
    start_time = models.TimeField(blank=True, null=True)
    finish_time = models.TimeField(blank=True, null=True)
    card = models.FileField(blank=True)

    def __str__(self):
        return f'{self.duty} {self.start_time} - {self.finish_time}'


class Friday(models.Model):
    duty = models.OneToOneField(Duty, on_delete=models.CASCADE, primary_key=True,
                                related_name='friday_duties', unique=True)
    start_time = models.TimeField(blank=True, null=True)
    finish_time = models.TimeField(blank=True, null=True)
    card = models.FileField(blank=True)

    def __str__(self):
        return f'{self.duty} {self.start_time} - {self.finish_time}'


class Saturday(models.Model):
    duty = models.OneToOneField(Duty, on_delete=models.CASCADE, primary_key=True,
                                related_name='saturday_duties', unique=True)
    start_time = models.TimeField(blank=True, null=True)
    finish_time = models.TimeField(blank=True, null=True)
    card = models.FileField(blank=True)

    def __str__(self):
        return f'{self.duty} {self.start_time} - {self.finish_time}'


class Sunday(models.Model):
    duty = models.OneToOneField(Duty, on_delete=models.CASCADE, primary_key=True,
                                related_name='sunday_duties', unique=True)
    start_time = models.TimeField(blank=True, null=True)
    finish_time = models.TimeField(blank=True, null=True)
    card = models.FileField(blank=True)

    def __str__(self):
        return f'{self.duty} {self.start_time} - {self.finish_time}'


class Rota(models.Model):
    saturday = models.ForeignKey(Saturday, on_delete=models.CASCADE,
                                 related_name='sat_rota', verbose_name='Saturday')
    sunday = models.ForeignKey(Sunday, on_delete=models.CASCADE,
                               related_name='sun_rota', verbose_name='Sunday')
    monday = models.ForeignKey(MondayThursday, on_delete=models.CASCADE,
                               related_name='mon_rota', verbose_name='Monday')
    tuesday = models.ForeignKey(MondayThursday, on_delete=models.CASCADE,
                                related_name='tue_rota', verbose_name='Tuesday')
    wednesday = models.ForeignKey(MondayThursday, on_delete=models.CASCADE,
                                  related_name='wed_rota', verbose_name='Wednesday')
    thursday = models.ForeignKey(MondayThursday, on_delete=models.CASCADE,
                                 related_name='thu_rota', verbose_name='Thursday')
    friday = models.ForeignKey(Friday, on_delete=models.CASCADE,
                               related_name='fri_rota', verbose_name='Friday')

    def __str__(self):
        return f'{self.saturday} {self.sunday} {self.monday} {self.tuesday}' \
               f' {self.wednesday} {self.thursday} {self.friday}'




