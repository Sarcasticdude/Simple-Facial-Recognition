# Simple-Facial-Recognition
A simple Facial Detection Engine built in Python using Pre-trained Haar Classifiers
------->	Project Name: 'Face and Eye Detection System'

-> Pre-requisites of the Program:

	1) Python 3
	2) An IDE (preferably 'Pycharm')
	3) A Camera/Webcam

-> Contents of this project

	1) Face_detect.py file (The only file containing the whole code.)
	2) BG-App2.png (Image for the background of the main window)
	3) fc-scan.ico (Image for the icon of the windows)
	4) Help Window.png (Image for the background of Help Window
	6) Read_me.txt

-> Libraries used:

	1) opencv-python (For face/eye detection)
	2) tkinter (For Graphical-User-Interface)[buit-in library, not needed to install]
	3) numpy (optional)

-> Steps:

- Create a folder named 'Images' in the file(Face_detect.py) directory of the IDE you are using
  (in the case of Pycharm it is PycharmProjects/*project-name).

- Change the directory of the images in the code accordingly if you have saved the Images somewhere else.

- Connect your Webcam/Camera/Webcam.

- According to the camera you are using change the value of 'cam_index' in the code. For the built-in
  camera of the device use index '0', for secondary webcams/cameras use '1','2',e.t.c.
