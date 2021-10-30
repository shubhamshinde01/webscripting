
import requests

from bs4 import BeautifulSoup

import pandas

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_MAX= 3

for page_num in range(1, page_num_MAX):
    req= requests.get(oyo_url+ str(page_num))
    content = req.content

    soup=BeautifulSoup(content, "html.parser")
    all_hotels = soup.find_all("div", {"class": "hotelCardListing"})"

   
    scraped_info_list = []

    for hotel in all_hotels:
       hotel_dict()
       hotel_dict["name"]= hotel.find("h3", {"class": "listingHotelDescription_hotelName"}).text
       hotel_dict["address"]= hotel.find("span", {"itemprop": "streetAddress"}).text
       hotel_dict ["price"]= hotel.find("span", {"class": "listingPrice_finalPrice"}).text

     #try... except

     try:
         hotel_dict ["rating"]= hotel.find("span", {"class": "hotelRating_ratingSummary")).text
         except AttributeError:
             pass

     parent_amenities element = hotel.find("div", {"class": "amenityWrapper"}}

     amenities_list = []

     for amenity in parent_amenities element.find_all("div", {"class": "amenityWrapper__amenity"}):
         amenities _list.append(amenity.find("span", {"class": "d-body-sm")).text.strip())
 
     hotel_dict["amenities"] = ', .join(amenities_list[:-1])
 
      scraped_info_list.append(hotel_dict)

     #print (hotel_name, hotel address, hotel_price, hotel_rating, amenities_list)

dataFrame = pandas.DataFrame(scraped_info_list)

dataFrame.to_csv ("Oyo.csv")
