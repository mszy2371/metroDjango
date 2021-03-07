from django.db import models


class Summer(models.Model):
    block = models.CharField(max_length=10, primary_key=True)
    year_2021 = models.DateField(blank=True, null=True)
    year_2022 = models.DateField(blank=True, null=True)
    year_2023 = models.DateField(blank=True, null=True)
    year_2024 = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Summer {self.block} {self.year_2021} {self.year_2022} {self.year_2023} {self.year_2024}'


class EarlyWinter(models.Model):
    block = models.CharField(max_length=10, default=True, primary_key=True)
    year_2021 = models.DateField(blank=True, null=True)
    year_2022 = models.DateField(blank=True, null=True)
    year_2023 = models.DateField(blank=True, null=True)
    year_2024 = models.DateField(blank=True, null=True)
    summer = models.ForeignKey(Summer, on_delete=models.CASCADE, related_name='summer_block', default=True)

    def __str__(self):
        return f'Early {self.block} {self.year_2021} {self.year_2022} {self.year_2023} {self.year_2024}'

class LateWinter(models.Model):
    block = models.OneToOneField(EarlyWinter, on_delete=models.CASCADE, related_name='common_block', primary_key=True)
    year_2021 = models.DateField(blank=True, null=True)
    year_2022 = models.DateField(blank=True, null=True)
    year_2023 = models.DateField(blank=True, null=True)
    year_2024 = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Late {self.block} {self.year_2021} {self.year_2022} {self.year_2023} {self.year_2024}'


class Driver(models.Model):
    name = models.CharField(max_length=30)
    block = models.ForeignKey(EarlyWinter, on_delete=models.CASCADE, related_name='holiday_block')

    def __str__(self):
        return f'{self.name} == {self.block}'