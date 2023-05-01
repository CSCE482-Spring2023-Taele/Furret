source venv/bin/activate
python audio2Midi.py "$1"
python sheetMusic2Midi.py "$2"
python midiSim.py *_basic_pitch.mid sheetMusic.mid
echo $OUTPUTDATETIME
