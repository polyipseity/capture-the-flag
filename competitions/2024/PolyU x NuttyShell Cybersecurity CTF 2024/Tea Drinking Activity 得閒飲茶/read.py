from sys import argv
import mido

with mido.MidiFile(argv[1]) as midi:
    midi.print_tracks()
