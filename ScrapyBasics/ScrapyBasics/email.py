import smtplib

class Email():
    
    def send_email(self, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('notifymebarranquilla@gmail.com', 'NOTIFYME2020')
        subject = 'New fines for your monitored plates'
        body = 'You have new fines for your monitored plates, please visit the official site: https://portal.barranquilla.gov.co/ConsultaEstadoCuenta/consultaPlaca'
        msg = f"Subject: {subject}\n\n{body}\n\n{message}"        
        server.sendmail(
            'notifymebarranquilla@gmail.com',
            'maurogzsa@gmail.com',
            msg
        )
        server.quit()