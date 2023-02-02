
lst=['apple','banana','tofu','cats']
def commacode(list):
    st=''
    for i in list:
        st+=i+','
    return st



print(commacode(lst))
