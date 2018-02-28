# Raspberry Pi triangulation module v1.0


# triangulation system of equations
# (Objx - S1x)^2 + (Objy - S1y)^2 = r1^2
# (Objx - S2x)^2 + (Objy - S2y)^2 = r2^2
# (Objx, Objy) element of beam 1, 2
#
# WolframAlpha
# {(x - q)^2 + (y- w)^2 = a^2, (x- e)^2 + (y- r)^2 = s^2, (x- t)^2 + (y- u)^2 = d^2}
# q = S1x, w = S1y, a = r1
# e = S2x, r = S2y , s = r2
# t = S3x, u = S3y, d = r3

# Sensor 1 = A
# Sensor 2 = B
# Sensor 3 = C
# Object = D

#Sensor1:  0 , 0
#Sensor2:  8 , 0
#r1: 3 ... r2: 5
#Solution1

#(X,Y) = ( 8.0 , 0.0 )


#Solution2

#(X,Y) = ( 8.0 , 0.0 )


import math
import random

def dist(a1, a2):
  return a1 - a2
  
#dist2D -- get distance between two points
def dist2D(x1, y1, x2, y2): 
  return math.sqrt((dist(x2,x1)**2) + (dist(y2,y1)**2))
  
def printXY(x, y):
  print("(", x, ",", y, ")")

def triangulate(S1x, S1y, S2x, S2y, r1, r2):
  S2S1x = dist(S2x,S1x) #S2x relative to S1x
  S2S1y = dist(S2y,S1y) #S2y relative to S1y
  
  cos1 = ((r1**2)-(S2S1x**2)+(r2**2))/(2*r1*r2)
  print("cos1: ", cos1)
  
  if abs(cos1) > 1:
    print("y-segment in complex domain")
    return 0, 0
  
  sin1 = math.sqrt(1-(cos1)**2)
  
  Objx1 = S2S1x*cos1 + S2S1y*sin1 + S1x
  Objy1 = S2S1y*cos1 - S2S1x*sin1 + S1y
  
  Objx2 = S2S1x*cos1 - S2S1y*sin1 + S1x
  Objy2 = S2S1y*cos1 + S2S1x*sin1 + S1y
  
  print("Solution1")
  print("(X,Y) = (",Objx1,",",Objy1,")\n\n")
  
  print("Solution2")
  print("(X,Y) = (",Objx2,",",Objy2,")\n\n")
  
  return Objx2, Objy2
  
def column(matrix, i):
  return [row[i] for row in matrix]

def percent_dif(x,y):
  return (abs(x-y)/((x+y)/2))*100

# get distances from sensors, store in variables
# filter outliers
# filter error cases

r =  [[14, 14, 14], [17, 17, 18], [32, 31, 28], [95, 42, 33], [48, 41, 40], [48, 42, 41], [40, 31, 40], [29, 20, 27], [35, 22, 31], [44, 31, 41], [116, 54, 20], [73, 48, 30], [78, 29, 51], [57, 43, 4], [5, 6, 4]]
  
r1 = column(r,0)
r2 = column(r,1)
r3 = column(r,2)
  
S1x = 0
S1y = 0
print("Sensor1: ", S1x, ",", S1y)
  
S2x = 5
S2y = 0
print("Sensor2: ",S2x, ",", S2y)

S3x = 10
S3y = 0
print("Sensor3: ",S3x, ",", S3y,"\n")

for i in range(0,15):
  
  print("\n")
  print("-----------------------------------------")
  print("Iteration #: ", i+1)
  print("-----------------------------------------")
  
  x1, y1 = triangulate(S1x, S1y, S2x, S2y, r1[i], r2[i])
  print("r1: ", r1[i], "r2: ", r2[i])
  print("Percent Difference: ", percent_dif(r1[i],r2[i]), "\n")
  
  x2, y2 = triangulate(S2x, S2y, S3x, S3y, r2[i], r3[i])
  print("r1: ", r2[i], "r2: ", r3[i])
  print("Percent Difference: ", percent_dif(r2[i],r3[i]), "\n")
  
  print("------------------------------------------")
  print("-      Average between solutions:        -")

  avgX = (x1+x2)/2
  avgY = (y1+y2)/2

  print("(X,Y) = (",avgX,",",avgY,")")
  print("------------------------------------------\n\n\n")
  
  