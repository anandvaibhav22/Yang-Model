'''
import sys

def add(a,b):
   print(int(a)+int(b))
    
if __name__ == "__main__":
	add(1,2)
'''
import sys

def add (a,b):
    return int(a)+int(b)

def printingvalues(value):
	print ('value is {}'.format(value))
	
def main():
    input_var = sys.argv[1]
    input_var1 = sys.argv[2]
    input_var2 = sys.argv[3]
    print(add(input_var,input_var1))
    print(printingvalues(input_var2))

if __name__ == '__main__':
    main()
