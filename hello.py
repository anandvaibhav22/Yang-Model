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

def main():
    input_var = sys.argv[1]
    input_var1 = sys.argv[2]
    print(add(input_var,input_var1))

if __name__ == '__main__':
    main()
