import os
import requests
from bs4 import BeautifulSoup
import csv

# Ensure the directory exists
os.makedirs(r'C:\GitHub\mytasks\jpazvd.github.io\resources', exist_ok=True)

import os

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

    # Append the data to publications_data list
    publications_data.append([title, link, date, description, authors])

# Define the full path to save the CSV file
csv_file = r'C:\GitHub\mytasks\jpazvd.github.io\resources\publications_data.csv'

# Save the data to a CSV file
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Title', 'Link', 'Date', 'Description', 'Authors'])
    # Write the rows
    writer.writerows(publications_data)

print(f"Data saved to {csv_file}")
