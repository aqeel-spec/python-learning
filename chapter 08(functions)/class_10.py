# from typing import Callable

# def my_decorator(func: Callable[[int], None]) -> Callable[[int], None]:
#     def wrapper(num1: int) -> None:
#         print("Something is happening before the function is called.")
#         func(num1)
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello(num1: int) -> None:
#     print(num1)

# say_hello(100)

# (( Exercise 01 ))

# def display_message() -> None:
#     """Display a message about what I'm learning."""
#     print("I'm learning about functions!")

# display_message()

# def favorite_book (title : str) -> None:
#     """function that accept only one parameters 
#      of book title and print a message about it.
#     """
#     print(f"One of my favorite books is {title.title()}")

# favorite_book("alice in wonderland")

# (( Exercise 02 ))

# Note : default parameters must be at the end of the list of parameters.
# def make_shirt(message:str, size : str = 'large') -> None:
#     """
#      This function prints a message on a T-shirt.
#      message : I love Python!.
#     """
#     print(f"Your shirt is size {size} and says {message}")

# # make a shirt of large size also has default parameters
# make_shirt("I love Python")

# # shirt having medium size
# make_shirt("I love Python","medium")

# def describe_city (city_name : str , country : str = 'Pakistan') -> None:
#     print(f"{city_name.title()} is in {country.title()}"  )
    
# describe_city('Karachi')
# describe_city('Lahore')
# describe_city('Tengah' , 'singapore' 

# from typing import Union, Optional

# def make_album (artist_name : str , album_title : str, no_of_songs: Optional[int] = None) -> dict[str,Union[str,int]]:
#     print('\n')
#     album : dict[str,Union[str,int]]  = {
#         'artist' : artist_name,
#         'album' : album_title
#     }
#     if no_of_songs is not None:
#         album['no_of_songs'] = no_of_songs
    
#     return album

# # print each dict to ensure that information is showing correctly
# print(make_album('Michael Jackson', 'Thriller'))
# print(make_album('Eminem', 'The Marshall Mathers LP'))
# print(make_album('Rihanna', 'Stay'))

# """use None to add an optional parameter to func \
#    that store number of songs on an album.
#    if no. of songs then add value to album dictionary
# """

# # at least one new function that includes no_of_songs on an album
# print(make_album('Michael Jackson', 'Thriller', 10))


# from typing import Union, Optional

# def make_album (artist_name : str , album_title : str, no_of_songs: Optional[int] = None) -> dict[str,Union[str,int]]:
#     print('\n')
#     album : dict[str,Union[str,int]]  = {
#         'artist' : artist_name,
#         'album' : album_title
#     }
#     if no_of_songs is not None:
#         album['no_of_songs'] = no_of_songs
    
#     return album



# # while loop untill user enter q
# while True:
#     # ask user to enter artist name and album title
#     artist_name : str = input('Enter artist name :\t')
#     album_title : str = input('Enter album title :\t')
#     # ask user to enter number of songs
#     no_of_songs : Optional[int] = int(input('Enter number of songs :\t'))

#     # stop keywords list
#     exit : list[str] = ['q','quit','stop','exit','cancel']
    
#     # check if user want to quit
#     if artist_name.lower() in exit or album_title.lower() in exit:
#         break
#     elif no_of_songs is None or no_of_songs == str :
#         no_of_songs = 0
#         print(f"InValid songs list :\t{no_of_songs}")
#         break
    
#     # create album
#     album = make_album(artist_name, album_title, no_of_songs)
#     print(album)





# Exercise 5
# from typing import Union,Optional,Mapping

# def build_profile(first : str, last : str, **user_info : str ) -> Mapping[str,Union[str,int]]:
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first 
#     user_info['last_name'] = last
#     return user_info

from typing import Union, List , Dict, Mapping

def car_Info ( manufecturer : str , model : str , **more : Dict[str,int] ) -> Mapping[str,Union[str,int]]:
    """Build a dictionary containing everything we know about a car."""
    car_info  = {
        'manufacture' : manufecturer,
        'model' : model
        # 'year' : year
        # 'color' : color
        # 'price' : price
    }
    return car_info