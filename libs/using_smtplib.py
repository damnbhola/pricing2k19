import smtplib

_subject = ''
_from = ''
_password = ''
_to = ''
_msg = ''


def send_mail():
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(_from, _password)

    s.sendmail(_from, _to, _msg)
    print("Hey email has been sent")
    s.quit()


send_mail()
