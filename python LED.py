from gpiozero import LED
from time import sleep


green= LED(17)
green1= LED(23)

while True:
green.on()
green1.off()
sleep(1);
green.off()
green1.on()
sleep(1);