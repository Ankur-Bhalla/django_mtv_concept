from django.db import models


# SuperUserInformation
# User: Ankur
# Email: training@home.com
# Password: testpassword

# CREATE SOME TEST DATA WITH SOME SHELL COMMANDS:
# python manage.py shell
# from mtv_app.models import Topic
# print(Topic.objects.all())
# t = Topic(top_name="Social Network")
# t.save()
# print(Topic.objects.all())
# quit()

# Run below commands to check the data
# python manage.py shell
# from mtv_app.models import Topic, Webpage, AccessRecord
# t = Topic.objects.all().values('id','top_name')
# t
# w = Webpage.objects.all().values('id','top_name','web_name','url')
# w
# a = AccessRecord.objects.all().values('id','web_name','date')
# a
# a = AccessRecord.objects.all().values('id','web_name','date').order_by('date')
# a
# quit()

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    class Meta:
        app_label = 'mtv_app'

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    top_name = models.ForeignKey(Topic, on_delete=models.CASCADE)
    web_name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    class Meta:
        app_label = 'mtv_app'

    def __str__(self):
        return self.web_name


class AccessRecord(models.Model):
    web_name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        app_label = 'mtv_app'

    def __str__(self):
        return str(self.date)
