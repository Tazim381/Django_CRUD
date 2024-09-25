from . models import Student
from django.db.models.signals import post_save, post_delete
from django.dispatch import  receiver

@receiver(post_save,sender=Student)
def create_update_signal(sender,instance,created,**kwargs):
    if created:
        print(f"Student Created signal is called")
    else:
        print("Student Updated Signal is Called")

@receiver(post_delete,sender=Student)
def delete_signal(sender,instance,**kwargs):
    print(f"Student with ID {instance.id} was deleted. Delete singal is called")