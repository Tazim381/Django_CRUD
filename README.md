# This application contains
## CRUD
## Custom Validation
## Custom Middleware
## Django Signal
## Emailing System 


# How to add singnal:  
## 1. First Create a signals.py file   
Then added this similar things for your project  
```
from . models import Student  
from django.db.models.signals import post_save, post_delete  
from django.dispatch import  receiver  

@receiver(post_save,sender=Student)  
def create_update_signal(sender,instance,created,**kwargs):  
    if created:  
        print(f"Student Created signal is called")  
    else:  
    print("Student Updated Signal is Called")  
```
## 2. Change apps.py file add ready function to the file   
```
 def ready(self):  
        import FormApp.signals   
```


# How to add custom Validator into Models
## Here is the example code 
```
from django.db import models
from django.core.exceptions import ValidationError

def validate_roll(value):
    if not value.isdigit():
        raise ValidationError('Roll must contain only digits')


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=20, null=True, validators=[validate_roll])
    email = models.EmailField(max_length=100, null=True)
    department = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

```

# How messages middleware, message context processor works.  
## 1. Include messages
from django.contrib import  messages  

## 2. Write success and error message  
  messages.success(request,'Email sent successfully')  
  ages.error(request,'All fields are required')  

## 3. Print message to to UI
```
  {% for msg in messages %}
        {{ msg }}
    {% endfor %}
```


# How send email works  
## 1. Configure SMTP (change settings.py) file
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER ='tazim@divine-it.net'
EMAIL_HOST_PASSWORD = 'XXXXXXXXXX'
```

## 2. Use send_mail() function for sending message:
```
from django.core.mail import send_mail
send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
```
