from email.message import EmailMessage
import smtplib
class email:
    def sender(self,email_to,user_name):
        email = EmailMessage()
        email["from"] = 'GAME USER'
        email["to"] = email_to
        email["subject"] = "THANK'S NOTE"
        email.set_content(f"{user_name} thank's for registering for game")
        
        with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("testingemail7127@gmail.com", 'nikhilvarma7127@gmail')
            smtp.send_message(email)
            print("send sucessfully")
if __name__ == "__main__":
    e = email()
    e.sender("nikhilvarma7127@gmail.com","nikhil varma")
