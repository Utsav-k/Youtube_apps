'''The Program parses youtube video links from a youtube playlist and downloads them,
 it lets you chose a downloads directory and downloads the videos'''

import requests
from bs4 import BeautifulSoup 									#This Library helps you extract video links from the playlist
from pytube import YouTube

url = raw_input("Please Enter A Playlist Url carefully--- ")    #e.g. --> https://www.youtube.com/playlist?list=PLx65qkgCWNJJDR_h7Yzb3KQrFv7auC0dw

a = []
playlist = [] 													#Contains all the video links in the playlist

r = requests.get(url)

soup = BeautifulSoup(r.content,'html.parser')

all_links = soup.find_all("a",{"class": "pl-video-title-link"}) #To get all the video links from playlist within the class "pl-video-title-link


for link in all_links:
	a.append(link.get('href'))									#Storing all video links in dictionary 'a'.

for link in a:
	if 'watch' in link:
		playlist.append(link)									#filtering urls only for video links.

string = 'https://www.youtube.com'								#adding string to url to complete the video link.
playlist = [string + x for x in playlist]

download_path = raw_input('Enter the download location--- ')  	#e.g. download path --> /videos/

for link in playlist:											#accesing my list of urls from playlist


	flag = 1
	while flag:
		try:
			yt = YouTube(link)
			flag = 0
		except:
			print("Error 404! Check your connection")
			continue
	try:
		print(yt.filename)
	except:
		pass

	video = yt.get('mp4','360p') 								#You may change the video resolution here; You may also change the video format
	try:
		print("Downloading video! Please wait.....")
		video.download(download_path)							#In case if your internet disconects this will keep your programme running
		print("Video Succesfully Downloaded!")					#For adding resume feature if interruption in internet connection occurs.
		print
	except:
		print("Error, File may already exist!")
		continue

print('Congratulations! your playlist has been downloaded')
