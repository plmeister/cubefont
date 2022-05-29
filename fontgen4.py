import fontforge

# run the script:
# & "c:\program files (x86)\fontforgebuilds\bin\fontforge.exe" -script fontgen4.py


f = fontforge.font()


f.fontname = "cube4"
f.fullname = "cube4"


characters = {
    "B": "B.svg", "B'": "B'.svg", "b": "bs.svg", "b'": "bs'.svg", "BW": "BW.svg", "BW'": "BW'.svg", "B2": "B2.svg", "B2'": "B2'.svg", "b2": "bs2.svg", "BW2": "BW2.svg",
    "D": "D.svg", "D'": "D'.svg", "d": "ds.svg", "d'": "ds'.svg", "DW": "DW.svg", "DW'": "DW'.svg", "D2": "D2.svg", "D2'": "D2'.svg", "d2": "ds2.svg", "DW2": "DW2.svg",
    "F": "F.svg", "F'": "F'.svg", "f": "fs.svg", "f'": "fs'.svg", "FW": "FW.svg", "FW'": "FW'.svg", "F2": "F2.svg", "F2'": "F2'.svg", "f2": "fs2.svg", "FW2": "FW2.svg",
    "L": "L.svg", "L'": "L'.svg", "l": "ls.svg", "l'": "ls'.svg", "LW": "LW.svg", "LW'": "LW'.svg", "L2": "L2.svg", "L2'": "L2'.svg", "l2": "ls2.svg", "LW2": "LW2.svg",
    "R": "R.svg", "R'": "R'.svg", "r": "rs.svg", "r'": "rs'.svg", "RW": "RW.svg", "RW'": "RW'.svg", "R2": "R2.svg", "R2'": "R2'.svg", "r2": "rs2.svg", "RW2": "RW2.svg",
    "U": "U.svg", "U'": "U'.svg", "u": "us.svg", "u'": "us'.svg", "UW": "UW.svg", "UW'": "UW'.svg", "U2": "U2.svg", "U2'": "U2'.svg", "u2": "us2.svg", "UW2": "UW2.svg",
    "X": "X.svg", "X'": "X'.svg", "X2": "X2.svg",
    "Y": "Y.svg", "Y'": "Y'.svg", "Y2": "Y2.svg",
    "Z": "Z.svg", "Z'": "Z'.svg", "Z2": "Z2.svg",
    "quotesingle": "Z.svg", "W": "Z.svg", "two": "Z.svg"
}

ligatures = {
    "B'": ("B", "quotesingle"), "B2": ("B", "two"), "B2'": ("B", "two", "quotesingle"), "BW": ("B", "W"), "BW'": ("B", "W", "quotesingle"), "b'": ("b", "quotesingle"), "b2": ("b", "two"), "BW2": ("B", "W", "two"),
    "D'": ("D", "quotesingle"), "D2": ("D", "two"), "D2'": ("D", "two", "quotesingle"), "DW": ("D", "W"), "DW'": ("D", "W", "quotesingle"), "d'": ("d", "quotesingle"), "d2": ("d", "two"), "DW2": ("D", "W", "two"),
    "F'": ("F", "quotesingle"), "F2": ("F", "two"), "F2'": ("F", "two", "quotesingle"), "FW": ("F", "W"), "FW'": ("F", "W", "quotesingle"), "f'": ("f", "quotesingle"), "f2": ("d", "two"), "FW2": ("F", "W", "two"),
    "L'": ("L", "quotesingle"), "L2": ("L", "two"), "L2'": ("L", "two", "quotesingle"), "LW": ("L", "W"), "LW'": ("L", "W", "quotesingle"), "l'": ("l", "quotesingle"), "l2": ("l", "two"), "LW2": ("L", "W", "two"),
    "R'": ("R", "quotesingle"), "R2": ("R", "two"), "R2'": ("R", "two", "quotesingle"), "RW": ("R", "W"), "RW'": ("R", "W", "quotesingle"), "r'": ("r", "quotesingle"), "r2": ("r", "two"), "RW2": ("R", "W", "two"),
    "U'": ("U", "quotesingle"), "U2": ("U", "two"), "U2'": ("U", "two", "quotesingle"), "UW": ("U", "W"), "UW'": ("U", "W", "quotesingle"), "u'": ("u", "quotesingle"), "u2": ("u", "two"), "UW2": ("U", "W", "two"),
    "X'": ("X", "quotesingle"), "X2": ("X", "two"),
    "Y'": ("Y", "quotesingle"), "Y2": ("Y", "two"),
    "Z'": ("Z", "quotesingle"), "Z2": ("Z", "two")
}

print("Importing glyphs")

for key in characters.keys():
    char = f.createChar(-1, key)
    char.width = 1000
    char.importOutlines("cube4\\"+characters[key])

f.addLookup('ligatures', 'gsub_ligature', (),
            [['rlig', [['latn', ['dflt']]]]])
f.addLookupSubtable('ligatures', 'ligatureshi')

print("Adding ligatures")

for key in ligatures.keys():
    print(key)
    glyph = f[key]
    glyph.addPosSub('ligatureshi', ligatures[key])


print("Saving cube4.sfd")
f.save("cube4.sfd")

print("saving cube4.ttf")
f.generate("cube4.ttf")
