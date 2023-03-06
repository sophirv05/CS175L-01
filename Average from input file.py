#CS 175L
#Sophia Ramirez Velandia
#Prof Gil
#Average from input file

def main():
    file=open('numbers.txt', 'r')
    x=0
    total=0
    for y in file:
        x+=1
        print('I read in',str(x), end=" ")
        print(f'{"number(s)  Current number is:":<33}', float(y), end=" ")
        print('Total is:   ', end=" ")
        total+=float(y)
        print(total)
    average=total/x
    print('Average:', average)

if __name__=='__main__':
    main()
    
    
