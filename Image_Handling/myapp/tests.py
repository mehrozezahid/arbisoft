from datetime import datetime
import os

from django.contrib.auth.models import User
from django.test import TestCase
import shutil
from Image_Handling import settings

from PIL import Image
from myapp.models import UserProfile


class ImageUploadTest(TestCase):
    def setUp(self):
        image = Image.open('/home/mahrozezahid/Desktop/Screenshot from '
                           '2015-08-17 12:45:39.png')
        user = User.objects.create(username='test', password='test', email='test@test.com')
        self.client.post('/myapp/uploadpicture', {'user': user, 'picture': image})

    def test_image_upload(self):
        self.assertTrue(os.path.isfile(settings.MEDIA_ROOT + 'test/' +
                                       datetime.today().strftime('%d-%m-%Y')))

    def tearDown(self):
        shutil.rmtree(settings.MEDIA_ROOT + 'test/')
