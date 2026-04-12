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
</br>

## Ohjelman käyttäminen  
### Rekisteröityminen  
Käyttäjä voi tehdä uuden tunnuksen rekisteröitymissivulla. Hän voi syöttää haluamansa käyttäjänimen, salasanan sekä salasanan uudelleen. Kun hän painaa "luo tunnus", tunnus luodaan ja hänet ohjataan edelleen kirjautumissivulle.  