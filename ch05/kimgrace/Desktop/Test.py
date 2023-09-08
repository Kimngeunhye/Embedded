import time
import picamera
from colour import Color
import io

picam = picamera.PiCamera()
picam.resolution = (1024, 768)
picam.framerate = 15 

try:
    filename = input('File name: ')
    picam.rotation = 180
    picam.start_preview(alpha = 127)
    picam.exposure_mode = 'night'
    picam.image_effect = 'blur'
    picam.awb_mode = 'sunlight'
    picam.brightness = 50
    picam.contrast = 50
    picam.saturation = 50
    picam.sharpness = 50
    
    picam.annotate_text_size = 50
    picam.annotate_background = picamera.Color('black')
    picam.annotate_foreground = picamera.Color('yellow')
    picam.annotate_text = time.ctime()

    picam.start_recording(filename+ '.h264')
    picam.wait_recording(5)
    picam.stop_recording()
    
    picam.stop_preview()
finally:
    picam.close()