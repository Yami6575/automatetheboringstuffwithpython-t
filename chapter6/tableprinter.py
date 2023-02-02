tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printtable(table):
    for i in range(len(table)):
        maxstring=''
        for j in tableData[i]:
            if len(j)>=len(maxstring):
                maxstring=j
        a=len(maxstring)
        for k in tableData[i]:
            print(k.rjust(a,' '),)
        
        
        
printtable(tableData)


