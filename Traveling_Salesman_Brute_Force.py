#uses embeded tuples for points, runs every permutation when its created and does not have a list of permutations(size x!).
#without uses lists of size x! this program uses much less memory and is only bottle necked by cpu power.
from tkinter import *
import time
import random
import math as m



    
class MyFrame(Frame):
    def __init__(self):
            Frame.__init__(self)
            num5=800
            self.myCanvas = Canvas(width=num5,height=num5,bg="black")
            self.myCanvas.grid()
            
            ##number of cities
            num2 = cities =10
            
            vals = []            
            num7= 1000
            points= []
            tempdistance= []
            distances = []
            tempperms= []
            tempdistance = []
            d1=0
            d2=0
            bestpath = [0 for i in range(num2+1)]
            worstpath = [0 for i in range(num2+1)]
            a=0
            b=10**12
            c=0
            showworstpath = False

            def swap(a,i,j):
                temp = a[i]
                a[i]=a[j]
                a[j] = temp

            def perms(n):
                if n==1:
                    return 1
                else:
                    return n*perms(n-1)

            ##makes random points
            for z in range(0,num2):    
                x =random.randint(0,num5)
                y= random.randint(0,num5)
                points.append((x,y))
            print(points)

            ##finds every distance
            for w in range(0,num2):
                for p in range(0,num2):
                    tempdistance.append(m.sqrt((points[p][0]-points[w][0])**2+(points[p][1]-points[w][1])**2))
                distances.append(tempdistance)
                tempdistance= []
                
            ##permutation function
            for t in range(0,num2):
                    vals.append(t)
                    
            #bruteforce loop
            for p in range(0,int(perms(len(vals)-1))):                  
                tempperms = vals[:]
                tempperms+=[0]
                
                #finds the distance of the permutation with appending it to a list.
                for s in range(0,len(tempperms)-1):                    
                    p1 = int(tempperms[s])
                    p2 = int(tempperms[s+1])
                    tempdistance.append(distances[p1][p2])

                ## simple if staments to remember the worst and best distances/paths without list.   
                if sum(tempdistance)<b:
                        b=sum(tempdistance)
                        print("current distance",b)
                        bestpath = tempperms
                        self.myCanvas.delete("all")
                        for z in range(0, num2):
                            d1 = int(bestpath[z])
                            d2 = int(bestpath[z+1])                            
                            self.myCanvas.create_line(points[d1][0],points[d1][1],points[d2][0],points[d2][1],fill="green")
                            self.myCanvas.update()                    
                        time.sleep(.2)
                        
                if sum(tempdistance)>c:
                        c=sum(tempdistance)
                        worstpath = tempperms
                        
                tempdistance = []
                ##step 1
                largestI= -1
                for i in range(0,len(vals)-1):
                    if vals[i]<vals[i+1]:
                        largestI = i

                if largestI == -1:
                    print("finished")
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
            if showworstpath:
                for h in range(0,num2):
                            d1 = int(worstpath[h])
                            d2 = int(worstpath[h+1])                
                            self.myCanvas.create_line(points[d1][0],points[d1][1],points[d2][0],points[d2][1],fill="red")
                            self.myCanvas.update()
                        
            print("Most Efficient Route",b,bestpath)
            print("Most Inefficient Route",c,worstpath)               
                       
frame02=MyFrame()
frame02.mainloop()

##notable points
##[(304, 288), (265, 742), (346, 29), (473, 290), (171, 266), (306, 21), (642, 250), (127, 533), (174, 366), (392, 268)]

