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
    

def dict_restaurantes(content):
    """Split up the content into a dictionary"""   

    restaurantes_rate = {}

    for restaurante in content:
            restaurante_splited = restaurante.rstrip().split(":")
            restaurante_name, rate = restaurante_splited[0:2]
            restaurantes_rate[restaurante_name] = int(rate)


    return restaurantes_rate


def print_restaurante_and_rate(content):
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

    counter = 0
    for file in list_of_files:
        counter += 1
        print(f"{counter}. {file}")


    work_file = int(input(f"Press the number of file you would you like to open: "))

    file_choosen = list_of_files[work_file-1]   

    
    return file_choosen


def prepare_data(file):
    """Prapare the data to work on the program"""
    
    updated_restaurantes = []
    restaurante_data = read_file(file)

    for data in restaurante_data:
        updated_restaurantes.append(data)


    return updated_restaurantes
     


list_of_files_to_choose = list_of_file_on_the_directory(".")    
file = choose_file(list_of_files_to_choose)
data = prepare_data(file)


while True:
    
    user_choice = int(input('''\nIf you would like to See all the ratings, press 1,\nTo Add a new Item and Rate, press 2,\nTo update an Item rating press 3, \nTo open another file press 4, \nOr press any other key to Quit: \n'''))    

    restaurantes_and_rates = dict_restaurantes(data)  
    
            
    if user_choice == 1:
        print("\n")
        print_restaurante_and_rate(restaurantes_and_rates) 

    elif user_choice == 2:
        user_restaurante = input("\nEnter a new Item: ").title()      

        while True:           
            user_rate = input("\nEnter a Rate: ")

            if not user_rate.isdigit():
                continue
            if user_rate not in "12345":
                continue
            else:
                break                  

        data.append(f"{user_restaurante}: {user_rate}")   

    elif user_choice == 3:   
        update_restaurante = input("\nWhich Item would you like to update? ").title()
        new_rate = input("\nWhat rate do you want to rate this Item with? Please enter a number from 1 to 5: ")
        data.append(f"{update_restaurante.title()}: {new_rate}")

    elif user_choice == 4:          
        file = choose_file(list_of_files_to_choose)
        data = prepare_data(file)

    else:    
        print("Thank you, Good bye")
        break    
        