"""Restaurant rating lister."""


def read_file(filename):
    """Read information from a file"""

    with open(filename) as file:

        content = file.readlines()       
   
        return content
    



def dict_restaurantes(content):
    """Split up the content into a dictionary"""
    
    # if content == "Thank you, Good bye":
    #     return "Thank you, Good bye"

    restaurantes_rate = {}

    for restaurante in content:
            restaurante_splited = restaurante.rstrip().split(":")
            restaurante_name, rate = restaurante_splited[0:2]
            restaurantes_rate[restaurante_name] = int(rate)

    return restaurantes_rate



def print_restaurante_and_rate(content):
    """Spits out the ratings in alphabetical order by restaurant,
     
    The result should should be like ...
    Donut You Want Me Baby is rated at 1.
    """

    # if type(content) != dict:
    #     print("Thank you, Good bye")
    #     return 
    
    result = []

    for rate in content.items():        
        result.append(f"{rate[0]} is rated as {rate[1]}.")

    for item in sorted(result):
        print(item)




new_restaurante_rate = []

while True:
    
    user_choice = int(input('''\nIf you would like to See all the ratings, press 1,\nTo Add a new restaurant and Rate, press 2,\nOr press any other key to Quit: '''))

    restaurante_data = read_file(f"scores.txt")  
    

    if len(new_restaurante_rate):
        new_restaurante_rate.extend(restaurante_data)
        restaurantes_and_rates = dict_restaurantes(new_restaurante_rate)
    else:
        restaurantes_and_rates = dict_restaurantes(restaurante_data)   


    if user_choice == 1:
        print_restaurante_and_rate(restaurantes_and_rates) 

    elif user_choice == 2:
        user_restaurante = input("\nEnter a new restaurante: ").title()      

        while True:           
            user_rate = input("\nEnter a Rate: ")

            if not user_rate.isdigit():
                continue
            if user_rate not in "12345":
                continue
            else:
                break                  

        new_restaurante_rate.append(f"{user_restaurante} : {user_rate}")             
            
    else:    
        print("Thank you, Good bye")
        break    
        