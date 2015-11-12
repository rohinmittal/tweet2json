#tweet2json

This code retrieves tweets from your twitter account and convert them to JSON format. 

<b>How to setup / run:</b><br>
a) Create a twitter account if you do not already have one.<br>
b) Go to https://apps.twitter.com/ and log in with your twitter credentials.<br>
c) Click "Create New App"<br>
d) Fill out the form, agree to the terms, and click "Create your Twitter application"<br>
e) In the next page, click on "API keys" tab, and copy your "API key" and "API secret".<br>
f) Scroll down and click "Create my access token", and copy your "Access token" and "Access token secret".<br>
g) Enter all these details in 'streamClass.py'<br>
i) In your terminal, execute "python run.py"<br>

<b>Output:</b><br>
The data will be dumped in your terminal in JSON format.

<b>Configure:</b><br>
You can update the run.py file to fetch only those tweets which have a specific word or multiple words. <br><br><i>The given code dumps only those "english" tweets which have "apple", "facebook" or "microsoft" in them. </i>
