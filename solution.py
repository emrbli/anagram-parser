
string1 = input("a : ")

string2 = input("b : ")
#-----------------------------------------------------------------------------------------
s1 = list(string1)
s2 = list(string2)            

s1 = sorted(s1)
s2 = sorted(s2)

# print(s1)
# print(s2)

dlist = list()
dlist2 = list()
sayac=0
sayac1=0
sayac2=0
sayac3=0

if len(s1) == len(s2):
    for i in s1:
        if i in s2:
            sayac=sayac+1
        else:
            dlist.append(i)
            sayac=sayac+1
    print("Please remove from '"+string1+"' >> "+str(dlist))
    for j in s2:
        if j in s1:
            sayac1=sayac1+1
        else:
            dlist2.append(j)
            sayac1=sayac1+1
    print("Please remove from '"+string2+"' >> "+str(dlist2))
#-------------------------------------------------------------------------
if len(s1) > len(s2):
    for i in s1:
        if i in s2:
            sayac=sayac+1
        else:
            dlist.append(i)
            sayac=sayac+1
    print("Please remove from '"+string1+"' >> "+str(dlist))
#-------------------------------------------------------------------------
if len(s2) > len(s1):
    for i in s2:
        if i in s1:
            sayac=sayac+1
        else:
            dlist.append(i)
            sayac=sayac+1
    print("Please remove from '"+string2+"' >> "+str(dlist))
#-------------------------------------------------------------------------
str1 = str(string1)

str2 = str(string2)






def anagram_mi(str1, str2):

    n1 = len(str1)

    n2 = len(str2)

    if n1 != n2:

        return 0

    str1 = sorted(str1)

    str2 = sorted(str2)

    for i in range(0, n1):

        if str1[i] != str2[i]:

            return 0

    return 1


if anagram_mi(str1, str2):

    print("Yes it is an Anagram.")

else:
    print("No, it is not an Anagram")
   