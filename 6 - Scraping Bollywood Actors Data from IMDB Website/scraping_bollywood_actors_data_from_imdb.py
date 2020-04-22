#Import required libraries.
from bs4 import BeautifulSoup
import requests
import os
import urllib.request
import pandas as pd

#Function to scrape data from IMDB website.
def get_data():

  url = 'https://www.imdb.com/list/ls002913270/'
  response = requests.get(url)

  soup = BeautifulSoup(response.text, 'lxml')

  actor_images_links = [a.attrs.get('src') for a in soup.select('div.lister-item-image a img')]
  actor_names = [a.attrs.get('alt') for a in soup.select('div.lister-item-image a img')]
  actors_info = [a.get_text().strip() for a in soup.select('div.lister-item-content p')]
  del actors_info[0::2]

  return actor_images_links, actor_names, actors_info

#Final functino to call
def make_database(format = 'consolidated'):

  links, names, info = get_data()

  if format is 'consolidated':

    os.makedirs('ActorImages')

    #List to store all the names of images.
    image_file_names = []

    for i in range(len(links)):

      #Defining the image name and storing it in the folder.
      image_name = str(i+1)+'-'+names[i]+'.jpg'
      image_file_names.append(image_name)
      urllib.request.urlretrieve(links[i],'ActorImages/'+image_name)

    #Making a .csv file containing information regarding actor name, actor data and actor's image file name.
    data = zip(names,image_file_names,info)
    database = pd.DataFrame(data,columns= ['Actor_Name', 'Actor_Image_File_Name', 'Actor_Data'])
    database.to_csv('Actors_Data.csv')

  elif format is 'distributed':

    os.makedirs('ActorDataBase')

    for i in range(len(links)):

      #Making folder of each Actor Seperately.
      folder_name = str(i+1)+'-'+names[i]
      os.makedirs('ActorDataBase'+'/'+folder_name)

      #Storing image in that folder.
      image_name = str(i+1)+'-'+names[i]+'.jpg'
      image_path = 'ActorDataBase/'+folder_name+'/'
      urllib.request.urlretrieve(links[i],image_path+image_name)

      #Storing meta data about the actor in a .txt file.
      file_name = str(i+1)+'-'+names[i]+'.txt'
      with open('ActorDataBase/'+folder_name+'/'+file_name,'w') as f:
        f.write(info[i])

#Making the function call.
make_database('consolidated')