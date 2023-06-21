from django.db import models

class whip_Credentials(models.Model):
    token = models.TextField()
    def __str__(self):
        template = '{0.token}'
        return template.format(self)

class whip_api_to_get(models.Model):
    whip_api = models.TextField()

    def __str__(self):
        template = '{0.whip_api}'
        return template.format(self)

class whip_api_output(models.Model):
    whip_api_output = models.TextField()

    def __str__(self):
        template = '{0.whip_api_output}'
        return template.format(self)