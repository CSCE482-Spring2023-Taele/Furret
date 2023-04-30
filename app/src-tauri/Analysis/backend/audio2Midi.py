import sys
import subprocess
import os


class Audio2Midi:
    def __init__(self, audioFilePath, midiFilePath = "userInput.mid"):
        subprocess.run(["basic-pitch", ".", audioFilePath, "--save-midi"])
        # path = "./audioMidiTemp"
        # fileName = os.listdir(path)[0]
        # # Detect the encoding of the file
        # with open(fileName, 'rb') as f:
        #     result = chardet.detect(f.read())
        
        

    
def main():
    Audio2Midi(sys.argv[1])



if __name__ == "__main__":
    main()