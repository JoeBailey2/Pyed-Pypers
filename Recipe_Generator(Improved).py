import random


recipe_name = {
  '1': 'Beef Burger & Chips',
  '2': 'Lasagne',
  '3': 'Steak & Chips',
  '4': 'Cheese Sandwich'
}

recipe = {
  '1':
    'Roll minced beef into a patty \n next slice tomatoes into thin circles \n chop lettuce and assemble the burger.',
  '2':
    'Heat cheese with flour and milk to make cheese sauce \n then heat tomato sauce and beef mince \n next layer the pasta sheets and mince sauce and cheese three times.',
  '3': 
    'Slice any excess fat off the steak, then chop potatoes into chips and heat for 40 minutes in oven, then fry mushrooms for 8 minutes and fry the steak according to personal taste.',
  '4':
     'Slice bread, cut cheese into thin slices, layer coleslaw onto the bread and then the cheese.'
}

ingredients = {
  '1':
    '200 grams Beef Mince \n'
    '1 Large White Bread Roll \n'
    '1 Whole Tomato \n'
    'Mixed Lettuce, One handful \n',
  '2': 
    'One liter Fresh Milk \n'
    '2 tbsp White Flour \n'
    'Tomato Sauce Puree \n'
    '500g Beef Mince \n'
    'Cheddar Cheese \n'
    'Pasta Sheets \n',
  '3': 
    '8 Oz Fillet Steak \n'
    '1/2 Portobello Mushroom(s) \n'
    'Potatoes \n',
  '4':
    'White Whole Loaf \n'
    '200g Cheese \n'
    'Coleslaw \n'
    }
    
random_number = random.random()
def find_recipe():
    if random_number > 0 and random_number < 0.25:
        print (recipe_name['1'] + '\n \n' + ingredients['1'] + ' \n' + recipe['1'])
    elif random_number >= 0.25 and random_number < 0.50:
        print (recipe_name['2'] + '\n \n' + ingredients['2'] + ' \n' + recipe['2'])
    elif random_number >= 0.5 and random_number < 0.75:
        print (recipe_name['3'] + '\n \n' + ingredients['3'] + ' \n' + recipe['3'])
    else:
        print (recipe_name['4'] + '\n \n' + ingredients['4'] + ' \n' + recipe['4'])
        
        
def check_user():
    check = input('Do you want to generate a recipe? (yes or no)').lower()
    if check == 'yes' or check == 'y' or check == 'yeah':
        find_recipe()
    elif check == 'no' or check =='n' or check =='nah':
        print ('Quitting Program')
    else:
        print ('Unrecognised Input- Please use yes or no.')
      
check_user()
        