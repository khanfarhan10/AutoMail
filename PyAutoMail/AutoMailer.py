"""
python PyAutoMail/AutoMailer.py
"""

import os

ROOT_DIR = os.getcwd()

def send_email():
    return 0
    

"""
import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls() 
# Authentication 
s.login("sender_email_id", "sender_email_id_password") 
# message to be sent 
message = "Message_you_need_to_send" 
# sending the mail 
s.sendmail("sender_email_id", "receiver_email_id", message) 
# terminating the session 
s.quit()
"""
