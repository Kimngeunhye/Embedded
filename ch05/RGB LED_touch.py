import RPi.GPIO as gpio
import time
import random

class RGB():

  gpio.setmode(gpio.BCM)

  def __init__(self):
      self.red = 13
      self.green = 19
      self.blue = 26

      gpio.setup(self.red, gpio.OUT)
      gpio.setup(self.green, gpio.OUT)
      gpio.setup(self.blue, gpio.OUT)      
      
  def turn_on(self, color):
      if(color == "red"):
          gpio.output(self.red, gpio.HIGH)
      if(color == "blue"):
          gpio.output(self.blue, gpio.HIGH)
      if(color == "green"):
          gpio.output(self.green, gpio.HIGH)
      if(color == "yellow"):
          gpio.output(self.red, gpio.HIGH)
          gpio.output(self.green, gpio.HIGH)
      if(color == "cyan"):
          gpio.output(self.blue, gpio.HIGH)
          gpio.output(self.red, gpio.HIGH)
      if(color == "magneta"):
          gpio.output(self.red, gpio.HIGH)
          gpio.output(self.blue, gpio.HIGH)
      if(color == "white"):
          gpio.output(self.red, gpio.HIGH)
          gpio.output(self.greenb, gpio.HIGH)
          gpio.output(self.blue, gpio.HIGH)
          
  def turn_off(self, color):
      if(color == "red"):
          gpio.output(self.red, gpio.LOW)
      if(color == "blue"):
          gpio.output(self.blue, gpio.LOW)
      if(color == "green"):
          gpio.output(self.green, gpio.LOW)
      if(color == "yellow"):
          gpio.output(self.red, gpio.LOW)
          gpio.output(self.green, gpio.LOW)
      if(color == "cyan"):
          gpio.output(self.blue, gpio.LOW)
          gpio.output(self.red, gpio.LOW)
      if(color == "magneta"):
          gpio.output(self.red, gpio.LOW)
          gpio.output(self.blue, gpio.LOW)
      if(color == "white"):
          gpio.output(self.red, gpio.LOW)
          gpio.output(self.greenb, gpio.LOW)
          gpio.output(self.blue, gpio.LOW)

RGB_LED = RGB()
    
# 터치 센서 18번 핀에 연결
touch_pin = 18

# 센서이므로 INPUT으로 설정.
# pull_up_down 파라미터로 풀다운 저항 연결 설정->라즈베리 파이 내부의 저항 이용
gpio.setup(touch_pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    
colors = ["red","green","blue"]
    
try:    
                # colors 리스트 중 랜덤하게 선택
    random_color = random.choice(colors)
    while True:
                # 조건식의 == 1  생략. 터치 센서가 on되면
        if(gpio.input(touch_pin)):            
                # 랜덤하게 선택된 색상을 출력
            RGB_LED.turn_on(random_color)
        else:   # 터치 센서가 off되면 색상을 다시 랜덤하게 선택
            RGB_LED.turn_off(random_color)
            random_color = random.choice(colors)
        time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    
gpio.cleanup()
