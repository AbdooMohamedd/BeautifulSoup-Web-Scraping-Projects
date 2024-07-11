# date of the project 16-10-2023

# import Important modules
import csv
from bs4 import BeautifulSoup
from itertools import zip_longest
from time import sleep
import requests
import codecs

# Initialize empty lists to store scraped data
product_id_list = []
product_title_list = []
price_range_list = []
ready_to_ship_list = []
min_order_list = []
product_link_list = []
image_link_list = []


page_number = 0

# Prompt the user to enter a product name
product = input("Please Enter the Product Name: ")

while page_number < 100:
    try:

        # Add a short delay to be polite to the website
        sleep(3)

        # Make a request to the Alibaba search page
        result = requests.get(f"https://www.alibaba.com/trade/search?keywords={product}&&page={page_number}")
        
        # Get the page content
        source = result.content
        
        # Create a BeautifulSoup object for parsing
        soup = BeautifulSoup(source, "html.parser")
        
        # Get all product elements on the page
        products = soup.find_all("div", {"class": "fy23-search-card fy23-gallery-card m-gallery-product-item-v2 J-search-card-wrapper"})
        

        for product in products:
            # Extract the "data-product_id" attribute value
            product_id = product['data-product_id']
            product_id_list.append(product_id)

            # Extract the product title information
            product_title = product.find('h2', class_='search-card-e-title').text.strip()
            product_title_list.append(product_title)

            # Extract the price range information
            price_range = product.find('div', class_='search-card-e-price-main').text.strip()
            price_range_list.append(price_range)

            # Extract the "Ready to Ship" information 
            ready_to_ship_element = product.find('span', {'data-sellpoint': 'Ready to Ship'})
            ready_to_ship = ready_to_ship_element.text.strip() if ready_to_ship_element else "N/A"
            ready_to_ship_list.append(ready_to_ship)

            # Extract the "Min. order" information 
            min_order_element = product.find('div', {'class': 'search-card-m-sale-features__item'})
            min_order = min_order_element.text.strip() if min_order_element else "N/A"
            min_order_list.append(min_order)

            # Extract the link for each Product 
            product_link = product.find('a')['href']
            product_link_list.append('https:' + product_link)

            # Extract the Product image link 
            image_element = soup.find('img', class_='search-card-e-slider__img')  
            image_link = image_element['src']
            image_link_list.append(image_link)


            print(f"Scraped Page {page_number}.")
            page_number += 1 
            length = len(product_id_list)
            print(f"The program scraped {length} Product informations.")

    except Exception as e:
        print("An error occurred:", e)
        page_number += 1


# Prepare data for CSV export
file_list = [product_id_list, product_title_list, price_range_list, ready_to_ship_list, min_order_list, product_link_list, image_link_list]
exported = zip_longest(*file_list)

# Create and write data to CSV file
csv_file_path = r"D:\Python Projects\Projects\Ali baba\Alibaba.csv"                                # change the Path
with codecs.open(csv_file_path, "w", encoding='utf-8', errors='replace') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Product ID", "Product Name", "Price Range", "Shipment", "Minimum Order", "Product Link", "Image"])
    wr.writerows(exported)

    # Iterate over exported data and decode and then write strings
    for row in exported:
        decoded_row = [item.decode('utf-8', 'replace') if isinstance(item, bytes) else item for item in row]
        wr.writerow(decoded_row)

print("Data scraped and saved to CSV:", csv_file_path)











