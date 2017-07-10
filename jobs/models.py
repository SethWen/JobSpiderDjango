from django.db import models
import json


# Create your models here.

class LagouJobs(models.Model):
    """ 
    keyWord = scrapy.Field()
    businessZones = scrapy.Field()
    companyFullName = scrapy.Field()
    companySize = scrapy.Field()
    createTime = scrapy.Field()
    district = scrapy.Field()
    education = scrapy.Field()
    financeStage = scrapy.Field()
    positionName = scrapy.Field()
    salary = scrapy.Field()
    workYear = scrapy.Field()
    """
    keyWord = models.CharField(max_length=20)
    businessZones = models.CharField(max_length=100)
    companyFullName = models.CharField(max_length=50)
    companySize = models.CharField(max_length=50)
    createTime = models.CharField(max_length=30)
    district = models.CharField(max_length=100)
    education = models.CharField(max_length=20)
    financeStage = models.CharField(max_length=50)
    positionName = models.CharField(max_length=50)
    salary = models.CharField(max_length=20)
    workYear = models.CharField(max_length=20)

    def __str__(self):
        return self.positionName

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        for attr in fields:
            d[attr] = getattr(self, attr)

        return json.dumps(d)

    # def toJSON(self):
    #     return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

    class Meta():
        db_table = 'jobs_lagou'


class ZhilianJobs(models.Model):
    keyWord = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    salary = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    pubDate = models.CharField(max_length=20)
    detailHref = models.CharField(max_length=200)

    def __str__(self):
        return self.position

    class Meta():
        db_table = 'jobs_zhilian'
