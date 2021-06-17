import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import urllib.request
import time
import smtplib
from email.message import EmailMessage


def name():
    a = input("Enter the content :")
    contconfirm(a)

def noattach(l,k,a):
    print('To : '+k+'\nSubject : '+l+'\nContent : '+a)
    subject = l
    msg_body = a
    sender = "YOUR_EMAIL-ID_"
    reciever = k
    password = 'YOUR_PASSWORD_'
    # action
    msg = EmailMessage()
    msg['subject'] = subject 
    msg['from'] = sender
    msg['to'] = reciever
    msg.set_content(msg_body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender,password)
        
        smtp.send_message(msg)
    print('Email Sent')
 
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

def review(k,a):
    l = input('Enter the subject :')
    attcon(l,k,a)

def send(l,k,a):
    print('To : '+k+'\nSubject : '+l+'\nContent : '+a)
    subject = l
    body = a
    sender_email = "YOUR_EMAIL-ID_"
    receiver_email = k
    password = 'YOUR_PASSWORD_'

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
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
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)

    a=input('Enter how many file you want to attach:')
    l=[]
    for i in range(0,int(a)):
        filename=input('Enter the file '+str(i+1)+' path:')
        l.append(filename)
    d = len(l)
    for j in range(0,int(d)):
        k=l
        print('Sending file '+ str(j+1)+' from path '+l[j])
        v = l[j]
        attach(v)
    print('Email Sent')
def fromemail():
    d = input('Enter FROM E-MAIL ID :')
    return d

def recemail():
    e = input('Enter RECIVER E-MAIL ID :')
    return e 

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
