import re # import the regex library, already included in python

'''
https://www.thebalance.com/what-do-the-numbers-on-your-credit-card-mean-4588401
Credit card numbers, called primary account numbers (PAN), are 16-digits. 
Each PAN has 3 important pieces of information: the card issuer, account info, and a check digit.
The card issuer can be identified by the first number.
1 - Airline
2 - Mastercard after 2017
3 - American Express / Diners Club
4 - Visa
5 - Mastercard
6 - Discover
7 - Petroleum
8 - Telecoms
9 - Government
'''

# With the above information, create a regex that will accept any credit card
creditcard = input("enter a credit card: ")
creditcardregex = "^[1-9]\d{15}$"
print(re.search(creditcardregex, creditcard))

# Vendor only accepts Visa or Mastercard
visamasterregex = "^(4|5)\d{15}$"
print(re.search(visamasterregex, creditcard))

# Vendor does not accept government issued cards
nogovernmentregex = "^[^09]\d{15}$"
print(re.search(nogovernmentregex, creditcardregex))