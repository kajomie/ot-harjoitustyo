import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luodun_kassapaatteen_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_luodun_kassapaatteen_lounaita_myyty_oikea_maara(self):
        myydytlounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(myydytlounaat, 0)

    def test_edulliset_kateismaksu_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihtoraha, 260)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.40)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaat_kateismaksu_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edulliset_kateismaksu_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_kateismaksu_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edulliset_korttimaksu_riittava(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(True, tulos)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.60)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_maukkaat_korttimaksu_riittava(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(True, tulos)
        self.assertEqual(self.maksukortti.saldo_euroina(), 6.0)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_edulliset_korttimaksu_ei_riita(self):
        kortti = Maksukortti(200)
        tulos = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(False, tulos)
        self.assertEqual(kortti.saldo_euroina(), 2.0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_maukkaat_korttimaksu_ei_riita(self):
        kortti = Maksukortti(300)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(False, tulos)
        self.assertEqual(kortti.saldo_euroina(), 3.0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kortin_saldo_muuttuu_kun_lataa_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 15.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1005.0)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)