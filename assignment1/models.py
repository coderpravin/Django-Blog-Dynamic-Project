from django.db import models

# Create your models here.
class About(models.Model):
    about_heading = models.CharField(max_length=200)
    about_description  = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    class Meta:
        verbose_name_plural = 'about'
    
    def __str__(self):
        return f"The About heading is {self.about_heading}"
    
class SocialLink(models.Model):
    platform = models.CharField(max_length=200)
    link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "SocialLinkAccount"
    
    def __str__(self):
        return f"The Plateform name is {self.platform}"
    
    