import unittest

import midiSim


class TestmidiSim(unittest.TestCase):
    def test_ProcessFiles(self):
        self.assertTrue(midiSim.MidiSim.processMidiFiles("app/src-tauri/Analysis/backend/midi_files/Criminal_1.mid"))


if __name__ == '__main__':
    unittest.main()
