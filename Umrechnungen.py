################################################################################################
### Hier sind alle 6 Umwandlungen zu finden. ###################################################
################################################################################################

# Die hier verwendeten Ansätze zur Umrechnung sind meine eigenen Ideen.
# Dass es auch kürzer und effizienter geht, ist mir bewusst.
# Das Thema behandle ich in der Dokumentation.


################################################################################################
### Umwandlung von Dezimalzahlen in Binärzahlen per Division. ##################################
### 10 - 2 ### 10 - 2 ### 10 - 2 ### 10 - 2 ### 10 - 2 ### 10 - 2 ### 10 - 2 ### 10 - 2 ########
################################################################################################

def dezimal_zu_binaer(Zahl):
    Erg = []  # Leere Liste für die zu speichernde Ausgabe
    Zahl = int(Zahl)  # Eingabe
    orgi_Zahl = Zahl

    while Zahl > 0:
        bit = Zahl % 2  # % 2 ergibt Bit: 0 / 1
        Erg.append(str(bit))  # Bit als String der Liste hinten anfügen
        Zahl = Zahl // 2

    # Liste umdrehen, weil sie bei der Division falsch herum ausgegeben wird:
    Erg.reverse()

    # Die Binärzahl als String ausgeben
    binärzahl = ''.join(Erg)

    return binärzahl



#
# ################################################################################################
# ### Umwandlung von Binärzahlen zu Dezimalzahlen per Potenzierung. ##############################
# ### 2 - 10 ### 2 - 10 ### 2 - 10 ### 2 - 10 ### 2 - 10 ### 2 - 10 ### 2 - 10 ### 2 - 10 ########
# ################################################################################################
#
# def binär_zu_dezimal(Zahl):
#
#
#
#     return dezimal
#
## Modul Umrechnung 2-10

# Die prüfung, ob es wirklich eine Binärzahl ist, erfolgt im Modul Rechenart.
# Hierher wird nur ein String überstellt, der zuverlässig aus 1 und 0 ohne Leerzeichen besteht.
# binärzahl = input('Gib die Binärzahl ein, die in Dezimal konvertiert werden soll. ')
#
# # Zahl umdrehen:
# umgekehrte_binärzahl = binärzahl[::-1]
#
# Ergebnis2zu10 = 0
#
# # Umwandeln des Zeichens im String in eine Zahl:
# for index, zeichen in enumerate(umgekehrte_binärzahl):
#     # Umrechnung der einzelnen Stellen:
#     Ergebnis2zu10+=int(zeichen)*(2**index)
#
# print(f'Die Binärzahl {binärzahl} ist im Dezimalsystem die {Ergebnis2zu10}.')

#
# ################################################################################################
# ### Umwandlung von Dezimalzahlen in Hexadezimalzahlen per Division. ############################
# ### 10 - 16 ### 10 - 16 ### 10 - 16 ### 10 - 16 ### 10 - 16 ### 10 - 16 ### 10 - 16 ### 10 - 16 #
# ################################################################################################
#
# def dezimal_zu_hexadezimal(Zahl):
#
#     return hexadezimal
#
#
# Umwandlung von Dezimalzahlen in Hexadezimal per Division
#
#
# Erg = []  # Leere Liste für die zu speichernde Ausgabe
# zahl = int('1000000')  # Eingabe
# orig_zahl=zahl # Speicherung für die Ausgabe am Ende
#
#
# if zahl==0:
#     print(f"Die Dezimalzahl {zahl} wird hexadezimal als {zahl} dargestellt.")
# else:
#     while zahl > 0:
#         hexa = zahl % 16  # % 2 ergibt hexarest: 0-15
#         if 0 <= hexa <= 9: # Wenn der Rest 0-9 ist, wird er direkt übernommen.
#             wert=hexa
#         elif 10 <= hexa <= 15: # Wenn der Rest 10-15 ist, wird er als A-F übernommen
#             wert=chr(hexa+55)
#         Erg.append(str(wert))  # wert als String der Liste hinten anfügen
#         zahl = zahl // 16
#
# # Liste umdrehen, weil sie bei der Division falsch herum ausgegeben wird:
#     Erg.reverse()
#
# # Die Hexazahl als String ausgeben
#     hexazahlen = ''.join(Erg)
#     print(f"Die Dezimalzahl {orig_zahl} wird Hexadezimalzahl als {hexazahlen} dargestellt.")
#

# ################################################################################################
# ### Umwandlung von Hexadezimalzahlen zu Dezimalzahlen per Potenzierung. ########################
# ### 16 - 10 ### 16 - 10 ### 16 - 10 ### 16 - 10 ### 16 - 10 ### 16 - 10 ### 16 - 10 ### 16 - 10 #
# ################################################################################################
#
# def hexadezimal_zu_dezimal(Zahl):
#
#     return dezimal
#
#
# Modul Umrechnung 16-10

