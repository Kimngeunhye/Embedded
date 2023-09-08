ifconfig
exit
sudo raspi-config
raspistill -o cam_capture.jpg
clear
raspistill -o cam_capture.jpg
vcgencmd get_camera
raspistill -o cam_capture.jpg
raspistill -o cam_capture_0.jpg -t 10000
raspistill -vf -o cam_capture_v.jpg -t 10000
raspistill -hf -o cam_capture_h.jpg -t 10000
raspistill -vf -hf -o cam_capture_v_h.jpg -t 10000
raspivid -o video.h264 -t 30000
sudo apt-get install -y gpac
MP4Box -add video00.h264 video00.mp4
clear
raspivid -t 30000 -w 640 -h 480 -fps 25 -b 1200000 -p 0,0,640,480 -o video00.h264
MP4Box -add video00.h264 video00.mp4
sudo apt-get install python3-picamera
exit()
exit
pip install colour
pip install color
python setup.py install
pip install colour
pip install git+https://github.com/vaab/colour
pip install git+https://github.com/vaab/colour@master
clear
sudo pat update
sudo apt update
sudo apt list --upgradable
sudo apt full-upgrade
sudo apt-get install python3-opencv
