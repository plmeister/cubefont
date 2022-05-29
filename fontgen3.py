import fontforge

# run the script:
# & "c:\program files (x86)\fontforgebuilds\bin\fontforge.exe" -script fontgen3.py


f = fontforge.font()


f.fontname = "cube3"
f.fullname = "cube3"

def getGlyphs(side):
    upper = side.upper()
    lower = side.lower()
    d = {
        "B": "B.svg", "B'": "B'.svg", "B2": "B2.svg", "B2'": "B2'.svg",
        "b": "bW.svg", "b'": "bW'.svg", "Bw": "bW.svg", "Bw'": "bW'.svg",
        "Bw2": "BW2.svg", "b2": "bW2.svg", "b2'": "Bw2'.svg", "Bw2'": "bw2'.svg"
    }
    r = {}
    for k in d.keys():
        kk = k.replace("B", upper).replace("b", lower)
        v = d[k].replace("B", upper).replace("b", lower)
        r[kk] = v
    return r

characters = {}
for face in 'UDLRFB':
    characters.update(getGlyphs(face))
    
characters.update({
    "M": "M.svg", "M'": "M'.svg", "M2": "M2.svg", "M2'": "M2'.svg",
    "E": "E.svg", "E'": "E'.svg", "E2": "E2.svg", "E2'": "E2'.svg",
    "S": "S.svg", "S'": "S'.svg", "S2": "S2.svg", "S2'": "S2'.svg",
    "X": "X.svg", "X'": "X'.svg", "X2": "X2.svg",
    "Y": "Y.svg", "Y'": "Y'.svg", "Y2": "Y2.svg",
    "Z": "Z.svg", "Z'": "Z'.svg", "Z2": "Z2.svg",
    "quotesingle": "Z.svg", "W": "Z.svg", "two": "Z.svg", "w": "Z.svg" # placeholder glyphs so we can use them in ligatures
})

def getLigaturesForFace(side):
    upper = side.upper()
    lower = side.lower()
    d = {
        # B already a glyph
        "B'": ("B", "quotesingle"),
        "B2": ("B", "two"),
        "B2'": ("B", "two", "quotesingle"),
        # double layer turns - lowercase faceletter, or uppercase + w
        "b": ("B", "w"), # alternate notation for lowercase letter
        "b2": ("b", "two"),
        "b2'": ("b", "two", "quotesingle"),
        "Bw'": ("B", "w", "quotesingle"),
        "b'": ("b", "quotesingle"),
        "Bw": ("B", "w"),
        "Bw2": ("B", "w", "two"),
        "Bw2'": ("B", "w", "two", "quotesingle")
    }
    r = {}
    for k in d.keys():
        kk = k.replace("B", upper).replace("b", lower)
        v = list(d[k])
        v[0] = v[0].replace("B", upper).replace("b", lower)
        r[kk] = tuple(v)
    return r

ligatures = {}

for side in 'UDLRFB':
    ligatures.update(getLigaturesForFace(side))

ligatures.update({
    "X'": ("X", "quotesingle"), "X2": ("X", "two"),
    "Y'": ("Y", "quotesingle"), "Y2": ("Y", "two"),
    "Z'": ("Z", "quotesingle"), "Z2": ("Z", "two"),
    "M'": ("M", "quotesingle"), "E'": ("E", "quotesingle"), "S'": ("S", "quotesingle"),
    "M2": ("M", "two"), "E2": ("E", "two"), "S2": ("S", "two"),
    "M2'": ("M", "two", "quotesingle"), "E2'": ("E", "two", "quotesingle"), "S2'": ("S", "two", "quotesingle")
})

print("Importing glyphs")

for key in characters.keys():
    char = f.createChar(-1, key)
    char.width = 1000
    char.importOutlines("cube3\\"+characters[key])

f.addLookup('ligatures', 'gsub_ligature', (),
            [['rlig', [['latn', ['dflt']]]]])
f.addLookupSubtable('ligatures', 'ligatureshi')

print("Adding ligatures")

for key in ligatures.keys():
    print(key)
    glyph = f[key]
    glyph.addPosSub('ligatureshi', ligatures[key])


print("Saving cube3.sfd")
f.save("cube3.sfd")

print("saving cube3.ttf")
f.generate("cube3.ttf")
