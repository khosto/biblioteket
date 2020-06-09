#Huvudmeny
def bok():
    böcker = open("bok.txt", "a")
    a = 1
#Funktionen börjar med en while loop 
    while a == 1:
        try:
            titel = input("Titel: ")
            författare = input("författare: ")
            sidor = int(input("antal sidor: "))
            inköpsår = int(input("inköpsår: "))    
            inköpspris = float(input("inköpspris:"))
            t = 2020 - inköpsår
#Kooden går vidare till variabler 
            if t < 50:
                värde = inköpspris * 0.9 ** t
            else:
                värde = inköpspris * 1.08 ** t
#här sparar vi alla variabler till text filen
            böcker.write((titel) + 'Författare:  ' + (författare)+ 'Antal sidor:  ' +str(sidor) + 'Inköpsåt:  ' +str(inköpsår)+ 'Inköpspris:  ' +str(inköpspris)+ 'Nuvarande värde:  '+ str(värde)+ '\n')
            böcker.close()
            a+=1
        except ValueError:
            print("Ogiltigt inmat, prova igen.")
            continue
#Musik funktionen är uppbyggd på exakt samma sätt som registreringen av böcker, med undantag att beräkningen av det nuvarande värdet är lite annorlunda
def cd():
    musik = open("cd.txt", "r+")
    a=1
    while a == 1:
        try:
            titel = input("Titel: ")
            artist = input("Artist: ")
            låtar = input("antal låtar: ")
            inköpsår = int(input("inköpsår: "))
            inköpspris = int(input("inköpspris:"))
            rad = 0
            skivor = ["a"]
                
            for line in musik:
                rad += 1
                if titel in line:
                    skivor.append((rad, line.rstrip()))
            antal = len(skivor)
            värde = round(inköpspris/antal)
            musik.write((titel)+'   Artist:  ' + (artist)+'  Antal låtar:  ' +str(låtar)+'  Inköpsår:  ' +str(inköpsår)+'  Inköpspris:   ' +str(inköpspris)+ '  Nuvarande värde:  '+str(värde)+"\n")
            a += 1  


        except ValueError:
            print("Ogiltigt inmat, prova igen")
            continue


def film():
    filmer = open("film.txt", "a")
    a =1
    while a == 1:
        try:
            titel = input("Titel: ")
            regisör = input("Regisör: ")
            tid = input("antal minuter lång: ")
            inköpsår = int(input("inköpsår: "))
            inköpspris = float(input("inköpspris:"))
            skick = int(input("Ange filmens skick 1-10, 10 är nyskick."))
            t = 2020 - inköpsår
            värdet = inköpspris*0.9**t
            a = skick / 10
            värde = värdet * a
            filmer.write((titel)+'Reg: ' + (regisör)+'Tid i min:  ' +str(tid)+'INköpsår:  ' +str(inköpsår)+'Inköpspris:  ' +str(inköpspris)+'Nuvarande värde:  '+ str(värde)+ "\n")
            a+=1
        except ValueError:
            print("ogiltigt svar, prova igen.")
            continue

#Tog hjälp av:
#https://thispointer.com/python-search-strings-in-a-file-and-get-line-numbers-of-lines-containing-the-string/
def söka():
    b = 1
    while b == 1:
        vad = input("Vad vill du leta efter(bok, cd, film)? Skriv 'stop' för att återgå till huvud meny.  ")
        if vad.lower() == 'bok':
            rad = 0
            söksvar = []
            böcker = open('bok.txt', 'r')
            namn1 = input("Ange bokens titel: ")
            for line in böcker:
                rad += 1
                if namn1 in line:
                    söksvar.append((rad, line.rstrip()))  
                    for i in söksvar:
                        print(i) 
        elif vad.lower() == 'cd':
            rad = 0
            söksvar = []
            musik = open("cd.txt", "r")
            namn2 = input("Ange skivans titel: ")
            for line in musik:
                rad += 1
                if namn2 in line:
                    söksvar.append((rad, line.rstrip()))         
                    print(söksvar)

        elif vad.lower() == 'film':
            rad = 0
            söksvar = []
            filmer = open("film.txt", "r")
            namn3 = input("Ange filmens titel: ")
            for line in filmer:
                rad += 1
                if namn3 in line: 
                    söksvar.append((rad, line.rstrip()))     
                    print(söksvar)
        
        elif vad.lower() == 'stop':
            b+=1

        else:
            print('ogiltigt svar!')
            continue 

#https://www.youtube.com/watch?v=T8UTagpN2mc&fbclid=IwAR0qO5FPr7di86ZlnEO2w-u6260_T5yN7S9bDN2KMD3zhvltjcw-KKMY3YE
def sortera():
    sortera = list()
    böcker = 'bok.txt'
    with open (böcker) as bk:
        for line in bk:
            sortera.append(line.strip())
    sortera.sort()
    böcker = 'bok1.txt'
    with open (böcker, 'w') as bc:
        for sorterat in sortera:
            bc.write((sorterat) + '\n')          

    sortera1 = list()
    musik = 'cd.txt'
    with open (musik) as cd:
        for line in cd:
            sortera1.append(line.strip())
    sortera1.sort()
    musik = 'cd1.txt'
    with open (musik, 'w') as cds:
        for sorterat1 in sortera1:
            cds.write((sorterat1) + '\n') 

    sortera2 = list()
    filmer = 'film.txt'
    with open (filmer) as film:
        for line in film:
            sortera2.append(line.strip())
    sortera2.sort()
    filmer = 'film1.txt'
    with open (filmer, 'w') as f:
        for sorterat2 in sortera2:
            f.write((sorterat2) + '\n') 


def main():
    a = 1
    while a == 1: 
        reg = input("vad vill du registrera (bok, cd, film) eller skriv 'stop' för att avsluta 'sök' för att söka i bibloteket: ")
        if reg.lower() == 'bok':
            bok()       
        elif reg.lower() == 'cd':
            cd()
        elif reg.lower() == 'film':
            film()
        elif reg.lower() == 'stop':
            sortera()
            a+=1 
        elif reg.lower() == 'sök':
            söka()
        else:
            print("ogiltigt svar!")
            continue


main()