#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pytube import YouTube
from IPython.display import Image, display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from googlesearch import search  


# In[2]:


def keyword_search():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')

    search_query = 'https://www.youtube.com/ AND ' + keyword
    search_query

    driver.get('https:www.google.com')
    sleep(2)

    search_query1 = driver.find_element_by_name('q')
    search_query1.send_keys(search_query)
    sleep(0.5)
    search_query1.send_keys(Keys.RETURN)
    sleep(3)

    links = []
    for j in search(search_query, tld="co.in", num=10, stop=10, pause=2): 
        links.append(j) 
    for j in range(10):
        url = links[j]
        my_video = YouTube(url)
        print("\nVideo Title",j+1," : ")
        print(my_video.title)
        print("Link ",j+1," : ")
        print(links[j])
        driver.get(links[j])
        print("\nThumbnail: ")
        print(my_video.thumbnail_url)
        video_thumbnail=my_video.thumbnail_url
        display(Image(video_thumbnail))
        sleep(3)
    driver.quit()
    video_select=int(input("\nEnter link number (1-10) to be downloaded : "))
    url_link = links[video_select-1]
    return url_link


# In[3]:


print("\Do you want to download via URL or search for keywords?: ")
print("\n1. Download via URL: ")
print("\n2. Search for Keywords: ")
choice=int(input("\nEnter choice : "))


# In[4]:


if choice==1:
    url=input("\nEnter URL : ")
elif choice==2:   
    keyword=input("\nEnter keyword to be searched : ")
    url=keyword_search()


# In[5]:


my_video = YouTube(url)

print("Video Title: ")
print(my_video.title)

print("\nThumbnail: ")
print(my_video.thumbnail_url)
video_thumbnail=my_video.thumbnail_url
display(Image(video_thumbnail))

my_video = my_video.streams.get_highest_resolution()

print("\nDownloading........ ")
my_video.download()

