# simple-authentication-project (WORK IN PROGRESS - NOT COMPLETE)
* For a long time I was interested in some of the aspects of account management and authentication systems of many big websites including how multi-factor authentication methods work etc. This is my first real attempt at trying to recreate some of the easier and simpler aspects of these systems such as: Log-in, Log-out, E-Mail Verification, Auth Tokens...
* Throughout making parts of this project, I learned many things about sending E-mails programmatically, practiced my SQL knowledge and started learning small bits of JavaScript as well as using and creating REST APIs through Python and JavaScript
* To help me make the API used in this, I have used the Python FastAPI module
* NOTE: this is nowhere near production level quality and there are some obvious key aspects of user authentication still missing. This project was mainly a way for me to practice my programming and learn new things through things that interest me such as user authentication.

# Improvements (other than the obvious ones)
* Most importantly in the future this could be improved by adding some sort of encryption and hashing system to ensure cruical data such as PASSWORDS or TOKENS are not stored as plain text but instead are encrypted and hashed, like in the real world (This project is overall simplified in some areas regarding database security)
* Since I do not own an SSL certificate nor a Domain at this moment in time, I can't test the usage of the REST API over HTTPS so this could be a vulnerability since data is not encrypted as it travels from client to server

# Here is an image showcasing some of the plans and my thought process of how things could work before starting this project
![image](https://github.com/user-attachments/assets/e196148a-b942-471f-a4f4-a5819048f7c3)

# This is a WIP (Work In Progress) preview of what has been done so far:
Video:

1) Client-side JS code makes a POST request to the server-side Python code with the appropriate username and password entered
2) Server-side python program then compares this to values found in the database to ensure they match, and if so, a result of valid is returned to the JS Client through the API and the python program also proceeds to send an e-mail confirming the login attempt
3) If credentials not found, an invalid result is returned to the JS client and a message is displayed
-----Future:-------
   - Continue by adding a code to the email that is sent to get the client to verify the code by typing it out and comparing them to ensure they are who they say they are...
