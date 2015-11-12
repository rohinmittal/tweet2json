#tweet2json

This code fetches tweets from your twitter account and convert them to JSON format. To run the code, you need to do the following:

a) Create a twitter account if you do not already have one.
b) Go to https://apps.twitter.com/ and log in with your twitter credentials.
c) Click "Create New App"
d) Fill out the form, agree to the terms, and click "Create your Twitter application"
e) In the next page, click on "API keys" tab, and copy your "API key" and "API secret".
f) Scroll down and click "Create my access token", and copy your "Access token" and "Access token secret".
g) Enter all these details in 'streamClass.py'
i) In your terminal, execute "python run.py"

The data will be dumped in your terminal in JSON format.

You can update the run.py file to fetch only those tweets which have a speciific word or multiple words. The given code dumps only those "english" tweets which have "apple", "facebook" or "microsoft" in them. 
