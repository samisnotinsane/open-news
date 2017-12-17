"""
" Retrieves top 10 headlines from: https://news.ycombinator.com/
""" 
from urllib.request import urlopen
from bs4 import BeautifulSoup

page_url = "https://news.ycombinator.com/"
print("[INFO] - Fetching HTML, please wait...")
html_doc = urlopen(page_url)
soup = BeautifulSoup(html_doc, 'html.parser')
print("[INFO] - HTML loaded and parsed.")

print("[INFO] - Getting storylinks...")
print("-------------------------------------------")
print("Hackernews top 30:")
print("-------------------------------------------")
i=1
for story in soup.find_all('a', class_='storylink'): 
    print(str(i) + ': ' + story.get_text() + '  <<<' + story['href'] + '>>>')
    i+=1
    
# print( soup.title.prettify() )

# print(soup.title)

# title_box = soup.find(‘td’, attrs={‘class’: ‘title’})

# print(title_box)