from game_data import data
from game_data import logo
import random
# print("Higher\n lower")
print(logo)
def format_data(account):
    account_name= account["name"]  
    account_descr= account["description"]  
    account_country= account["country"] 
    return f"{account_name},a {account_descr}, from {account_country}"

account_a=random.choice(data)
account_b=random.choice(data)
if account_a==account_b:
    account_b = random.choice(data)

print(f" Compare A: {format_data(account_a)}")
print(f" Compare B:{format_data(account_b)}")
