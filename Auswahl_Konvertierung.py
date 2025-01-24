# Hier erfolgt die Auswahl der Umwandlung

from Umrechnungen import dezimal_zu_binaer

Abfrage = 'ja'

print('')
print('Moin, dieses Programm kann Zahlen aus dem dezimalen, binären und hexadezimalen Zahlensystem umwandeln.')
print('')
while Abfrage != 'X':
    Zahl = input('Wie lautet die Zahl, die du umwandeln willst? ')
    print()
    if Zahl == '0' or Zahl == '1':
        print(f'Die {Zahl} wird in allen drei Zahlensystemen als {Zahl} dargestellt. In diesem Fall gibt es nichts umzuwandeln. :)')
    else:
        AusgangsZahlensystem = input('In welchem Zahlensystem liegt die Zahl vor? Bitte schreibe "2" für Binär, "10" für Dezimal und "16" für Hexadezimal: ')
        print('')
        ZielZahlensystem = input('In welches Zahlensystem möchtest du die Zahl umwandeln? Bitte schreibe "2" für Binär, "10" für Dezimal und "16" für Hexadezimal: ')
        if AusgangsZahlensystem == ZielZahlensystem:
            print(f'Da du im gleichen Zahlensystem bleibst, bleibt auch deine Zahl {Zahl}...')
        elif AusgangsZahlensystem == '10' and ZielZahlensystem == '2':
            print('')
            print(f'Die dezimale {Zahl} wird als binäre Zahl {dezimal_zu_binaer(Zahl)} geschrieben.')
    print('')
    Abfrage = input('Wenn du das Programm beenden willst, drücke "X". Mit der Eingabetaste kommst du zu einer neuen Umwandlung. ')
    print('')