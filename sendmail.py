import smtplib
import os 
import csv
import time
import schedule


from email.message import EmailMessage

def get_recpients():
    return ["adityasmulay@gmail.com", "sn2203adityamulay@gmail.com", "madhura.mulay@gmail.com"]


def send_mail():
    sender = "sn2203adityamulay@gmail.com"
    password = "ftsr dpag npek hcvu"

    recipients = get_recpients()

    for recipient in recipients:
        msg = EmailMessage()
        msg['subject'] = "How are you ??"
        msg['from'] = "sn2203adityamulay@gmail.com"
        msg['to'] = recipient
        msg.set_content("how are you ? Thos mail is sent using python code")

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender, password)
                server.send_message(msg)
                print(f"Mail sent to {recipient}")
        except Exception as e:
            print(f"Error sending to {recipient}: {e}")

def job():
    print("Running job of sending emails")
    send_mail()
    print("Job done")

schedule.every().monday.at("08:00").do(send_mail)

print("Schedule started sending emails every monday at 8 am ")

while True:
    schedule.run_pending()
    time.sleep(1)


# if __name__ == "__main__":
#     send_mail()
#     print("Mail sent")

