"""Restaurant rating lister."""


def read_file(filename):
    """Read information from a file"""

    with open(filename) as file:

        content = file.readlines()
        
    user_restaurante = input("Enter a new restaurante: ") 
    user_rate = input("Enter a Rate: ")
    content.append(f"{user_restaurante}:{user_rate}")     
   
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
    """Spits out the ratings in alphabetical order by restaurant
     
    The result should should be like ...
    Donut You Want Me Baby is rated at 1.
    """

    result = []

    for rate in content.items():        
        result.append(f"{rate[0]} is rated as {rate[1]}.")

    for item in sorted(result):
        print(item)




data = read_file(f"scores.txt")
# print(data)
restaurantes_and_rates = dict_restaurantes(data)
# print(restaurantes_and_rates)  
print_restaurante_and_rate(restaurantes_and_rates) 
    