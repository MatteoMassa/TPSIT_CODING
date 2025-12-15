import re
import random

studenti = [
    "Luca Ciaone",
    "Matteo Parmiciaoli",
    "Claudio Rossi",
    "Luigi Macioni",
    "Gino Ricci",
    "Gino Belli",
    "Anna Bassi",
    "Marco Neri",
    "Sofia Orlandi",
    "Paolo Verdi"
]

def filtra_e_estrai(studenti, testo):
    t = testo.strip()
    if not t:
        return []

    patt1 = re.compile(re.escape(t), re.IGNORECASE)
    filtrati = [s for s in studenti if patt1.search(s)]

    if not filtrati:
        patt2 = re.compile("[" + re.escape(t) + "]", re.IGNORECASE)
        filtrati = [s for s in studenti if patt2.search(s)]

    if not filtrati:
        a = min(t.lower())
        b = max(t.lower())
        patt3 = re.compile(rf"[{re.escape(a)}-{re.escape(b)}A-Z ]", re.IGNORECASE)
        filtrati = [s for s in studenti if patt3.search(s)]

    if len(filtrati) <= 3:
        return filtrati
    return random.sample(filtrati, 3)

testi = ["cia", "rrr", "qz"]

for x in testi:
    estratti = filtra_e_estrai(studenti, x)
    print(f"Input: {x} -> {estratti}")






