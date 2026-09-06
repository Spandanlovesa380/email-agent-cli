## Send Emails From The Terminal
This is Mailo, your helpful assistant who sends emails for you, straight from your Gmail account. 

"Send **recipient** an email asking him out on a coffee date. Make it sound cute. "

***Cloning Instructions***
 1. Clone the repository.
 2. Install requirements from *requirements.txt*
 3. Open Google Apps Script, create a new script, paste *gmail_bridge.gs*
 4. Click 'deploy' and go through the user flow, copy the url provided.
 5. You may be prompted to give access to your inbox.
 6. Configure .env (model is any local llm that you have running with Ollama)

```dotenv
APP_SCRIPT_URL=xyz  
MODEL=modelname
```

7. Run

```bash
python main.py
```

in your terminal and start prompting.

***Release 2026.0***: 
This is currently a bare minimum chatbot. It can reliably send emails when provided with the recipient's email and gist of email content. Currently it **does NOT ask for authorisation** before sending mails, so use at your own risk.

***Coming Up 2026.1***:
Authorisation before sending mails, context optimisation to make it more compatible and multiple recipients in to, cc and bcc are in the works and will be released soon.
