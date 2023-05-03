import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

# url = "https://www.work.ua/jobs-kyiv/"
#
headers = {
    "Accept": "*/*",
    "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
# req = requests.get(url)
# src = req.text
# # print(src)
# with open('index.html', 'w', encoding='utf-8') as file:
#     file.write(src)
# with open("index.html", encoding='utf-8') as file:
#     src = file.read()
# soup = BeautifulSoup(src, 'lxml')
# all_products_hrefs = soup.find_all(class_="card card-hover card-visited wordwrap job-link js-hot-block")
#
# all_profession_dict = {}
# for item in all_products_hrefs:
#     item_title = item.h2.a.get('title')
#     item_url = "https://www.work.ua" + item.h2.a.get('href')
#     all_profession_dict[item_title] = item_url
# with open('all_profession_dict.json', 'w',) as file:
#     json.dump(all_profession_dict, file, indent=4, ensure_ascii=False)
with open('all_profession_dict.json',) as file:
    all_profession = json.load(file)
count = 0
for category_name, category_url in all_profession.items():
        rep = [',', ' ', '-']
        for item in rep:
            if item in category_name:
                category_name = category_name.replace(item, '_')

        req = requests.get(url=category_url)
        src = req.text
        with open(f'data/{count}_{category_name}.html', 'w', encoding='utf-8') as file:
            file.write(src)
        with open(f'data/{count}_{category_name}.html', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        job_description = soup.find_all(id='job-description')
        job_description_json = []
        for item in job_description:
            job_description_json.append(item.text + '\n')
        with open(f'data_json/{count}_job_description.json', 'w', encoding='utf-8' ) as file:
            json.dump(job_description_json, file, indent=2, ensure_ascii=False)

        count += 1