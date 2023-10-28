# importing library
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier 

# create an object to ToastNotifier class 

n = ToastNotifier() 

# enter city name
city = str(input("Enter the city name: "))

# creating url and requests instance
url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

# formatting data
data = str.split('\n')
time = data[0]
sky = data[1]

# getting all div tag
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text

# getting other required data
pos = strd.find('Wind')
other_data = strd[pos:]

# printing all data
print("Temperature is", temp)
print("Sky Description: ", sky)
#print(other_data)

result = "current temp " + temp + "  in " + city +", " + sky

n.show_toast("live Weather update", result, duration = 10) 