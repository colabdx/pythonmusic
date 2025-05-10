from music21 import *

# Define the double E Flat Major key
key_signature = key.KeySignature(-10)  # -10 means 10 flats, which corresponds to double E Flat Major
print(f"Key Signature: {key_signature}")

# Create an double E Flat Major scale
scale = key.Key('E--').getScale('major')  # 'E--' denotes double E flat
print("double E Flat Major Scale Notes:", [str(p) for p in scale.getPitches()])

# Create a stream (musical score)
stream_part = stream.Stream()
stream_part.append(key_signature)

# Add the scale notes to the stream for playback
for pitch in scale.getPitches():
    note_item = note.Note(pitch)
    stream_part.append(note_item)

# Play the stream
stream_part.show('midi')  # This will open your default MIDI player and play the scale
