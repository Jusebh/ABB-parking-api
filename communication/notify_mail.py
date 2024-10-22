import os
from azure.communication.email import EmailClient

connection_string = os.getenv("EMAIL_CONN_STRING")


def notify_mail(email_adress, date_of_reservation):
    email_client = EmailClient.from_connection_string(os.getenv("EMAIL_CONN_STRING"))
    message = {
        "content": {
            "subject": "Przypomnienie o rezerewacji parkingu",
            "html": f"""  <div style="background-color: #f6f6f6">
    <h1 style="background-color: #d9d9d9; color: rgb(95, 90, 90)">Witaj!</h1>
    <p>
      Przypominamy o twojej rezerwacji na dzien <strong>{date_of_reservation}</strong>.
    </p>
    <p>
      Jeżeli już wiesz, że tego dnia nie zjawisz się w pracy, prosimy o
      anulowanie swojej rezerwacji, możesz zrobić to z poziomu aplikacji
      moblinej lub po skontaktowaniu się z pracownikiem recepcji.
    </p>
  </div>""",
        },
        "recipients": {"to": [{"address": email_adress}]},
        "senderAddress": os.getenv("AZURE_MAIL"),
    }

    poller = email_client.begin_send(message)
    print(poller.result())
