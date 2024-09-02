from customtkinter import CTkLabel, CTkFrame
import tkinter as tk

myfont = ("Elephant", 18)
white = "#FFFFFF"

class TimerWidget(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(fg_color="transparent")
        self.pack()
        self.create_widgets()
        self.remaining_time = 0

    def create_widgets(self):
        self.label = CTkLabel(self, text="", fg_color="transparent", font=myfont)
        self.label.pack(pady=40, padx=10, side=tk.TOP, anchor=tk.CENTER)

    def start_timer(self):
        self.remaining_time = 5
        self.update_timer()

    def update_timer(self, text="wait!"):
        if self.remaining_time > 0:
            self.label.configure(text=f" {self.remaining_time} sec")
            self.remaining_time -= 1
            self.after(1000, self.update_timer)  # Call update_timer after 1000 milliseconds (1 second)
        else:
            self.label.configure(text=text)

if __name__ == "__main__":
    root = tk.Tk()

    timer_widget2 = TimerWidget(master=root)

    root.mainloop()
