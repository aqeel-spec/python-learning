# from typing import Dict, Union, Optional
# import pprint

# Key = Union[int,str] # create custom type
# Value = Union[int, str, list, dict, tuple, set]

# user_details : Dict[Key,Value] = {
#                                   "name":"Aqeel Shahzad",
#                                   "fname" : "Ghulam Jafir",
#                                   "graduation" : "BS Mathematics",
#                                   "age" : 20,
#                                   "address" : {
#                                       "city" : "Chiniot",
#                                       "country" : "Pakistan"
#                                     },
#                                     "hobbies" : ["cricket","football"],
#                                     0 : "JAMstack developer",
#                                     {1,2,3} : "Hello",
#                                     [1,2,3] : "world",
#                                     (1,2,3) : "Hello"
#                                 }
                                
# pprint.pprint(user_details)

# abc : set[str] = { 'a','b','a','c','d','e','f' }
# print(abc)

# xyz : list[str] = list(abc)
# print(xyz)


# from typing import Dict, Union , Optional
# import pprint


# Key = Union[int,str,set] # create custom type
# Value = Union[int,str,list,dict,tuple, set]

# data : dict[Key,Value] = {}

# data['name'] = "Muhammad Qasim" # Add new key and value
# data['fname'] = "Muhammad Aslam"
# data['education'] = 'MSDS'

# print(data)

from typing import Dict, Union

Key = Union[str,int,set]
Value = Union[str,int,set,tuple , list , dict]

# str = ''
# int = 0
# set = {}
# tuple = ()
# list = []
# dict = {}

# Examples
# tuple = (1,2,3) output : (1,2,3)
# list = [1,2,3] output : [1,2,3]
# dict = {1:2,3:4} output :   {1:2,3:4}
# set = {1,2,3,2,3,1,1,1,1} output : {1,2,3}


# person details having first_name , last_name , age and city
# person : Dict[Key,Value] = {
#     'first_name': 'shubham',
#     'last_name': 'kumar',
#     'age': '21',
#     'city': 'delhi'
# }

# rivers : Dict[str,str] = {
#         'nile': 'egypt',
#         'amazon': 'brazil',
#         'yangtze': 'china'
#     }

# for river, country in rivers.items():
#     print(f"\nThe {river.title()} runs through {country.title()}.")
#     # name of each river in the dictionary
#     print(river.title())
#     # name of each country in the dictionary
#     print(country.title())

# # Solution two

# # list of places and three names "person names" want to use as a key
# # also store their places
# favourite_places : Dict[str,list[str]] = {
#     "John" : ["New York", "London", "Paris"],
#     "Mary" : ["Paris", "London", "New York"],
#     "Peter" : ["Singapor", "Swizerland", "Dubai"]
# }

# # Friends suggestions for their favourite places 
# # looping through dict to print each person's name and their favourite place
# for person, fav_places in favourite_places.items():
#     print(f"{person.title()}'s favourite places are :")
#     for place in fav_places:
#         print(f"\t{place.title()}")




# # dictionary to store prople favourite number
# favourite_numbers : Dict[str,list[int]] = {
#     "jen": [5,6,7,8],
#     "sarah": [1213,15],
#     "edward": [56,57,58],
#     "phil": [8],
#     "usman" : [67,68,69,80]
# }

# for person , fav_numbers in favourite_numbers.items():
#     print(f"{person.title()}'s favourite number are:")
#     # loop through fav_numbers
#     for number in fav_numbers:
#         print(f"\t{number}")


# making dictionary having name cities
# name of three cities as keys 
# dict as values having "city is in", "approximate populaltion" and 1 "fact" about city
cities : dict[str,dict] = {
    "karachi" : {
        "country" : "Pakistan",
        "population" : "14.91 million",
        "fact" : "Karachi is the Hub of IT industry of Pakistan"
    },
    "lahore" : {
        "country" : "Pakistan",
        "population" : "11.13 million",
        "fact" : "Lahore is the Heart of Pakistan"
    },
    "islamabad" : {
        "country" : "Pakistan",
        "population" : "10.00 million",
        "fact" : "Islamabad is the Capital of Pakistan"
    },
}
# print names of each city and all of its details
for city, details in cities.items():
    print(f"City : {city.title()}")
    for key, value in details.items():
        print(f"{key} : {value}")
