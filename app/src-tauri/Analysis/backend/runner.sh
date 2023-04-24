echo "testing"
echo "$1"
echo "$2"
source venv/bin/activate
python audio2Midi.py "$1"
python sheetMusic2Midi.py "$2"
python midiSim.py userInput.mid sheetMusic.mid
echo "complete"
