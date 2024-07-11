# Web Scraping Alibaba Products

## Project Date: 16-10-2023

This project demonstrates how to scrape product information from Alibaba using BeautifulSoup, requests, and CSV modules. The script collects various product details and saves them into a CSV file.

## Overview

The script scrapes product information such as product ID, name, price range, shipment details, minimum order quantity, product link, and image link from Alibaba's search results (https://www.alibaba.com). The collected data is stored in a CSV file for further analysis.

## Technologies Used

- Python
- BeautifulSoup
- requests
- csv
- itertools
- time
- codecs

## How to Use

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies:
    ```bash
    pip install beautifulsoup4 requests
    ```
3. Run the scraping script:
    ```bash
    web scraping Alibaba.py
    ```

## Script Explanation

1. **Import Modules**: The script imports necessary modules like `csv`, `BeautifulSoup`, `requests`, etc.
2. **Initialize Lists**: Empty lists are initialized to store the scraped data.
3. **User Input**: Prompts the user to enter a product name to search on Alibaba.
4. **Loop through Pages**: Scrapes data from multiple pages of search results.
5. **Parse HTML**: Uses BeautifulSoup to parse the HTML content.
6. **Extract Data**: Extracts product information and appends it to the respective lists.
7. **Export to CSV**: Exports the scraped data to a CSV file.

## Sample Output

The output CSV file contains the following columns:
- Product ID
- Product Name
- Price Range
- Shipment
- Minimum Order
- Product Link
- Image

Here is a sample of the output data:
| Product Name | Price Range | Shipment | Minimum Order | Product Link | Image |
|--------------|-------------|----------|---------------|--------------|-------|
| Aoro A17 Octa core 12.5mm slim smart phone android handheld 108MP camera feature rugged mobile phones 3g&4g smartphone rugged | $575.00 - $580.00 | Ready to Ship | Shipping per set: $43.00 | [Link](https://www.alibaba.com/product-detail/Aoro-A17-Octa-core-12-5mm_1600713688510.html) | ![Image](//s.alicdn.com/@sc04/kf/H396c3c10d77f4188847b51c398d415cdE.png_300x300.png) |


