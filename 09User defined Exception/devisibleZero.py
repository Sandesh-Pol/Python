for _ in range(int(input())):
    a, b = input().split() 
    try:
        result = int(a)//int(b)
    except ZeroDivisionError as e:
        print(f"Error Code:",e)
    except ValueError as e:
        print(f"Error Code:",e)    
    else:
        print(result)