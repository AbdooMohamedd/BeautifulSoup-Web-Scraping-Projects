import csv
import codecs
from bs4 import BeautifulSoup
from itertools import zip_longest
from time import sleep
import requests

# Create lists to store data for multiple players
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

pace_list = []
shooting_list = []
passing_list = []
dribbiling_list = []
defendibg_list = []
physicality_list = []


Acceleration_list = []
Sprint_Speed_list = []
AcceleRATE_list = []
Positioning_list = []
Finishing_list = []
Shot_Power_list = []
Long_Shots_list = []
Volleys_list = []
Penalties_list = []
Vision_list = []
Crossing_list = []
FK_Accuracy_list = []
Short_Passing_list = []
Long_Passing_list = []
Curve_list = []
Agility_list = []
Balance_list = []
Reactions_list = []
Ball_Control_list = []
Dribbling_list = []
Composure_list = []
Interceptions_list = []
Heading_Accuracy_list = []
Defensive_Awareness_list = []
Standing_Tackle_list = []
Sliding_Tackle_list = []
Jumping_list = []
Stamina_list = []
Strength_list = []
Aggression_list = []

lowest_bin_list = []
last_update_list = []
price_range_list = []
average_bin_24h_list = []
cheapest_sale_24h_list = []
discard_value_list = []



Page_Number = 1

while Page_Number <= 5:  
    try:
        # Make a request to the URL
        # result = requests.get(f"https://www.fut.gg/players/?positions=20%2C17%2C16%2C14%2C18%2C15%2C13%2C10%2C8%2C12%2C6%2C5%2C4%2C1%2C2%2C3%2C11&rarity_id=309%2C304%2C302%2C339%2C318%2C306%2C343%2C316%2C335%2C325%2C317%2C334%2C310%2C326%2C328%2C308%2C364%2C355%2C350%2C347%2C363&page={Page_Number}")
        result = requests.get(f"https://www.fut.gg/players/women/?positions=20%2C17%2C16%2C14%2C18%2C15%2C11%2C13%2C10%2C8%2C12%2C6%2C5%2C4%2C1%2C2%2C3&page={Page_Number}")

        # Sleep for 2 second before making the request
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

        # elements headers
        player = soup.find("div", {"data-js-selector":"player-attributes"})

        # elements headers
        elements_headers = []
        headers = player.find_all("div", class_='font-bold text-center')
        for head in headers:
            elements_headers.append(head.text.strip())
        pace_list.append(elements_headers[0])
        shooting_list.append(elements_headers[1])
        passing_list.append(elements_headers[2])
        dribbiling_list.append(elements_headers[3])
        defendibg_list.append(elements_headers[4])
        physicality_list.append(elements_headers[5])

        # elements in elements
        elements_numbers = []
        numbers = player.find_all("span", class_= "text-white font-bold text-sm text-shadow-sm shadow-black")

        for number in numbers:
            elements_numbers.append(number.text.strip())
        Acceleration_list.append(elements_numbers[0])
        Sprint_Speed_list.append(elements_numbers[1])
        AcceleRATE_list.append(elements_numbers[2])
        Positioning_list.append(elements_numbers[3])
        Finishing_list.append(elements_numbers[4])
        Shot_Power_list.append(elements_numbers[5])
        Long_Shots_list.append(elements_numbers[6])
        Volleys_list.append(elements_numbers[7])
        Penalties_list.append(elements_numbers[8])
        Vision_list.append(elements_numbers[9])
        Crossing_list.append(elements_numbers[10])
        FK_Accuracy_list.append(elements_numbers[11])
        Short_Passing_list.append(elements_numbers[12])
        Long_Passing_list.append(elements_numbers[13])
        Curve_list.append(elements_numbers[14])
        Agility_list.append(elements_numbers[15])
        Balance_list.append(elements_numbers[16])
        Reactions_list.append(elements_numbers[17])
        Ball_Control_list.append(elements_numbers[18])
        Dribbling_list.append(elements_numbers[19])
        Composure_list.append(elements_numbers[20])
        Interceptions_list.append(elements_numbers[21])
        Heading_Accuracy_list.append(elements_numbers[22])
        Defensive_Awareness_list.append(elements_numbers[23])
        Standing_Tackle_list.append(elements_numbers[24])
        Sliding_Tackle_list.append(elements_numbers[25])
        Jumping_list.append(elements_numbers[26])
        Stamina_list.append(elements_numbers[27])
        Strength_list.append(elements_numbers[28])
        Aggression_list.append(elements_numbers[29])



        print(f"Player {player_number} Has been Scraped. ")
        player_number +=1 


# Your existing lists
file_list = [
    player_id_list, names_list, titles_list, clubs_list, nations_list, leagues_list, foot_list,
    skill_moves_list, weak_foot_list, accele_rate_list, height_list,
    att_def_wr_list, age_list, images_list, links_list,
    pace_list, Acceleration_list, Sprint_Speed_list, AcceleRATE_list,
    shooting_list, Positioning_list, Finishing_list, Shot_Power_list, Long_Shots_list, Volleys_list, Penalties_list,
    passing_list, Vision_list, Crossing_list, FK_Accuracy_list, Short_Passing_list, Long_Passing_list, Curve_list,
    dribbiling_list, Agility_list, Balance_list, Reactions_list, Ball_Control_list, Dribbling_list, Composure_list, 
    defendibg_list, Interceptions_list, Heading_Accuracy_list, Defensive_Awareness_list, Standing_Tackle_list, Sliding_Tackle_list, 
    physicality_list, Jumping_list, Stamina_list, Strength_list, Aggression_list, 
    lowest_bin_list, last_update_list, price_range_list, average_bin_24h_list, cheapest_sale_24h_list, discard_value_list
]


# Create and write data to CSV file
csv_file_path = r"D:\Python Projects\Projects\FIFA\Women Fifa Players 22.csv"  # change the Path
with open(csv_file_path, "w", newline="", encoding='utf-8') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
    wr.writerow([
        "Player ID", "Name", "Card Title", "Club", "Nation", "League", "Foot", "Skill Moves",
        "Weak Foot", "AcceleRATE", "Height", "Att/Def. WR", "Age", "Player Card Image", "Player Card Link",
        "Pace", "Acceleration", "Sprint Speed", "AcceleRATE",
        "Shooting", "Positioning", "Finishing", "Shot Power", "Long Shots", "Volleys", "Penalties",
        "Passing", "Vision", "Crossing", "FK Accuracy", "Short Passing", "Long Passing", "Curve",
        "Dribbling", "Agility", "Balance", "Reactions", "Ball Control", "Dribbling", "Composure",
        "Defending", "Interceptions", "Heading Accuracy", "Defensive Awareness", "Standing Tackle", "Sliding_Tackle_list",
        "Physicality", "Jumping", "Stamina", "Strength_list", "Aggression"
        "Lowest BIN", "Last Update", "Price Range", "Average BIN (24h)", "Cheapest Sale (24h)", "Discard Value"
    ])
    exported = zip_longest(*file_list)
    wr.writerows(exported)

print("Data scraped and saved to CSV:", csv_file_path)