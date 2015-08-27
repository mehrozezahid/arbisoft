from datetime import datetime
import os
import errno
import shutil

from django import forms
from myapp.models import UserProfile
from django.contrib.auth.models import User

from Image_Handling import settings


class UserSignUp(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UploadPictureForm(forms.Form):
    picture = forms.ImageField(label='Select an Image')

    # def save_image(self, user, pic):
    #     """"Function saves image on disk in a path using default image
    #      folder and separate directory for each user, and returns the
    #      path of the image to be stored in db"""
    #
    #     # setting directory to IMAGE_PATH from settings + user directory
    #     directory = settings.IMAGE_PATH + \
    #                 user.username.encode('ascii', 'ignore') + '/'
    #
    #     # check if picture for user already exists, if so delete from
    #     # db and disk
    #     if UserProfile.objects.filter(user=user).exists():
    #         shutil.rmtree(directory)
    #         UserProfile.objects.filter(user=user).delete()
    #
    #     # check if directory exists, if not create
    #     try:
    #         os.makedirs(directory)
    #     except OSError as exception:
    #         if exception.errno != errno.EEXIST:
    #             raise
    #
    #     # change filename to current date
    #     directory += datetime.today().strftime('%d-%m-%Y') + '.jpg'
    #
    #     # write file to disk
    #     destination = open(directory, 'wb+')
    #     for chunk in pic.chunks():
    #         destination.write(chunk)
    #         destination.close()
    #
    #     # return path to image
    #     return directory
