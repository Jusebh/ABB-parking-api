import os
from azure.communication.email import EmailClient

connection_string = os.getenv("EMAIL_CONN_STRING")

def status_changed_mail(email_adress, date_of_reservation, new_status):
    if new_status == "Approved":
        new_status = "Potwierdzony"
    elif new_status == "Rejected":
        new_status = "Odrzucony"
    elif new_status == "Pending":
        new_status = "Oczekujący"
    elif new_status == "Cancelled":
        new_status = "Anulowany"
    email_client = EmailClient.from_connection_string(os.getenv("EMAIL_CONN_STRING"))
    message = {
        "content":{
            "subject": "Status twojej rezerwacji uległ zmianie",
            "html": f"""  <div style="background-color: #f6f6f6">
    <h1 style="background-color: #d9d9d9; color: rgb(95, 90, 90)">Witaj!</h1>
    <p>
      Status twojej rezerwacji na dzien <strong>{date_of_reservation}</strong> zmienił się na "{new_status}".
    </p>
  </div>"""
        },
        "recipients":{
            "to": [
                {
                    "address": email_adress
                }
            ]
        },
        "senderAddress": os.getenv("AZURE_MAIL")
    }
    
    poller = email_client.begin_send(message)
    print(poller.result())
