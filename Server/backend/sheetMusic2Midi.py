import subprocess
import os

class sheetMusic2Midi:
    def __init__(self, sheetMusicFilePath, midiFilePath="sheetMusic.midi"):
        self.sMusFP = sheetMusicFilePath
        self.midiFP = midiFilePath
        self.scanningMusic(self.sMusFP, self.midiFP)
        

    def scanningMusic(self, input_path, output_path):
        self.folderSheetMusic(output_path)
        command = ['oemer', input_path, '-o', output_path, '--save-cache']
        subprocess.run(command, check=True)
    

    def folderSheetMusic(self, output_path):
        if not os.path.exists(output_path):
            os.makedirs(output_path)

def main():
    sheetMusicFilePath = "dragonspire.jpg"
    sheetMusic2Midi(sheetMusicFilePath)

if __name__ == "__main__":
    main()