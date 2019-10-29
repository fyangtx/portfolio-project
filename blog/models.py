from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to ='images/')

    # this function for db to use title as name of the record.
    def __str__(self):
        return self.title

    def summary(self):
        briefText = self.body
        if(len(self.body) > 100):
            briefText = self.body[:100] + '...'
        return briefText

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')