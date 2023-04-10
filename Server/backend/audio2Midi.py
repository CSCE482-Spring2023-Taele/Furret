import librosa
import numpy as np
import mido
import sys
import librosa
import crepe
from mido import Message, MidiFile, MidiTrack


class Audio2Midi:
    def __init__(self, audioFilePath, midiFilePath = "userInput.mid"):
        self.audio_to_midi(audioFilePath, midiFilePath)
    
    def audio_to_midi(self, audio_file, midi_file):
        # Load the audio file
        audio_data, sr = librosa.load(audio_file, sr=44100, mono=True)

        # Predict the pitch of the audio signal using Crepe
        time, frequency, confidence, activation = crepe.predict(audio_data, sr=sr, viterbi=True)

        # Convert the pitch predictions to MIDI notes
        midi_notes = []
        for t, f in zip(time, frequency):
            midi_note = int(round(librosa.hz_to_midi(f)))
            midi_notes.append((t, midi_note))

        # Save the MIDI notes to a file
        with open(midi_file, 'w') as f:
            for t, note in midi_notes:
                f.write('%.2f,%d\n' % (t, note))
        


def main():
    Audio2Midi(sys.argv[1])



if __name__ == "__main__":
    main()