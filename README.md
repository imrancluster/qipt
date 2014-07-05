QIPT
====

qipt-quantum ip telephony's user management system. It's a very small django app.
I made it for linux centos asteristik ip telephony user management system.

Installation process
====================

01) I have uploaded a database into this repository database-bk/qipt.sql.zip, extract it and upload into your mysql server.<br />
02) Now we have to set gmail email backend settings in settings.py, the following info-

<pre>
#For send mail configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Email Backend Settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'example@gmail.com'
EMAIL_HOST_PASSWORD = 'email password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
</pre>

03) Now time to run project using the following command - 

<pre>
>>python manage.py runserver

Validating models...

0 errors found
May 27, 2013 - 00:40:45
Django version 1.5c1, using settings 'qipt.settings'
Development server is running at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
</pre>

04) Copy http://127.0.0.1:8000/ and paste into your browser. 


Note :
=====
Please don't click "SIP File" and "Apply Zone" link. Because It's a linux asteristik file that is not present here.

--
Thank You


