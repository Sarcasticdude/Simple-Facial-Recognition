import cv2
import tkinter as tk
from tkinter import *


# Fundamentals of Programming Project.
# Project Name: 'Face and Eye Detection System'
# Class: BEE-13-B
# Group no. '6'
# Group members:Eaman Safdar(388110), Muhammad Huzaifa(369168), Muhammad Aqdas(369849)


def whole_code():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

    # Declaring video variables
    cam_index = 1
    window_x = 1366
    window_y = 769
    total_time = 0
    init_time = 150

    def set_video_specs(rec):
        """
        sets the width, height and brightness of video respectively.
        """
        rec.set(3, window_x)
        rec.set(4, window_y)
        rec.set(10, 10)

    def initialize_camera(cam_index):
        """
          starts the video recording from camera.
        """
        rec = cv2.VideoCapture(cam_index)
        return rec

    def detect_faces(img, gray):
        """
        coverts video feed to grayscale inorder to apply Haar_cascade properties
        and draws rectangles around the faces detected.
        """
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        total_faces = len(faces)
        faces_present = total_faces > 0
        for face in faces:
            (x, y, w, h) = face
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return faces, faces_present, total_faces

    def detect_eyes(img, gray, face):
        """
           highlights the eyes detected on the faces detected.
        """
        (x, y, w, h) = face
        roi_gray_face = gray[y:y + h, x:x + w]
        roi_color_face = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray_face, 1.1, 5, minSize=(30, 30), maxSize=(80, 80))
        total_eyes = len(eyes)
        for eye in eyes:
            (ex, ey, ew, eh) = eye
            cv2.rectangle(roi_color_face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        return eyes, total_eyes

    def read_eyes(face, eyes, total_eyes):
        """
            Tells which eyes are open and which are closed.
        """
        (x, y, w, h) = face
        text_position = (int(x), int(y + (12 * h / 10)))
        if total_eyes >= 2:
            cv2.putText(flipped, 'Eyes open', text_position, cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (100, 100, 0), 2)
        elif total_eyes == 1:
            positional_ratio = eyes[0][0] / abs(w - eyes[0][0])
            if positional_ratio >= 1.0:
                cv2.putText(flipped, 'Left closed', text_position, cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (100, 100, 0), 2)
            else:
                cv2.putText(flipped, 'Right closed', text_position, cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (100, 100, 0), 2)
        elif total_eyes == 0:
            cv2.putText(flipped, 'Eyes closed', text_position, cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (100, 100, 0), 2)
        else:
            pass

# Main Body of Code Starts Here

    print('\n\t# ----Welcome to CAM-STUDIO---- #')
    cap = initialize_camera(cam_index)
    set_video_specs(cap)
    while cap.isOpened():
        total_time += 1
        success, img = cap.read()
        flipped = cv2.flip(img, 1)      # The feed from the Webcam is inverted, hence must be flipped.
        if not success:
            raise 'Reading from video capture failed'
        gray = cv2.cvtColor(flipped, cv2.COLOR_BGR2GRAY)
        faces, faces_present, total_faces = detect_faces(flipped, gray)
        start = total_time > init_time
        if start:
            if faces_present:
                cv2.putText(img, f'{total_faces} Face(s) detected', (520, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                            (55, 0, 250), 2)

                for face in faces:
                    eyes, total_eyes = detect_eyes(flipped, gray, face)
                    read_eyes(face, eyes, total_eyes)
            else:
                cv2.putText(flipped, 'NO FACE DETECTED', (520, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (55, 0, 250), 2)
        else:
            cv2.putText(flipped, '...INITIALIZING CAM-STUDIO...', (450, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 0),
                        2)
        cv2.putText(flipped, "Press 'q' to quit the program.", (0, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                    (100, 50, 50), 2)
        cv2.imshow('Cam Studio', flipped)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            root.destroy()      # On pressing 'q' the main root window also closes
            break
    cv2.destroyAllWindows()
    print('\n\t#---- Face Detection Terminated ----#')


###------------------------------------------GRAPHICAL.USER.INTERFACE----------------------------------------------###

root = tk.Tk()
root.title("Cam Studio")
root.iconbitmap("Images/fc-scan.ico")

def open_help():
    help_win = Toplevel(root)
    help_win.title("Help")
    help_win.iconbitmap("Images/fc-scan.ico")

    help_bg = PhotoImage(file="Images/Help Window.png")
    canvas2 = tk.Canvas(help_win, height=396, width=712)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=help_bg, anchor="nw")
    help_quit = Button(help_win, text="EXIT", font="Helvetica, 18", command=help_win.destroy)
    help_quit_window = canvas2.create_window(610, 340, anchor="nw", window=help_quit)

    help_win.mainloop()


bg = PhotoImage(file="Images/BG-App2.png")
canvas = tk.Canvas(root, height=769, width=1366)
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, image=bg, anchor="nw")
canvas.create_text(350, 650, text="Cam Studio", font="Ariel, 72")

button_1 = Button(root, text="START", font=("Helvetica", 18), command=whole_code)
button_1_window = canvas.create_window(1050, 400, anchor="nw", window=button_1)

button_2 = Button(root, text="HELP", font=("Helvetica", 18), command=open_help)
button_2_window = canvas.create_window(1056, 500, anchor="nw", window=button_2)

button_quit = Button(root, text="EXIT", font="Helvetica, 18", command=root.quit)
button_quit_window = canvas.create_window(1061, 600, anchor="nw", window=button_quit)

root.mainloop()
