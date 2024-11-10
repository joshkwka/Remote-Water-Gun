# Remote Water Gun

For this project, I designed and modelled a mount for a spray bottle which allows motors to control the pitch and yaw movement of the nozzle. 
A motor also controls the trigger so that the "water gun" can be shot remotely. 


![alt text](https://github.com/joshkwka/Remote-Water-Gun/blob/main/watergun1.JPG)


### Mechanisms:

#### Trigger:
The Trigger is controlled by attaching the motor and trigger of the spray bottle with a pin, creating a slider crank. The slider crank converts the rotational force given by the motor into linear movement which pulls the trigger.

#### Pitch:
The water gun turns on its pitch axis by directly mounting a motor to the mount made for the trigger mechanism.

#### Yaw:
The water gun turns on its yaw axis by two gears. A motor sits behind the water gun assembly facing downwards with a 35mm gear attached to it. A 40mm gear is attached to the bottom of the pitch turning assembly, and when the gears mesh the motor's rotational energy is transmitted inversely to the water gun assembly.


#### Necessary Equipment:
* Raspberry Pi
* Pi Camera
* 3 Servo Motors
* Spray bottle top
* A 3D Printer


#### Controls:

The code in this repository allows you to see what the water gun is pointing at via Pi Camera, and to use keyboard controls to move the water gun and fire.

* Z or R must first be pressed to set the positions of the motors. <br/>
* W A S D or the arrow keys can be used to adjust pitch and yaw. <br/>
* Space Bar is used to fire. <br/> 
* Q is used to quit the program.
