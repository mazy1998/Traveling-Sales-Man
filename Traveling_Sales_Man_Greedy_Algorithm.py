from tkinter import *
import time
import random
import math as m

num2 = cities =500
num5=800
vals = []            
num7= 1000
points= []
tempdistance= []
distances = []
tempperms= []
tempdistance = []
d1=0
d2=0
bestpath=[0,]

## max distance
longest = num5*m.sqrt(2)+1
a=0
b=10**12
c=0

##makes random points
for z in range(0,num2):    
    x =random.randint(5,num5-5)
    y= random.randint(5,num5-5)
    points.append((x,y))


##finds every distance
for w in range(0,num2):
    for p in range(0,num2):
        if m.sqrt((points[p][0]-points[w][0])**2+(points[p][1]-points[w][1])**2) == 0:
            tempdistance.append(longest)
        else:
            tempdistance.append(m.sqrt((points[p][0]-points[w][0])**2+(points[p][1]-points[w][1])**2))
    
    distances.append(tempdistance)
    tempdistance= []

for k in range(num2):
    distances[k][0]=longest
    

nextpoint = 0

##finds closest point in a list then repeats in that list
for x in range(0,num2):
    nextpoint = distances[nextpoint].index(sorted(distances[nextpoint])[0])
    bestpath.append(nextpoint)
    ## replaces that index with longest distance
    for y in range(0,num2):
        distances[y][nextpoint]=longest
print(bestpath)


class MyFrame(Frame):
    def __init__(self):
            Frame.__init__(self)
            self.myCanvas = Canvas(width=num5,height=num5,bg="black")
            self.myCanvas.grid()
            for z in range(0, num2-1):
                d1 = int(bestpath[z])
                d2 = int(bestpath[z+1]) 
                self.myCanvas.create_line(points[d1][0],points[d1][1],points[d2][0],points[d2][1],fill="green")
                time.sleep(.1)
            
frame02=MyFrame()
frame02.mainloop()


