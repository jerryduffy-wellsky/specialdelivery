# Config:
# Python version: 3
# Source: https://github.com/ggrammar/pizzapi
# git clone git@github.com:ggrammar/pizzapi.git pizzapi
# cd pizzapi


from pizzapi import *

customer = Customer('FirstName', 'LastName', 'email@gmail.com', '8595551212')
address = Address('street address', 'Lexington', 'KY', '40514')

store = address.closest_store()

print(store.get_details()) 

menu = store.get_menu() 

menu.search(Name='Pep')

# Output:
# 10SCPFEAST Small (10") Hand Tossed Ultimate Pepperoni $11.99 10 S_PIZPX {'X': '1', 'C': '1', 'P': '1.5', 'Cs': '1', 'Cp': '1'}
# 10TPFEAST Small (10") Thin Ultimate Pepperoni $11.99 10 S_PIZPX {'X': '1', 'C': '1', 'P': '1.5', 'Cs': '1', 'Cp': '1'}
# 12SCPFEAST Medium (12") Hand Tossed Ultimate Pepperoni $13.99 12 S_PIZPX {'X': '1', 'C': '1', 'P': '1.5', 'Cs': '1', 'Cp': '1'}
# 12TPFEAST Medium (12") Thin Ultimate Pepperoni $13.99 12 S_PIZPX {'X': '1', 'C': '1', 'P': '1.5', 'Cs': '1', 'Cp': '1'}
# PBKIREPX Large (14") Brooklyn Ultimate Pepperoni $15.99 14 S_PIZPX {'X': '1', 'C': '1', 'P': '1.5', 'Cs': '1', 'Cp': '1'}
# 14SCPFEAST Large (14") Hand Tossed Ultimate Pepperoni $15.99 14 S_PIZPX {'X': '1', 'C': '1', 'P': '1.5', 'Cs': '1', 'Cp': '1'}
# 14TPFEAST Large (14") Thin Ultimate Pepperoni $15.99 14 S_PIZPX {'X': '1', 'C': '1', 'P': '1.5', 'Cs': '1', 'Cp': '1'}
# P10IGFPX Small (10") Gluten Free Crust Ultimate Pepperoni $11.99 10 S_PIZPX {'X': '1', 'C': '1', 'P': '1.5', 'Cs': '1', 'Cp': '1'}
# P12IPAPX Medium (12") Handmade Pan Ultimate Pepperoni $14.99 12 S_PIZPX {'X': '1', 'C': '1', 'P': '1.5', 'Cs': '1', 'Cp': '1'}
# REDPEPPER Red Pepper Packets $0.25  F_SIDRED {}

# Create Order:
order = Order(store, customer, address)
order.add_item('14SCPFEAST') # add a 14-inch pan pizza ultimate pepperoni
#order.add_item('MARINARA') # with an extra marinara cup
#order.add_item('20BCOKE')  # and a 20oz bottle of coke
# Output:
'''
{'Code': '14SCPFEAST',
 'FlavorCode': 'HANDTOSS',
 'ImageCode': '14SCPFEAST',
 'Local': False,
 'Name': 'Large (14") Hand Tossed Ultimate Pepperoni',
 'Price': '15.99',
 'ProductCode': 'S_PIZPX',
 'SizeCode': '14',
 'Tags': {'Specialty': True,
  'DefaultSides': '',
  'DefaultToppings': 'X=1,C=1,P=1.5,Cs=1,Cp=1'},
 'AllowedCookingInstructions': 'WD,NB,PIECT,SQCT,UNCT,GO,NGO',
 'DefaultCookingInstructions': 'NB,PIECT,GO',
 'Prepared': True,
 'Pricing': {'Price2-4': '21.99',
  'Price1-0': '15.99',
  'Price1-3': '20.49',
  'Price2-3': '20.49',
  'Price1-4': '21.99',
  'Price2-2': '18.99',
  'Price1-1': '17.49',
  'Price2-1': '17.49',
  'Price1-2': '18.99',
  'Price2-0': '15.99'},
 'Surcharge': '0',
 'ID': 1,
 'isNew': True,
 'Qty': 1,
 'AutoRemove': False}
'''

#order.pay_with(card) # Test - dry run
order.place(card)  #submits order and payment info

