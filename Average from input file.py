#CS 175L
#Sophia Ramirez Velandia
#Prof Gil
#Average from input file V2

def main():
    x=0
    total=0
    try:
        file=open('numbers.txt', 'r')
        for y in file:
            try:
                x+=1
                print('I read in',str(x), end=" ")
                print(f'{"number(s)  Current number is:":<33}', float(y), end=" ")
                print('Total is:   ', end=" ")
                total+=float(y)
                print(total)

            except ValueError:
                print('Non-numeric data found in the file.')
            
        average=total/x
        print('Average:', average)

    except IOError:
        print('An error occured trying to read in file.')

    except:
        print('An error occured.')

if __name__=='__main__':
    main()
    
    
