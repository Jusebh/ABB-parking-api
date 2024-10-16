import os
from azure.communication.email import EmailClient

connection_string = os.getenv("EMAIL_CONN_STRING")

def admin_mail(email_addresses: list, content, subject):
    email_client = EmailClient.from_connection_string(os.getenv("EMAIL_CONN_STRING"))
    recipents = []
    for address in email_addresses:
        recipents.append({"address": f"<{address}>"})
    message = {
        "content":{
            "subject": subject,
            "text": content
        },
        "recipients":{
            "to": recipents
        },
        "senderAddress": os.getenv("AZURE_MAIL")
    }
    
    poller = email_client.begin_send(message)
    print(poller.result())
