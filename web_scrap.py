import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

# for multiple urls
for i in range(1, 10):
    URL = 'https://islamqa.info/en/answers/' +str(i)
    page = requests.get(URL)
    if(page.status_code == 200):
        print('Data fetched successfully ', i)
        soup = bs(page.content,'html.parser')
        questionanswer = soup.find_all(attrs= {'class':'content'})
        summary = soup.find(attrs={"class":'title is-4 is-size-5-touch'}).text.replace('\n', '').replace(' ','')
        QuestionNo = int(soup.find(attrs={"class":'subtitle has-text-weight-bold has-title-case cursor-pointer tooltip'}).text.replace('\n',''))
        source = soup.find(attrs={'class':'subtitle is-6 has-text-weight-bold is-capitalized'}).text.replace('\n','').replace('Source:','').replace(' ','')
        data.insert(QuestionNo, [url, QuestionNo, summary, source ])
    else:
        print('URL Not Found', i)
df = pd.DataFrame(data, columns=['url', 'Question #', 'Summary', 'Source'])
df.to_csv('pagedata.csv')
