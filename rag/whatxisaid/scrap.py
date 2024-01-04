import requests
from bs4 import BeautifulSoup

# URL of the web page to scrape
url = 'http://en.qstheory.cn/thegovernanceofchinaI.html'

print("Start")

# Send a GET request to the web page and get the HTML content
try:
    response = requests.get(url)
    html_content = response.text
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

print(html_content)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the contents you're interested in
# For example, let's say you want to extract all the paragraphs on the page
paragraphs = soup.find_all(class_='tw3')

# Print the paragraphs
for paragraph in paragraphs:
    print(paragraph.text)
