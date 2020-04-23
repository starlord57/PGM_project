## INPUT FORMAT
#n
#m
#samples
#DAG


## TAKING INPUT 
n = int(input())
m = int(input())
samples = []
for i in range(m):
    delta = [int(x) for x in input().split()]
    samples.append(delta)
DAG = []
for i in range(n):

        delta = [int(x) for x in input().split() ]
        DAG.append(delta)

print("Number of nodes ",n)
print("Number of samples ",m)
print("The samples given are :")
for i in range(m):
    print(samples[i])


print("The DAG given is :")
for i in range(n):
    print(DAG[i])













# C R E A T I N G    T H E   D E P E N D E N C Y    L I S T S

dep = [[]*n for i in range(n)] #List of list for storing the dependency of each varibale
ndep = [0]*n #List to store the number of variables a particular variable is dependent upon
# print(dep)
for j in range(n):
    for i in range(n):
        if DAG[i][j]==1:
            dep[j].append(i)
            ndep[j]+=1
print(dep)




for i in range(n): #iterating through all the variable constructing their CPT
    num = ndep[i] # 'num' represents the number of variables that the current variable is dependent upon
    print("For variable ",i,"dependent upon",dep[i])

    # The number of rows in the CPT are 2^num (for all combinations)
    for a in range(2**num): # Generating all 2^n combinations
        # print(a,999)
        delta = []
        for b in range(num): # Iterating through all the variables in the dependency list
            temp = 1<<b
            # print(a&temp)
            if a&temp:
                delta.append(1)
            else:
                delta.append(0)
            # delta.append(a&temp) #Adding the value of the dependency variables in the current sample
        zero = 0
        one = 0
        for sample in samples: #iterating through all the samples
            c0 = 0
            for c in range(num):
                element = dep[i][c]
                if sample[element]==delta[c]: # if the value of the variable in the sample is equal to the value of the variable in the current combination
                    c0+=1
            if c0 == num: # if all elements match only then is the current sample considered for the current combination
                if sample[i]==0:
                    zero+=1 # if the value of the variable is 0 we increase the count of zeros for the current combination
                else:
                    one+=1 # else count of 1
        total = zero+one
        if total==0:
            print(delta,"NA") # The case where no sample contained the current combination
        else:
            print(delta,":","0 :",zero/total,"1 :",one/total)
