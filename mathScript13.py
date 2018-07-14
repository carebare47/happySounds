
import sys
from math import log, pow

#                feed_xyz[i] = freq_xyz[i] * 60.0 / machine_ppi    # feedrate in IPM for each axis individually
import fnmatch
machine_ppi = 2032
global inputFreq
inputFreq = 99999

A4 = 440
C0 = A4 * pow(2, -4.75)
print(C0)
name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def pitch(freq):
    h = round(12 * log((freq / C0),2))
    octave = h // 12
    n = h % 12
    #print("h: ", h, " octave: ", octave, " n: ", n)
    return name[n] + str(octave)

def pitch2(freq):
    h = round(12 * log((freq / C0),2))
    #h = log2(freq/c0)
    #freq = (2^h)*c0
    #h = 12 log2(P / C0).
    #h/12 = log2(p/c0)
    #(p/c0) = 2^(h/12)
    #p = 2^(h/12)*(c0)
    #p = 2^(

 #   c4
 #   c, 4
#octave = 4
#letter = c

def test(f):
    #print(f)
    sharpFlag = 0
    flatFlag = 0
    l = list(f)
    letter = l[0]
    if "#" in f:
        number = int(l[2])
        sharpFlag = 1
    else:
        number = int(l[1])
        sharpFlag = 0
    let = 15
    for i in range(0, 12):
        #print("i: ", i)
        #print("name[i], note: ", type(name[i]), ", ", type(note))
        #print("name[i]: ", name[i], ", ", note)
        if (name[i] == letter):
            let = i
            if (sharpFlag == 1):
                let = let + 1
    p = pow(2, ((let+(number*12)))/12)*C0
    p = round(p, 3)
    global inputFreq
    #print("Nearest note: ", f, ". Input frequency: ", inputFreq, ". New quantized frequency: ", p)
    feedrate = p * 60.0 / 2000
    #print("feedrate: ", feedrate)
    return p


    #l = ['RT07010534.txt', 'RT07010533.txt', 'RT02010534.txt']
    pattern = 'F'
    #matching = fnmatch.filter(l, pattern)



        #matching = fnmatch.filter(l, pattern)





    #steps_from_C0 = let+(12*octave)
    #pitch = 12*log( ,2)

    #440*2^((-1)*

ppm = 80

def fr_to_hz(fr):
    global ppm
    #hz*60/ppi = fr
    #fr*ppi = hz*60
    hz = fr*ppm/60
    return hz

def hz_to_fr(hz):
    global ppm
    fr = hz*60/ppm
    #fr*ppi = hz*60
    return fr


def hz_to_note(hz):
    note = note_name(hz)
    octave = find_octave(hz)

    for i in range(0, 12):
        #print("i: ", i)
        #print("name[i], note: ", type(name[i]), ", ", type(note))
        #print("name[i]: ", name[i], ", ", note)
        if (name[i] == note):
            #print("matching note found")
            #test(name[i], octave)
            return test(pitch(hz))


counter = 0

def get_line(strung):
    #strung = "G0 X12 Y3 F300 E27.9"
    global counter, inputFreq
    if (";" in strung):
        strung = strung.split(";")
        strung = strung[0]
    strung = strung.split(" ")
    if ("E" not in strung):
        reduceFlag = 1
    else:
        reduceFlag = 0
    #print(strung)
    # matching = fnmatch.filter(strung, "F")
    # print(matching)
    for i in range(0, len(strung)):
        if ('F' in strung[i]):
            # print(strung[i])
            #print(i)
            #print("db1: ", strung[i])
            #print("r=: ", round(3085.7, 0), " r1: ", round(3085.7, 1))
            strang = strung[i].replace("F", "")
            #print("strang", strang, "strangtype", type(strang))
            fStrang = float(strang)
            if reduceFlag:
                fStrang
            iStrang = int(fStrang)
            #roundedStrang = round(int(),0)
            inputFR = iStrang
            #print("F = ", inputFR)
            counter = counter + 1
            hz = fr_to_hz(inputFR)
            inputFreq = hz
            return hz_to_note(hz)

