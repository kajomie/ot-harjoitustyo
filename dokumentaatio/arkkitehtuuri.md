# Arkkitehtuuri  

![Sovelluksen pakkauskaavio](/dokumentaatio/kuvat/pakkauskaavio.png)  

## Rakenne  
Ohjelma pyrkii noudattamaan repository-suunnittelumallia. Sovellus on jaettu neljään osaan: **ui**, **classes**, **repositories** ja **application**. Ui-hakemistossa on käyttöliittymä, kun taas classes sisältää luokat, repositories vastaavasti repositoriot ja application sovelluslogiikan.  

## Käyttöliittymä  
Käyttöliittymässä on neljä eri näkymää, joista jokaisella on oma luokkansa. Ne ovat:  
- **RegisterView** eli rekisteröitymissivu.  
- **LoginView** eli kirjautumissivu.  
- **FrontPageView** eli etusivu johon käyttäjä ohjataan kirjautumisen jälkeen ja jossa voi valita erilaisia toimintoja kuten esim. muistikorttien luominen ja uuden pakan luominen.  
- **CardView** eli itse muistikortti, jossa on kaksi eri puolta eli kysymys ja vastaus. CardView'ssä käyttäjälle näytetään ensin kysymyspuoli ja painiketta painamalla voi nähdä vastauksen.  

## Sovelluslogiikka  
Sovelluksessa on kolme eri luokkaa:  
- **User**, joka vastaa sovelluksen käyttäjää. Käyttäjästä tallennetaan id, käyttäjänimi ja salasana.  
- **Card**, joka vastaa muistikorttia. Korteista tallennetaan id, kysymys, vastaus ja sen pakan id.   
- **Deck**, joka kuvaa pakkaa. Pakasta tallennetaan id, nimi ja sen luoneen käyttäjän id.  
Käyttäjä voi luoda monia muistikortteja, mutta kullakin muistikortilla voi olla vain 1 luoja eli siihen liittyvä käyttäjä. Käyttäjä voi luoda monta pakkaa. Pakassa on monta korttia, mutta kullakin kortilla voi olla vain 1 pakka.  

Luokka **CardService** sisältää sovelluslogiikan toiminnot, kuten rekisteröityminen ja kirjautuminen, ja se hyödyntää siinä repositorioita UserRepository ja CardRepository kutsumalla niiden metodeja.  

## Datan tallennus  
Repositoriot **UserRepository** ja **CardRepository** vastaavat käyttäjiin, kortteihin ja pakkoihin liittyvän datan tallennuksesta. Molemmat repositoriot tallentavat tietoa sqlite3:n avulla tietokantaan tauluihin users, cards ja decks. Tietokanta alustetaan initialize_database-tiedoston avulla.  

## Toiminnallisuus  
### Rekisteröityminen  
![Rekisteröitymisen sekvenssikaavio](/dokumentaatio/kuvat/sekvenssikaavio-register.png)  

Kun käyttäjä on rekisteröitymissivulla, hän voi valita käyttäjänimen ja salasanan. Jos käyttäjänimi on jo käytössä, niin siitä tulee virheilmoitus.  
Tapahtumankäsittelijä antaa CardServicen metodille create_new_user parametreina käyttäjänimen ja salasanan, joka edelleen kutsuu UserRepositoryn search_user ja sitten create_user-metodia, joka taas tallentaa tiedot tietokantaan. Mikäli käyttäjän luominen ei onnistu, niin käyttäjälle esitetään virheilmoitus.    
Kun käyttäjä on luotu onnistuneesti, hänet ohjataan kirjautumissivulle jossa hän voi kirjautua sisään uudella tunnuksellaan.  

### Sisään- ja uloskirjautuminen  
![Kirjautumisen sekvenssikaavio](/dokumentaatio/kuvat/sekvenssikaavio-login.png)  

Käyttäjä voi syöttää tunnuksen ja salasanan. Tapahtumankäsittelijä kutsuu CardServicen login-metodia, joka edelleen kutsuu UserRepositoryn check_login-metodia, joka taas etsii käyttäjän käyttäjänimen ja salasanan avulla tietokannasta. Jos käyttäjänimeä ja salasanaa vastaava käyttäjä löytyy tietokannasta, niin UserRepository palauttaa käyttäjän oliona CardServicelle. Käyttäjä kirjataan sisään ja sisäinen user-muuttuja muutetaan vastaamaan kyseistä käyttäjää. Jos kirjautuminen ei onnistu (esim. väärän tunnuksen tai salasanan takia), niin käyttäjä saa siitä virheilmoituksen.  
Kun kirjautuminen onnistuu, niin käyttäjä ohjataan etusivulle. Etusivun kautta voi valita suorittaa erilaisia sovelluksen tarjoamia toimintoja, kuten selata aiemmin luotuja muistikortteja tai tehdä uusia muistikortteja.  
Uloskirjautuminen toimii samoin tapahtumakäsittelijän kautta, joka taaskin kutsuu CardServicen logout-metodia. CardServicen sisäinen muuttuja user tyhjennetään ja käyttäjä ohjataan takaisin kirjautumissivulle.  

