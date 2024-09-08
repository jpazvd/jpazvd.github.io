import os
import requests
from bs4 import BeautifulSoup
import json

# Ensure the directory exists
os.makedirs(r'C:\GitHub\mytasks\jpazvd.github.io\resources', exist_ok=True)


# URL of the page to scrape
url = 'https://www.worldbank.org/en/about/people/j/joao-pedro-azevedo'

# Send a request to fetch the content of the page
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Initialize an empty list to store all publication metadata
publications_data = []

# Assuming publications are contained in specific HTML elements like 'div', 'article', etc.
publications = soup.find_all('div', class_='publication')  # Adjust the class name based on the actual structure

# Loop through each publication block and collect data
for pub in publications:
    title = pub.find('a').get_text().strip() if pub.find('a') else 'No Title Found'
    link = pub.find('a').get('href') if pub.find('a') else 'No Link Found'
    date = pub.find('span', class_='date').get_text().strip() if pub.find('span', class_='date') else 'No Date Found'
    description = pub.find('p', class_='description').get_text().strip() if pub.find('p', class_='description') else 'No Description Found'
    authors = pub.find('span', class_='authors').get_text().strip() if pub.find('span', class_='authors') else 'No Authors Found'

    # Append the data as a dictionary to the publications_data list
    publications_data.append({
        'Title': title,
        'Link': link,
        'Date': date,
        'Description': description,
        'Authors': authors
    })

# Define the full path to save the JSON file
json_file = r'C:\GitHub\mytasks\jpazvd.github.io\resources\publications_data.json'

# Save the data to a JSON file
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(publications_data, file, ensure_ascii=False, indent=4)

print(f"Data saved to {json_file}")
