# Web scraping https://www.passiton.com/inspirational-quotes Quotes website
# Project date 06-10-2023


import requests
import csv
import codecs
from bs4 import BeautifulSoup
from itertools import zip_longest
from time import sleep

# Initialize lists to store extracted information
themes = []
urls = []
images = []
lines = []
authors = []
author_jobs = []

page_number = 1  

while page_number <= 51:  

    try:
        URL = f"https://www.passiton.com/inspirational-quotes?page={page_number}"

        # Make a request to the URL
        result = requests.get(URL)

        # Get the page content
        source = result.content

        # Create a BeautifulSoup object for parsing
        soup = BeautifulSoup(source, 'html.parser')

        quotes = soup.find_all('div', class_='col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top')

        # Loop through each quote and extract information
        for quote in quotes:
            # Extract theme
            theme = quote.h5.text.strip()
            themes.append(theme)

            # Extract URL and append the base URL
            url = "https://www.passiton.com" + quote.a['href']
            urls.append(url)

            # Extract image source
            image = quote.img['src']
            images.append(image)

            # Extract lines
            line = quote.img['alt'].split(" #")[0]
            lines.append(line)

        print(f"Scraped Page {page_number}.")
        length = len(urls)
        print(f"The program scraped {length} quote informations.")

        page_number += 1  

        # Sleep for a second before making the next request
        sleep(1)

    except Exception as e:
        print("An error occurred:", e)
        break


auther_num = 1
# Separate loop to fetch author information for each URL
for url in urls:
    try:
        result = requests.get(url)
        source = result.content
        soup = BeautifulSoup(source, 'html.parser')

        # Extract Author info
        author_tag = soup.find('p')

        # Extracts the first part (author name)
        author_name = author_tag.contents[0].strip()  

        # Extracts the small tag content (author job)
        author_job = author_tag.small.get_text().strip()  

        authors.append(author_name)
        author_jobs.append(author_job)

        print(f"Author {auther_num} has been scraped. ")
        auther_num += 1

    except Exception as e:
        print("An error occurred while fetching author information:", e)

# Prepare data for CSV export
file_list = [themes, lines, urls, images, authors, author_jobs]
exported = zip_longest(*file_list)

# Create and write data to CSV file
csv_file_path = "quotes.csv"
with codecs.open(csv_file_path, "w", encoding='utf-8', errors='replace') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Theme", "Lines", "URLs", "Image", "Author", "Author job"])
    wr.writerows(exported)

print("Data scraped and saved to CSV:", csv_file_path)