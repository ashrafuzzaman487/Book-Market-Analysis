import requests
from bs4 import BeautifulSoup
import csv
import re  # ১. নতুন করে 're' মডিউল ইম্পোর্ট করলাম

url = 'http://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
books = soup.find_all('article', class_='product_pod')

with open('cheap_books.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Book Name', 'Price (GBP)'])

    for book in books:
        title = book.h3.a['title']
        price_text = book.find('p', class_='price_color').text
        
        # ২. রেগুলার এক্সপ্রেশন দিয়ে শুধু সংখ্যা এবং ডট খুঁজে বের করা
        price_number = re.findall(r"[\d.]+", price_text)
        
        if price_number:
            price_value = float(price_number[0])
            
            # ৩. ফিল্টারিং লজিক
            if price_value < 20:
                writer.writerow([title, price_value])

print("Professional file 'cheap_books.csv' has been saved successfully!")
