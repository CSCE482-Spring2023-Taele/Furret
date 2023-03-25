import music21
from pydub import AudioSegment
from music21 import audioSearch

import librosa
import mido
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def mp3_to_midi(mp3_path, midi_path):
    # Load audio file
    y, sr = librosa.load(mp3_path)

    # Extract pitches and timing from audio file
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitches = pitches.T
    magnitudes = magnitudes.T

    # Create MIDI file
    midi_file = mido.MidiFile()
    track = mido.MidiTrack()
    midi_file.tracks.append(track)

    # Add pitch and timing data to MIDI file
    ticks_per_beat = midi_file.ticks_per_beat
    max_magnitude = np.amax(magnitudes)
    for frame, frame_pitches in enumerate(pitches):
        time = librosa.frames_to_time(frame, sr=sr)
        for pitch, magnitude in zip(frame_pitches, magnitudes[frame]):
            if magnitude > 0:
                velocity = int(magnitude / max_magnitude * 127)
                note_on = mido.Message('note_on', note=int(round(pitch)),
                                       velocity=velocity,
                                       time=int(time * ticks_per_beat))
                note_off = mido.Message('note_off', note=int(round(pitch)),
                                        velocity=0,
                                        time=int((time + 0.01) * ticks_per_beat))
                track.append(note_on)
                track.append(note_off)

    # Save MIDI file
    midi_file.save(midi_path)


mp3_to_midi("S:\\CSCE 482\\Furret\Server\\audioSamples\\Joji-Glimpse of Us.mp3", "S:\\CSCE 482\\Furret\Server\\audioSamples")