import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 30.0)

    def test_saldo_vahenee_oikein_kun_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(self.maksukortti.saldo_euroina(), 8.0)

    def test_saldo_ei_muutu_kun_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_metodi_palauttaa_true_jos_rahat_riittivat(self):
        tulos = self.maksukortti.ota_rahaa(200)
        self.assertEqual(True, tulos)

    def test_metodi_palauttaa_false_jos_rahat_eivat_riita(self):
        tulos = self.maksukortti.ota_rahaa(5000)
        self.assertEqual(False, tulos)
