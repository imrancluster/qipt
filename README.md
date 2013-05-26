qipt
====

qipt-quantum ip telephony's user management. It's a very small django app. 
I made it for linux centos asteristik ip telephony user management. 

Installation process
====================

01) I have uploaded a database into this repository database-bk/qipt.sql.zip, extract it and upload into your mysql server.
02) Now we have to set gmail email backend, the following info-

#For send mail configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Email Backend Settins
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'you gmail user name'
EMAIL_HOST_PASSWORD = 'you gmail email password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

03) Now time to run project using the following command - 


python manage.py runserver

Validating models...

0 errors found
May 27, 2013 - 00:40:45
Django version 1.5c1, using settings 'qipt.settings'
Development server is running at http://127.0.0.1:8000/
Quit the server with CONTROL-C.


04) Copy http://127.0.0.1:8000/ and paste into your browser. 


Note :
=====
Please don't click "SIP File" and "Apply Zone" link. Becouse It's a linux asteristik file that is not presend here.

This is my first small app. so don't mind If you see some problems. 

--
Thank You


