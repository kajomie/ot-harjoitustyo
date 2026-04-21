# Changelog  

## Viikko 3  
- Lisätty luokat User ja Card käyttäjille ja muistikorteille.  
- Lisätty repositoriot UserRepository ja CardRepository, jotka tallentavat käyttäjien ja korttien tiedot sqlite3:n avulla tietokantaan.  
- Aloitettu (hyvin alustava) käyttöliittymän alku, joka on sijoitettu omaan ui-hakemistoonsa.  
- Luotu tietokantayhteyksiä varten tiedostot initialize_database ja database_connection.  
- Tehty testi että käyttäjän luominen onnistuu UserRepositoryssä.  

## Viikko 4  
- Otettu Pylint käyttöön.  
- Tehty RegisterView ja LoginView eli uuden käyttäjän luomissivu sekä kirjautumissivu käyttöliittymään.  
- Tehty application-hakemisto ja sinne CardService.py sovelluslogiikkaa varten.    
- Tehty alustava käyttöohje.  
- Luotu FrontPageView eli etusivu, johon käyttäjä ohjataan kirjautumisen jälkeen.  
- Käyttäjä pystyy nyt luomaan uuden tunnuksen ja kirjautumaan sillä sisään.  
- Tehty testit että käyttäjän luominen onnistuu CardServicessä, kirjautuminen toimii, ja get_user palauttaa oikean käyttäjän.  
- Lisätty arkkitehtuuri.md ja sinne sovelluksen pakkauskaavio.  

## Viikko 5  
- Tehty virheilmoituksia LoginView'lle ja RegisterView'lle sekä testit niille.  
- Käyttäjä pystyy kirjautumaan ulos.  
- Tehty CardView korttinäkymää varten.  
- Käyttäjä voi nyt luoda omia muistikortteja.  
- Käyttäjä voi selata luomiaan kortteja.  
- Käyttäjä voi tarkastella yksittäistä korttia.  
- Lisätty arkkitehtuuri.md:hen sisäänkirjautumisen sekvenssikaavio.  