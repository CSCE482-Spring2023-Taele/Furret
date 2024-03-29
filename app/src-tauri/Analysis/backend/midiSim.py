import mido
import numpy as np
import argparse    
import sys

midi_to_note = {12: 'C0', 13: 'C#0', 14: 'D0', 15: 'Eb0', 16: 'E0', 17: 'F0', 18: 'F#0', 19: 'G0', 20: 'Ab0', 
                21: 'A0', 22: 'Bb0', 23: 'B0', 24: 'C1', 25: 'C#1', 26: 'D1', 27: 'Eb1', 28: 'E1', 29: 'F1', 
                30: 'F#1', 31: 'G1', 32: 'Ab1', 33: 'A1', 34: 'Bb1', 35: 'B1', 36: 'C2', 37: 'C#2', 38: 'D2', 
                39: 'Eb2', 40: 'E2', 41: 'F2', 42: 'F#2', 43: 'G2', 44: 'Ab2', 45: 'A2', 46: 'Bb2', 47: 'B2', 
                48: 'C3', 49: 'C#3', 50: 'D3', 51: 'Eb3', 52: 'E3', 53: 'F3', 54: 'F#3', 55: 'G3', 56: 'Ab3', 
                57: 'A3', 58: 'Bb3', 59: 'B3', 60: 'C4', 61: 'C#4', 62: 'D4', 63: 'Eb4', 64: 'E4', 65: 'F4', 
                66: 'F#4', 67: 'G4', 68: 'Ab4', 69: 'A4', 70: 'Bb4', 71: 'B4', 72: 'C5', 73: 'C#5', 74: 'D5', 
                75: 'Eb5', 76: 'E5', 77: 'F5', 78: 'F#5', 79: 'G5', 80: 'Ab5', 81: 'A5', 82: 'Bb5', 83: 'B5', 
                84: 'C6', 85: 'C#6', 86: 'D6', 87: 'Eb6', 88: 'E6', 89: 'F6', 90: 'F#6', 91: 'G6', 92: 'Ab6', 
                93: 'A6', 94: 'Bb6', 95: 'B6', 96: 'C7', 97: 'C#7', 98: 'D7', 99: 'Eb7', 100: 'E7', 101: 'F7', 
                102: 'F#7', 103: 'G7', 104: 'Ab7', 105: 'A7', 106: 'Bb7', 107: 'B7', 108: 'C8', 109: 'C#8', 
                110: 'D8', 111: 'Eb8', 112: 'E8', 113: 'F8', 114: 'F#8', 115: 'G8', 116: 'Ab8', 117: 'A8', 
                118: 'Bb8', 119: 'B8', 120: 'C9', 121: 'C#9', 122: 'D9', 123: 'Eb9', 124: 'E9', 125: 'F9', 
                126: 'F#9', 127: 'G9'}

class MidiSim:
    def __init__(self, ui_fp : str, sm_fp : str):
        self.userinput_file_path =  ui_fp # 'midi_files/Criminal_1.mid'
        self.sheetmusic_file_path = sm_fp # 'midi_files/criminal_2.mid
        # output_file_path = sys.argv[3]'
        self.notes1 = self.processMidiFiles(self.userinput_file_path)
        self.notes2 = self.processMidiFiles(self.sheetmusic_file_path)
        self.simScore = self.midiComp()

        self.musicDataOuput()

    def l2Norm(self, list1, list2):
        distance = 0
        v1Mag = sum([sum([x**2 for x in row]) for row in list1])
        v2Mag = sum([sum([x**2 for x in row]) for row in list2])
        for sub1, sub2 in zip(list1, list2):
            sub_distance = 0
            for x, y in zip(sub1, sub2): sub_distance += x*y
            distance += sub_distance
        distance /= np.sqrt(v1Mag) * np.sqrt(v2Mag)
        return distance

    def midiComp(self):
        """Compares the user performance with the sheet music midi.

        Args:
            notes1 (list): Contains information from User Performance midi
            notes2 (list): Contains information from Sheet Music midi

        Returns:
            float: Returns the similarity score between user performance and sheet music.
        """
        val1, val2 = [], []
        for val, notes in [(val1, self.notes1), (val2, self.notes2)]:
            # print(msg.note, msg.velocity, msg.time)
            for note in notes:
                time, pitch, vel = note[1]-note[0], note[2], note[3]
                if val and pitch == val[-1][-1] + 1: val[-1].append(pitch) # Append pitch to last group
                else: val.append([pitch]) # Create new group for pitch

        # Calculate similarity for each group of pitches
        similarity_score = self.l2Norm(val1, val2)
        return similarity_score

    def musicDataOuput(self, outFile = "output.txt"):
        """This function writes out midi Data, similiraity scores, and intelligent feedback to a .txt file.


        Args:
            userData (list): user music data, where userData[i] = [startTime, endTime, note, velocity]
            sMusData (list): sheet music data, where sMusData[i] = [startTime, endTime, note, velocity]
            simScore (float): Similarity score between both userData nad sMusData.
            outFile (str, optional): File Path to output text file. Defaults to "output.txt".
        """
        output = ""
        for label, midiSet in [("User Music Data", self.notes1), ("Sheet Music Data", self.notes2)]:
            output += label + "\n"
            output += f"Size = {len(midiSet)}\n"
            output += "StartTime EndTime Note Velocity\n"
            for note in midiSet: 
                note[2] = midi_to_note[note[2]] # Covnerts numerical note (1...127) to letter note.
                output += " ".join(map(str, note)) + "\n"
            output += "\n"

        output += f"Similarity Score = {self.simScore:.10f}"

        with open(outFile, "w") as file:
            file.write(output)
            file.flush()  # Potential issues could rise with concurrency, so flush forces the output to be written to disk
        
        return

    def processMidiFiles(self, midiFile : str, accThreshold = 10):
        """This processes a midi file and extracts timing data, note data, and velocity.

        Args:
            midiFile (str): Path to the midi file
            accThreshold (int, optional): Time threshold for accidental note being played 

        Returns:
            notes (list): returns list with each element of the form [startTime, endTime, note, velocity]
        """
        notes = []

        midi = mido.MidiFile(midiFile) # Load midi file
        deltaT = 0
        for msg in mido.merge_tracks(midi.tracks):
            if 'note_on' in msg.type:
                pitch, force, time = msg.note, msg.velocity, msg.time
                # print(msg)
                if time <= accThreshold: # Checks if note is accidental
                    deltaT += time # Need to add to the time to the offset
                    continue # Don't add accidental note to the list of notes played

                notes.append([deltaT, deltaT + time, pitch, force])
                deltaT += time
        
        return notes


def main():
    # parser = argparse.ArgumentParser(prog="Midi Comparison & Output",
    #                                  description="This script takes in 2 midi files, compares them, and outputs into a textfile.",
    #                                  epilog="-----------------------END-----------------------")
    # parser.add
    MidiSim(sys.argv[1], sys.argv[2])
    


if __name__ == "__main__":
    main()

