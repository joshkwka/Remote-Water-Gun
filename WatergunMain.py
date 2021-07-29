from picamera import PiCamera
import MotorModule as motor
import KeyPressModule as kp
from time import sleep

########SETUP#########
motor1 = motor.Motor(11) #trigger
motor2 = motor.Motor(13) #vertical
motor3 = motor.Motor(15) #horizontal

kp.init()

######################

def main():
    if kp.getKey('a') or kp.getKey('LEFT'):
        old_pos = motor3.position
        new_pos = motor3.position + 10
        if 40 >= new_pos >= -40:
            sleep(0.2)
            motor3.goto(new_pos)
            print(f'left {old_pos} --> {motor3.position}')
            sleep(0.2)
        else:
            print(f'out of range: {motor3.position}')
    elif kp.getKey('d') or kp.getKey('RIGHT'):
        old_pos = motor3.position
        new_pos = motor3.position - 10
        if 40 >= new_pos >= -40:
            sleep(0.2)
            motor3.goto(new_pos)
            print(f'right {old_pos} --> {motor3.position}')
            sleep(0.2)
        else:
            print(f'out of range: {motor3.position}')
    elif kp.getKey('w') or kp.getKey('UP'):
        old_pos = motor2.position
        new_pos = motor2.position - 15
        if 75 >= new_pos >= 45:
            sleep(0.2)
            motor2.goto(new_pos)
            print(f'up {old_pos} --> {motor2.position}')
            sleep(0.2)
        else:
            print(f'out of range: {motor2.position}')
    elif kp.getKey('s') or kp.getKey('DOWN'):
        old_pos = motor2.position
        new_pos = motor2.position + 15
        if 75 >= new_pos >= 45:
            sleep(0.2)
            motor2.goto(new_pos)
            print(f'up {old_pos} --> {motor2.position}')
            sleep(0.2)
        else:
            print(f'out of range: {motor2.position}')
    elif kp.getKey('SPACE'):
        print('shoot')
        sleep(0.5)
        motor1.goto(25)
        sleep(0.2)
        motor1.goto(90)
        sleep(3)
    elif kp.getKey('r') or kp.getKey('z'):
        print('initializing up motors')
        motor1.goto(90)
        motor1.position = 90
        sleep(0.5)
        motor2.goto(75)
        motor2.position = 75
        sleep(0.5)
        motor3.goto(0)
        motor3.position = 0
        print('motor positions reset')
        

if __name__ == '__main__':
    camera = PiCamera()
    camera.start_preview(alpha=192)
    camera.rotation = 90
    
    kp.init()
    print('press z to initialize motor positions. arrows to aim and space to shoot')
    while True:
        sleep(0.1)
        main()
        if kp.getKey('q'):
            break
    camera.stop_preview()
