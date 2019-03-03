

import numpy as np
import cv2
import math
import random
import copy

class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.parent=None

class RRT():
    def __init__(self):
         self.start=Point(529,964)            
         self.radius=6
         self.path=[self.start]
         self.img=np.zeros((1500,1500,1),np.uint8) 
        
    def RandomPointGenerator(self):
         self.random_point=Point(random.randrange(463,1457),random.randrange(49, 1027))
        
    def DrawLine(self,frame):
        self.frame=frame
        if self.frame == None:
          self.videoCall()
        x_increment=0
        y_increment=0
        min_distance=90000000000000
        for element in self.path:
          if min_distance>math.sqrt((self.random_point.y-element.y)**2+(self.random_point.x-element.x)**2):
            min_distance=math.sqrt((self.random_point.y-element.y)**2+(self.random_point.x-element.x)**2)
            self.j=self.path.index(element)                    #j is the index of element with smallest distance
        if self.random_point.x==self.path[self.j].x :
          theta=1.57
        else:
          theta=-(math.atan((self.random_point.y-self.path[self.j].y)/(self.random_point.x-self.path[self.j].x))+math.pi)
        check=1
        for h in np.arange(0,50,1): 
            x_increment=h*math.cos(theta)
            y_increment=h*math.cos(theta)
            if x_increment+self.random_point.x<1080 and y_increment+self.random_point.y<1400:
             if (self.frame[int(x_increment+self.path[self.j].x),int(y_increment+self.path[self.j].y)][0]>=30 or self.frame[int(x_increment+self.path[self.j].x),int(y_increment+self.path[self.j].y)][1]>=30 or self.frame[int(x_increment+self.path[self.j].x),int(y_increment+self.path[self.j].y)][2]>=30) and (self.frame[int(x_increment+self.path[self.j].x),int(y_increment+self.path[self.j].y)][0]<=225 or self.frame[int(x_increment+self.path[self.j].x),int(y_increment+self.path[self.j].y)][1]>=30 or self.frame[int(x_increment+self.path[self.j].x),int(y_increment+self.path[self.j].y)][2]>=30) :
              continue
             else:
              check = 0
              break

        if check:
          pointAppend=Point(int(x_increment+self.path[self.j].x),int(y_increment+self.path[self.j].y))
          pointAppend.parent=self.j
          self.path.append(pointAppend)
          print (pointAppend.x,pointAppend.y)
          self.img[pointAppend.x,pointAppend.y]=255
          cv2.imshow('img',self.img)

          
          
          
    def Dest(self):
      if self.random_point.x<1080 and self.random_point.y<1400:
        if self.frame[self.path[self.j].x, self.path[self.j].y][0]<10 and self.frame[self.path[self.j].x, self.path[self.j].y][1]>249 and self.frame[self.path[self.j].x, self.path[self.j].y][2]<10 :
            return 1
        else :
            return 0


    def videoCall(self):
         cap = cv2.VideoCapture('path.mkv')

         while cap.isOpened():
            ret, frame = cap.read()
            self.RandomPointGenerator()
            self.DrawLine(frame)
            if self.Dest():
             print "destination has been reached"
            if ret==True:
                  print "show"
                  cv2.imshow('frame',frame)
         
                  if cv2.waitKey(1) & 0xFF == ord('q'):  #press q to exit
                    break
         cap.release()
 
        # Closes all the frames
         cv2.destroyAllWindows()
             

def main():
    cap = cv2.VideoCapture('path.mkv')

    while cap.isOpened():
        ret, frame = cap.read()
        rrt=RRT()
        rrt.RandomPointGenerator()
        rrt.DrawLine(frame)
        if rrt.Dest():
            print "destination has been reached"    
        if ret==True:
    
            cv2.imshow('frame',frame)
    
            if cv2.waitKey(1) & 0xFF == ord('q'):  #press q to exit
             break
    cap.release()
 
       # Closes all the frames
    cv2.destroyAllWindows()

       
if __name__ == '__main__':
    main()





