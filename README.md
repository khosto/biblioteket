# biblioteket.py 

Ett program för att lagra, sortera och söka objekt som böcker, filmer och musik.
Användaren behöver skapa en text fil som heter cd.txt innan programmet körs.
Programmet är provkört på https://repl.it/languages/python3. 

En beskrivning av hur programmet fungerar och vad den gör. 
Programmet består av fem funktioner och en main funktion. 
• En funktion för att registrera böcker, och räkna ut nuvarande värde. 
• En funktion för att registrera musik, och räkna ut nuvarande värde. 
• En funktion för att registrera film, och räkna ut nuvarande värde. 
• En funktion som söker i de olika text filerna efter det objekt som användaren önskar hitta. 
• En funktion som när användaren vill avsluta programmet sorterar de registrerade objekten i bokstavsordning.
• En main funktion som består av huvudmenyn och som kallar på de andra funktionerna.  

Användaren blir tillfrågad vad hen vill göra; registrera en bok, cd eller film eller söka i sortimentet. Användaren kan också avsluta programmet, då kommer alla filer automatiskt sorteras i bokstavsordning. Vid val av registrering återvänder användaren alltid tillbaka till huvudmenyn efter varje registrerat objekt.

Registrering:

Bok – Användaren blir tillfrågad titel, författare, antal sidor, inköpsår, inköpspris. Sedan räknar programmet ut det nuvarande värdet med hjälp av inköpsår och inköpspris. Böcker äldre än 50 år stiger 8 % i värde per år, annars sjunker värdet 10 % per år. 

Musik – Användaren blir tillfrågad titel, artist, antal låtar, lnköpsår, inköpspris. Programmet räknar också ut värdet på cd skivan beroende på hur ånga andra skivor med samma titel som finns. Inköpspriset delas med antalet skivor och avrundas till närmsta heltal. 

Film – Användaren blir tillfrågad titel, regissör, längd i minuter, inköpsår, inköpspris. Värdet beräknas beroende ålder och skick. Då användaren blir tillfrågad skicket på skivan 1-10, 10 är nyskick. För varje avdragen poäng och år i ålder sjunker värdet 10 %.

Söka:
Om användaren väljer att söka i biblioteket blir hen skickad till en ny meny där man kan välja att söka efter bok, cd eller film. När man valt kategori anger man titel på objektet, om programmet hittar ett objekt med titeln skriver den ut alla matchningar och all tillhörande info. 

Avsluta:
När användaren har registrerat och sökt klart, avslutar man programmet genom att skriva ’stop’ då sparas alla objekt i bokstavsordning.
