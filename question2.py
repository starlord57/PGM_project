## I N P U T     F O R M A T
#n
#DAG
#CPD
#m

n = int(input())
print("Number of nodes : ",n)
DAG = []

for i in range(n):
    delta = [int(x) for x in input().split()]
    DAG.append(delta)
print("DAG : ")
for i in range(n):
    print(DAG[i])






from random import choices
population = [0,1]

dep = [[]*n for i in range(n)]
ndep = [0]*n

for j in range(n):
    for i in range(n):
        if DAG[i][j]==1:
            dep[j].append(i)
            ndep[j]+=1

print("Dependency lists for all nodes :")
print(dep)
print("")
print("")

CPD = []
for i in range(n):
    delta1 = []
    for j in range(2**ndep[i]):
        delta2 = [float(x) for x in input().split()]
        delta1.append(delta2)
    CPD.append(delta1)

print("CPT tables :")
for i in range(n):
    print("node :",i)
    for j in range(2**ndep[i]):
        print(CPD[i][j])
    print("")







m = int(input())
for i in range(m):
    delta = []
    for a in range(n): # For each sample iterating through each variable randomly selecting its value based on the CPT
    # We keep chosing the values of variables and then the other variables CPT row is selected based upon the earlier choices made
        num = ndep[a]
        val = 0
        for b in dep[a]:
            # print(a,b)
            temp = delta[b] # The value of this particular dependency variable in the current sample
            # print("temp",temp)
            # print(temp[0])
            val+=temp*(2**(num-1)) # CPT row number (2^num rows in CPT of a variable )
            # print("val",val)
            num-=1
        # print(val,"v",delta)
        weights = CPD[a][val] # The weights to be considered while selecting the value of the current variable randomly ( a particular row of its CPT)
        selected = choices(population,weights) # The selected choice
        # print(selected,55)
        delta.append(selected[0]) # Adding it as other values will be based on this
    print("Sample :", i+1,delta)
