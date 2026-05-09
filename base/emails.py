from django.conf import settings
from django.core.mail import send_mail
 

def contact_mail(sender_name, sender_email, subject, message, full_name):
    email_from = settings.EMAIL_HOST_USER

    mail_subject = f"New Portfolio Message from {sender_name}"

    mail_message = f"""
Hello {full_name},

You’ve received a new message through your portfolio website.

--- Contact Details ---
Name: {sender_name}
Email: {sender_email}
Subject: {subject}

--- Message ---
{message}
------------------

Please respond to the sender directly at: {sender_email}

Best regards,  
Your Portfolio System
"""

    send_mail(mail_subject, mail_message, email_from, [email_from])
    
    
def auto_reply_mail(sender_name, sender_email, subject, message, full_name):
    email_from = settings.EMAIL_HOST_USER
    mail_subject = f"Thanks for reaching out to {full_name}"
    message=(f"""
Hello {sender_name},

Thank you for reaching out to {full_name} via the portfolio website.

This is an automated confirmation that your message has been received. I will review your inquiry and get back to you as soon as possible.

--- Your Message ---
Subject: {subject}

{message}
--------------------

If your matter is urgent, feel free to follow up directly via email.

Best regards,  
{full_name}
""")
    send_mail(mail_subject, message, email_from, [sender_email])