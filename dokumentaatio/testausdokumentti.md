# Testausdokumentti  

## Yksikkö- ja integraatiotestaus  
CardServicen testauksesta vastaa CardServiceTest-luokka. CardService käyttää luokkia UserRepositoryStub ja CardRepositoryStub, jotka simuloivat oikeiden repositorioiden toimintaa.  
UserRepositoryn testauksesta vastaa UserRepositoryTest-luokka ja vastaavasti CardRepositoryn testausta hoitaa CardRepositoryTest-luokka.  

## Testauskattavuus  

## Järjestelmätestaus  
Testaus on tehty käyttäen Linux Ubuntua.  

## Sovellukseen jääneet ongelmat  
- Testausta ei ole tehty Mac- tai Windows-ympäristöissä.
- Tällä hetkellä testeissä käytetään oikeaa tietokantaa, eikä dotenv-kirjastoa ympäristömuuttujineen.