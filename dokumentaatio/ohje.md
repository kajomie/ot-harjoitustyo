# Käyttöohje  
Sovelluksen uusin release voidaan ladata osiosta [Releases](https://github.com/kajomie/ot-harjoitustyo/releases) zip-tiedostona painamalla "Source code (zip)" ja purkamalla se haluamassaan sijainnissa.  

## Käynnistys  
Poetry voidaan asentaa seuraavasti:  
poetry install  
</br>
Tietokanta voidaan alustaa suorittamalla:  
poetry run invoke build  
</br>
Tai komentoriviltä seuraavasti:  
python3 src/initialize_database.py  
</br>
Sen jälkeen sovellus saadaan käynnistettyä:  
poetry run invoke start  
</br>

## Ohjelman käyttäminen  
### Rekisteröityminen  
Käyttäjä voi tehdä uuden tunnuksen rekisteröitymissivulla. Hän voi syöttää haluamansa käyttäjänimen, salasanan sekä salasanan uudelleen. Kun hän painaa "Luo tunnus" ja tunnuksen luonti onnistuu, tunnus luodaan ja hänet ohjataan edelleen kirjautumissivulle. Jos tunnusta ei kuitenkaan saatu luotua, käyttäjälle esitetään virheilmoitus pop-up-viestin muodossa.  

### Kirjautuminen sisään  
Kun tunnus on luotu, niin käyttäjä voi kirjautua sisään kirjautumissivulta. Kun käyttäjätunnus ja salasana on syötetty, niin painetaan "Kirjaudu sisään". Jos kirjautuminen sujuu onnistuneesti, niin käyttäjä ohjataan etusivulle. Jos kirjautuminen ei jostain syystä onnistu, käyttäjälle näytetään virheilmoitus ponnahdusikkunan avulla.  

### Korttien luominen  
Muistikortteja voi luoda etusivulla vasemmalla puolella sijaitsevalla "Luo uusi muistikortti"-lomakkeella. Käyttäjä kirjoittaa kysymyksen ja vastauksen kenttiin ja valitsee kortin pakan olemassaolevista pakoista. Painamalla "Luo uusi muistikortti" luodaan uusi kortti. Käyttäjälle esitetään pop-up-viesti, jos kortin luonti onnistui.  

### Pakkojen luominen  
Pakan luominen toimii etusivun vasemman puolen alakulman "Luo uusi pakka"-lomakkeella. Käyttäjä kirjoittaa pakan nimen ja painaa "Luo uusi pakka", joka luo uuden pakan. Käyttäjälle näytetään ponnahdusikkuna, kun pakan luonti onnistui.  

### Korttien selaaminen  
Kun käyttäjä painaa etusivulla nappia "Selaa kortteja", hänet ohjataan korttinäkymään. Vasemmalta löytyy pudotusvalikko, jossa luetellaan kaikki käyttäjän pakat, ja sen alapuolella lista korteista. Kun korttia painaa, se avautuu oikealle korttinäkymään.  
Ensin kortista näkyy pelkkä kysymys, ja kun painaa "Näytä vastaus"-nappia, sen alapuolelle ilmestyy vastaus. Kun painaa "Piilota vastaus"-nappia, vastaus piilotetaan uudelleen.  

### Kortin poistaminen  
Kun oikean alakulman "Poista kortti"-nappia painetaan, käyttäjälle ilmestyy ponnahdusikkuna, jossa varmistetaan, haluaako hän todella poistaa valitsemansa kortin. Jos käyttäjä painaa "Cancel", korttia ei poisteta. Jos hän painaa "Ok", kortti poistetaan, jolloin myös korttinäkymä tyhjenee ja korttilista päivittyy.   

### Kortin muokkaaminen  
Kun oikeassa alakulmassa olevaa "Muokkaa korttia"-nappia painaa, korttinäkymä muuttuu muokkaustilaan, ja kortissa olevaa kysymystä sekä vastausta voi muokata syöttämällä muokkaustilan kenttiin uudet tiedot. Jos käyttäjä painaa "Takaisin", hänet ohjataan takaisin korttinäkymään ja kortti pysyy samana. Jos käyttäjä taas painaa "Tallenna muutokset", kortin muutokset tallentuvat tietokantaan ja korttinäkymä sekä korttilista päivittyvät.  

### Korttien suodattaminen pakkojen avulla  
Kun pakat listaavasta pudotusvalikosta valitaan pakka, sen alapuolella sijaitseva korttilista muuttuu kyseisen pakan korteiksi. Valitsemalla "(Näytä kaikki kortit)" käyttäjä voi palata selaamaan kaikkien pakkojen kortteja.  

### Kirjautuminen ulos  
Etusivun oikeassa yläkulmassa on "Kirjaudu ulos"-nappi. Painamalla sitä käyttäjä kirjataan ulos sovelluksesta ja hänet ohjataan takaisin kirjautumissivulle.  