#s = "sandesh pol"

#s = " ".join(s.split(s.title()))

#print(s)


def swap_case(s):
    temp=''
    for litter in s:
        if(litter==litter.upper()):
            temp += litter.lower()
        else: 
            temp += litter.upper()
    return temp

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

