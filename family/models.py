from django.db import models
from customuser.models import TimeStampedModel, User


class Family(TimeStampedModel):
    surname = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.surname


class Person(TimeStampedModel):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]
    name = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    birth_date = models.DateField(null=True)
    death_date = models.DateField(blank=True, null=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name


class ParentChildRelationship(TimeStampedModel):
    parent = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='parent_relationships', null=True)
    child = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='child_relationships', null=True)


class MarriageRelationship(TimeStampedModel):
    spouse_one = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='marriages_1', null=True)
    spouse_two = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='marriages_2', null=True)
    marriage_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.spouse_one} + {self.spouse_two}"
