import simpleaudio as sa
import numpy as np

# Function to generate a tone
def generate_tone(frequency, duration=0.5, sample_rate=44100, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return wave

# Function to play the scale
def play_scale(scale_binary, base_frequency=440):
    # Notes in an octave (assuming equal temperament)
    semitone_ratio = 2 ** (1 / 12)
    scale_notes = []

    for i, bit in enumerate(scale_binary):
        if bit == "1":
            # Add frequency for this note
            scale_notes.append(base_frequency * (semitone_ratio ** i))

    # Play each note in the scale
    for frequency in scale_notes:
        wave_data = generate_tone(frequency)
        wave_data = (wave_data * 32767).astype(np.int16)  # Convert to 16-bit PCM
        audio = sa.WaveObject(wave_data, 1, 2, 44100)
        play_obj = audio.play()
        play_obj.wait_done()

if __name__ == "__main__":
    # Scale binary pattern
    scale_binary = "100000010"
    play_scale(scale_binary)