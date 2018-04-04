import math

def dist(a1, a2):
  return a1 - a2
  
#dist2D -- get distance between two points
def dist2D(x1, y1, x2, y2): 
  return math.sqrt((dist(x2,x1)**2) + (dist(y2,y1)**2))

def triangulate(S1x, S1y, S2x, S2y, r1, r2):
  
  S2S1x = dist(S2x,S1x) #S2x relative to S1x
  S2S1y = dist(S2y,S1y) #S2y relative to S1y
  
  cos1 = float(((r1**2)+(S2S1x**2)-(r2**2))) / float((2*r1*S2S1x))

  if abs(cos1) > 1:
    print("y-segment in complex domain")
    return -1, -1
  
  sin1 = math.sqrt(1-(cos1**2))
  
  # A = S1, B = S2

  # get location of B relative to A
  
  Bx = S2x - S1x
  By = S2y - S1y

  # Scale by r1/S2S1x

  Bx = Bx*(r1/S2S1x)
  By = By*(r1/S2S1x)
  
  x = Bx*cos1 - By*sin1 + S1x
  y = By*cos1 + Bx*sin1 + S1y

  return x, y
  
def avg(x1, y1, x2, y2):
  avgX = (x1+x2)/2
  avgY = (y1+y2)/2
  return avgX, avgY
  
def complete_tri(r1, r2, r3, S1x, S1y, S2x, S2y, S3x, S3y):
  #if all distances are greater than distance threshold -- all invalid
##  print("start tri")
  #print(r1, r2, r3)
  
  if (abs(r1-r2) == abs(S1x-S2x)):
    return -1, -1
  elif (abs(r2-r3) == abs(S1x-S2x)):
    return -1, -1
  
  
  if ((r1 >= diameter) and (r2 >= diameter) and (r3 >= diameter)):
    print("Sensor distances are greater than threshold.")
    return -1, -1

  #if all distances are less than distance threshold -- valid
  if ((r1 < diameter) and (r2 < diameter) and (r3 < diameter)):
    #print("here")
    #exclude r1, keep r2 and r3
    if ((r1 > r2*factor) and (r1 > r3*factor)):
      #print("fwef1")
      x1, y1 = triangulate(S2x, S2y, S3x, S3y, r2, r3)
      x2 = x1
      y2 = y1
      return avg(x1, y1, x2, y2)
    #exclude r2, keep r1 and r3
    elif ((r2 > r1*factor) and (r2 > r3*factor)):
      #print("2")
      x1, y1 = triangulate(S1x, S1y, S3x, S3y, r1, r3)
      x2 = x1
      y2 = y1
      return avg(x1, y1, x2, y2)
    #exclude r3, keep r1 and r2
    elif ((r3 > r1*factor) and (r3 > r2*factor)):
      #print("3")
      x1, y1 = triangulate(S1x, S1y, S2x, S2y, r1, r2)
      x2 = x1
      y2 = y1
      return avg(x1, y1, x2, y2)
    #keep r1, exclude r2 and r3
    elif (r2 > r1*factor and r3 > r1*factor):
      #print("4")
      x1 = S1x
      y1 = r1
      x2 = x1
      y2 = y1
      return avg(x1, y1, x2, y2)
    #keep r2, exclude r1 and r3
    elif (r1 > r2*factor and r3 > r2*factor):
      #print("5")
      x1 = S2x
      y1 = r2
      x2 = x1
      y2 = y1
      return avg(x1, y1, x2, y2)
    #keep r3, exclude r1 and r2
    elif (r1 > r3*factor and r2 > r3*factor):
      #print("6")
      x1 = S3x
      y1 = r3
      x2 = x1
      y2 = y1
      return avg(x1, y1, x2, y2)
    #use all distances
    else:
      #print("7")
      x1, y1 = triangulate(S1x, S1y, S2x, S2y, r1, r2)
      x2, y2 = triangulate(S2x, S2y, S3x, S3y, r2, r3)
      if (x1 == -1 and y1 == -1):
        return x2, y2
      elif (x2 == -1 and y2 == -1):
        return x1, y1
      else:
        return avg(x1, y1, x2, y2)
  #if any distances are greater than distance threshold
  else:
    
    #only r1 > distance
    if (r1 > diameter and (r2 < diameter and r3 < diameter)):
      #keep r3
      
      if (r2 > r3*factor):
        #print("8")
        x1 = S3x
        y1 = r3
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
      #keep r2  
      elif (r3 > r2*factor):
        #print("9")
        x1 = S2x
        y1 = r2
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
      #keep r2 and r3
      else:
