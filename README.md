# Gmail Filter Solution
Simple Python app that interacts with Gmail API to filter out all of your emails in the last 24 hours depending on the allowed/blocked senders in blacklist.txt and whitelist.txt files. wildcards are also allowed for greater flexibility of filtering out a wider sender domain. This app is intended to be run for users with a valid Gmail account and have access to a Google Cloud environment. I have this service run as a Cloud Run container service on GCP that gets triggered to run via HTTP daily using a Cloud Scheduler Job while securing my secrets with GCP secret manager and reference it in my code as environmental variables. 

## Run
### 1.)
to run this
