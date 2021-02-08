a=(input())
for i in a:
    if (a[0] in "a e i o u y  b c d f g h j k l m n p q r s t v w x z") and (a[1:-1] in "A E I O U Y  B C D F G H J K L M N P Q R S T V W X Z") and (a[-1] in  "A E I O U Y  B C D F G H J K L M N P Q R S T V W X Z"):
    
        print(a[0].upper()+a[1:-1].lower()+a[-1].lower())
        break
    else:
        print(a)
        break
    