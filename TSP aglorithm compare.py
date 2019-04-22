#Mazeayr Moeini mf04026, Fatima Moin fm03771, Shehryar Mughal sm04210

import tkinter
from tkinter import *
import time
import random
import math as m

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.patches as mpatches


f = Figure(figsize=(12,4), dpi=100)
graph = f.add_subplot(111)


global stop1
stop1 = False

def returnGreedy(points,num5,num2):



    distances = []
    tempdistance = []
    bestpath = [0, ]
    
    longest = num5 * m.sqrt(2) + 1

    for w in range(0, num2):
        for p in range(0, num2):
            if m.sqrt((points[p][0] - points[w][0]) ** 2 + (points[p][1] - points[w][1]) ** 2) == 0:
                tempdistance.append(longest)
            else:
                tempdistance.append(m.sqrt((points[p][0] - points[w][0]) ** 2 + (points[p][1] - points[w][1]) ** 2))

        distances.append(tempdistance)
        tempdistance = []

    for k in range(num2):
        distances[k][0] = longest

    nextpoint = 0
    for x in range(0, num2):
        nextpoint = distances[nextpoint].index(sorted(distances[nextpoint])[0])
        bestpath.append(nextpoint)
        for y in range(0, num2):
            distances[y][nextpoint] = longest

    return (bestpath)




