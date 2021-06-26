#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                     SEND EMAIL USING COMMAND PROMPT (cmd)                        #
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import urllib.request
import time
from email.message import EmailMessage
import os
import shutil 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Storing the email which is not send, as backup and send if internet is connected
def storetoretrive(l,k,a):
    try:
        os.mkdir('Mail_Not_Send')
        with open('Mail_Not_Send/subject.txt', 'w') as f:
            f.write(l)
        f.close()
        with open('Mail_Not_Send/reciever.txt', 'w') as b:
            b.write(k)
        b.close()
        with open('Mail_Not_Send/msg_body.txt', 'w') as n:
            n.write(a)
        n.close()
        print('Email saved')
    except:
        print('It seems you already have unsent emails')

# Send Email without attachments
def noattach(l,k,a):
    try:
        print('To : '+k+'\nSubject : '+l+'\nContent : '+a)
        subject = l
        msg_body = a
        sender = "YOUR_EMAIL-ID_" # Check you have filled this required data
        reciever = k
        password = 'YOUR_PASSWORD_' # Check you have filled this required data
        # action
        msg = EmailMessage()
        msg['subject'] = subject 
        msg['from'] = sender
        msg['to'] = reciever
        msg.set_content(msg_body)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender,password)
            smtp.send_message(msg)
            print('======================================+++++++++++++++++++=======================================')
            print('\t\t\t\t\tEmail Sent')
            print('======================================+++++++++++++++++++=======================================')
    except:
            print('Check you internet connection or please verify the app password for your mail id in the script')
            print('======================================+++++++++++++++++++=======================================')
            print('\t\t\t\t\tEmail not Sent')
            print('======================================+++++++++++++++++++=======================================')
            storetoretrive(subject,reciever,msg_body)
            

def getinfore(m):
    f = open(m, "r")
    rep = f.readlines()
    r=str(rep).replace('[','')
    r=str(r).replace(']','')
    r=str(r).replace("'",'')
    return r

def sendwiatt(l,k,a):
    print('To : '+k+'\nSubject : '+l+'\nContent : '+a)
    subject = l
    body = a
    sender_email = "YOUR_EMAIL-ID_" # Check you have filled this required data
    receiver_email = k
    password = 'YOUR_PASSWORD_' # Check you have filled this required data

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  
    message.attach(MIMEText(body, "plain"))

    def attach(filename):
        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)
        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()
        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        se = os.listdir(path='Files_to_send')
        if count == len(se):
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)
    nose = os.listdir(path='Files_to_send')
    global count
    count=0
    for i in range(0,len(nose)):
        fename="Files_to_send/"+nose[i]
        count+=1
        attach(fename)
        print('======================================+++++++++++++++++++=======================================')
        print('\t\t\t\tFile sent '+ str(i+1)+' successfully')
        print('======================================+++++++++++++++++++=======================================')
    
# Sending email which is not send
def sendretrived():
    sub ="Mail_Not_Send/subject.txt"
    subjectre = getinfore(sub)
    rev ="Mail_Not_Send/reciever.txt"
    reciverre = getinfore(rev)
    msg ="Mail_Not_Send/msg_body.txt"
    msgre = getinfore(msg)
    os.remove("Mail_Not_Send/subject.txt")
    os.remove("Mail_Not_Send/reciever.txt")
    os.remove("Mail_Not_Send/msg_body.txt")
    try:
        sendwiatt(subjectre,reciverre,msgre)
        print('======================================+++++++++++++++++++=======================================')
        print('\t\t\t\t\tEmail Sent')
        print('======================================+++++++++++++++++++=======================================')
        shutil.rmtree('Files_to_send')
        shutil.rmtree('Mail_Not_Send')
    except:
        noattach(subjectre,reciverre,msgre)
        print('======================================+++++++++++++++++++=======================================')
        print('\t\t\t\tEmail sent successfully with no attachments given')
        print('======================================+++++++++++++++++++=======================================')
        shutil.rmtree('Files_to_send')
        shutil.rmtree('Mail_Not_Send')
        
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# If internet connection is present
print('|======================+++++++++++++++++++++++++++++++++++++=======================|')
print('|                      SEND EMAIL USING COMMAND PROMPT (cmd)                       |')
print('|======================+++++++++++++++++++++++++++++++++++++=======================|')
def name():
    a = input("Enter the content :")
    if a == 'not send' or a == 'not sent':
        sendretrived()
    else:
        contconfirm(a)
        
