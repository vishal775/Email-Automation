# Version 2.0.1

   **Email-Automation**
   Sending mail **professionally** using python with N number of **attachments and without attachments with all confirmations**

**!!!  IMPORTANT NOTES  !!!**

    1) Create a folder and extract the python file.
    2) Check your internet connectivity before running your code since the program is coded to send mail.

**!!!  REQUIRED PYTHON PACKAGES   !!!**

    import smtplib, ssl
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import urllib.request
    import time
    import smtplib
    from email.message import EmailMessage
    import os
    import shutil
    

**Do check all the libraries are installed properly if you are using offline software for python (like IDLE, Pycharm etc.,)**

**HOW TO RUN THE CODE OR THE PROCEDURE TO GET THE OUTPUT**

   1) There are **_2 steps_** to to run this code 
   2) **_Step 1_** - Go to 'Manage your Google Account' setting and click on 'Security'.
        * Turn on the '2-Step Verification' with the user credentials.
        * It is always safe to turn on 2-Step Verification for your google gmail account.
   3) **_Step 2_** - Again go to 'Manage your Google Account' setting and click on 'Security'.
        * just below '2-Step Verification' you have 'App passwords'.
        * Click on select app and give custom name of yours and click on generate.
        * You will get 16-digit 'Your app password for your device' copy it.
        * Now open Email.py in editor mode paste it in YOUR_PASSWORD_ and also give your email-id for which you generated 16-digit in YOUR_EMAIL-ID_ (_line number: 39,41,74,76,181,183_)
   4) Now Run the code 

# _License & Copyrights_

_© Vishal J M, Sri Ramakrishna Engineering College_
