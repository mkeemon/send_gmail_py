import smtplib
from config import config


def main():


    server = connect()

    contacts = get_csv_contents(config['csv_fname'])
    contacts.pop(0) #get rid of headings row

    for c in contacts:
        (sender, recipient, content) = get_email(c)
        server.sendmail(sender, recipient, content)

    server.quit()


def connect():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(config['username'],config['password'])
    return server

def get_email(contact):
    #contact format:
    #contact = [company, name, email]

    sender = config['username']+'@gmail.com'

    company = contact[0]
    recip_name = contact[1]
    recipient = contact[2]

    msg = get_email_msg(recip_name, config['sender_name'], company)


    headers = ["From: "     + sender,
               "Subject: "  + config['email_subject'],
               "To: "       + recipient]

    headers = "\r\n".join(headers)

    content = headers + "\r\n\r\n" + msg

    return (sender, recipient, content)

def get_csv_contents(fname):
    contents = []
    file = open(fname, 'r')
    for line in file:
        contact = line.split(',')
        contents.append(contact)
    file.close()
    return contents


def get_email_msg(recipient, sender, company):
    file = open(config['template_fname'], 'r')
    msg = file.read()
    file.close()

    #replace fields
    msg = msg.replace('__RECIPIENT__', recipient)
    msg = msg.replace('__SENDER_NAME__', sender)
    msg = msg.replace('__COMPANY__', company)

    return msg

if __name__ == "__main__":
    main()
