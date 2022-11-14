tekst = "Witaj świecie"
tekst2 = tekst.upper()
tekst.upper()
imie = "Tomek"
# print(tekst)
# print(tekst2.lower())
# print(tekst.removeprefix('Witaj'))
# print(tekst.removesuffix('świecie'))
# print(tekst[6:55])
# print(tekst.removeprefix("W"))
encoded_s = tekst.encode('utf-8')
print(encoded_s)
print(type(encoded_s))
print(encoded_s.decode('utf-8'))


tekst_bajtowy = b"Tutaj jest tekst bajtowy"
print(tekst.count("i", 0, 4))
teskt_format = f"Mam\t na imię {imie} \ni lubię \bPythona"
print(teskt_format)
starszy = "Witaj %s!"
print(starszy % imie)
print("Witaj {}".format(imie))