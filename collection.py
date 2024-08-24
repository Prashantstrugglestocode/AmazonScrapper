from bs4 import BeautifulSoup
import os
import pandas as pd
import project as pj


titles = []
prices = []
links = []

value =pj.query

for file in os.listdir("data"):
    with open(f"data/{file}") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')
    title_element = soup.find("h2", class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2")
    price_element = soup.find("span", class_="a-price-whole")
    link_element = title_element.find('a', href=True) if title_element else None
    
    if title_element and price_element and link_element:
        title = title_element.get_text(strip=True)
        price = price_element.get_text(strip=True)
        link = link_element['href']
        
    titles.append(title)
    prices.append(price)
    links.append(link)

    df = pd.DataFrame({
    'Title': titles,
    'Price': prices,
    'Link': links
})
    df = df.sort_values(by='Price', ascending=True)

# Save the DataFrame to a CSV file
    df.to_csv('output.csv', index=False)
