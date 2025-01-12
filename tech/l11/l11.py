import tkinter as tk
from threading import Thread, Event
from time import sleep, strftime

class ClockApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Clock App")
        
        self.label_hours = tk.Label(master, text="Hours", font=("Helvetica", 48))
        self.label_hours.pack()
        
        self.label_minutes = tk.Label(master, text="Minutes", font=("Helvetica", 48))
        self.label_minutes.pack()
        
        self.label_seconds = tk.Label(master, text="Seconds", font=("Helvetica", 48))
        self.label_seconds.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_threads)
        self.start_button.pack(side=tk.LEFT, padx=20)
        
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_threads)
        self.stop_button.pack(side=tk.RIGHT, padx=20)
    
        self.stop_event = Event()
        
        self.thread_hours = Thread(target=self.update_hours)
        self.thread_minutes = Thread(target=self.update_minutes)
        self.thread_seconds = Thread(target=self.update_seconds)

    def start_threads(self):
        self.stop_event.clear()
        if not self.thread_hours.is_alive():
            self.thread_hours = Thread(target=self.update_hours)
            self.thread_hours.start()
        if not self.thread_minutes.is_alive():
            self.thread_minutes = Thread(target=self.update_minutes)
            self.thread_minutes.start()
        if not self.thread_seconds.is_alive():
            self.thread_seconds = Thread(target=self.update_seconds)
            self.thread_seconds.start()

    def stop_threads(self):
        self.stop_event.set()

    def update_hours(self):
        while not self.stop_event.is_set():
            current_time = strftime("%H")
            self.label_hours.config(text=current_time)
            sleep(1)

    def update_minutes(self):
        while not self.stop_event.is_set():
            current_time = strftime("%M")
            self.label_minutes.config(text=current_time)
            sleep(1)

    def update_seconds(self):
        while not self.stop_event.is_set():
            current_time = strftime("%S")
            self.label_seconds.config(text=current_time)
            sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()
