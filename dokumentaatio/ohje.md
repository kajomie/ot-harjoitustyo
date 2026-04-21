# Käyttöohje  

## Käynnistys  
Poetry voidaan asentaa seuraavasti:  
poetry install  
</br>
Tietokanta voidaan alustaa komentoriviltä:  
python3 src/initialize_database.py  
</br>
Sen jälkeen sovellus saadaan käynnistettyä:  
poetry run invoke start  
</br>

## Ohjelman käyttäminen  
### Rekisteröityminen  
Käyttäjä voi tehdä uuden tunnuksen rekisteröitymissivulla. Hän voi syöttää haluamansa käyttäjänimen, salasanan sekä salasanan uudelleen. Kun hän painaa "Luo tunnus", tunnus luodaan ja hänet ohjataan edelleen kirjautumissivulle.  

### Kirjautuminen sisään  
Kun tunnus on luotu, niin käyttäjä voi kirjautua sisään kirjautumissivulta. Kun käyttäjätunnus ja salasana on syötetty, niin painetaan "Kirjaudu sisään". Jos kirjautuminen onnistuu, niin käyttäjä ohjataan etusivulle.  

### Muistikorttien luominen  
Muistikortteja voi luoda etusivulla vasemmalla puolella sijaitsevalla "Luo uusi muistikortti"-lomakkeella. Käyttäjä kirjoittaa kysymyksen ja vastauksen kenttiin. Painamalla "Luo uusi muistikortti" luodaan uusi kortti.  

### Kirjautuminen ulos  
Etusivun oikeassa yläkulmassa on "Kirjaudu ulos"-nappi. Painamalla sitä käyttäjä kirjataan ulos sovelluksesta ja ohjataan takaisin kirjautumissivulle.  