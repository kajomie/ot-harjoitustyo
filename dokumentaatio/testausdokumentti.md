# Testausdokumentti  

## Yksikkö- ja integraatiotestaus  
Yksikkö- ja integraatiotestaus on tehty Unittest-kirjaston avulla. Kaikkien luokkien kaikille metodeille on pyritty kirjoittamaan testit, kuten myös yleisimmille virhetilanteille kuten vaikkapa tyhjät syötteet.  
CardServicen testauksesta vastaa CardServiceTest-luokka. CardService käyttää apunaan luokkia UserRepositoryStub ja CardRepositoryStub, jotka simuloivat oikeiden repositorioiden toimintaa.  
UserRepositoryn testauksesta vastaa UserRepositoryTest-luokka ja edelleen CardRepositoryn testausta hoitaa CardRepositoryTest-luokka.  

## Testauskattavuus  
![Testauskattavuusraportti](/dokumentaatio/kuvat/testauskattavuus.png)  
Testauskattavuus on raportin mukaan 90%, ja se olisi mahdollisesti korkeampi mikäli build.py ja initialize_database.py jättäisi pois. Käyttöliittymä ja index.py on jätetty kokonaan pois coverage-raportista.  

## Järjestelmätestaus  
Testaus on tehty manuaalisesti, käyttäen Linux Ubuntua. Kaikkia sovelluksen tarjoamia toimintoja (käyttäjän luonti, sisäänkirjautuminen, uloskirjautuminen, kortin luonti, pakan luonti, kortin poisto, kortin muokkaus) on pyritty testaamaan käyttöliittymän kautta. Lisäksi on yritetty testata käyttöliittymän omien metodien toimivuutta, eli esimerkiksi sitä että korttien ja pakan listauksen päivitys toimii oikein eri tilanteissa. Testaus on tehty niin oikeilla kuin myös tyhjilläkin syötteillä.    

## Sovellukseen jääneet ongelmat  
- Testausta ei ole tehty Macilla tai Windowsilla.
- Tiedostot build.py ja initialize_database.py jäivät testaamatta.
- Mahdollisesti olisi voinut toteuttaa enemmän virheilmoituksia eri tilanteisiin.
- Tällä hetkellä testeissä käytetään oikeaa tietokantaa ja tietokantayhteyttä, eikä dotenv-kirjastoa ympäristömuuttujineen.