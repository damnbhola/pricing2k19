import os
from requests import Response, post
from typing import List


class Mailgun:
    MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY', None)
    MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN', None)
    FROM_NAME = 'Pricing Service'
    FROM_EMAIL = 'do-not-reply@sandbox74ea290b6b1043f7b89a44830a239891.mailgun.org'

    @classmethod
    def send_email(cls, to_emails: List[str], subject: str, content: str, html: str) -> Response:
        api_key = os.environ.get('MAILGUN_API_KEY', None)
        domain = os.environ.get('MAILGUN_DOMAIN', None)
        if api_key is None:
            print("Failed to load Mailgun Api Key.")
        if domain is None:
            print("Failed to load Mailgun Domain.")
        response = post(domain,
                        auth=("api", api_key),
                        data={"from": f"{cls.FROM_NAME} <{cls.FROM_EMAIL}>",
                              "to": to_emails,
                              "subject": subject,
                              "text": content,
                              "html": html})
        if response.status_code != 200:
            print("An error occurred while sending e-mail.")
        print(response.json())
        return response


"""
print(Mailgun.send_email(to_emails=['damanbhola1022@gmail.com'],
                         subject='Test e-mail',
                         content='This is a test e-mail',
                         html="<p>This is a html text.</p>"))
"""
