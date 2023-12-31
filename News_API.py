import requests
from send_email import send_email

api_key = "925661043211420f8f68b6f9acb9646f"
country = "us"
category = "technology"
url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}"

request = requests.get(url)
content = request.json()

#  articles: title, description, publishedAt, content, source
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + str(article["title"]) + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
user_email = "trevorr@rogers.com"

# From: {user_email}

message = f"""\
Subject: Daily News
{body}
"""

send_email(message=body)