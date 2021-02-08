
l1=['A','a','e','E',"i",'I', "O",'o','U','u']
l2=['B','b', 'C','c', 'D','d', 'F','f','g', 'G','h', 'H','j' ,'J', 'k', 'K','l', 'L', 'm', 'M', 'N','n','p', 'P','q', 'Q','r', 'R','s', 'S','t' 'T','v', 'V','w', 'W','x', 'X', 'Y','y','z', 'Z']
for i in range(1):
    a=str(input()).lower()
    if a[i]==l1:
        print(a.replace(l1,'.'))