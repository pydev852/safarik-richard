# moje_meno
# cislo1
# cislo_1
# mojePrveMeno = "Fero"
# _vek = 5
# _ = 5
# _______________________ = 99
# cena_usd
# premenna

# meno = "Alena Nováková"
# vek = 35
# praca = "programatorka"

# -------------------------------------------------------------
# Vytvorte premenné nazov_produktu, cena a pocet_kusov. 
# Uložte do nich ľubovoľné hodnoty (napr. "Laptop", 1200.50, 5). 
# Potom ich obsah vypíšte pomocou funkcie print().

# Očakávaný výstup:
# Produkt: Laptop
# Cena: 1200.5
# Počet kusov na sklade: 5

# nazov_produktu = "Omen"
# cena_produktu = 1000
# pocet_kusov = 8

# print("Produkt: " + nazov_produktu)
# print("Cena: " + str(cena_produktu))
# print("Pocet kusov na sklade: " + str(pocet_kusov))

# -------------------------------------------------------------
# Ktoré aritmetické operátory sa nedajú použiť s reťazcami (strings) v jazyku Python?
# a) *
# b) –
# c) +
# d) Všetky z uvedených

# -------------------------------------------------------------
# Vytvorte premenné x, y, z a priraďte im hodnoty 10, 20, 30  na jedinom riadku kódu. 
# a = 20
# x, y, z = a, a, a

# a = "bryndzove halusky"
# b = "vyprazany syr"

# # print(a,b)

# # b = "bryndzove halusky"
# # a = "vyprazany syr"

# a, b = b, a
# print(a,b)

# "Poznanie sa nezakladá len na pravde, ale aj na omyle." Carl Gustav Jung

# print('"Poznanie sa nezakladá len na pravde, \nale aj na omyle." Carl Gustav Jung')

# Čo raz z úst vypustíš, 
# ani štyrmi koňmi nazad nevtiahneš. 

# print("Čo raz z úst vypustíš, \nani štyrmi koňmi nazad nevtiahneš. ")

# -------------------------------------------------------------
# Napíšte tri print() príkazy. 
# Prvý vytlačí "Učím sa", druhý "programovať v" a tretí "Pythone.". 

# print("Ucim sa", end=" ")
# print("programovat v", end=" ")
# print("Pythone.")


# print("Ucim sa","programovat v","Pythone.", sep="\n")

# G:\My Drive\SHARE\_PYTHON\LEKCIE

# -------------------------------------------------------------

# Máte časti cesty k súboru: C:, Users, Jano, Dokumenty, projekt.py. 
# Vytlačte ich ako jednu cestu, pričom ako oddeľovač použijete lomku /.

# print("C:","Users","Jano","Documenty","projekt.py", sep="/")

# -------------------------------------------------------------
# Cieľ: Kreatívne skombinovať parametre end a sep.
# Zadanie: Vytlačte čísla od 1 do 5. 
# Medzi každým číslom má byť bodka a medzera. 
# Na konci celého výpisu majú byť tri bodky.
# 1. 2. 3. 4. 5...
# print(1,2,3,4,5, sep=". ", end="... ")



# -------------------------------------------------------------
# Použite násobenie reťazcov na vytvorenie dynamického rámčeka.
# Vytvorte premennú hlaska = "Dôležitá správa". 
# Vytlačte túto správu do konzoly tak, aby bola orámovaná hviezdičkami. 
# Rámček by sa mal prispôsobiť dĺžke textu.

# Očakávaný výstup:

# ************************
# * Moja Dôležitá správa *
# ************************

# hlaska = "Moja Dôležitá správa"

# print("*" * (len(hlaska) + 4 ))
# print("* " + hlaska + " *")
# print("*" * (len(hlaska) + 4 ))


# ----------------------- ULOHA KALKULCK -----------------------
# Program sa opýta používateľa na dĺžku strany štvorca v centimetroch. 
# Následne vypočíta a vypíše jeho obvod a obsah.


print()