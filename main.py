from recorder import record_voice
from AcausticFeaturesExtract import extract_features
from XGBmodel import xgb_predict
from tools import modern_window
from customtkinter import *


myfont = ("Elephant", 16)
white = "#FFFFFF"
app = modern_window("gender recognizer", mode="dark")
app.geometry("500x500")

def new_rec():
    lbl.configure(text="")
    btn.configure(state=DISABLED)

    timer.configure(text="Speak!", font=("Elephant", 18))
    app.update()
    voice = record_voice()
    timer.configure(text="Wait!", font=("Elephant", 18))
    app.update()
    features = extract_features(voice)
    prediction = xgb_predict(features)
    lbl.configure(text=prediction, font=("Elephant", 18))

    btn.configure(state=NORMAL)

def record():
    btn.configure(state=DISABLED)

    timer.configure(text="Speak!", font=("Elephant", 18))
    app.update()
    voice = record_voice()
    timer.configure(text="Wait!", font=("Elephant", 18))
    app.update()
    features = extract_features(voice)
    prediction = xgb_predict(features)
    lbl.configure(text=prediction, font=("Elephant", 18))

    btn.configure(state=NORMAL, command=new_rec)


lbl = CTkLabel(app, text="", fg_color="transparent")
lbl.pack(pady=40, padx=10, side=TOP, anchor=CENTER)

btn = CTkButton(app, text="RECORD", text_color=white, fg_color='red', font=myfont)
btn.configure(command=record)
btn.pack(pady=80, padx=10, side=BOTTOM, anchor=CENTER)

timer = CTkLabel(app, text="", fg_color="transparent")
timer.pack(pady=40, padx=10, side=BOTTOM, anchor=CENTER)

app.mainloop()