def run(self,canvas,r2,r3,num5):
    graph.clear()
    canvas.draw()

    global stop1
    stop1 = False
    self.myCanvas.delete("all")
    num2 = r3.get()


    algorithmRecord = [[],[],[]]

    vals = []
    num7 = 1000
    points = []
    tempdistance = []
    distances = []
    nextpoint = 0
    tempdistance = []
    d1 = 0
    d2 = 0
    bestpath = [0 for i in range(num2 + 1)]
    worstpath = [0 for i in range(num2 + 1)]
    randompath = [i for i in range(1, num2)]
    randombest = []
    bestgreedy = []
    distgreedy = []
    a = 0
    b = b1 = 10 ** 12

    c = 0

    def swap(a, i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    def perms(n):
        if n == 1:
            return 1
        else:
            return n * perms(n - 1)


    for z in range(0, num2):
        x = random.randint(5, num5 - 5)
        y = random.randint(5, num5 - 5)
        points.append((x, y))
    print(points)


    for w in range(0, num2):
        for p in range(0, num2):
            tempdistance.append(m.sqrt((points[p][0] - points[w][0]) ** 2 + (points[p][1] - points[w][1]) ** 2))
        distances.append(tempdistance)
        tempdistance = []


    vals = list(range(num2))
    print(vals)

    bestgreedy = returnGreedy(points, num5, num2)

    for s in range(0, len(bestgreedy) - 1):
            p1 = int(bestgreedy[s])
            p2 = int(bestgreedy[s + 1])
            distgreedy.append(distances[p1][p2])



    for p in range(0, int(perms(len(vals) - 1))):

        random.shuffle(randompath)
        randomaf = [0] + randompath[:] + [0]
        randomtemp = []

        tempperms = vals[:]
        tempperms += [0]


        for s in range(0, len(tempperms) - 1):
            p1 = int(tempperms[s])
            p2 = int(tempperms[s + 1])
            tempdistance.append(distances[p1][p2])

        for s in range(0, len(randomaf) - 1):
            p1 = int(randomaf[s])
            p2 = int(randomaf[s + 1])
            randomtemp.append(distances[p1][p2])


        bestest = False
        
        if sum(randomtemp) < b1:
            b1 = sum(randomtemp)
            randombest = randomaf
            bestest = True

        bestest1 = False
        if sum(tempdistance) < b:
            b = sum(tempdistance)
            bestpath = tempperms
            bestest1 = True

        if  bestest1 or bestest:
            bestest = False
            bestest1 = False
            print("current distance brute:", round(b, 3), "random:", round(b1, 3), "greedy:", round(sum(distgreedy), 3))
            
            algorithmRecord[0].append(round(b, 3))
            algorithmRecord[1].append(round(b1, 3))
            algorithmRecord[2].append(round(sum(distgreedy), 3))
            
            self.myCanvas.delete("all")

            for point in points:
                self.myCanvas.create_oval(point[0], point[1], point[0] + 5, point[1] + 5, outline="gray", fill="blue",
                                          width=2)
                self.myCanvas.create_oval(point[0] + num5, point[1], point[0] + 5 + num5, point[1] + 5, outline="gray", fill="blue", width=2)

                self.myCanvas.create_oval(point[0] + 2*num5, point[1], point[0] + 5 + 2*num5, point[1] + 5, outline="gray",
                                          fill="blue", width=2)

            for z in range(0, num2):
                d1 = int(bestpath[z])
                d2 = int(bestpath[z + 1])
                self.myCanvas.create_line(points[d1][0], points[d1][1], points[d2][0], points[d2][1], fill="green")

                f1 = int(randombest[z])
                f2 = int(randombest[z + 1])
                self.myCanvas.create_line(points[f1][0] + num5, points[f1][1], points[f2][0] + num5, points[f2][1], fill="green")

                f1 = int(bestgreedy[z])
                f2 = int(bestgreedy[z + 1])
                self.myCanvas.create_line(points[f1][0] + 2*num5, points[f1][1], points[f2][0] + 2*num5, points[f2][1], fill="green")




                self.myCanvas.update()
                time.sleep(r2.get())
                
            graph.clear()
            red_patch = mpatches.Patch(color='red', label='Random '+str(round(b1, 3)))
            blue_patch = mpatches.Patch(color='blue', label='Brute Force '+str(round(b, 3)))
            black_patch = mpatches.Patch(color='Black', label='Greedy Benchmark '+str(round(sum(distgreedy), 3)))
            graph.legend(handles=[red_patch,blue_patch,black_patch])
            graph.plot(algorithmRecord[0],"blue")
            graph.plot(algorithmRecord[1],"red")
            graph.plot(algorithmRecord[2],"black")
            graph.set_title("TSP Distance Comparison")
            graph.set_ylabel('Distance')
            graph.set_xlabel("Iteration")
            
            canvas.draw()

        if sum(tempdistance) > c:
            c = sum(tempdistance)
            worstpath = tempperms

        tempdistance = []

        largestI = -1
        for i in range(0, len(vals) - 1):
            if vals[i] < vals[i + 1]:
                largestI = i

        if largestI == -1:
            print("finished")
            break

        largestJ = -1
        for j in range(0, len(vals)):
            if vals[largestI] < vals[j]:
                largestJ = j

        swap(vals, largestI, largestJ)

        endArray = vals[largestI + 1:len(vals)]
        endArray.reverse()
        vals = vals[0:largestI + 1] + endArray

        if stop1:
            print("Cleared")
            graph.clear()
            canvas.draw()
            self.myCanvas.delete("all")
            stop1 = False
            break

    showworstpath = False
    

    graph.set_title("TSP Distance Comparison DONE")
 
    canvas.draw()

    if showworstpath:
        for h in range(0, num2):
            d1 = int(worstpath[h])
            d2 = int(worstpath[h + 1])
            self.myCanvas.create_line(points[d1][0], points[d1][1], points[d2][0], points[d2][1], fill="red")
        self.myCanvas.update()

    print("Most Efficient Route", round(b, 3), bestpath, "Random:", randombest, round(b1, 3), "Greedy", bestgreedy, round(sum(distgreedy),3))



def stop(yes):
    global stop1

    stop1  = yes

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        num5 = 350
        
        
        
        Buttons = Frame()
        
        self.myCanvas = Canvas(Buttons, width= 3 * num5, height=num5, bg="black")
        
        
        self.myCanvas.grid(row=0,column=1)
        
        can = Frame()
        
        canvas = FigureCanvasTkAgg(f,can)
        canvas.get_tk_widget().grid(row=0, column=0)
        canvas.draw()
        
        tool = Frame()
        
        canvas._tkcanvas.grid(row=0, column=0)
        can.grid(row = 1, column =0, stick = "NW")
        
        toolbar = NavigationToolbar2Tk(canvas, tool)  
        toolbar.update()

        scalevar = tkinter.IntVar()
        scalevar.set(.1)

        scalevar1 = tkinter.IntVar()
        scalevar1.set(10)

        r2 = Scale(Buttons,from_=0, to=1,resolution=0.1,  length=200, orient=HORIZONTAL, label = "Seconds", variable=scalevar   )
        r2.grid(row=0, column=0)

        r3 = Scale(Buttons,from_=4, to=30, length=200, orient=HORIZONTAL, label = "Cities", variable = scalevar1 )
        r3.grid(row=0, column=0, stick="N")


        button3 = Button(Buttons,text="Run Simulation",command=lambda: run(self,canvas,r2,r3,num5))
        button3.grid(row=0, column=0, stick="WS" )

        global stop1
        stop1 = False

        button4 = Button(Buttons,text="Clear", command = lambda: stop(True))
        button4.grid(row=0, column=0, stick="ES")

        Buttons.grid(row = 0 , column =0)


frame02 = MyFrame()
frame02.mainloop()


