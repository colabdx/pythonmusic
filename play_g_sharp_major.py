from music21 import *

# Define the G Sharp Major key
key_signature = key.KeySignature(8)  # 8 sharps correspond to G Sharp Major
print(f"Key Signature: {key_signature}")

# Create an E Sharp Major scale
scale = key.Key('G#').getScale('major')  # 'G#' denotes G sharp
print("G Sharp Major Scale Notes:", [str(p) for p in scale.getPitches()])

# Create a stream (musical score)
stream_part = stream.Stream()
stream_part.append(key_signature)

# Add the scale notes to the stream for playback
for pitch in scale.getPitches():
    note_item = note.Note(pitch)
    stream_part.append(note_item)

# Play the stream
stream_part.show('midi')  # This will open your default MIDI player and play the scale
