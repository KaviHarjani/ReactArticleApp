from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class WorkingCenter(models.Model):
    name = models.CharField(max_length=100)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    working_center = models.ForeignKey(WorkingCenter, on_delete=models.CASCADE)


class Contract(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="contracts"
    )
