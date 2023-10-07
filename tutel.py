
from turtle import *
def f2():
     print('x y z w')
f2()
for x in range(2):
   for y in range(2):
      for z in range(2):
         for w in range(2):
            if (not(y<=x) or (z<=w) or not(z))==False:
               print(x, y, z, w)
def f5():
     for i in range(1,100):
         num=(bin(i)[2:])
         if num.count('1')%2==0:
             chislo='10'+num[2:]+'0'

         if num.count('1')%2!=0:
             chislo='11'+num[2:]+'1'
         if int(chislo,2)>40:
             print (i, int(chislo,2))
             break
f5()
def f6():

     left(90)
     for i in range(7):
         forward(300)
         right(120)
     pu()
     for x in range(1,9):
         for y in range(1,10):
             goto(x*30,y*30)
             dot(2)
     done()
f6()

def f12():
     for n in range( 108, 250, 9):
          s="5"*n
          while "555" in s or "11" in s or 2 in s:
               s= s.replace("555", "1", 1)
               s= s.replace("11", "25", 1)
               s= s.replace("2", "5", 1)
          print(n,s)
f12()
               












               
               



          

а
