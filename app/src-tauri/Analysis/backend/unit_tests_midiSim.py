import unittest
import mido
from midi_sim import MidiSim

class TestMidiSim(unittest.TestCase):

    def test_l2Norm(self):
        midi_sim = MidiSim(None, None)
        list1 = [[1, 2], [3, 4]]
        list2 = [[1, 2], [3, 4]]
        self.assertEqual(midi_sim.l2Norm(list1, list2), 1.0)
        list1 = [[1, 2], [3, 4]]
        list2 = [[0, 1], [1, 1]]
        self.assertAlmostEqual(midi_sim.l2Norm(list1, list2), 0.9486832980505138)

    def test_midiComp(self):
        ui_fp = "midi_files/test_user_input.mid"
        sm_fp = "midi_files/test_sheet_music.mid"
        midi_sim = MidiSim(ui_fp, sm_fp)
        self.assertAlmostEqual(midi_sim.simScore, 1.0)

    def test_midi_to_note(self):
        midi_sim = MidiSim(None, None)
        self.assertEqual(midi_sim.midi_to_note[12], "C0")
        self.assertEqual(midi_sim.midi_to_note[13], "C#0")
        self.assertEqual(midi_sim.midi_to_note[60], "C4")
        self.assertEqual(midi_sim.midi_to_note[127], "G9")
