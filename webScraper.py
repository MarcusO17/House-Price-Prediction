from csv import  writer
from bs4 import BeautifulSoup
import requests



hdrs ={
    'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
}

page = 1

with open('housing.csv','w',encoding='utf8',newline='') as file:
    thewriter = writer(file)
    headerCSV = ['Title', 'Price', 'Location', 'BuildArea', 'NoOfBedrooms', 'NoOfBathrooms']
    thewriter.writerow(headerCSV)
    while page !=  548:
          url = f"https://www.mudah.my/penang/apartment-condominium-for-sale?o={page}"
          page = page + 1
          webpage = requests.get(url, headers=hdrs).text

          soup = BeautifulSoup(webpage, 'lxml')
          print(f'Page Progress: {page}')
          for housing in soup.find_all('div', class_='sc-fHSTwm kPxBwp'):
              # title
              title = housing.find('a', class_='sc-cgHJcJ EaieH').text

              # price
              price = housing.find('div', class_='sc-hARARD cOEWki').text

              # location
              location = housing.find('span', class_='sc-fKGOjr kokWXc').text

              # BuildArea
              buildArea = housing.find('div', class_='sc-jQMNup hTRZZu', title='Size').div.text

              # No Of Bedrooms
              noOfBedrooms = housing.find('div', class_='sc-jQMNup hTRZZu', title='Bedrooms').div.text

              # No of Bathrooms
              noOfBathrooms = housing.find('div', class_='sc-jQMNup hTRZZu', title='Bathrooms').div.text
                

              info = [title, price, location, buildArea, noOfBedrooms, noOfBathrooms]
              thewriter.writerow(info)
