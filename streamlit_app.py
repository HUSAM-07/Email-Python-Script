import smtplib
import csv

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'YOUR_EMAIL@gmail.com' #<----------------# Enter your gmail Email address here##########

PASSWORD = 'YOUR PASSWORD'  #<----------------# Enter your gmail password here##########


def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = []
    emails = []
    contacts_file = open(filename)
    contactslist = csv.reader(contacts_file)
    for contact in contactslist:
        names.append(contact[0])
        emails.append(contact[1])
    return names, emails


def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def main():
    names, emails = get_contacts('YOUR FILE PATH OF Connections.csv')  # read contacts
    message_template = read_template('YOUR FILE PATH TO message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "Let's {grow} to gether - Test Automation | RPA | Freelancing "  ### CHANGE THE SUBJECT OF THE EMAIL HERE###

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == '__main__':
    main()