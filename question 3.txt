QUESTION 3

Django signals do run in the same database transaction as the caller. 
This means that the signal handlers are executed within the transaction that is initiated by the code that triggered the signal. 
If the transaction is rolled back, the signal handlers will not be committed either.

CODE:

# Signal receiver function
@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        # Simulate a transaction rollback
        transaction.set_rollback(True)

# Django view to create a new user
def create_user_view(request):
    User.objects.create(username="new_user")
    return HttpResponse("User creation attempted")

###When you call the create_user_view, the user will not be created because the transaction is rolled back due to the signal.
###This confirms that Django signals run in the same transaction as the caller, as the signal's rollback affects the transaction initiated by the view.