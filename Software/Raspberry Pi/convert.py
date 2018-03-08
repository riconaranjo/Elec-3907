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
  
  print("Solution")
  print("(X,Y) = (",Objx2,",",Objy2,")\n\n")
  
  return Objx2, Objy2
  
def column(matrix, i):
  return [row[i] for row in matrix]

def percent_dif(x,y):
  return (abs(x-y)/((x+y)/2))*100
  
def avg(x1, y1, x2, y2):
  avgX = (x1+x2)/2
  avgY = (y1+y2)/2
  return avgX, avgY

def complete_tri(r1, r2, r3, S1x, S1y, S2x, S2y, S3x, S3y):
  #if all distances are greater than distance threshold -- all invalid
  if ((r1 > diameter) and (r2 > diameter) and (r3 > diameter)):
    print("Sensor distances are greater than threshold.")
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    return avg(x1, y1, x2, y2)

  #if all distances are less than distance threshold -- valid
  if ((r1 < diameter) and (r2 < diameter) and (r3 < diameter)):
    
    #exclude r1, keep r2 and r3
    if ((r1 > r2*factor) and (r1 > r3*factor)):
      x1, y1 = triangulate(S2x, S2y, S3x, S3y, r2, r3)
      x2 = x1
      y2 = y1
      return avg(x1, y1, x2, y2)
    #exclude r2, keep r1 and r3
    elif ((r2 > r1*factor) and (r2 > r3*factor)):
      x1, y1 = triangulate(S1x, S1y, S3x, S3y, r1, r3)
      x2 = x1
      y2 = y1
      return avg(x1, y1, x2, y2)
    #exclude r3, keep r1 and r2
    elif ((r3 > r1*factor) and (r3 > r2*factor)):
      x1, y1 = triangulate(S1x, S1y, S2x, S2y, r1, r2)
      x2 = x1
      y2 = y1
      return avg(x1, y1, x2, y2)
    #keep r1, exclude r2 and r3
    elif (r2 > r1*factor and r3 > r1*factor):
      x1 = S1x
      y1 = r1
      x2 = x1
      y2 = y1
      return avg(x1, y1, x2, y2)
    #keep r2, exclude r1 and r3
    elif (r1 > r2*factor and r3 > r2*factor):
      x1 = S2x
      y1 = r2
      x2 = x1
      y2 = y1
      return avg(x1, y1, x2, y2)
    #keep r3, exclude r1 and r2
    elif (r1 > r3*factor and r2 > r3*factor):
      x1 = S3x
      y1 = r3
      x2 = x1
      y2 = y1
      return avg(x1, y1, x2, y2)
    #use all distances
    else:
      x1, y1 = triangulate(S1x, S1y, S2x, S2y, r1, r2)
      x2, y2 = triangulate(S2x, S2y, S3x, S3y, r2, r3)
      return avg(x1, y1, x2, y2)
  #if any distances are greater than distance threshold
  else:
    #only r1 > distance
    if (r1 > diameter and (r2 < diameter and r3 < diameter)):
      #keep r3
      if (r2 > r3*factor):
        x1 = S3x
        y1 = r3
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
      #keep r2  
      elif (r3 > r2*factor):
        x1 = S2x
        y1 = r2
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
      #keep r2 and r3
      else:
        x1, y1 = triangulate(S2x, S2y, S3x, S3y, r2, r3)
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
    #only r2 > distance
    elif (r2 > diameter and (r1 < diameter and r3 < diameter)):
      #keep r3
      if (r1 > r3*factor):
        x1 = S3x
        y1 = r3
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
      #keep r1
      elif (r3 > r1*factor):
        x1 = S1x
        y1 = r1
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
      #keep r1 and r3
      else:
        x1, y1 = triangulate(S1x, S1y, S3x, S3y, r1, r3)
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
    #only r3 > distance
    elif (r3 > diameter and (r1 < diameter and r2 < diameter)):
      #keep r1
      if (r2 > r1*factor):
        x1 = S1x
        y1 = r1
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
      #keep r2
      elif (r1 > r2*factor):
        x1 = S2x
        y1 = r2
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
      #keep r1 and r1
      else:
        x1, y1 = triangulate(S1x, S1y, S2x, S2y, r1, r2)
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
        
    #more than one r is greater than diameter
    else:
      #only r1 is valid
      if (r1 < diameter):
        x1 = S1x
        y1 = r1
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
      #only r2 is valid
      elif (r2 < diameter):
        x1 = S2x
        y1 = r2
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
      #only r3 is valid
      else:
        x1 = S3x
        y1 = r3
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
        
def convert(r1, r2, r3, r4, r5, r6):
  avgX1, avgY1 = complete_tri(r1, r2, r3, S1x, S1y, S2x, S2y, S3x, S3y)
  #inverse x and y so that coordinates are relative to Sensor Bank 1
  avgY2, avgX2 = complete_tri(r4, r5, r6, S4x, S4y, S5x, S5y, S6x, S6y)
  
  avgX2 = abs(avgX2 - diameter)
  
  return avgX1, avgY1, avgX2, avgY2

# -----------------------
# ---- Sensor Bank 1 ----
# -----------------------

print("Sensor Bank 1")
  
S1x = 5
S1y = 0
print("Sensor1: ", S1x, ",", S1y)
  
S2x = 10
S2y = 0
print("Sensor2: ",S2x, ",", S2y)

S3x = 15
S3y = 0
print("Sensor3: ",S3x, ",", S3y,"\n")

# -----------------------
# ---- Sensor Bank 2 ----
# -----------------------

print("Sensor Bank 2")

S4x = 5 #0
S4y = 0 #5
print("Sensor4: ", S4x, ",", S4y)

S5x = 10 #0
S5y = 0 #10
print("Sensor5: ",S5x, ",", S5y)

S6x = 15 #0
S6y = 0 #15
print("Sensor6: ",S6x, ",", S6y,"\n")


# -------------------------
# ---- Other Variables ----
# -------------------------

diameter = 30
factor = 1.5