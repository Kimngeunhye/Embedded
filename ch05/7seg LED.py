import RPi.GPIO as gpio
import time 

class Segment():

    def __init__(self):

        gpio.setmode(gpio.BCM)
        # 핀 번호 설정
        self.a = 9
        self.b = 4
        self.c = 23
        self.d = 8
        self.e = 7
        self.f = 10
        self.g = 25
        self.h = 18
        # 모든 핀을 출력으로 설정
        gpio.setup(self.a, gpio.OUT) 
        gpio.setup(self.b, gpio.OUT) 
        gpio.setup(self.c, gpio.OUT) 
        gpio.setup(self.d, gpio.OUT) 
        gpio.setup(self.e, gpio.OUT) 
        gpio.setup(self.f, gpio.OUT) 
        gpio.setup(self.g, gpio.OUT) 
        gpio.setup(self.h, gpio.OUT)

    def hide_number(self):
        # 모든 digit을 off
        gpio.output(self.a,gpio.LOW)
        gpio.output(self.b,gpio.LOW)
        gpio.output(self.c,gpio.LOW)
        gpio.output(self.d,gpio.LOW)
        gpio.output(self.e,gpio.LOW)
        gpio.output(self.f,gpio.LOW)
        gpio.output(self.g,gpio.LOW)
        gpio.output(self.h,gpio.LOW)
        
    def show_number(self,number):
        # 다음 숫자를 출력하기 전에 초기화
        self.hide_number()
        
        # 각 숫자에 대응하는 LED를 ON
        if(number == 0):            
            gpio.output(self.a,gpio.HIGH)
            gpio.output(self.b,gpio.HIGH)
            gpio.output(self.c,gpio.HIGH)
            gpio.output(self.e,gpio.HIGH)
            gpio.output(self.f,gpio.HIGH)
            gpio.output(self.g,gpio.HIGH)
            
        elif(number == 1):
            gpio.output(self.c,gpio.HIGH)
            gpio.output(self.f,gpio.HIGH)
            
        elif(number == 2):
            gpio.output(self.a,gpio.HIGH)
            gpio.output(self.c,gpio.HIGH)
            gpio.output(self.d,gpio.HIGH)
            gpio.output(self.e,gpio.HIGH)
            gpio.output(self.g,gpio.HIGH)
            
        elif(number == 3):
            gpio.output(self.a,gpio.HIGH)
            gpio.output(self.c,gpio.HIGH)
            gpio.output(self.d,gpio.HIGH)
            gpio.output(self.f,gpio.HIGH)
            gpio.output(self.g,gpio.HIGH)
            
        elif(number == 4):
            gpio.output(self.b,gpio.HIGH)
            gpio.output(self.c,gpio.HIGH)
            gpio.output(self.d,gpio.HIGH)
            gpio.output(self.f,gpio.HIGH)
            
        elif(number == 5):            
            gpio.output(self.a,gpio.HIGH)
            gpio.output(self.b,gpio.HIGH)
            gpio.output(self.d,gpio.HIGH)
            gpio.output(self.f,gpio.HIGH)
            gpio.output(self.g,gpio.HIGH)
            
        elif(number == 6):
            gpio.output(self.a,gpio.HIGH)
            gpio.output(self.b,gpio.HIGH)
            gpio.output(self.d,gpio.HIGH)
            gpio.output(self.e,gpio.HIGH)
            gpio.output(self.f,gpio.HIGH)
            gpio.output(self.g,gpio.HIGH)
            
        elif(number == 7):
            gpio.output(self.a,gpio.HIGH)
            gpio.output(self.c,gpio.HIGH)
            gpio.output(self.f,gpio.HIGH)
            
        elif(number == 8):
            gpio.output(self.a,gpio.HIGH)
            gpio.output(self.b,gpio.HIGH)
            gpio.output(self.c,gpio.HIGH)
            gpio.output(self.d,gpio.HIGH)
            gpio.output(self.e,gpio.HIGH)
            gpio.output(self.g,gpio.HIGH)
            gpio.output(self.f,gpio.HIGH)
            
        elif(number == 9):
            gpio.output(self.a,gpio.HIGH)
            gpio.output(self.b,gpio.HIGH)
            gpio.output(self.c,gpio.HIGH)
            gpio.output(self.d,gpio.HIGH)
            gpio.output(self.f,gpio.HIGH)
        else:
            # 0 ~ 9의 숫자가 아닐 경우에는 digit point만 on
            gpio.output(self.h,gpio.HIGH)

# Segment 클래스를 initialize
segment = Segment()

# 1초 간격으로 각 숫자를 디스플레이
for i in range(0,10):
    segment.show_number(i)
    time.sleep(1)
    
gpio.cleanup()
