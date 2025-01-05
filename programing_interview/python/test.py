import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from msal import ConfidentialClientApplication

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'connectoajay@gmail.com'
smtp_password = 'drjqjmrqrxvwqyfz'

# Email content
from_email = smtp_username
to_email = 'ajaysingh@extremenetworks.com'
subject = 'Test Email from Python Script'
body = 'This is a test email sent from a Python script using SMTP authentication with Microsoft Outlook.'

# Create the email message
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    server.login(smtp_username, smtp_password)  # Log in to the SMTP server

    # Send the email
    server.sendmail(from_email, to_email, msg.as_string())
    print('Email sent successfully!')

except Exception as e:
    print(f'Failed to send email: {e}')

finally:
    # Close the connection to the SMTP server
    server.quit()
