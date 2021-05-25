# Hindeline kodutöö

## Hindamine
Hinne kujuneb selle kodutöö eest järgmiselt:
- Hinne 3: tuleb teha ülesanded 1.1 kuni 1.4
- Hinne 4: tuleb lisaks eelnevale teha ka ülesanded 1.5 ja 1.6
- Hinne 5: tuleb lisaks eelnevale teha ka ülesanne 1.7

### ÜL 1.1
Looge PyCharmis 2 faili:
- Raamat.py
- Külastaja.py

### ÜL 1.2
Raamat.py failis looge klass Raamat ja selle init meetod, millel on vähemalt järgmised omadused:
- tiitel, milles hoiame raamatu tiitlit/pealkirja
- autor, milles hoiame raamatu autori nime
- lehekülgedeArv, milles hoiame raamatu lehekülgede arvu

NB: Kõik nende parameetrite väärtused peavad olema sisse antavad sisend parameetriga init meetodis.

### ÜL 1.3
Külastaja.py failis looge klass Külastaja ja selle init meetod, millel on vähemalt järgmised omadused:
- eesNimi, kus hoiame külastaja eesnime
- perekonnaNimi, kus hoiame külastaja perekonnanime
- laenutatudRaamatud, tehke alguses tühi list

NB: Kõik nende parameetrite väärtused (välja arvatud laenutatudRaamatud) peavad olema sisse antavad sisend parameetriga init meetodis.

### ÜL 1.4
Looge klassis Külastaja uus funktsioon laenutaRaamat(self), mis teeb järgmist:
- Võtab sisend parameetriks Raamat objekti.
- Lisab sisendina antud Raamat objekti külastaja laenutatudRaamatud listi.

### ÜL 1.5
Looge klassis Külastaja uus funktsioon tagastaRaamat(self), mis teeb järgmist:
- Võtab sisend parameetriks Raamat objekti.
- Eemaldab sisendina antud Raamat objekti külastaja laenutatudRaamatud listist.

### ÜL 1.6
Looge klassis Külastaja uus funktsioon kuvaLaenutatudRaamatud(self), mis teeb järgmist:
- Prindib kõik külastaja poolt laenutatud raamatute tiitlid.

### ÜL 1.7
Täiendage Raamat klassi nii, et lisate init meetodisse uue omaduse:
- laenutatud, mille väärtus on vaikimisi False

Täiendage laenutaRaamat(self) funktsiooni järgmiselt:
- Funktsioon alguses kontrollib **kas** sisendina antud raamat on juba laenutatud (mõelge millise omaduse true/false väärtust kontrollite).
    - Kui raamat **ei ole** laenutatud, siis funktsioon lisab raamatu laenutatudRaamatud listi. Lisaks määratakse raamat laenutatuks.
    - Kui raamat **on** laenutatud, siis funktsioon prindib teate "Raamatut ei saa laenutada, see on juba välja laenutatud!".
    
### Kontrollimine
Kontrollimiseks võite luua külastaja objekti järgmiste omadustega:
- eesnimi: "Joosep"
- perekonnanimi: "Joosepson"

Võite luua raamatu objekti järgmiste omadustega:
- tiitel: "Mingi vahva raamat"
- autor: "Keegi kaval autor"
- lehekülgede arv: 305

Ja veel ühe:
- tiitel: "Parimad koka road"
- autor: "Kuulus Ekspert"
- lehekülgede arv: 275

Kui käivitate laenutaRaamat funktsiooni ning annate sisendiks need 2 raamatut ja siis tagastate neist esimese. Peaks kuvaLaenutatudRaamatud funktsioon välja printima ainult tiitli "Parimad koka road".

Kui olete teinud ka ülesande 1.7 ning proovite uuesti laenutada seda teist raamatut (mida me ei ole veel tagastanud), siis peaksite vastuseks saama "Raamat on juba laenutatud".
