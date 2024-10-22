import os
from azure.communication.email import EmailClient

connection_string = os.getenv("EMAIL_CONN_STRING")

def new_reservation_mail(email_adress, days: list):
  try:
    string = ""
    for day in days:
      string += (str(day) + ", ") 
    email_client = EmailClient.from_connection_string(os.getenv("EMAIL_CONN_STRING"))
    message = {
          "content":{
              "subject": "Informacja dotycząca twoich nowych rezerwacji.",
              "html": f"""  <div style="background-color: #f6f6f6">
      <h1 style="background-color: #d9d9d9; color: rgb(95, 90, 90)">Witaj!</h1>
      <p>
        Twoje rezerwacje na dni {string} zostały przyjęte w systemie.
      </p>
      <p>
        Oczekuj dalszych informacji na temat ich statusów.
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
  except:
    print("Something went wrong!")