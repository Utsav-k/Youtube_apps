import os
import random
import requests
from bs4 import BeautifulSoup
import webbrowser

query = input("Enter song name: ")
mystring = query.replace(' ' ,'+')

pref = "https://www.youtube.com/results?search_query="
url = pref+mystring

print("Directing to the url, Please wait!")

user_agent = {'User-agent': 'Mozilla/5.0'}
r = requests.get(url, headers = user_agent)

if r.status_code == 200:
	print("Request Approved!")

html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')
soup.prettify()

result = str()

for link in soup.find_all('a'):
	a = link.get('href')
	if 'watch' in a:
		result = a
		break

new_url = 'https://www.youtube.com'+result

webbrowser.open_new_tab(new_url)

print("Hold on! It's your browser taking time.....")


saveFile =  open('video_list.txt')

lines = saveFile.readlines()
lines = [x.strip() for x in lines]

text = new_url
ctr = True
for line in lines:
	if text == line:
		ctr = False
		break

if ctr == True:
	saveFile = open('video_list.txt','a')
	saveFile.write('\n'+text)

saveFile.close()
