# Module dedicated to songs :)

def melody():

    import winsound;

    beatlength = 300;

    winsound.Beep(262, beatlength) # C
    winsound.Beep(262, beatlength) # C
    winsound.Beep(294, beatlength) # D
    winsound.Beep(330, beatlength) # E

    winsound.Beep(262, beatlength) # C
    winsound.Beep(330, beatlength) # E
    winsound.Beep(294, 2*beatlength) # D (double length)

    winsound.Beep(262, beatlength) # C
    winsound.Beep(262, beatlength) # C
    winsound.Beep(294, beatlength) # D
    winsound.Beep(330, beatlength) # E

    winsound.Beep(262, 2*beatlength) # C (double length)
    winsound.Beep(247, 2*beatlength) # B (double length)

    winsound.Beep(262, beatlength) # C
    winsound.Beep(262, beatlength) # C
    winsound.Beep(294, beatlength) # D
    winsound.Beep(330, beatlength) # E

    winsound.Beep(349, beatlength) # F
    winsound.Beep(330, beatlength) # E
    winsound.Beep(294, beatlength) # D
    winsound.Beep(262, beatlength) # C

    winsound.Beep(247, beatlength) # B
    winsound.Beep(196, beatlength) # G
    winsound.Beep(220, beatlength) # A
    winsound.Beep(247, beatlength) # B

    winsound.Beep(262, 2*beatlength) # C (double length)
    winsound.Beep(262, 2*beatlength) # C (double length)

def bigben():
    # play music on the PC internal speaker
    # tested with Python24 on a Windows XP computer  vegaseat  15aug2005
    import winsound
    import time
    # the notes
    P = 0   # pause
    C = 1
    CS = 2  # C sharp
    D = 3
    DS = 4
    E = 5
    F = 6
    FS = 7
    G = 8
    GS = 9
    A = 10
    AS = 11
    B = 12
    EN = 100  # eighth note
    QN = 200  # quarter note
    HN = 400  # half note
    FN = 800  # full note
    def play(octave, note, duration):
        """play note (C=1 to B=12), in octave (1-8), and duration (msec)"""
        if note == 0:    # a pause
            time.sleep(duration/1000)
            return
        frequency = 32.7032           # C1
        for k in range(0, octave):    # compute C in given octave
            frequency *= 2
        for k in range(0, note):      # compute frequency of given note
            frequency *= 1.059463094  # 1.059463094 = 12th root of 2
        time.sleep(0.010)             # delay between keys
        winsound.Beep(int(frequency), duration)


    play(4,E,HN)
    play(4,C,HN)
    play(4,D,HN)
    play(3,G,HN+QN); play(3,P,QN)
    play(3,G,HN)
    play(4,D,HN)
    play(4,E,HN)
    play(4,C,HN+QN)

def Star_Wars():
    ## Impreial March
    from winsound import Beep
    Beep(440, 500); Beep(440, 500); Beep(440, 500); Beep(349, 350) ;
    Beep(523, 150) ;Beep(440, 500); Beep(349, 350); Beep(523, 150) ;
    Beep(440, 1000) ;Beep(659, 500); Beep(659, 500) ;Beep(659, 500) ;
    Beep(698, 350); Beep(523, 150) ;Beep(415, 500) ;Beep(349, 350);
    Beep(523, 150); Beep(440, 1000)

def au_clair_de_la_lune():
    import math
    import winsound
    import time

    labels = ['a','a#','b','c','c#','d','d#','e','f','f#','g','g#']
    # name is the complete name of a note (label + octave). the parameter
    # n is the number of half-tone from A4 (e.g. D#1 is -42, A3 is -12, A5 is 12)
    name   = lambda n: labels[n%len(labels)] + str(int((n+(9+4*12))/12))
    # the frequency of a note. the parameter n is the number of half-tones
    # from a4, which has a frequency of 440Hz, and is our reference note.
    freq   = lambda n: int(440*(math.pow(2,1/12)**n))

    # a dictionnary associating note frequencies to note names
    notes  = {name(n): freq(n) for n in range(-42,60)}

    # the period expressed in second, computed from a tempo in bpm
    period = lambda tempo: 1/(tempo/60)

    # play each note in sequence through the PC speaker at the given tempo
    def play(song, tempo):
        for note in song.lower().split():
            if note in notes.keys():
                winsound.Beep(notes[note], int(period(tempo)*1000))
            else:
                time.sleep(period(tempo))

    # "au clair de la lune"!! 'r' is a rest
    play( 'c4 c4 C4 d4 e4 r d4 r c4 e4 d4 d4 c4 r r r '
          'c4 C4 c4 d4 e4 r d4 r c4 e4 d4 d4 c4 r r r '
          'd4 d4 d4 d4 A3 r a3 r d4 c4 B3 a3 g3 r r r '
          'c4 c4 c4 d4 e4 r d4 r c4 e4 d4 d4 c4 r r r ', 180 )

