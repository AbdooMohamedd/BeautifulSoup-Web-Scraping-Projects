import csv
from bs4 import BeautifulSoup
from itertools import zip_longest
from time import sleep
import requests

# Create lists to store data for multiple players
# (Your existing lists)
links_list = []
titles_list = []
images_list = []
names_list = []
clubs_list = []
nations_list = []
leagues_list = []
foot_list = []
skill_moves_list = []
weak_foot_list = []
accele_rate_list = []
height_list = []
att_def_wr_list = []
age_list = []
player_id_list = []

# Initialize empty lists for attributes
pace_list = []
shooting_list = []
passing_list = []
dribbling_list = []
defending_list = []
physicality_list = []

# Initialize separate lists to store information
lowest_bin_list = []
last_update_list = []
price_range_list = []
average_bin_24h_list = []
cheapest_sale_24h_list = []
discard_value_list = []


Page_Number = 1

while Page_Number <= 1:
    try:
        # Make a request to the URL
        result = requests.get(f"https://www.fut.gg/players/?page={Page_Number}&positions=20%2C17%2C16%2C14%2C18%2C15%2C11%2C13%2C10%2C8%2C12%2C6%2C5%2C4%2C1%2C2%2C3")

        # Sleep for 2 seconds before making the request
        sleep(2)

        # Get the page content
        source = result.content

        # Create a BeautifulSoup object for parsing
        soup = BeautifulSoup(source, "html.parser")

        # Extract information from each element
        elements = soup.find_all('a', class_='relative group fc-card-container fut-card-container block')

        for element in elements:
            # Extract the Player link, title, and image URL
            link = element.get('href')
            img = element.find('img')
            title = img['title']
            img_url = img['src']

            # Append the Player link, title, and image URL
            links_list.append("https://www.fut.gg" + link)
            titles_list.append(title)
            images_list.append(img_url)

        print(f"Scraped Page {Page_Number}.")
        Page_Number += 1
        length = len(titles_list)
        print(f"The program scraped {length} Player informations.")

    except Exception as e:
        print("An error occurred:", e)
        break


player_number = 1

for link in links_list:
    # Make a request to the URL
    response = requests.get(link)
    sleep(1)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        player_info = soup.find('div', class_='paper mb-3 hidden md:block')
        if player_info:
            # Extract data for each attribute
            name = player_info.find('div', string='Name').find_next('div').text.strip()

            try:
                club = player_info.find('div', string='Club').find_next('div').text.strip()
            except AttributeError:
                club = "N/A"

            try:
                nation = player_info.find('div', string='Nation').find_next('div').text.strip()
            except AttributeError:
                nation = "N/A"

            try:
                league = player_info.find('div', string='League').find_next('div').text.strip()
            except AttributeError:
                league = "N/A"

            try:
                foot = player_info.find('div', string='Foot').find_next('div').text.strip()
            except AttributeError:
                foot = "N/A"

            try:
                skill_moves = player_info.find('div', string='Skill Moves').find_next('div').text.strip().encode('utf-8', 'ignore').decode('utf-8')
            except AttributeError:
                skill_moves = "N/A"

            try:
                weak_foot = player_info.find('div', string='Weak Foot').find_next('div').text.strip().encode('utf-8', 'ignore').decode('utf-8')
            except AttributeError:
                weak_foot = "N/A"

            try:
                accele_rate = player_info.find('div', string='AcceleRATE').find_next('div').text.strip()
            except AttributeError:
                accele_rate = "N/A"

            try:
                height = player_info.find('div', string='Height').find_next('div').text.strip()
            except AttributeError:
                height = "N/A"

            try:
                att_def_wr = player_info.find('div', string='Att/Def. WR').find_next('div').text.strip()
            except AttributeError:
                att_def_wr = "N/A"

            try:
                age = player_info.find('div', string='Age').find_next('div').text.strip()
            except AttributeError:
                age = "N/A"

            try:
                player_id = player_info.find('div', string='Player ID').find_next('div').text.strip()
            except AttributeError:
                player_id = "N/A"

            # Append the data for this player to the respective lists
            names_list.append(name)
            clubs_list.append(club)
            nations_list.append(nation)
            leagues_list.append(league)
            foot_list.append(foot)
            skill_moves_list.append(skill_moves)
            weak_foot_list.append(weak_foot)
            accele_rate_list.append(accele_rate)
            height_list.append(height)
            att_def_wr_list.append(att_def_wr)
            age_list.append(age)
            player_id_list.append(player_id)




# Prepare data for CSV export
file_list = [player_id_list, names_list, titles_list, clubs_list, nations_list, leagues_list, foot_list,
            skill_moves_list, weak_foot_list, accele_rate_list, height_list,
            att_def_wr_list, age_list, images_list, links_list,
            pace_list, shooting_list, passing_list, dribbling_list, defending_list, physicality_list]
exported = zip_longest(*file_list)

# Create and write data to CSV file
csv_file_path = r"D:\Python Projects\Projects\FIFA\Fifa Players.csv"
with open(csv_file_path, "w", newline="", encoding='utf-8') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
    wr.writerow([
        "Player ID", "Name", "Card Title", "Club", "Nation", "League", "Foot", "Skill Moves",
        "Weak Foot", "AcceleRATE", "Height", "Att/Def. WR", "Age", "Player Card Image", "Player Card Link",
        "Pace", "Shooting", "Passing", "Dribbling", "Defending", "Physicality"])
    wr.writerows(exported)

print("Data scraped and saved to CSV:", csv_file_path)