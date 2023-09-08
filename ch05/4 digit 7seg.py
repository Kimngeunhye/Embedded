import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
 
# 7seg 핀 번호. a,b,c,d,e,f,g,h
segments = (9,4,23,8,7,10,18,25)
 
for segment in segments:
    gpio.setup(segment, gpio.OUT)
    gpio.output(segment, 0)
 
# 4개의 digit를 연결할 핀
digits = (22,27,17,24)

# output 값이 1이면 해당 핀의 digit, 0이면 on 
for digit in digits:
    gpio.setup(digit, gpio.OUT)
    gpio.output(digit, 1)
 
num = { ' ':(0,0,0,0,0,0,0),    # 딕셔너리 num에 off, 0~9를 튜플 형식으로 지정
        '0':(1,1,1,1,1,1,0),
        '1':(0,1,1,0,0,0,0),
        '2':(1,1,0,1,1,0,1),
        '3':(1,1,1,1,0,0,1),
        '4':(0,1,1,0,0,1,1),
        '5':(1,0,1,1,0,1,1),
        '6':(1,0,1,1,1,1,1),
        '7':(1,1,1,0,0,0,0),
        '8':(1,1,1,1,1,1,1),
        '9':(1,1,1,1,0,1,1)  }
 
try:
    while True:
        n = time.ctime()[11:13]+time.ctime()[14:16] # 현재 시각의 시,분 데이터
        s = n.rjust(4)  # 오른쪽 정렬. 생략 가능
        for digit in range(4):
            for loop in range(0,7):
                # segments[loop]에 의해 9,4,23,8,7,10,18,25번 중 핀을 결정
                # num[s[digit]] 는 '시'의 10의 자리의 딕셔너리 key. ex) 18시 42분일 경우 1
                # [loop]는 '시'의 10의 자리의 딕셔너리 value인 튜플의 index value
                #       ex) num[s[digit]]가 1일 경우
                #            loop 0 => key '0', 1 => key '1', 2 => key '1', 3 => key '0' ...
                gpio.output(segments[loop], num[s[digit]][loop])
                
                # 25번 핀(h, digit point)을 1초 on, 1초 off
                # 초의 1의 자리가 짝수일 경우에는 25번 핀(h, digit point) on
                if (int(time.ctime()[18:19])%2 == 0) and (digit == 1):
                    gpio.output(25, 1)
                    
                # 초의 1의 자리가 홀수일 경우에는 25번 핀(h, digit point) off
                else:
                    gpio.output(25, 0)
                    
            # 4개의 digit를 순차적으로 1ms on 후 off. dynamic display
            gpio.output(digits[digit], 0)
            time.sleep(0.001)
            gpio.output(digits[digit], 1)
finally:
    gpio.cleanup()
