## I N P U T     F O R M A T
#n
#DAG
#CPD
#queyn
#queryd

n = int(input())
print("Number of nodes : ",n)
DAG = []
dep = [[]*n for i in range(n)]
ndep = [0]*n

for i in range(n):
    delta = [int(x) for x in input().split()]
    DAG.append(delta)
print("DAG : ")
for i in range(n):
    print(DAG[i])

for j in range(n):
    for i in range(n):
        if DAG[i][j]==1:
            dep[j].append(i)
            ndep[j]+=1

print("Dependency lists for all nodes :")
print(dep)
print("")
print("")

CPT = []
for i in range(n):
    delta1 = []
    for j in range(2**ndep[i]):
        delta2 = [float(x) for x in input().split()]
        delta1.append(delta2)
    CPT.append(delta1)

print("CPT tables :")
for i in range(n):
    print("node :",i)
    for j in range(2**ndep[i]):
        print(CPT[i][j])
    print("")




queryn = [int(x) for x in input().split()]
queryd = [int(x) for x in input().split()]





## CHECKING IF THE QUERY IS VALID
flag = 0
for i in range(n):

        if queryn[i]!=2 and queryd[i]!=2:
            if queryn[i]!= queryd[i]:
                flag = 1

                break
if flag ==1 :
    print("Result : 0 as there is clash ")
else:
    numerator = []
    for i in range(n):
        if queryn[i]==2:
            numerator.append(queryd[i])
        else:
            numerator.append(queryn[i])


    denominator = queryd
    print("Numerator :",numerator)
    print('Denominator :',denominator)



    ## F I N D I N G   T H E   N U M E R A T O R   P R O B A B I L I T Y
    nprob = 0
    print(" Calculating the numerator ")
    for c in range(2**n): # Generating all 2^n combinations
        # print("combination number ",c)
        FLAG = 0
        for i in range(n):
            # print("variable ",i)
            temp = 1<<i
            temp2 = c&temp
            if temp2>0:
                temp2 = 1
            # print("value of varibale in combination",temp2)
            if numerator[i]!=2:
                if numerator[i]!=temp2:
                    FLAG = 1
                    # print("value doesnt match query therefore current combination ignored ",temp2,)
                    break
        if FLAG==1:
            continue
        # print("valid combination ")
        cprob = 1
        for i in range(n):
            t = 1<<i
            t2 = c&t
            if t2>0:
                t2=1

            val = 0 # the final value of val will tell which row of the CPT we will select
            # for j in range(ndep[i]):
            delta= ndep[i]

            for k in dep[i]:
                    temp = 1<<k #
                    temp2 = c&temp
                    if temp2>0:
                        temp2=1 # contains the value of the current dependency variable
                    val+=temp2*(2**(delta-1))
                    delta-=1

            cprob*=CPT[i][val][t2]
        print("Combination ",c," contributes ",cprob)
        nprob+=cprob

    print("nprob",nprob)
    ### F I N D I N G    D E N O M I N A T O R     P R O B A B I L I T Y
    dprob = 0
    print("Calculating the denominator ")
    for c in range(2**n): # Generating all 2^n combinations
        FLAG = 0
        for i in range(n):
            temp = 1<<i
            temp2 = c&temp
            if temp2>0:
                temp2=1
            if denominator[i]!=2:
                if denominator[i]!=temp2:
                    FLAG = 1
                    break
        if FLAG==1:
            continue
        cprob = 1
        for i in range(n):
            t = 1<<i
            t2 = c&t
            if t2>0:
                t2=1
            val = 0 # the final value of val will tell which row of the CPT we will select
            # for j in range(ndep[i]):
            delta= ndep[i]
            # print("i",i)

            for k in dep[i]:
                    # print("k",k)
                    temp = 1<<k #
                    # print("val of k",k)
                    temp2 = c&temp # contains the value of the current dependency variable
                    if temp2>0:
                        temp2=1
                    val+=temp2*(2**(delta-1))
                    delta-=1
            # print("vald",val,t2)

            cprob*=CPT[i][val][t2]
        print("combination ",c,"contributes ",cprob)
        dprob+=cprob
    print("dprob",dprob)
    ans = nprob/dprob
    print("The result of the current query is",ans)
