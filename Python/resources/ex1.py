def fn1(a,b):
    c= []
    for i in range(a,b):
        if (i%2==0):
            c.append(i)
    return c
l=fn1(10,20)
print(l)

def is_Lst_Palindrome(Lst):
    return Lst == Lst[::-1]
l=is_Lst_Palindrome([1,2,3,2,1])
l2=is_Lst_Palindrome([1,2,3,4,5])
print(l)
print(l2)

def check_duplicate(Lst):
    l2=[]
    for i in Lst:
        if i not in l2:
            l2.append(i)
        else:
            return True
    return False
l=check_duplicate([1,2,3,2,1])
l2=check_duplicate([1,2,3,4,5])
print(l)
print(l2)

def Assign_grade(Lst):
    for i in Lst:
        if i >= 90:
            print("Marks:",i,"Grade A")
        elif i >= 80 and i < 90:
            print("Marks:",i,"Grade B")
        elif i > 65 and i < 80:
            print("Marks:",i,"Grade C")
        elif i >= 40 and i <= 65:
            print("Marks:",i,"Grade D")
        elif i < 40:
            print("Marks:",i,"Grade F")
        else:
            print("Invalid Marks")

Assign_grade([78, 90, 34, 56, 89])