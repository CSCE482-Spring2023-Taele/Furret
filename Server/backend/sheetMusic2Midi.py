import subprocess
import os
from music21 import *
import sys

class sheetMusic2Midi:
    def __init__(self, sheetMusicFilePath, xmlFilePath="tempSheetMusic.musicxml", midiFilePath="sheetMusic.mid"):
        self.smusFP  = sheetMusicFilePath
        self.midiFP  = midiFilePath
        self.mxmlFP  = xmlFilePath
        self.scanningMusic()
        self.xmlTOmidi()
        

    def scanningMusic(self):
        print("Oemer Started!")
        command = ['oemer', self.smusFP, '-o', self.mxmlFP, '--save-cache']
        subprocess.run(command, check=True)
        print("Oemer Completed!")
    
    def xmlTOmidi(self):
        s = converter.parse(self.mxmlFP)
        mf = midi.translate.streamToMidiFile(s)
        mf.open(self.midiFP, 'wb')
        mf.write()
        mf.close()
        

def main():
    sheetMusicFilePath = sys.argv[1]
    sheetMusic2Midi(sheetMusicFilePath)

if __name__ == "__main__":
    main()