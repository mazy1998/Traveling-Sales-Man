## pythom version https://github.com/CodingTrain/Rainbow-Code/blob/master/CodingChallenges/CC_35_TSP/CC_35.2_LexicographicOrder/sketch.js
## from Dan Shiffman http://shiffman.net

vals = [0,1,2,3]

def swap(a,i,j):
    temp = a[i]
    a[i]=a[j]
    a[j] = temp

def perms(n):
    if n==1:
        return 1
    else:
        return n*perms(n-1)
    
## Dans version would run through all x! perms, but we only need (x-1)! in a
## closed loop with no reversals.
##while 1:
##  ^^ for all perms
    
for p in range(0,perms(len(vals)-1)):
    print vals
    
    ##step 1
    largestI= -1
    for i in range(0,len(vals)-1):
        if vals[i]<vals[i+1]:
            largestI = i

    if largestI == -1:
        print "finished"
        break
    
    ##step 2    
    largestJ= -1
    for j in range(0,len(vals)):
        if vals[largestI] < vals[j]:
            largestJ = j
    ##step 3        
    swap(vals, largestI, largestJ)

    ##step 4
    endArray = vals[largestI+1:len(vals)]
    endArray.reverse()
    vals = vals[0:largestI+1] + endArray
    
