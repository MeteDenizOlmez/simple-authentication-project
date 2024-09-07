HOST = "localhost"
USERNAME = "authentication_project"
PASSWORD = ""
DATABASE = "authentication_project"

MAIL_USERNAME = ""
MAIL_PASSWORD = ""


from fastapi import FastAPI
from pydantic import BaseModel
import MySQLdb
from fastapi.middleware.cors import CORSMiddleware

#imports for mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = FastAPI() #create a fastapi instance


origins = [
    "http://localhost",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#A "schema" is a definition or description of something. Not the code that implements it, but just an abstract description.

#The term "schema" might also refer to the shape of some data, like a JSON content.
#In that case, it would mean the JSON attributes, and data types they have, etc.


#Operations:
#POST, GET, PUT, DELETE (use POST for destructive actions like creation, editing, deletion / use GET in the address bar...)
#OPTIONS, HEAD, PATCH, TRACE

#IMPORTANT:
"""
POST is also more secure than GET, because you aren't sticking information into a URL.
And so using GET as the method for an HTML form that collects a password or other sensitive
information is not the best idea.
"""

class Credentials(BaseModel):
    email: str
    password: str


def EmailVerification(email):
    me = MAIL_USERNAME   #FROM - DO NOT CHANGE THIS!!!!!!!!!!!
    #-----------TO:-------------
    you = email    #Recipient
    #---------------------------

    # Create message properties
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Recent Log-in Attempt"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (plain + html)
    text = """
    There was recently a log-in made to your account. Please change your password if this wasn't you!
    """

    html = """\
    There was recently a log-in made to your account. Please change your password if this wasn't you!
    """

    

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    #GMAIL ONLY-----------

    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login(MAIL_USERNAME, MAIL_PASSWORD)
    mail.sendmail(me, you, msg.as_string())
    print("mail sent.")




@app.post("/login/") #@something <- this is called a decorator - "path operation decorator"
def login(credentials: Credentials):
    
    #connect to db
    connection = MySQLdb.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        db=DATABASE
    )
    
    returned=""
    cursor = connection.cursor()
    try:
        # cursor.execute(f'SELECT email FROM authentication_project.users WHERE email=? AND password=?', [f"{credentials.email}",f"{credentials.password}"])
        cursor.execute(f"SELECT email FROM users WHERE email=%s AND password=%s", [credentials.email, credentials.password])
        for row in cursor.fetchall():
            returned = row[0]
        
    except:
        pass
    cursor.close()
    connection.close()

    if returned == "":
        return {
            "message": "CREDENTIALS INVALID"
        }
    else:
        EmailVerification(credentials.email)
        return {
            "message": "CREDENTIALS VALID"
        }
