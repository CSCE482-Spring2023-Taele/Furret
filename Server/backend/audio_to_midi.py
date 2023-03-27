import librosa
import numpy as np
import math
import pretty_midi

# Load audio file using librosa
y, sr = librosa.load('Dragonspine.wav')

# Extract pitch information using librosa
pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)

# Set a threshold to filter out pitches with low magnitudes
threshold = np.mean(magnitudes) * 0.5
pitches[magnitudes < threshold] = 0

# Convert pitch information to MIDI notes
midi_notes = []
for pitch in pitches:
    if np.max(pitch) == 0:
        midi_note = None
    else:
        midi_note = int(round(69 + 12 * math.log2(np.argmax(pitch) / 440.0)))
    midi_notes.append(midi_note)

# Create a MIDI file using pretty_midi
midi = pretty_midi.PrettyMIDI()
piano = pretty_midi.Instrument(program=0)
start_time = 0
for note in midi_notes:
    if note is None:
        start_time += 0.01
    else:
        end_time = start_time + 0.01
        piano.notes.append(pretty_midi.Note(
            velocity=100,
            pitch=note,
            start=start_time,

