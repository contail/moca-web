#-*- coding: utf-8 -*-
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

class MemberManager(BaseUserManager):
    def create_user(self, name, email=None,):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not name:
            raise ValueError('Users must have a name')
        import datetime
        last_access_time = datetime.datetime.now()
        user = self.model(
            name=name,
            email = email,
            last_access_time = last_access_time,
        )

        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(username,
                                password=password
                                )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Member(AbstractBaseUser):
    email = models.CharField(max_length=100)
    last_access_time = models.DateTimeField(null=True, db_index=True)
    name = models.CharField(
        max_length=255,
        unique=True,
        null= True,
    )
    objects = MemberManager()

    def __str__(self):
        return "{0} {1}".format(self.id, self.name)




