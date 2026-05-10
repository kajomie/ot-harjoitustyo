# Muistikorttisovellus  

Muistikorttisovelluksessa käyttäjä voi tunnuksen tehtyään ja sisäänkirjauduttuaan tehdä omia muistikortteja (_flashcard_) ja käyttää niitä opiskelunsa tukena. Sovelluksessa voi lisäksi selata aiemmin tekemiään kortteja ja esimerkiksi suodattaa niitä niiden pakan mukaan.  

## Dokumentaation linkit  
[vaatimusmaarittely.md](https://github.com/kajomie/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)  
[tyoaikakirjanpito.md](https://github.com/kajomie/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)  
[changelog.md](https://github.com/kajomie/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)  
[ohje.md](https://github.com/kajomie/ot-harjoitustyo/blob/main/dokumentaatio/ohje.md)  
[arkkitehtuuri.md](https://github.com/kajomie/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)  
[testausdokumentti.md](https://github.com/kajomie/ot-harjoitustyo/blob/main/dokumentaatio/testausdokumentti.md)  
</br>

## Releaset   
[Viikko 5](https://github.com/kajomie/ot-harjoitustyo/releases/tag/viikko5)  
[Viikko 6](https://github.com/kajomie/ot-harjoitustyo/releases/tag/viikko6)  
[Loppupalautus](https://github.com/kajomie/ot-harjoitustyo/releases/tag/loppupalautus)  
</br>

## Käynnistys  
Poetry saadaan asennettua komennolla:  
poetry install  
</br>
Tietokanta voidaan alustaa suorittamalla:  
poetry run invoke build  
</br>
Tietokanta voidaan myös alustaa komentoriviltä:  
python3 src/initialize_database.py  
</br>
Sovellus voidaan sitten käynnistää seuraavasti:  
poetry run invoke start  
</br>

## Testaus  
Ohjelman testit saadaan tehtyä suorittamalla:  
poetry run invoke test  
</br>
Testikattavuusraportti saadaan seuraavasti:  
poetry run invoke coverage-report  
</br>

## Pylint  
Pylint-tarkastus voidaan tehdä suorittamalla:  
poetry run invoke lint  
</br>