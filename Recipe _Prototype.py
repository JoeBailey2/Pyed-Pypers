meals = {'Burger': {'Ingredients': 'Beef Mince, Bap, Tomato, Lettuce', 'Recipe': 'Roll minced beef into a patty, next slice tomatoes into thin circles, chop lettuce and assemble the burger.'}, 'Lasagna': {'Ingredients': 'Milk, Flour, Tomato Sauce, Beef Mince, Cheese, Pasta', 'Recipe': 'Heat cheese with flour and milk to make cheese sauce, then heat tomato sauce and beef mince, next layer the pasta sheets and mince sauce and cheese three times.'}, 'Steak': {'Ingredients': 'Steak Fillet, Potato, Mushrooms', 'Recipe': 'Slice any excess fat off the steak, then chop potatoes into chips and heat for 40 minutes in oven, then fry mushrooms for 8 minutes and fry the steak according to personal taste.'}, 'Sandwich': {'Ingredients': 'Bread, Cheese, Coleslaw', 'Recipe': 'Slice bread, cut cheese into thin slices, layer coleslaw onto the bread and then the cheese.'}}



import random

random_number = random.random()


def find_recipe():
    if random_number > 0 and random_number < 0.25:
        print ('Homemade Burger!' + str(meals['Burger']))
    elif random_number >= 0.25 and random_number < 0.50:
        print ('Lasagna!' + str(meals['Lasagna']))
    elif random_number >= 0.5 and random_number < 0.75:
        print ('Steak and Chips!' + str(meals['Steak']))
    else:
        print ('Cheese Sandwich!' + str(meals['Sandwich']))
        
def check_user():
    ui= input('Do you want to see a random recipe?')
    if ui == 'yes' or ui == 'yeah':
        find_recipe()
    else:
        print ('Oh well, maybe next time...')

