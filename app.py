# get the lib ... 
import openai
# ...
import os
# ...
import requests
# ...
import bs4
# ------------------------------------------------
#   API
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("API_KEY")

# test 
# print(openai.api_key) # success ... 
# get sites 
news_sites = {
    "chinese": ("https://cn.chinadaily.com.cn", "div.Home_content_Item_Text h1 a"),
   "arabic": ("https://aljazeera.net", "h3.fte-article__title")
}
# test sites ... 
# print(news_sites['china']) #success ... 
# -----------------------------------------------
# user lang ... 
user_language = input("what language are you interested in hearing news headlines summarised in?")
# selected_url = news_sites.get(user_language, "Language not supported")
# print(selected_url)
# ---------------------------------------------------------------------- 
# get data ... 
# response = requests.get(selected_url)
# test .. 
# print(response.text) # success 
# lib ... initial 
# soup = bs4.BeautifulSoup(response.text, 'lxml')   
# test soup .. 
# print(soup.select('div.Home_content_Item_Text h1 a'))
# ------- --------------------------------------------- 
# fun ... 
def fetch_headlines(language):
    url, tag = news_sites.get(language, (None, None))
    if not url:
        print("Language not supported")
        return
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'xml')
    headlines = [h.getText() for h in soup.select(tag)[:5]]
    return headlines
selected_headlines = fetch_headlines(user_language)
print(selected_headlines)
# .....................................................................
# fun ... 
def create_prompt(headlines):
    joined_headlines = "\n".join(headlines)
    prompt = f"Translate the following headlines into English:\n{joined_headlines}"
    return prompt

# test ... 
# print(create_prompt(selected_headlines))
# .....................................................................
# fun 0101 
prompt = create_prompt(selected_headlines)
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.1,
    max_tokens=200
)

print(response['choices'][0]['text'])
# .....................................................................