source Analysis/backend/venv/bin/activate
python Analysis/backend/audio2Midi.py "$1"
python Analysis/backend/sheetMusic2Midi.py "resources/sheets/$2"
python Analysis/backend/midiSim.py Analysis/backend/*_basic_pitch.mid Analysis/backend/sheetMusic.mid
if test -f "Analysis/backend/output.txt"; then
  OUTPUTDATETIME=$( date '+%s' )
  cp "Analysis/backend/output.txt" "resources/outputs/$OUTPUTDATETIME.txt"
  echo $OUTPUTDATETIME
fi
rm -r *.mid
