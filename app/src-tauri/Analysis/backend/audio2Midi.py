import sys
import subprocess
import codecs
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
import os
import chardet


class Audio2Midi:
    def __init__(self, audioFilePath, midiFilePath = "./audioMidiTemp"):
        subprocess.run(["basic-pitch", midiFilePath, audioFilePath, "--save-midi"])
        path = "./audioMidiTemp"
        fileName = os.listdir(path)[0]
        # # Detect the encoding of the file
        # with open(fileName, 'rb') as f:
        #     result = chardet.detect(f.read())
        
        

    
def main():
    Audio2Midi(sys.argv[1])



if __name__ == "__main__":
    main()