from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

@receiver(user_logged_in)
def user_Loggin_success(sender, request, user, **kwargs):
    print(f"The user Logged in :{user.username}")

@receiver(user_logged_out)
def user_Logout_message(sender, request, user, **kwargs):
    print(f"The user Logout Success :{user.username}")



