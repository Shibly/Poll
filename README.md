Poll
====
Online poll app is a django powered polling application influenced by Abu Ashraf Masnun's 
recent tutorial and official tutorial from Django's site. The app does a fairly simple job :). 
User will select a poll , choose an answer and vote it. An immediate result will be displayed 
just after the vote. The app uses django's builtin admin app and hook the poll app into it to 
provide an interface to perform CRUID operation on the app.


This app uses bootstrapped theme for the admin app. So you need to add it to the installed app. 
Download it from PyPi with 'pip install django-admin-bootstrapped'

Add 'django_admin_bootstrapped' into the INSTALLED_APPS list before 'django.contrib.admin'

You are done.
