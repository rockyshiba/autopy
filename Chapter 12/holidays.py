import requests
import bs4 # install library first: pip3 install beautifulsoup4
from datetime import datetime

'''
Goal is to scrape the holidays from webpage into an array of datetime objects
Scraping a web page requires an internet connection.

Scraping requires knowledge of HTML and knowing the HTML of the target.

Most importantly, web scraping requires pattern recognition in order to reliably web scrape
'''

# later to contain dictionaries of holidays containing date and name
holidays = []

year = '2020'
country = 'japan'
url = f"https://www.timeanddate.com/holidays/{country}/{year}"

# table id containing dates
table_id = "#holidays-table"

# capture webpage as a request object
res = requests.get(url)

# does nothing if everything is okay
res.raise_for_status()

# use html text of request object, create beautifulsoup object
holidaySoup = bs4.BeautifulSoup(res.text, 'html.parser')

# store the array result of .select into a variable
holiday_table = holidaySoup.select(table_id)

# loop through the rows of the holiday table
for row in holiday_table[0].find_all('tr'):

    print(row)

    # the milliseconds of time can be parsed into a date and is stored within the data-date attribute
    date = row.attrs.get('data-date')
    if date:
        print(date)
        # The name of the holiday associated with that date is the child of <a> tags
        # Use find to find the first <a> and extract the text inside using .text
        holiday_name = row.find('a').text
        print(holiday_name)

        # The dates in milliseconds can be converted to datetime
        # 1. Convert the date into a float, divide by 1000.0
        # 2. datetime.fromtimestamp will convert those milliseconds to a datetime object
        holidays.append(
            {
                'date': datetime.fromtimestamp( float(date) / 1000.0 ),
                'name': holiday_name
            })

print(holidays)