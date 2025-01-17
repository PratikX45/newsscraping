# -*- coding: utf-8 -*-
"""indianex_scrap.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JdYT7zPV37ZH2tgtVLfX4wqoxoeIwi_O
"""

!pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# URL of the article
url = "https://indianexpress.com/article/technology/artificial-intelligence/top-ai-jobs-in-2025-roles-salaries-and-trends-to-watch-9782512/"

# Send a GET request to the article URL
response = requests.get(url)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the headline
    headline = soup.find('h1', class_='native_story_title')  # Update the class name based on the website structure
    headline = headline.text.strip() if headline else "Headline not found"

    # Extract the description
    description = soup.find('meta', attrs={'name': 'description'})
    description = description['content'].strip() if description else "Description not found"

    # Extract the author
    author = soup.find('a', rel='author')
    author = author.text.strip() if author else "Author not found"

    # Extract the date/time
    date_time = soup.find('meta', attrs={'property': 'article:published_time'})
    date_time = date_time['content'].strip() if date_time else "Date/time not found"

    # Extract tags
    tags_section = soup.find('meta', attrs={'name': 'keywords'})
    tags = tags_section['content'].split(',') if tags_section else ["Tags not found"]

    # Extract the main content
    content = soup.find('div', class_='articles')
    paragraphs = content.find_all('p') if content else []
    content_text = "\n".join(p.text.strip() for p in paragraphs) if paragraphs else "Content not found"

    # Display the extracted data
    print(f"Headline: {headline}\n")
    print(f"Description: {description}\n")
    print(f"Author: {author}\n")
    print(f"Date/Time: {date_time}\n")
    print(f"Tags: {', '.join(tags)}\n")
    print(f"Content:\n{content_text}\n")

else:
    print(f"Failed to retrieve the article. HTTP Status Code: {response.status_code}")