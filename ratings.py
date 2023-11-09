import os
import sys


"""Restaurant rating lister."""

def list_of_file_on_the_directory(dir_path):
    """List all files in a given directory"""
    
    dir_list = os.listdir(dir_path)

    extension = ".txt"
    files = []

    for file in dir_list:
        if extension in file:
            files.append(file)  

    return files


def read_file(filename):
    """Read information from a file"""

    with open(filename) as file:
        
        content = file.readlines() 

   
        return content
    

def dict_restaurants(content):
    """Split up the content into a dictionary"""   

    restaurants_rate = {}

    for restaurant in content:
            restaurant_splited = restaurant.rstrip().split(":")
            restaurant_name, rate = restaurant_splited[0:2]
            restaurants_rate[restaurant_name] = int(rate)


    return restaurants_rate


def print_restaurant_and_rate(content):
    """Splits out the ratings in alphabetical order by restaurant,
     
    The result should should be like ...
    Donut You Want Me Baby is rated at 1.
    """

    result = []

    for rate in content.items():        
        result.append(f"{rate[0]} is rated as {rate[1]}.")

    for item in sorted(result):
        print(item)


def choose_file(list_of_files):
    """Ask the user which file to work on"""


    for num in range(0, len(list_of_files)):
        print(f"{num}. {list_of_files[num]}")


    work_file = int(input(f"Press the number of file you would you like to open: "))

    file_choosen = list_of_files[work_file-1]   

    
    return file_choosen


def prepare_data(file):
    """Prapare the data to work on the program"""
    
    updated_restaurants = []
    restaurant_data = read_file(file)

    for data in restaurant_data:
        updated_restaurants.append(data)


    return updated_restaurants
     


list_of_files_to_choose = list_of_file_on_the_directory(".")    
file = choose_file(list_of_files_to_choose)
data = prepare_data(file)


while True:
    
    user_choice = int(input('''\nIf you would like to See all the ratings, press 1,\nTo Add a new Item and Rate, press 2,\nTo update an Item rating press 3, \nTo open another file press 4, \nOr press any other key to Quit: \n'''))    

    restaurants_and_rates = dict_restaurants(data)  
    
            
    if user_choice == 1:
        print("\n")
        print_restaurant_and_rate(restaurants_and_rates) 

    elif user_choice == 2:
        user_restaurant = input("\nEnter a new Item: ").title()      

        while True:           
            user_rate = input("\nEnter a Rate: ")

            if not user_rate.isdigit():
                continue
            if user_rate not in "12345":
                continue
            else:
                break                  

        data.append(f"{user_restaurant}: {user_rate}")   

    elif user_choice == 3:   
        update_restaurant = input("\nWhich Item would you like to update? ").title()
        new_rate = input("\nWhat rate do you want to rate this Item with? Please enter a number from 1 to 5: ")
        data.append(f"{update_restaurant.title()}: {new_rate}")

    elif user_choice == 4:          
        file = choose_file(list_of_files_to_choose)
        data = prepare_data(file)

    else:    
        print("Thank you, Good bye")
        break    
        