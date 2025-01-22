# get news from API and parse
import requests
from dotenv import load_dotenv
import os
from constants import KNOWLEDGE_CUTOFF_DATE, NEWS_ARTICLES_PLAN_LIMIT
import newspaper   
import json

def get_news(q):
    load_dotenv()
    api_key = os.getenv("THE_NEWS_API_TOKEN")
    print('api_key',api_key)
    params = {
        "api_token":api_key,
        "language":"en",
        "limit":NEWS_ARTICLES_PLAN_LIMIT,
        "search":q,
        "published_before":KNOWLEDGE_CUTOFF_DATE,
        "sort": True
        }
    url = "https://api.thenewsapi.com/v1/news/all"
    response = requests.get(url, params=params).json()
    print("\n\nAPI RESPONSE:\n\n",json.dumps(response, indent=4))
    #print("API RESPONSE Found#:\n\n",response["found"])
    result = []
    if len(response) > 0:
        for r in response["data"]:
            try:
                article = newspaper.article(r["url"])
                print("Article Text:\n",article.text)
                print("\n\n")
                result.append(article.text)
            except:
                print("failed to get from", r["title"])
                print("url:",r["url"])
                continue
    return result
#get_news('Who is winning the 2024 election')