#task1
print('print the words beginning with the letter "e"')
n=int(input())
count=0
for i in range(n):
    s1=str(input())
    if(s1[0]=='e'):
        count=count+1 
print(count)
#task2
print('count the numbers of replacements')
s1=str(input())
count1=0
for i in range(len(s1)):
    if(s1[i]==':'):
        count1=count1+1
print(s1.replace(':','%'))
print('count of replacmentletters',count1)
print('\n')

#task 3
print('delete the dot')
s1=str(input())
count1=0
for i in range(len(s1)):
    if(s1[i]=='.'):
        count1=count1+1
print(s1.replace('.',''))
print('count of replacmentletters',count1)
print('\n')
#task4
print('replace a and o')
s2=str(input())
count=0
for i in range(len(s2)):
    if(s2[i]=='a'):
        print(s2.replace('a','o'))
        count=count+1
print('count of replacmentletters',count)
print('count of all characters in string',len(s2))
print('\n')
#task 5
print('chaneg all uppecase letters to lower case')
s3=str(input())
print(s3.lower())
print('\n')
#task 6
print('delete all the letter with a')
s4=str(input())
count1=0
for i in range(len(s4)):
    if(s4[i]=='a'):
        count1=count1+1
print(s4.replace('a',''))
print('count of replacmentletters',count1)
print('\n')
#task7
print('replace n and *')
s5=str(input())
n=int((len(s5)/2))
for i in range(n):
    if(s5[i]=='n'):
        print(s5.replace('n','*'))
print('replacement string',len(s5))
print('\n')
#task8
print('count have many words are in line')
s6=str(input())
count1=0
for i in range(len(s6)):
    if(s6[i]!='.'):
        count1=count1+1
print(s6.replace('.',''))
print('count of replacmentletters',count1)
print(s6)
print('\n')
#Task 9
print('word in the text')
text = "This sentence is a sentence without mistake :D."
result = text.split()
print ("The total number of words is: "  + str(len(result)))
print ("The word 'sentence' occurs: " + str(result.count("sentence")))
print('\n')
#task 10
print(' word with the uppercase')
words="QWERTyUIOPASDFGHJKLZXCVBNM"
text1 = "This sentence is a sentence without mistake :D."
result1 = text.title()
print(result1)
print('\n')
#task 11
print ('Longest Consecutive Subsequence')
import re
string = 'nnnnnnnnnnnnaaaaaaaa!bruh moment ! show your skill!'
n = re.findall('[nn]+',string)
n_len = map(len,n)
maximal_n = max(n_len)
print(maximal_n)
string_replaced = string.replace('!','.')
print(string_replaced)
print('\n')
#task 12
print('find all words ending with i letter')
words = "hi,I am borring, i am have in osu 120 bpi oaoaoosi asodoasodasi ai"
word = words.split()
for w in word:
    if ( w.endswith('i')):
        print(w)
print('\n')
#task13
T = str(input("Enter text "))
i = []
count12 = 0
for w2 in T:
     count12+=1
     if w == '"':
         T = T[i[0]:i[1]-1]
print(T)
print('\n')
#task 14
print('find all words ending with i letter')
words1 = "hi,I am borring, i am have in osu 120 bpi oaoaoosi asodoasodasi ai"
word2 = words1.split()
for w3 in word2:
    if (w3[0]=='a'):
        if(w3.endswith('i')):
            print(w3)
print('\n')
#Task15
task15 = str(input("Enter smt "))
count = 0
while Task15.find("t") != -1:
    Task15 = Task15.replace("t", "", 1)
    count += 1
print(count)




    


