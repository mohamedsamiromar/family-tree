from customuser.models import TimeStampedModel, User
from django.db import models
from django.utils.translation import gettext_lazy as _



class UserInformation(TimeStampedModel):
    first_name = models.CharField(verbose_name=_('first_name'), max_length=150)
    middle_name = models.CharField(verbose_name=_('middle_name'), max_length=150)
    last_name = models.CharField(verbose_name=_('last_name'), max_length=255)


class GreatGrandFather(TimeStampedModel):
    user = models.OneToOneField(UserInformation, default=False, on_delete=models.CASCADE,
                                related_name='great_grand_father_user_information')

    def __str__(self):
        return self.user.full_name


class GreatGrandMother(TimeStampedModel):
    user = models.OneToOneField(UserInformation, default=False, on_delete=models.CASCADE,
                                related_name='great_grand_mother_user_information')

    def __str__(self):
        return self.user.full_name


class GrandFather(TimeStampedModel):
    user = models.OneToOneField(UserInformation, default=False, on_delete=models.CASCADE,
                                related_name='grand_father_user_information')
    great_grand_father = models.ForeignKey(
        GreatGrandFather, on_delete=models.CASCADE, default=False, related_name='father_great_grand_father')
    great_grand_mather = models.ForeignKey(
        GreatGrandMother, on_delete=models.CASCADE, default=False, related_name='father_mather_grand_mather')

    def __str__(self):
        return self.user.full_name


class GrandMother(TimeStampedModel):
    user = models.OneToOneField(UserInformation, default=False, on_delete=models.CASCADE,
                                related_name='grand_mather_user_information')
    great_grand_father = models.ForeignKey(
        GreatGrandFather, on_delete=models.CASCADE, default=False, related_name='mather_great_grand_father')
    great_grand_mather = models.ForeignKey(
        GreatGrandMother, on_delete=models.CASCADE, default=False, related_name='matter_mather_grand_mather')

    def __str__(self):
        return self.user.full_name


class Mather(TimeStampedModel):
    user = models.OneToOneField(UserInformation, default=False, on_delete=models.CASCADE,
                                related_name='mather_user_information')
    grand_father = models.ForeignKey(GrandFather, on_delete=models.CASCADE, default=False,
                                     related_name='mather_grand_father')
    grand_mather = models.ForeignKey(GrandMother, on_delete=models.CASCADE, default=False,
                                     related_name='mather_grand_mather')

    def __str__(self):
        return self.user.full_name


class Father(TimeStampedModel):
    user = models.OneToOneField(UserInformation, default=False, on_delete=models.CASCADE,
                                related_name='father_user_information')
    grand_father = models.ForeignKey(GrandFather, on_delete=models.CASCADE, default=False,
                                     related_name='father_grand_father')
    grand_mather = models.ForeignKey(GrandMother, on_delete=models.CASCADE, default=False,
                                     related_name='father_grand_mather')

    def __str__(self):
        return self.user.full_name


class Wife(TimeStampedModel):
    user = models.OneToOneField(UserInformation, on_delete=models.CASCADE, default=False,
                                related_name='user_wife_information')
    father = models.ForeignKey(Father, on_delete=models.CASCADE, default=False, related_name='father_wife')
    mather = models.ForeignKey(Mather, on_delete=models.CASCADE, default=False, related_name='mather_wife')


class Husband(TimeStampedModel):
    user = models.OneToOneField(UserInformation, on_delete=models.CASCADE, default=False,
                                related_name='user_information_husband')
    father = models.ForeignKey(Father, on_delete=models.CASCADE, default=False, related_name='father_husband')
    mather = models.ForeignKey(Mather, on_delete=models.CASCADE, default=False, related_name='mather_husband')


class Person(TimeStampedModel):
    class Gender(models.TextChoices):
        Male = "male", _("male")
        Female = "female", _("female")
        Other = "other", _("other")

    user = models.OneToOneField(
        User, default=False, on_delete=models.CASCADE, related_name='person_user')
    father = models.ForeignKey(
        Father, on_delete=models.CASCADE, related_name='father_person')
    mather = models.ForeignKey(
        Mather, on_delete=models.CASCADE, related_name='mather_person')
    gender = models.CharField(
        verbose_name=_('gender'), choices=Gender.choices, default=Gender.Other, max_length=50)
    wife = models.OneToOneField(Wife, on_delete=models.CASCADE, default=False, related_name='person_wife')
    husband = models.OneToOneField(Husband, on_delete=models.CASCADE, default=False, related_name='person_husband')

    def __str__(self) -> str:
        return self.user.full_name
