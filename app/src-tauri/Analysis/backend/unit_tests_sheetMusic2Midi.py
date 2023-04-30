import unittest
import os.path
from music21 import *

class TestSheetMusic2Midi(unittest.TestCase):
    
    def test_scanning_music(self):
        # create temporary sheet music file for testing
        test_smus_file = "test_sheet_music.smus"
        with open(test_smus_file, "w") as f:
            f.write("test sheet music")
        
        # create sheetMusic2Midi object and run scanningMusic() method
        sm2m = sheetMusic2Midi(test_smus_file)
        sm2m.scanningMusic()
        
        # check that tempSheetMusic.musicxml file was created
        self.assertTrue(os.path.isfile("tempSheetMusic.musicxml"))
        
        # remove temporary files
        os.remove(test_smus_file)
        os.remove("tempSheetMusic.musicxml")
        
    def test_xml_to_midi(self):
        # create temporary MusicXML file for testing
        test_musicxml_file = "test_music.xml"
        s = stream.Stream()
        n = note.Note("C4")
        s.append(n)
        s.write("xml", test_musicxml_file)
        
        # create sheetMusic2Midi object and run xmlTOmidi() method
        sm2m = sheetMusic2Midi("", test_musicxml_file, "test_output.mid")
        sm2m.xmlTOmidi()
        
        # check that sheetMusic.mid file was created
        self.assertTrue(os.path.isfile("test_output.mid"))
        
        # read MIDI file and check that it contains one note
        mf = midi.MidiFile()
        mf.open("test_output.mid")
        mf.read()
        mf.close()
        self.assertEqual(len(mf.tracks[0].events), 2)  # MIDI header event + note event
        
        # remove temporary files
        os.remove(test_musicxml_file)
        os.remove("test_output.mid")
        
if __name__ == '__main__':
    unittest.main()