# Die prüfung, ob es wirklich eine Hexadezimal ist, erfolgt im Modul Rechenart.
# Hierher wird nur ein String überstellt, der zuverlässig aus einer Hexadezimalzahl ohne Leerzeichen besteht.
# hexazahl = input('Gib die Hexadezimalzahl ein, die in Dezimal konvertiert werden soll. ')
#
# # Zahl umdrehen:
# umgekehrte_hexazahl = hexazahl[::-1]
#
# Ergebnis16zu10 = 0
#
# Umwandeln des Zeichens im String in eine Zahl:
# for index, zeichen in enumerate(umgekehrte_hexazahl):
#     # Umrechnung der einzelnen Stellen:
#     # Unterscheidung Buchstaben-Zahlen
#     if zeichen.isdigit():
#         wert=int(zeichen)
#     elif zeichen in 'ABCDEF':
#         wert=ord(zeichen) - 55
#     Ergebnis16zu10+=wert*(16**index)
#
# print(f'Die Hexadezimalzahl {hexazahl} ist im Dezimalsystem die {Ergebnis16zu10}.')
#
#
#
#
# ################################################################################################
# ### Umwandlung von Binärzahlen in Hexadezimalzahlen. ###########################################
# ### 2 - 16 ### 2 - 16 ### 2 - 16 ### 2 - 16 ### 2 - 16 ### 2 - 16 ### 2 - 16 ### 2 - 16 ########
# ################################################################################################
#
# def binär_zu_hexadezimal(Zahl):
#
#     return hexadezimal
#
# Umrechnung Binär -Hexadezimal
#
# eingabezahl = '11001100100'                             # Hier kommt die eingegebene Zahl als String an.
# originale_eingabezahl = eingabezahl             # Speichern der Eingabe für den Print-Satz am Ende
# Ergebnis = []                                   # Leere Liste zum Ergebnis speichern.
#
# # Falls 0 konvertiert werden soll, greift "if".
# # Da unter "else" die Nullen vor der Zahl gekürzt werden und in diesem Fall ein leeres Ergebnis zurückgegeben würde.
# if eingabezahl == '0':
#     print(f'Die binäre Zahl {eingabezahl} wird als Hexadezimalzahl auch als {eingabezahl} dargestellt.')
#
# # Unter else sind alle 16 möglichen Werte gespeichert. Das ist nicht mathematisch elegant,
# sorgt aber für eine einfache Schreibweise des Codes und vermeidet lange Logikketten.
# else:
#     while len(eingabezahl) % 4 != 0:
#         eingabezahl = '0'+ eingabezahl
#     for element in range(0, len(eingabezahl), 4):
#         block = eingabezahl[element:element+4]
#         if block == '0000':
#             Ergebnis.append('0')
#         elif block == '0001':
#             Ergebnis.append('1')
#         elif block == '0010':
#             Ergebnis.append('2')
#         elif block == '0011':
#             Ergebnis.append('3')
#         elif block == '0100':
#             Ergebnis.append('4')
#         elif block == '0101':
#             Ergebnis.append('5')
#         elif block == '0110':
#             Ergebnis.append('6')
#         elif block == '0111':
#             Ergebnis.append('7')
#         elif block == '1000':
#             Ergebnis.append('8')
#         elif block == '1001':
#             Ergebnis.append('9')
#         elif block == '1010':
#             Ergebnis.append('A')
#         elif block == '1011':
#             Ergebnis.append('B')
#         elif block == '1100':
#             Ergebnis.append('C')
#         elif block == '1101':
#             Ergebnis.append('D')
#         elif block == '1110':
#             Ergebnis.append('E')
#         elif block == '1111':
#             Ergebnis.append('F')
#
#     Hexazahl = ''.join(Ergebnis)
#
#     print(f'Die Binärzahl {originale_eingabezahl} wird hexadezimal als {Hexazahl} dargestellt.')
#
#
#
#
#
#
#
#

#
# ################################################################################################
# ### Umwandlung von Hexadezimalzahlen in Binärzahlen. ###########################################
# ### 16 - 2 ### 16 - 2 ### 16 - 2 ### 16 - 2 ### 16 - 2 ### 16 - 2 ### 16 - 2 ### 16 - 2 ########
# ################################################################################################
#
# def hexadezimal_zu_binär(Zahl):
#
#     return binär
#
#
# # Umrechnung Hexadezimal - Binär
#
# eingabezahl = '9D'                             # Hier kommt die eingegebene Zahl als String an.
# originale_eingabezahl = eingabezahl             # Speichern der Eingabe für den Print-Satz am Ende
# Ergebnis = []                                   # Leere Liste zum Ergebnis speichern.
#
# # Falls 0 konvertiert werden soll, greift "if".
# # Da unter "else" die Nullen vor der Zahl gekürzt werden und in diesem Fall ein leeres Ergebnis zurückgegeben würde.
# if eingabezahl == '0':
#     print(f'Die hexadezimale Zahl {eingabezahl} wird als Binärzahl auch als {eingabezahl} dargestellt.')
#
# # Unter else sind alle 16 möglichen Werte gespeichert. Das ist nicht mathematisch elegant,
# # sorgt aber für eine einfache Schreibweise des Codes und vermeidet lange Logikketten.
# else:
#     for element in eingabezahl:
#         if element == '0':
#             Ergebnis.append('0000')
#         elif element == '1':
#             Ergebnis.append('0001')
#         elif element == '2':
#             Ergebnis.append('0010')
#         elif element == '3':
#             Ergebnis.append('0011')
#         elif element == '4':
#             Ergebnis.append('0100')
#         elif element == '5':
#             Ergebnis.append('0101')
#         elif element == '6':
#             Ergebnis.append('0110')
#         elif element == '7':
#             Ergebnis.append('0111')
#         elif element == '8':
#             Ergebnis.append('1000')
#         elif element == '9':
#             Ergebnis.append('1001')
#         elif element == 'A':
#             Ergebnis.append('1010')
#         elif element == 'B':
#             Ergebnis.append('1011')
#         elif element == 'C':
#             Ergebnis.append('1100')
#         elif element == 'D':
#             Ergebnis.append('1101')
#         elif element == 'E':
#             Ergebnis.append('1110')
#         elif element == 'F':
#             Ergebnis.append('1111')
#
#
#     binaerzahl = ''.join(Ergebnis)
#     binaerzahl_ohne_null_vorne = binaerzahl.lstrip('0')
#
#     print(f'Hexadezimal {originale_eingabezahl} wird binär als {binaerzahl_ohne_null_vorne} dargestellt.')
#
#







