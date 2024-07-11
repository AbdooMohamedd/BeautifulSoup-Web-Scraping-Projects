# date of the project 04-09-2023
import csv
import codecs
import re
from bs4 import BeautifulSoup
from itertools import zip_longest
from time import sleep
import requests

# Lists to store product information
names = []
num_ratings = []
ratings = []
old_prices = []
current_prices = []
discount_percentages = []
links = []
available = []
offer_type = []
door_delivery = []
pickup_station = []
return_policy = []
seller_info = []


page_num = 1
num_of_pages = int(input("Inter The Number of Pages You Want to Scrape: "))


while True:
    try:
        # Sleep for a second before making the request
        sleep(1)

        # Make a request to the URL
        result = requests.get(f"https://www.jumia.com.eg/laptops/?page={page_num}")

        # Get the page content
        source = result.content

        # Create a BeautifulSoup object for parsing
        soup = BeautifulSoup(source, "lxml")

        # Break the loop if we've fetched enough pages 
        if page_num > (num_of_pages):
            break

        # Extract product name, current price and Product link
        product_name_elements = soup.find_all("h3", {"class": "name"})
        price_elements = soup.find_all("div", {"class": "prc"})
        # discount_percentage_elements = soup.find_all("div", {"class": "bdg _dsct _sm"})
        link_elements = soup.find_all('a', class_='core')


        # for loop to extract 
        for i in range(len(product_name_elements)):
            names.append(product_name_elements[i].text)

            if link_elements:
                link = link_elements[i]['href']
                links.append("https://www.jumia.com.eg" + link)  
                length = len(links) 

            current_prices.append(price_elements[i].text)

        print(f"Scraped Page {page_num}. ")
        page_num += 1 
    
        print(f"the program scraped {length} laptop informations. ")

    except Exception as e:
        print("An error occurred:", e)
        break

laptop_num = 1

for link in links:
    result = requests.get(link)
    source = result.content
    soup = BeautifulSoup(source, "lxml")
    
        # Find availability elements and extract text from each
    availability_elements = soup.find_all("p", class_="-df -i-ctr -fs12 -pbs -rd5")
    availability_texts = [element.text.strip() for element in availability_elements]
    available.extend(availability_texts)

        # Find rating elements and extract text from each
    rating_element = soup.find("div", class_="stars _m _al")
    rating_text = "No ratings available"
    if rating_element:
        rating_text = rating_element.text.strip()
    ratings.append(rating_text)

        # Find number of ratings elements and extract text
    num_ratings_element = soup.find("a", class_="-plxs _more")
    num_ratings_text = "No ratings available"
    if num_ratings_element:
        num_ratings_text = num_ratings_element.text.strip()
    num_ratings.append(num_ratings_text)

        # Find door delivery details
    door_delivery_element = soup.find("div", class_="-df -fw-w -c-bet -fg1")
    if door_delivery_element:
        delivery_fees = door_delivery_element.find("em").text
        delivery_dates = door_delivery_element.find_all("em")[1].text
        ready_time = door_delivery_element.find_all("em")[2].text
        door_delivery_info = f"Delivery Fees: {delivery_fees}, Delivery Dates: {delivery_dates}, Ready Time: {ready_time}"
    else:
        door_delivery_info = "Door delivery information not available"
    door_delivery.append(door_delivery_info)

        # Find pickup station details
    pickup_station_element = soup.find("div", class_="-df -fw-w -c-bet -fg1")
    if pickup_station_element:
        pickup_fees = pickup_station_element.find("em").text
        pickup_dates = pickup_station_element.find_all("em")[1].text
        ready_time = pickup_station_element.find_all("em")[2].text
        pickup_station_info = f"Pickup Fees: {pickup_fees}, Pickup Dates: {pickup_dates}, Ready Time: {ready_time}"
    else:
        pickup_station_info = "Pickup station information not available"
    pickup_station.append(pickup_station_info)

        # Find return policy details
    return_policy_element = soup.find("p", class_="-ptxs")
    if return_policy_element:
        return_policy_text = return_policy_element.text.strip()
        return_policy_link = return_policy_element.find("a")["href"]
        return_policy_info = f"Return Policy: {return_policy_text}, For more details: {return_policy_link}"
    else:
        return_policy_info = "Return policy information not available"
    return_policy.append(return_policy_info)

        # Find offer type details
    offer_type_element = soup.find("div", class_="-df -i-ctr -pts")
    if offer_type_element:
        offer_type_a = offer_type_element.find("a")
        if offer_type_a:
            offer_type_text = offer_type_a.text.strip()
            offer_type_info = f"Offer Type: {offer_type_text}"
        else:
            offer_type_info = "Offer type: information not available"
    else:
        offer_type_info = "Offer type: information not available"
    offer_type.append(offer_type_info)

   # Find seller name and score
    seller_section = soup.find("div", class_="-hr -pas")
    if seller_section:
        seller_name_element = seller_section.find("p", class_="-m -pbs")
        seller_score_element = seller_section.find("bdo", class_="-m -prxs")
        
        if seller_name_element:
            seller_name = seller_name_element.text.strip()
        else:
            seller_name = "Seller name not available"
        
        if seller_score_element:
            seller_score = seller_score_element.text.strip()
        else:
            seller_score = "Seller score not available"
        
        seller_info_text = f"Seller Name: {seller_name}, Score: {seller_score}"
    else:
        seller_info_text = "Seller information not available"
    seller_info.append(seller_info_text)

        # Find discount and old price details
    discount_element = soup.find("span", class_="bdg _dsct _dyn -mls")
    old_price_element = soup.find("span", class_="-tal -gy5 -lthr -fs16 -pvxs")

    if discount_element:
        discount_percentage = discount_element["data-disc"]
    else:
        discount_percentage = "0%" 

    if old_price_element:
        old_price = old_price_element.text.strip()
    else:
        old_price = "Old price not available"

    discount_percentages.append(discount_percentage)
    old_prices.append(old_price)


    print(f"Laptop {laptop_num} information has been scraped. ")
    laptop_num += 1



# Prepare data for CSV export
file_list = [names, old_prices, discount_percentages, current_prices, ratings, num_ratings , links, available, offer_type, seller_info, door_delivery, pickup_station, return_policy]
exported = zip_longest(*file_list)

# Create and write data to CSV file
csv_file_path = r"D:\Python Projects\Web scraped data\Jumia.csv"                                # change the Path
with codecs.open(csv_file_path, "w", encoding='utf-8', errors='replace') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Laptop Name", "Old Price", "Discount Percentages", "Current Prices", "Rating", "Number of Ratings", "Link", "Unit Available", "Offer Type", "Seller Name and Score", "Door Delivery Info", "Pickup Station Info", "Return Policy Info"])
    wr.writerows(exported)

        # Iterate over exported data and decode and then write strings
    for row in exported:
        decoded_row = [item.decode('utf-8', 'replace') if isinstance(item, bytes) else item for item in row]
        wr.writerow(decoded_row)

print("Data scraped and saved to CSV:", csv_file_path)