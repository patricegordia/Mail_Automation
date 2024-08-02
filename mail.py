import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
USERNAME = 'yourmail'
PASSWORD = 'app_password'
FROM_EMAIL = 'yourmail'
TO_EMAIL = 'recipient'
SUBJECT = 'Daily Report'


# Create the email content
def create_email_content():
    # Customize the email content as needed
    report_content = "This is your daily report."
    return report_content


# Send email function
def send_email():
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = TO_EMAIL
        msg['Subject'] = SUBJECT

        # Attach the email body
        body = create_email_content()
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(USERNAME, PASSWORD)
            server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")


# Schedule the email to be sent daily
schedule.every().day.at("12:13").do(send_email)  # Change time as needed

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait a minute before checking the schedule again
