import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from application.interfaces.email_service_interface import EmailServiceInterface

class EmailServiceImpl(EmailServiceInterface):
    def send_email(self, to_address: str, subject: str, body: str):
        sender_email = "tu_email@example.com"  
        sender_password = "tu_contraseña"  

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_address
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.example.com', 587)  
            server.starttls() 
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, to_address, text)
            server.quit()
            return True
        except Exception as e:
            print(f"Error al enviar el correo electrónico: {e}")
            return False
