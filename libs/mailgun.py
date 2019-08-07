import os
import env
from typing import List
from requests import Response, post
from libs.strings import gettext




# Custom exception with customized message
class MailGunException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class Mailgun:
    MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN')
    MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
    FROM_TITLE = "Bookstore REST API"
    MAILGUN_EMAIL = os.environ.get('MAILGUN_EMAIL')

    @classmethod
    def send_email(cls, email: List[str], subject: str, text: str, html: str) -> Response:
        if cls.MAILGUN_API_KEY is None:
            raise MailGunException(gettext("mailgun_failed_load_api_key"))

        if cls.MAILGUN_DOMAIN is None:
            raise MailGunException(gettext("mailgun_failed_load_domain"))

        response = post(
            f"https://api.mailgun.net/v3/{cls.MAILGUN_DOMAIN}/messages",
            auth=("api", cls.MAILGUN_API_KEY),
            data={
                "from": f"{cls.FROM_TITLE} <{cls.MAILGUN_EMAIL}>",
                "to": email,
                "subject": subject,
                "text": text,
                "html": html
            },
        )

        if response.status_code != 200:
            raise MailGunException(gettext("mailgun_error_send_email"))

        return response
