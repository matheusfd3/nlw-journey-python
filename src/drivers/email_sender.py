import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_address, body):
    from_address = 'tcrauup3rl7zfgpv@ethereal.email'
    login = 'tcrauup3rl7zfgpv@ethereal.email'
    password = 'jVrVfje5e1aaup9WWe'

    message = MIMEMultipart()
    message['From'] = 'viagens_confirmar@email.com'
    message['To'] = ', '.join(to_address)

    message['Subject'] = 'Confirmação de participação em viagem'
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.ethereal.email', 587)
    server.starttls()
    server.login(login, password)
    text = message.as_string()

    for email in to_address:
        server.sendmail(from_address, email, text)
    
    server.quit()