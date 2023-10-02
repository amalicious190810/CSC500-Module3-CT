# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 23:23:45 2023

@author: pulik
"""

#%%

# Part 1: Meal Purchase Calculator

# Ask user to enter charge for food
food_charge = float(input("Enter the charge for the food:\n$"))

# Calculate the tip (18%)
tip_percent = .18
tip_amount = food_charge * tip_percent

# Calculate sales tax (7%)
sales_tax_percent = .07
sales_tax_amount = food_charge * sales_tax_percent

# Calculate total price
total_price = food_charge + tip_amount + sales_tax_amount

# Diplay each amount and total price
print(f'Food Charge: ${food_charge: .2f}')
print(f'Tip (18%): ${tip_amount: .2f}')
print(f'Sales Tax (7%): ${sales_tax_amount: .2f}')
print(f'Total Price: ${total_price: .2f}\n')

#%%

# Part 2: 24-hour Clock Calculator

# Ask user to enter current hour
current_hour = int(input("Enter the current hour:\n"))

# Ask user to enter number of hours to wait for alarm
wait_hours = int(input("Enter the number of horus to wait for the alarm:\n"))

# Calculate hour on a 24-hour clock when alarm goes off
alarm_hour = (current_hour + wait_hours) % 24

# Output time on 24-hour clock when alarm goes off
print(f'The alarm will go off at {alarm_hour}:00.')
