###QUESTION 1

Django signals are executed synchronously. This means that when a signal is sent, the receiver function is executed immediately and within the same request-response cycle.

###Code : 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

# Signal receiver function
@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f"Signal received for user: {instance.username}")
        # Simulate a delay to show synchronous behavior
        time.sleep(5)  # Sleep for 5 seconds
        print("Signal processing completed.")

# Django view to create a new user
def create_user_view(request):
    print("Before creating user")
    # Create a new user (this triggers the post_save signal)
    User.objects.create(username="new_user")
    print("User creation initiated!")
    return HttpResponse("User created")

When you call the create_user_view
###output:
Before creating user
Signal received for user: new_user
# 5-second delay...
Signal processing completed.
User creation initiated!

The print statement Signal received for user: new_user appears before User creation initiated! because the signal handler (user_created_signal) is executed synchronously.