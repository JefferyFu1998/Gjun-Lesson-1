from gpiozero import RGBLED
from time import sleep
print(__name__);
colors= [(1,0,0),(1,1,0),(1,0,1),(0,1,0),(0,1,1),(0,0,1),(1,1,1)];

if __name__ == '__main__':

   print('run'); #it is within the if tap, need to block behind the "if" command
   
   rgbled= RGBLED(17,27,22); #this is a tuple
   while True:  #while True command creates a loop
       #print('run');
       #rgbled.color=(1,0,0);
       #sleep(1);
       #rgbled.color=(0,1,0);
       #sleep(1);
       #rgbled.color=(0,0,1);
       #sleep(1);
       for color in colors:
           rgbled.color=color;
           sleep(1);
       
                