##        print("10")
        #print("tri")
        x1, y1 = triangulate(S2x, S2y, S3x, S3y, r2, r3)
        x2 = x1
        y2 = y1
        #print(x1,y1)
        return avg(x1, y1, x2, y2)
    #only r2 > distance
    elif (r2 > diameter and (r1 < diameter and r3 < diameter)):
      #keep r3
      if (r1 > r3*factor):
        #print("11")
        x1 = S3x
        y1 = r3
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
      #keep r1
      elif (r3 > r1*factor):
        #print("12")
        x1 = S1x
        y1 = r1
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
      #keep r1 and r3
      else:
        #print("13")
        x1, y1 = triangulate(S1x, S1y, S3x, S3y, r1, r3)
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
    #only r3 > distance
    elif (r3 > diameter and (r1 < diameter and r2 < diameter)):
      #keep r1
      if (r2 > r1*factor):
        #print("14")
        x1 = S1x
        y1 = r1
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
      #keep r2
      elif (r1 > r2*factor):
        #print("15")
        x1 = S2x
        y1 = r2
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
      #keep r1 and r1
      else:
        #print("16")
        x1, y1 = triangulate(S1x, S1y, S2x, S2y, r1, r2)
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
        
    #more than one r is greater than diameter
    else:
      #only r1 is valid
      if (r1 < diameter):
        #print("17")
        x1 = S1x
        y1 = r1
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
      #only r2 is valid
      elif (r2 < diameter):
        #print("18")
        x1 = S2x
        y1 = r2
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
      #only r3 is valid
      else:
        #print("19")
        x1 = S3x
        y1 = r3
        x2 = x1
        y2 = y1
        return avg(x1, y1, x2, y2)
        
def convert(r1, r2, r3, r4, r5, r6):
##  print("start convert")
  #print(r1, r2, r3)
  avgX1, avgY1 = complete_tri(r1, r2, r3, S1x, S1y, S2x, S2y, S3x, S3y)
##  print(avgX1, avgY1)
  # check if within 15 deg
  
  # check if too far left
  #tan theta = y / x
  if(S1x > avgX1) :
      angle = math.atan(avgY1-S1y, S1x-avgX1)
      if(angle*180/math.pi > 15) :
          r = min(r1,r2,r3)
          avgX1, avgY1 = complete_tri(r, diameter+1, diameter+1, S1x, S1y, S2x, S2y, S3x, S3y)

  # check if too far right
  elif (S3x < avgX1) :
      angle = math.atan2(avgY1-S3y, avgX1-S3x)
      if(angle*180/math.pi > 15) :
          r = min(r1,r2,r3)
          avgX1, avgY1 = complete_tri(r, diameter+1, diameter+1, S1x, S1y, S2x, S2y, S3x, S3y)

##  print("finished first")
  # inverse x and y so that coordinates are relative to Sensor Bank 1
  avgY2, avgX2 = complete_tri(r4, r5, r6, S4x, S4y, S5x, S5y, S6x, S6y)
##  print("finished second")
  
  # check if too far left
  #tan theta = y / x
  if(S4x > avgX2) :
      angle = math.atan2(avgY2-S4y, S4x-avgX2)
      print(angle)
      if(angle*180/math.pi > 15) :
          r = min(r4,r5,r6)
          avgX2, avgY2 = complete_tri(r, diameter+1, diameter+1, S4x, S4y, S5x, S5y, S6x, S6y)

  # check if too far right
  elif (S6x < avgX2) :
      angle = math.atan2(avgY2-S6y, S6x-avgX2)
      if(angle*180/math.pi > 15) :
          r = min(r4,r5,r6)
          avgX2, avgY2 = complete_tri(r, diameter+1, diameter+1, S4x, S4y, S5x, S5y, S6x, S6y)

  if (avgY2 != -1):
    avgX2 = abs(avgX2 - diameter)
  
  # careful when calling this function, the if statement returns two values, the else returns 4 values (workaround: the first 2 values will be non zero, the latter 2 values will be zero)
  
  # if points are close to the same point (i.e. if the points are within [factor_2] percent of each other), return one point
  # change factor_2 accordingly (default set to 10%)
  
  # another option is to just return the same 2 points
  
  #if (avgX1 < avgX2*factor_2 and avgY1 < avgY2*factor_2):
  #  return avg(avgX1, avgY1, avgX2, avgY2), 0, 0
  # else, return 2 distinct points
  #else:
  print(avgX1, avgY1, avgX2, avgY2)
  return avgX1, avgY1, avgX2, avgY2

# -----------------------
# ---- Sensor Bank 1 ----
# -----------------------

S1x = 18
S1y = -3
  
S2x = 23
S2y = -3

S3x = 28
S3y = -3

# -----------------------
# ---- Sensor Bank 2 ----
# -----------------------

S4x = 17.5 #0
S4y = -3 #5

S5x = 22.5 #0
S5y = -3 #10

S6x = 27.5 #0
S6y = -3 #15

diameter = 45
factor = 1.2