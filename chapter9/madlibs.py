import os
adjective=input("enter")
noun=input("enter")
verb=input("enter")
adverb=input("enter")
textfile=open('/home/nikhil/test/test.txt','r')
testfile=textfile.read()
print(testfile)
a=[]
a=testfile.split()
print(a)

for i in a:
    if i=='ADJECTIVE':
        a[a.index(i)]==adjective
    if i=='VERB':
        a[a.index(i)]==verb
    if i=='NOUN':
        a[a.index(i)]==noun
    if i=='ADVERB':
        a[a.index(i)]==adverb

writefile=open('/home/nikhil/test/test.txt','w')
wrtfile=writefile.write(f'The {adjective} panda walked to the {noun} and then {verb}. A nearby {noun} was unaffected by these events.')

textfile.close()
writefile.close()