source venv/bin/activate
python audio2Midi.py "$1"
python sheetMusic2Midi.py "resources/sheets/$2"
python midiSim.py userInput.mid sheetMusic.mid
if test -f "Analysis/backend/output.txt"; then
  OUTPUTDATETIME=$( date '+%s' )
  #cp "Analysis/backend/output.txt" "resources/outputs/$OUTPUTDATETIME.txt"
  echo $OUTPUTDATETIME
fi
