
import sys

from math import log2, pow

A4 = 440
C0 = A4 * pow(2, -4.75)
name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def pitch(freq):
    h = round(12 * log2(freq / C0))
    octave = h // 12
    n = h % 12
    return name[n] + str(octave)


def main(argv):

    #From mid2cnc:
   # ((2^((81−69)/12))−1)⋅440
   # freq_xyz[i] = pow(2.0, (nownote - 69) / 12.0) * 440.0  # convert note numbers to frequency for each axis in Hz
   # feed_xyz[i] = freq_xyz[i] * 60.0 / machine_ppi  # feedrate in IPM for each axis individually
   # distance_xyz[i] = feed_xyz[i] * (((note[0] - last_time) + 0.0) / (midi.division + 0.0)) * (
   # tempo / 60000000.0)  # distance in inches for each axis

#((2^((81−69)/12))−1)⋅440
freq_xyz[i] = pow(2.0, (nownote - 69) / 12.0) * 440.0  # convert note numbers to frequency for each axis in Hz
feed_xyz[i] = freq_xyz[i] * 60.0 / machine_ppi  # feedrate in IPM for each axis individually

if __name__ == "__main__":
    main(sys.argv)
