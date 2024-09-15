from django.db import models
from django.contrib.auth.models import User
class Notes(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True , null=True , upload_to='notes')
    created_by = models.ForeignKey(User, blank=True,null=True, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title