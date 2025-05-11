import tkinter as tk
from music21 import key, note, stream

def play_f_flat_major():
    key_signature = key.KeySignature(-8)
    print(f"Key Signature: {key_signature}")

    scale = key.Key('F-').getScale('major')
    print("F Flat Major Scale Notes:", [str(p) for p in scale.getPitches()])

    stream_part = stream.Stream()
    stream_part.append(key_signature)

    for pitch in scale.getPitches():
        note_item = note.Note(pitch)
        stream_part.append(note_item)

    stream_part.show('midi')

def play_e_sharp_major():
    key_signature = key.KeySignature(11)
    print(f"Key Signature: {key_signature}")

    scale = key.Key('E#').getScale('major')
    print("E Sharp Major Scale Notes:", [str(p) for p in scale.getPitches()])

    stream_part = stream.Stream()
    stream_part.append(key_signature)

    for pitch in scale.getPitches():
        note_item = note.Note(pitch)
        stream_part.append(note_item)

    stream_part.show('midi')

root = tk.Tk()
root.title("secret base")
root.geometry("300x300")

# Create a button for F Flat Major
button_f_flat_major = tk.Button(root, text="Fes", font=('Helvetica', 24), command=play_f_flat_major)
button_f_flat_major.pack()

# Create a button for E Sharp Major
button_e_sharp_major = tk.Button(root, text="Eis", font=('Helvetica', 24), command=play_e_sharp_major)
button_e_sharp_major.pack()

root.mainloop()
