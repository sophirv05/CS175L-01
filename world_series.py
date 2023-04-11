#CS 175L
#Sophia Ramirez Velandia
#Professor Gil
#Programming Exercise 7-10


def champions():
    file = open ('WorldSeriesWinners.txt', 'r')
    champ = []
    for infile in file:
        infile = infile.rstrip('\n')
        champ.append(infile)
    file.close()
    return champ

def search(champ):
    file = open ('WorldSeriesWinners.txt', 'r')
    name = ''
    while name != 'quit':
        name = input('Enter the name of the team or Quit: ')
        name = name.lower()
        if name != 'quit':
            search = [look for look in champ if look.lower() == name]
            times = (len(search))
            if times > 0:
                print(f'The {name} won the world series {times} times between 1903 and 2009')
            else:
                print('Team not found!')
        else:
            print('Bye! Have a nice day!')
            
def main():
    file = open ('WorldSeriesWinners.txt', 'r')
    infile = file.readline()
    champ = champions()
    search(champ)
    
    
if __name__ == '__main__':
    main()
