import unittest
from unittest.mock import patch
from audio2midi import Audio2Midi

class TestAudio2Midi(unittest.TestCase):
    
    def test_audio2midi_runs_successfully(self):
        with patch('subprocess.run') as mock_run:
            Audio2Midi('test_audio.wav')
            mock_run.assert_called_once_with(['basic-pitch', '.', 'test_audio.wav', '--save-midi'])
    
    @patch('subprocess.run')
    def test_audio2midi_with_custom_midi_filepath(self, mock_run):
        Audio2Midi('test_audio.wav', midiFilePath='custom_midi.mid')
        mock_run.assert_called_once_with(['basic-pitch', '.', 'test_audio.wav', '--save-midi'])
    
if __name__ == '__main__':
    unittest.main()
