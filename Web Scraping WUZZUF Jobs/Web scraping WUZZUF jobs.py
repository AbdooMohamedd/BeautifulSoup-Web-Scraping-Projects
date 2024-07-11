# Import necessary modules
import requests
import csv
import codecs
import re
from bs4 import BeautifulSoup
from itertools import zip_longest

# Lists to store job information
job_title = []
company_name = []
location = []
job_type = []
job_skill = []
links = []
salary_list = []  
responsibilities_list = []  
date = []

page_num = 0
n = 1

# Main loop for scraping job listings
while True:
    try:
        # Make a request to the URL
        result = requests.get(f'https://wuzzuf.net/search/jobs/?a=navbl&q=data&start={page_num}')
        
        # Get the page content
        source = result.content
        
        # Create a BeautifulSoup object for parsing
        soup = BeautifulSoup(source, "lxml")
        
        # Find the total number of pages
        page_limit_text = soup.find("strong").text
        page_limit = int(page_limit_text.replace(',', ''))
        
        # Break the loop if we've fetched enough pages 
        if page_num > (page_limit // 15):
            break
        
        # Extract job information from the current page
        job_titles = soup.find_all("h2", {"class": "css-m604qf"})
        company_names = soup.find_all("a", {"class": "css-17s97q8"})
        locations = soup.find_all("span", {"class": "css-5wys0k"})
        job_types = soup.find_all("a", {"class": "css-n2jc4m"})
        job_skills = soup.find_all("div", {"class": "css-y4udm8"})
        posted_new = soup.find_all("div", {"class": "css-4c4ojb"})
        posted_old = soup.find_all("div", {"class": "css-do6t5g"})
        posted = [*posted_new, *posted_old]
        
        # Extract data from each job listing
        for i in range(len(job_titles)):
            job_title.append(job_titles[i].text)
            links.append("https://wuzzuf.net" + job_titles[i].find("a")["href"])
            company = company_names[i].text
            company_name.append(company[:-1])
            location.append(locations[i].text)
            job_type.append(job_types[i].text)
            job_skill.append(job_skills[i].text)
            date.append(posted[i].text)
        
        # Increment page number and print status
        print(f"Scraped Page {n}")
        page_num += 1
        n += 1
    except Exception as e:
        print("An error occurred:", e)
        break

# Prepare data for CSV export
file_list = [job_title, company_name, location, date, job_type, job_skill, links, salary_list, responsibilities_list]
exported = zip_longest(*file_list)

# Create and write data to CSV file
csv_file_path = r"D:\Python Projects\Web scraped data\WUZZUF.csv"
with codecs.open(csv_file_path, "w", encoding='utf-8', errors='replace') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Job Title", "Company Name", "Location", "Posted Date", "Job Type", "Job Skills", "Link", "Salary", "Responsibilities"])

    # Iterate over exported data and decode and then write strings
    for row in exported:
        decoded_row = [item.decode('utf-8', 'replace') if isinstance(item, bytes) else item for item in row]
        
        # Convert to Unicode and remove non-ASCII characters from "Job Skills"
        job_skills_index = 5  # Index of "Job Skills" column
        job_skills = decoded_row[job_skills_index]
        cleaned_job_skills = re.sub(r'[^\x00-\x7F]+', '', job_skills)  # Remove non-ASCII characters
        cleaned_job_skills = cleaned_job_skills.replace(' آ· ', '|')  # Replace separator with '|'
        decoded_row[job_skills_index] = cleaned_job_skills
        
        wr.writerow(decoded_row)

print("Data scraped and saved to CSV:", csv_file_path)