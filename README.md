

# How Signal Added:  
## 1. First Create a signals.py file   
Then added this similar things for your project  

from . models import Student  
from django.db.models.signals import post_save, post_delete  
from django.dispatch import  receiver  

@receiver(post_save,sender=Student)  
def create_update_signal(sender,instance,created,**kwargs):
    if created:  
        print(f"Student Created signal is called")  
    else:  
    print("Student Updated Signal is Called")  

## 2. Change apps.py file add ready function to the file   
 def ready(self):  
        import FormApp.signals   
