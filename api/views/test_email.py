"""style view"""

from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from django.core.mail import EmailMessage


class EmailView(ViewSet):
    """Email views"""

    def list(self, _):
        """test sending email for Muka"""

        email = EmailMessage(
            'Test for Muka',  # Email subject
            'This is a test',  # Email message
            'help.muka@gmail.com',  # Sender email
            ['help.muka@gmail.com'],
            # List of recipient emails, add yours if you'd like otherwise it's just sending to itself
        )

        email.send()

        return Response({'message': 'Email Sent!'}, status=status.HTTP_204_NO_CONTENT)
