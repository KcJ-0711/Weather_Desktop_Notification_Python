# importing library
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier 

# create an object to ToastNotifier class 

n = ToastNotifier() 

# enter city name
city = str(input("Enter the city name: "))

# creating url and requests instance
url = "https://www.google.com/search?q="+"weather%20"+city
html = requests.get(url).content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')
#print(soup)

temperature = soup.findAll("div", class_ = "BNeawe iBp4i AP7Wnd")
city = soup.findAll("span", class_ = "BNeawe tAd8D AP7Wnd")

def temp_output(var = temperature):
    temperaturelocal = str(temperature[1])
    temp_first_index = temperaturelocal.find("\">") +2
    temp_last_index = temperaturelocal.find("</div>")
    return (temperaturelocal[temp_first_index:temp_last_index])

    
def place_output(var = city):
    citylocal = str(city[0])
    city_first_index = citylocal.find("\">") +2
    city_last_index = citylocal.find("</span>")
    return (citylocal[city_first_index:city_last_index])

msg = "Temperature of {place} is {temp}".format(place = place_output(), temp = temp_output())
# print(msg)
n.show_toast(title="Heads Up 🙌 Weather Update !!!", msg= msg)
# temp_output()
# place_output()