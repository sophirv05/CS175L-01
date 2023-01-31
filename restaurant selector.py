#CS175L
#Sophia Ramirez Velandia
#restaurant
#Professor Gil

vegetarian= False
vegan= False
gluten_free= False

answer1= input('Is anyone in your party a vegetarian? ')
if answer1 == 'yes' and 'Yes':
    vegetarian = True

answer2= input('Is anyone in your party a vegan? ')
if answer2 == 'yes'and 'Yes':
    vegan = True

answer3= input('Is anyone in your party gluten-free? ')
if answer3 == 'yes'and 'Yes':
    gluten_free = True

print('Here are your restaurant choices: ')
    
if vegetarian == False and vegan == False and gluten_free == False:
    print("    Joe's Gourment Burgers")

if vegetarian == True and vegan == False and gluten_free == True:
    print("    Main Street Pizza Company")

if vegetarian == True and vegan == True and gluten_free == True:
    print("    Corner Café")

if vegetarian == True and vegan == False and gluten_free == False:
    print("    Mama's Fine Italian")

if vegetarian == True and vegan == True and gluten_free == True:
    print("    The Chef's Kitchen")
    

    


