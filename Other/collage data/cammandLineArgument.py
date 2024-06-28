import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python script_name.py num1 num2")
        return
    
    num1 = float(sys.argv[1])  
    num2 = float(sys.argv[2])  
    
    result = num1 + num2
    
    print("Sum:", result)

if __name__ == "__main__":
    main()
