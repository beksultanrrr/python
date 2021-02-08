word = input()
small = 0
cap = 0
for i in word:
        if 'a' <= i <= 'z':
                small += 1       
        elif 'A' <= i <= 'Z':
                cap += 1
        else:
                pass     
            
if small<cap:
    print(word.upper())