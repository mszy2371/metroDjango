from django.db import models


class Summer(models.Model):
    block = models.CharField(max_length=10, primary_key=True)
    year_2021 = models.DateField(blank=True, null=True)
    year_2022 = models.DateField(blank=True, null=True)
    year_2023 = models.DateField(blank=True, null=True)
    year_2024 = models.DateField(blank=True, null=True)


class EarlyWinter(models.Model):
    block = models.CharField(max_length=10, default=True, primary_key=True)
    year_2021 = models.DateField(blank=True, null=True)
    year_2022 = models.DateField(blank=True, null=True)
    year_2023 = models.DateField(blank=True, null=True)
    year_2024 = models.DateField(blank=True, null=True)
    summer = models.ForeignKey(Summer, on_delete=models.CASCADE, related_name='summer_block', default=True)

class LateWinter(models.Model):
    block = models.OneToOneField(EarlyWinter, on_delete=models.CASCADE, related_name='common_block', primary_key=True)
    year_2021 = models.DateField(blank=True, null=True)
    year_2022 = models.DateField(blank=True, null=True)
    year_2023 = models.DateField(blank=True, null=True)
    year_2024 = models.DateField(blank=True, null=True)


class Driver(models.Model):
    name = models.CharField(max_length=30)
    block = models.ForeignKey(EarlyWinter, on_delete=models.CASCADE, related_name='holiday_block')