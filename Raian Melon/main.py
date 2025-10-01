#Funkcija za učitavanje teksta iz datoteke 
def ucitaj_tekst(filepath):
    try:
        # KOd za otvaranje datoteke ide ovdje
        with open (filepath, 'r', encoding='utf-8') as file:
            sadrzaj = file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f"Greška: Datoteka na putanji '{filepath}' nije pronađena")
        return None # Vratit ćemo 'ništa' ako datoteka ne postoji
      
      # Funkcija za proišćavanje teksta 
def ocisti_tekst(tekst):
#Kod za pročišćavanje teksta ide ovdje
    tekst = tekst.lower()

    interpunkcija = ['.', ',', '!', '?', ':', '"', "'", '(', ')']
    for znak in interpunkcija:
        tekst = tekst.replace(znak, '')

    lista_rijeci = tekst.split()

    return lista_rijeci
       
def broji_rijeci(lista_rijeci):
    rijecnik = {}
    for rijec in lista_rijeci:
        if rijec in rijecnik:
            rijecnik[rijec] += 1
        else:
            rijecnik[rijec] = 1
    return rijecnik

if __name__=="__main__":
    filepath = "tekst.txt"
    print(f"Učitavam tekst iz datoteke: {filepath}")
    ucitani_tekst = ucitaj_tekst(filepath)
    if ucitani_tekst:
        print("Učitani tekst je:")
        #print(ucitani_tekst)
    else:
        print("Greška pri učitavanju datoteke.")

    ucitani_tekst = ocisti_tekst(ucitani_tekst)

    if ucitani_tekst:
        print("Očišćeni tekst je:")
        print(ucitani_tekst)
    else:
        print("Greška pri očišćavanju teksta.")
        
    rijeci_brojanje = broji_rijeci(ucitani_tekst)
    
    print("Broj ponavljanja riječi:")
    for rijec, broj in sorted(rijeci_brojanje.items(), key=lambda x: x[1], reverse=True):
        print(f"{rijec}: {broj}")
