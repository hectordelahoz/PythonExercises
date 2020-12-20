import smtplib

def send_email(receiver,subject,bodymessage):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('notifymebarranquilla@gmail.com', 'Notify@2020')
    msg = f'Subject: {subject}\n\n{bodymessage}'        
    server.sendmail(
        'notifymebarranquilla@gmail.com',
        'hectordelahoz@gmail.com',
        msg
    )
    server.quit()

def main():
 send_email('hectordelahoz@gmail.com','test', 'this is a test - my name is hector')

if __name__ == '__main__':
    main()