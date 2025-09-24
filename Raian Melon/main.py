#Funkcija za učitavanje teksta iz datoteke
def ucitaj_tekst(filepath):
    try:
        # ovdje ide logika za citanje datoteke
        with open(filepath, 'r', encoding='utf-8') as file:
            sadrzaj = file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f"Datoteka {filepath} nije pronađena.")
        return None

#Funkcija za prociscavanje teksta
def procisti_tekst(tekst):
    # ovdje ide logika za prociscavanje teksta
    tekst = tekst.lower()
    return tekst

if __name__ == "__main__":
    filepath = 'tekst.txt'
    print(f"Pokušavam učitati datoteku: {filepath}")
    tekst = ucitaj_tekst(filepath)
    if tekst:
        print("Sadržaj datoteke:")
        print(tekst)
    else:
        print("Nije moguće učitati sadržaj datoteke.")
    
    tekst_prociscen = procisti_tekst(tekst)
    if tekst_prociscen:
        print("Pročišćeni tekst:")
        print(tekst_prociscen)
    else:
        print("Nije moguće pročitati ili pročišćiti tekst.")

    