# add attachments
def attcon(l,k,a):
    m = input('Do you want to add attachment Y/N :')
    n = m.lower()
    if n == 'y' or n == 'yes':
        send(l,k,a)
    elif n == 'n' or n == 'no':
        noattach(l,k,a)
    else:
        print('Please the enter the valid information')
        attcon(l,k,a)

# Subject and verification
def review(k,a):
    l = input('Enter the subject :')
    attcon(l,k,a)

# Send email with attachments
def send(l,k,a):
    print('To : '+k+'\nSubject : '+l+'\nContent : '+a)
    subject = l
    body = a
    sender_email = "YOUR_EMAIL-ID_" # Check you have filled this required data
    receiver_email = k
    password = 'YOUR_PASSWORD_' # Check you have filled this required data
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email
    message.attach(MIMEText(body, "plain"))

    def attach(filename): 
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())  
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        message.attach(part)
        text = message.as_string()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
    try:
        a=input('Enter how many file you want to attach:')
        l=[]
        os.mkdir('Files_to_send')
        for i in range(0,int(a)):
            filename=input('Enter the file '+str(i+1)+' path:')
            l.append(filename)
        d = len(l)
        for m in range(0,int(d)):
            v = l[m]
            add = str(v).replace("\\",'/')  
            dest = 'Files_to_send'
            shutil.copy(add, dest)
        for j in range(0,int(d)):
            print('Sending file '+ str(j+1)+' from path '+l[j])
            v = l[j]
            attach(v)
            print('======================================+++++++++++++++++++=======================================')
            print('\t\t\t\tFile '+ str(j+1)+' sent successfully')
            print('======================================+++++++++++++++++++=======================================')
    except:
        print('Check you internet connection or please verify the app password for your mail id in the script')
        print('======================================+++++++++++++++++++=======================================')
        print('\t\t\t\t\tFile not sent')
        print('======================================+++++++++++++++++++=======================================')
        storetoretrive(subject,receiver_email,body)
        
# Get reciver mail-id        
def recemail():
    e = input('Enter RECIVER E-MAIL ID :')
    return e 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Content and other confirmations
def editcontent(a):
    print('Previous content : '+a)
    print('Please enter the content form first')
    c = input('Editing Content :')
    contconfirm(c)

def lasteditcontent(a):
    print('Previous content : '+a)
    print('Please enter the content form first')
    c = input('Editing Content :')
    return c

def noedit(k,a):
    i = input('1. RECIVER E-MAIL ID,\n2. CONTENT\n3. PROCEED FOR SUBJECT\nEnter SERIAL NUMBER you want to edit :')
    if i == '1':
        k = recemail()
        noedit(k,a)
    elif i == '2':
        l = lasteditcontent(a)
        noedit(k,l)
    elif i == '3':
        review(k,a)
    else:
        print('Please the enter the valid information')
        noedit(k,a)

def editfull(k,a):
    g = input('Do you want to confirm email-id Y/N :')
    h = g.lower()
    if h == 'y' or h == 'yes':
        review(k,a)
    elif h == 'n' or h == 'no':
        noedit(k,a)
    else:
        print('Please the enter the valid information')
        editfull(k,a)

def emailid(a):
    k = recemail()
    editfull(k,a)

def contconfirm(a):
    b = input('Do you want to sent this content Y/N :')
    f = b.lower()
    if f == 'y' or f == 'yes':
        emailid(a)
    elif f == 'n' or f == 'no':
        editcontent(a)
    else:
        print('Please the enter the valid information')
        contconfirm(a)
        
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#To check internet connection

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False

def internet():
    time.sleep(1)
    if connect():
        print('Internet Connected')
        name()
        
    else:
        print('No Internet Connection!')
        print('Retrying to connect')
        internet()
             
internet()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