def get_fr(strung):
    #strung = "G0 X12 Y3 F300 E27.9"
    global counter, inputFreq
    if (";" in strung):
        strung = strung.split(";")
        strung = strung[0]
    strung = strung.split(" ")
    if ("E" not in strung):
        reduceFlag = 1
    else:
        reduceFlag = 0
    #print(strung)
    # matching = fnmatch.filter(strung, "F")
    # print(matching)
    for i in range(0, len(strung)):
        if ('F' in strung[i]):
            # print(strung[i])
            #print(i)
            #print("db1: ", strung[i])
            #print("r=: ", round(3085.7, 0), " r1: ", round(3085.7, 1))
            strang = strung[i].replace("F", "")
            #print("strang", strang, "strangtype", type(strang))
            fStrang = float(strang)
            if reduceFlag:
                fStrang
            iStrang = int(fStrang)
            return iStrang




def note_name(freq):
    h = round(12 * log((freq / C0),2))
    octave = h // 12
    n = h % 12
    return name[n]


def find_octave(freq):
    h = round(12 * log((freq / C0),2))
    octave = h // 12
    return octave




print("This is the name of the script: ", sys.argv[0], ". Number of arguments: ", len(sys.argv),
      ". The arguments are: ", str(sys.argv[1]))

#
# f=open('myfile','r')
# with open(filepath) as fp:
#     line = fp.readline()
#     cnt = 1
#     while line:
#         # print("Line {}: {}".format(cnt, line.strip()))
#         oldFr = get_fr(line.strip())
#         newFreq = get_line(line.strip())
#         #string = "F" +
#         print("Old line: ", line)
#         print("Old feedrate: ", str(oldFr), ". New feedrate = ", hz_to_fr(newFreq))
#         print("New line: ", line.replace("F" + str(oldFr), "F" + str(hz_to_fr(newFreq))))
#         #line = line.replace("F" + str(oldFr), "F" + str(hz_to_fr(newFreq)))
#         #fp.write(li)
#         line = fp.readline()
#         cnt += 1
#


    #oem: feed_xyz = freq_xyz * 60.0 / machine_ppi    # feedrate in IPM for each axis individually
    #h = (f.m)/60
    #feed = parseFeed()
    #the scalars are wrong, fix this
    # global inputFreq
    # feed_xyz = (int(sys.argv[1]))
    # inputFreq = feed_xyz
    # #print("direct conversion", pitch(feed_xyz))
    # freq_xyz = (feed_xyz*machine_ppi) / 6000.0
    #print("freq_xyz = (feed_xyz*machine_ppi) / 6000.0 = ", freq_xyz)
    #note = note_name(freq_xyz)

file = sys.argv[1]
cnt = 0
#file = 'test4'
f = open(file + '.txt', 'r')
linelist = f.readlines()
f.close

# Re-open file here
f2 = open(file + '.gcode', 'w')
for line in linelist:
    oldFr = get_fr(line.strip())
    newFreq = get_line(line.strip())
    # string = "F" +
    #print("Old line: ", line)
    print("Old feedrate: ", str(oldFr), ". New feedrate = ", hz_to_fr(newFreq))
    #print("New line: ", line.replace("F" + str(oldFr), "F" + str(hz_to_fr(newFreq))))
    line = line.replace("F" + str(oldFr), "F" + str(hz_to_fr(newFreq)))
    f2.write(line)
    cnt += 1
f2.close()
print("total feedrates: ", counter, " total lines: ", cnt)
print("File ", file + '.gcode', " created.")


#
#
# f=open('myfile','r')
# text = f.readlines()
# f.close()
#
# i =0;
#
# fw=open('mynewfile', 'w')
#
# myNumber = 2 - number
# myNumberasString = str(myNumber)
# for line in text:
#
#     if 'word' in line:
#         line = line.replace('word', myNumberasString)
#
#     fw.write(line)
# fw.close()