### Muistikortit  
Muistikorteilla on kaksi puolta, kysymys ja vastaus. Molemmat niistä annetaan korttia luodessa. Uudelle kortille valitaan myös sen pakka, joka tulee luoda ennen korttia. Muistikorttinäkymässä näytetään ensin kysymys, ja painiketta painamalla käyttäjä voi valita, milloin haluaa nähdä tai piilottaa vastauksen.  

#### Kortin luominen  
![Kortin luomisen sekvenssikaavio](/dokumentaatio/kuvat/sekvenssikaavio-card.png)  

Uutta korttia luodessa tapahtumankäsittelijä kutsuu CardServicen metodia uuden kortin luomiseen, joka edelleen ottaa yhteyttä CardRepositoryyn ja tallentaa tiedot tietokantaan. Kun kortti on luotu, niin käyttöliittymä näyttää tämän luodun kortin korttinäkymän. Pakan luominen toimii samalla tavalla.   

#### Kortin muokkaaminen  
![Kortin muokkaamisen sekvenssikaavio](/dokumentaatio/kuvat/sekvenssikaavio-card-edit.png)  

Korttia muokattaessa käyttöliittymä vaihtaa ensin näkymää tavallisesta korttinäkymästä muokkaustilaan, joka on erillinen tkinterin frame CardView-luokan sisällä. Sen jälkeen kutsutaan samoin käyttöliittymän kautta CardServicen edit_card-metodia, parametreinaan muokatut tiedot. CardService edelleen kutsuu CardRepositorya, joka muokkaa tietokantataulua halutun kortin osalta. CardRepository palauttaa muokatun kortin oliomuodossa CardServicelle, joka ottaa sen vastaan ja palauttaa sen edelleen käyttöliittymälle. Käyttöliittymä vaihtaa muokkausnäkymästä takaisin normaaliin korttinäkymään ja päivittää valittuna olleen kortin tiedot.  

#### Kortin poistaminen  
![Kortin poistamisen sekvenssikaavio](/dokumentaatio/kuvat/sekvenssikaavio-card-delete.png)  

Kortin poistossa käyttöliittymä kutsuu CardServicea parametrinaan card_id eli poistettavan kortin id. CardService kutsuu CardRepositorya, joka etsii kortin sen id:n avulla tietokannasta ja poistaa sen. Sen jälkeen käyttöliittymä hakee toisen metodinsa (joko get_cards tai get_deck_cards, riippuen siitä oliko pakkaa valittuna) kautta uudestaan korttilistan. Kummatkin metodit toimivat samoin kuin ylempänäkin olevat eli (UI -> CardService -> CardRepository -> CardService -> UI). Korttilistaus päivittyy, jolloin kortti on poistunut korttilistauksesta.  

## Sovelluksen heikkoudet  
- Alustavasta vaatimusmäärittelydokumentistä jäi toteuttamatta pakkojen poisto. Samoin kortin muokkaukseen olisi voinut lisätä pakan vaihdon, kun nyt siinä voi muokata vain kortin kysymystä ja vastausta.  
- Pylint-virheitä jäi vähän liikaa, sillä ilmeisesti se ei pidä siitä, että monen luokan id-muuttujan nimi on nimenomaan id. En kuitenkaan tiennyt, onko sallittua laittaa se ignooraamaan tuo, joten jätin sen vain tuollaiseksi. Pylint jäi myös valittamaan liian monesta parametrista, mutta en tiedä, saanko refaktoroitua niitä mitenkään järkevästi pois (ainakaan esim. Card-luokassa), joten nekin saivat jäädä siihen.  
- Korttinäkymää CardView olisi voinut ehkä jakaa osiin, sillä se kasvoi aika suureksi, ja lisäksi sen (kuten muidenkin näkymäsivujen sekä testiluokkien) koodia olisi ehkä muutenkin refaktoroida paremmaksi.  
- Sovellus käyttää testaamiseen oikeaa tietokantaa eikä testitietokantaa.  