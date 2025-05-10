from music21 import *

# Define the F Flat Major key
key_signature = key.KeySignature(-8)  # -8 means 8 flats, which corresponds to F Flat Major
print(f"Key Signature: {key_signature}")

# Create an F Flat Major scale
scale = key.Key('F-').getScale('major')  # 'F-' denotes F flat
print("F Flat Major Scale Notes:", [str(p) for p in scale.getPitches()])

# Create a stream (musical score)
stream_part = stream.Stream()
stream_part.append(key_signature)

# Add the scale notes to the stream for playback
for pitch in scale.getPitches():
    note_item = note.Note(pitch)
    stream_part.append(note_item)

# Play the stream
stream_part.show('midi')  # This will open your default MIDI player and play the scale