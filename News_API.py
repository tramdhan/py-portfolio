import requests
from send_email import send_email

api_key = "925661043211420f8f68b6f9acb9646f"
country = "us"
category = "technology"
keyword = "python"
# url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}"
url = f"https://newsapi.org/v2/everything?q={keyword}&language=en&sortBy=publishedAt&pageSize=20&apiKey={api_key}"

request = requests.get(url)
content = request.json()

#  articles: title, description, publishedAt, content, source
body = "Subject: Python News" + "\n"
for article in content["articles"][:10]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["publishedAt"] + "\n" \
               + article["url"] + 2*"\n"

body =  body.encode("utf-8")

send_email(message=body)
