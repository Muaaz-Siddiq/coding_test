from djongo import models

# Create your models here.
class Customer_FeedBack(models.Model):
    topic = models.TextField()
    objects = models.DjongoManager()

    def __str__(self):
        return self.topic


