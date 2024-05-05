def start():
    import tkinter as tk
    from tkinter import filedialog
    import cv2
    from PIL import Image, ImageTk

    class VideoPlayer:
        def __init__(self, root):
            self.root = root
            self.root.title("Video Player")

            self.video_path = None
            self.cap = None
            self.paused = False

            self.canvas = tk.Canvas(root, width=640, height=480)
            self.canvas.pack()

            self.btn_open = tk.Button(root, text="Open Video", command=self.open_video)
            self.btn_open.pack()

            self.btn_play_pause = tk.Button(root, text="Play", command=self.play_pause)
            self.btn_play_pause.pack()

            self.scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_position)
            self.scale.pack()

            self.update_video()

        def open_video(self):
            self.video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
            if self.video_path:
                self.cap = cv2.VideoCapture(self.video_path)
                self.scale.config(to=self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

        def play_pause(self):
            if self.cap is None:
                return
            self.paused = not self.paused
            if self.paused:
                self.btn_play_pause.config(text="Play")
            else:
                self.btn_play_pause.config(text="Pause")

        def set_position(self, value):
            if self.cap is None:
                return
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, int(value))
            self.update_video()

        def update_video(self):
            if self.cap is None or self.paused:
                return
            ret, frame = self.cap.read()
            if not ret:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                return
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            frame = ImageTk.PhotoImage(image=frame)
            self.canvas.img = frame
            self.canvas.create_image(0, 0, anchor=tk.NW, image=frame)
            self.scale.set(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
            self.root.after(30, self.update_video)


    root = tk.Tk()
    app = VideoPlayer(root)
    root.mainloop()

