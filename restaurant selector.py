#CS175L
#Sophia Ramirez Velandia
#restaurant V2
#Professor Gil

vegetarian= False
vegan= False
gluten_free= False

keep_going= 'yes'
while keep_going =='yes':
    answer1= input('Is anyone in your party a vegetarian? ')
    answer1lower=answer1.lower()
    if answer1 == 'yes':
        vegetarian = True  

    answer2= input('Is anyone in your party a vegan? ')
    answer2lower=answer2.lower()
    if answer2 == 'yes':
        vegan = True

    answer3= input('Is anyone in your party gluten-free? ')
    answer3lower=answer3.lower()
    if answer3 == 'yes':
        gluten_free = True

    print('\nHere are your restaurant choices:')
    
    if not vegetarian and not vegan and gluten_free:
        print("Joe's Gourmet Burgers")

    elif not vegan and not gluten_free:
        print("Mama's Fine Italian")

    elif not vegan:
        print("Main Street Pizza")

    print("Corner Cafe")
    print("Chef's Kitchen")


    keep_going= input('Do you want to do keep going? ')

    

    


