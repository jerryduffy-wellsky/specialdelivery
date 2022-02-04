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

#Output: 
'''
{'Order': {'Address': {'Street': '2108 Twain Ridge Dr.',
   'City': 'Lexington',
   'Region': 'KY',
   'PostalCode': '40514',
   'Type': 'House',
   'StreetNumber': '2108',
   'StreetName': 'TWAIN RIDGE DR',
   'CountyName': 'FAYETTE',
   'CountyNumber': '067'},
  'Coupons': [],
  'CustomerID': '',
  'Extension': '',
  'OrderChannel': 'OLO',
  'OrderID': 'j_FJrHOtu8teBv6dP_nu',
  'NoCombine': True,
  'OrderMethod': 'Web',
  'Payments': [{'Type': 'CreditCard',
    'Expiration': '0622',
    'Amount': 19.94,
    'CardType': 'MASTERCARD',
    'Number': '1058',
    'SecurityCode': 237,
    'PostalCode': 40514}],
  'Market': 'UNITED_STATES',
  'Currency': 'USD',
  'ServiceMethod': 'Delivery',
  'Tags': {},
  'Version': '1.0',
  'SourceOrganizationURI': 'order.dominos.com',
  'LanguageCode': 'en',
  'Partners': {},
  'NewUser': True,
  'metaData': {'PiePassPickup': False},
  'Amounts': {'Menu': 18.98,
   'Discount': 0,
   'Surcharge': 2.99,
   'Adjustment': 0,
   'Net': 18.98,
   'Tax': 0.96,
   'Tax1': 0.96,
   'Tax2': 0,
   'Bottle': 0,
   'Customer': 19.94,
   'Payment': 19.94},
  'BusinessDate': '2022-02-03',
  'EstimatedWaitMinutes': '35-45',
  'AmountsBreakdown': {'FoodAndBeverage': '15.99',
   'Adjustment': '0.00',
   'Surcharge': '0.00',
   'DeliveryFee': '2.99',
   'Tax': 0.96,
   'Tax1': 0.96,
   'Tax2': 0,
   'Tax3': 0,
   'Tax4': 0,
   'Tax5': 0,
   'Bottle': 0,
   'Customer': 19.94,
   'RoundingAdjustment': 0,
   'Cash': 0,
   'Savings': '0.00'},
  'StoreID': '1407',
  'Email': 'tim.kessler@gmail.com',
  'FirstName': 'Tim',
  'LastName': 'Kessler',
  'Phone': '8594023394',
  'IP': '199.168.73.11',
  'UserAgent': 'python-requests/2.24.0',
  'Promotions': {'Redeemable': [],
   'AvailablePromos': {'EndOfOrder': '8130'},
   'Valid': []},
  'AvailablePromos': {'EndOfOrder': '8130'},
  'PulseOrderGuid': '654c330f-3ef7-4b7e-9bdc-9a13ec700d27',
  'PricingFlag': '0',
  'Status': 0,
  'PlaceOrderTime': '2022-02-03 20:49:43',
  'Products': [{'ID': 1,
    'Code': '14SCPFEAST',
    'Qty': 1,
    'CategoryCode': 'Pizza',
    'SizeCode': '14',
    'FlavorCode': 'HANDTOSS',
    'Price': 15.99,
    'Amount': 15.99,
    'Status': 0,
    'LikeProductID': 0,
    'Name': 'Large (14") Hand Tossed Ultimate Pepperoni',
    'IsNew': False,
    'NeedsCustomization': False,
    'AutoRemove': False,
    'Fulfilled': False,
    'SideOptions': [],
    'Tags': {'Specialty': 'true',
     'DefaultSides': '',
     'DefaultToppings': 'X=1,C=1,P=1.5,Cs=1,Cp=1'},
    'descriptions': [{'portionCode': '1/1',
      'value': 'Robust Inspired Tomato Sauce, Cheese, Extra Pepperoni, Shredded Parmesan, Shredded Provolone Cheese'}]}],
  'LoadTime': 60,
  'Loyalty': {'EligibleForPOE': True},
  'StorePlaceOrderTime': '2022-02-03 20:49:46',
  'StoreOrderID': '2022-02-03#1049',
  'PlaceOrderMs': 2796,
  'OrderAcknowledgedAt': '2022-02-04 01:49:46',
  'dssRouteMode': 'NONE',
  'ID': '654c330f-3ef7-4b7e-9bdc-9a13ec700d27'},
 'Status': 0,
 'Offer': {'CouponList': [], 'ProductOffer': ''},
 'EmailHash': '815b78f6c0603ae140ec14c8d89f8936074fdd2d62e344c9523c75e05f7dd50d',
 'DeviceId': '08c77b90bceb4f55b14fbd9fe4f3b79c822dcaf026a6b37046cbce883403862d',
 'NeedsInStoreProcessing': False,
 'StatusItems': [{'Code': 'Success'}]}
 '''