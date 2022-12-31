# Gmail Filter Solution
Simple Python app that interacts with Gmail API to filter out all of your emails in the last 24 hours depending on the allowed/blocked senders in blacklist.txt and whitelist.txt files. Wildcards are also allowed for greater flexibility of filtering out a wider sender domain. This app is intended to be run for users with a valid Gmail account and have access to a Google Cloud environment. I have this service run as a Cloud Run container on GCP that gets triggered to run via HTTP daily using a Cloud Scheduler Job while securing my secrets with GCP secret manager. Allowing me to reference it in my code as environmental variables. This app also allow a discord notification feature that'll alert me on the emails that were quarantined (sent to spam) and the emails that were caught as spam/phishing but was actually legitimate to inboxes. 

## Intructions
1.) Go to your Google Cloud Console. Hover to -> Credentials -> create Credentials -> OAuth client ID. Choose Desktop app for application type and click on create.

2.) After creation click on download credential Json file and save it in the same directory as this app and rename it as "credentials.json".

3.) Enable Gmail API in Google Cloud Console.

4.) Configure an OAuth consent screen for authorization and add your gmail account as a test users.

5.) Configure the secrets in the codes accordingly to your own such as your discord serverID, channelID, Token etc. If you don't wish to include discord notification you can simply comment the line out in gmail.py. Logs will be written out to "logfile.txt".

6.) Add your lists of senders you wish or wish not to receive from and add them to the whitelist and blacklist txt files.

7.) Install all the requirement libraries in requirements.txt

8.) Run app.py locally and authenticate to the consent screen to retrieve a json file with token informations in it.

## Local Docker
`docker build -t gmail-filter-app .`

`docker run -it --rm -p 8080:8080 gmail-filter-app:latest`
