from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ScrapClass import Scraping
import selenium

districts = {
    "Adana": ['ALADAĞ', 'CEYHAN', 'ÇUKUROVA', 'FEKE', 'İMAMOĞLU', 'KARAİSALI', 'KARATAŞ', 'KOZAN', 'POZANTI', 'SAİMBEYLİ', 'SARIÇAM', 'SEYHAN', 'TUFANBEYLİ', 'YUMURTALIK', 'YÜREĞİR'],
    "Adıyaman": ['BESNİ', 'ÇELİKHAN', 'GERGER', 'GÖLBAŞI', 'KAHTA', 'MERKEZ', 'SAMSAT', 'SİNCİK', 'TUT'],
    "AfyonKarahisar": ['BAŞMAKÇI', 'BAYAT', 'BOLVADİN', 'ÇAY', 'ÇOBANLAR', 'DAZKIRI', 'DİNAR', 'EMİRDAĞ', 'EVCİLER', 'HOCALAR', 'İHSANİYE', 'İSCEHİSAR', 'KIZILÖREN', 'MERKEZ', 'SANDIKLI', 'SİNANPAŞA', 'SULTANDAĞI', 'ŞUHUT'],
    "Ağrı": ["Merkez", "Diyadin","Doğubayazıt","Eleşkirt","Hamur","Patnos","Taşlıçay", "Tutak"],
    "Aksaray":['AĞAÇÖREN', 'ESKİL', 'GÜLAĞAÇ', 'GÜZELYURT', 'MERKEZ', 'ORTAKÖY', 'SARIYAHŞİ', 'SULTANHANI'],
    "Amasya" : "GÖYNÜCEK, GÜMÜŞHACIKÖY, HAMAMÖZÜ, MERKEZ, MERZİFON, SULUOVA, TAŞOVA".replace(" ", "").split(","),
    "Ankara": "AKYURT, ALTINDAĞ, AYAŞ, BALA, BEYPAZARI, ÇAMLIDERE, ÇANKAYA, ÇUBUK, ELMADAĞ, ETİMESGUT, EVREN, GÖLBAŞI, GÜDÜL, HAYMANA, KAHRAMANKAZAN, KALECİK, KEÇİÖREN, KIZILCAHAMAM, MAMAK, NALLIHAN, POLATLI, PURSAKLAR, SİNCAN, ŞEREFLİKOÇHİSAR, YENİMAHALLE".replace(" ", "").split(","),
"Antalya": "AKSEKİ, AKSU, ALANYA, DEMRE, DÖŞEMEALTI, ELMALI, FİNİKE, GAZİPAŞA, GÜNDOĞMUŞ, İBRADI, KAŞ, KEMER, KEPEZ, KONYAALTI, KORKUTELİ, KUMLUCA, MANAVGAT, MURATPAŞA, SERİK".replace(" ", "").split(","),
"Ardahan": "ÇILDIR, DAMAL, GÖLE, HANAK, MERKEZ, POSOF".replace(" ", "").split(","),
"Artvin": "ARDANUÇ, ARHAVİ, BORÇKA, HOPA, KEMALPAŞA, MERKEZ, MURGUL, ŞAVŞAT, YUSUFELİ".replace(" ", "").split(","),
"Aydın": "BOZDOĞAN, BUHARKENT, ÇİNE, DİDİM, EFELER, GERMENCİK, İNCİRLİOVA, KARACASU, KARPUZLU, KOÇARLI, KÖŞK, KUŞADASI, KUYUCAK, NAZİLLİ, SÖKE, SULTANHİSAR, YENİPAZAR".replace(" ", "").split(","),
"Balıkesir": "ALTIEYLÜL, AYVALIK, BALYA, BANDIRMA, BİGADİÇ, BURHANİYE, DURSUNBEY, EDREMİT, ERDEK, GÖMEÇ, GÖNEN, HAVRAN, İVRİNDİ, KARESİ, KEPSUT, MANYAS, MARMARA, SAVAŞTEPE, SINDIRGI, SUSURLUK".replace(" ", "").split(","),
"Bartın": "AMASRA, KURUCAŞİLE, MERKEZ, ULUS".replace(" ", "").split(","),
"Batman": "BEŞİRİ, GERCÜŞ, HASANKEYF, KOZLUK, MERKEZ, SASON".replace(" ", "").split(","),
"Bayburt": "AYDINTEPE, DEMİRÖZÜ, MERKEZ".replace(" ", "").split(","),
"Bilecik": "BOZÜYÜK, GÖLPAZARI, İNHİSAR, MERKEZ, OSMANELİ, PAZARYERİ, SÖĞÜT, YENİPAZAR".replace(" ", "").split(","),
"Bingöl": "ADAKLI, GENÇ, KARLIOVA, KİĞI, MERKEZ, SOLHAN, YAYLADERE, YEDİSU".replace(" ", "").split(","),
"Bitlis": "ADİLCEVAZ, AHLAT, GÜROYMAK, HİZAN, MERKEZ, MUTKİ, TATVAN".replace(" ", "").split(","),
"Bolu": "DÖRTDİVAN, GEREDE, GÖYNÜK, KIBRISCIK, MENGEN, MERKEZ, MUDURNU, SEBEN, YENİÇAĞA".replace(" ", "").split(","),
"Burdur": "AĞLASUN, ALTINYAYLA, BUCAK, ÇAVDIR, ÇELTİKÇİ, GÖLHİSAR, KARAMANLI, KEMER, MERKEZ, TEFENNİ, YEŞİLOVA".replace(" ", "").split(","),
"Bursa": "BÜYÜKORHAN, GEMLİK, GÜRSU, HARMANCIK, İNEGÖL, İZNİK, KARACABEY, KELES, KESTEL, MUDANYA, MUSTAFAKEMALPAŞA, NİLÜFER, ORHANELİ, ORHANGAZİ, OSMANGAZİ, YENİŞEHİR, YILDIRIM".replace(" ", "").split(","),
"Çanakkale": "AYVACIK, BAYRAMİÇ, BİGA, BOZCAADA, ÇAN, ECEABAT, EZİNE, GELİBOLU, GÖKÇEADA, LAPSEKİ, MERKEZ, YENİCE".replace(" ", "").split(","),
"Çorum": "ALACA, BAYAT, BOĞAZKALE, DODURGA, İSKİLİP, KARGI, LAÇİN, MECİTÖZÜ, MERKEZ, OĞUZLAR, ORTAKÖY, OSMANCIK, SUNGURLU, UĞURLUDAĞ".replace(" ", "").split(","),
"Çankırı": "ATKARACALAR, BAYRAMÖREN, ÇERKEŞ, ELDİVAN, ILGAZ, KIZILIRMAK, KORGUN, KURŞUNLU, MERKEZ, ORTA, ŞABANÖZÜ, YAPRAKLI".replace(" ", "").split(","),
"Denizli": "ACIPAYAM, BABADAĞ, BAKLAN, BEKİLLİ, BEYAĞAÇ, BOZKURT, BULDAN, ÇAL, ÇAMELİ, ÇARDAK, ÇİVRİL, GÜNEY, HONAZ, KALE, MERKEZEFENDİ, PAMUKKALE, SARAYKÖY, SERİNHİSAR, TAVAS".replace(" ", "").split(","),
"Diyarbakır": "BAĞLAR, BİSMİL, ÇERMİK, ÇINAR, ÇÜNGÜŞ, DİCLE, EĞİL, ERGANİ, HANİ, HAZRO, KAYAPINAR, KOCAKÖY, KULP, LİCE, SİLVAN, SUR, YENİŞEHİR".replace(" ", "").split(","),
"Düzce": "AKÇAKOCA, CUMAYERİ, ÇİLİMLİ, GÖLYAKA, GÜMÜŞOVA, KAYNAŞLI, MERKEZ, YIĞILCA".replace(" ", "").split(","),
"Edirne": "ENEZ, HAVSA, İPSALA, KEŞAN, LALAPAŞA, MERİÇ, MERKEZ, SÜLOĞLU, UZUNKÖPRÜ".replace(" ", "").split(","),
"Elazığ": "AĞIN, ALACAKAYA, ARICAK, BASKİL, KARAKOÇAN, KEBAN, KOVANCILAR, MADEN, MERKEZ, PALU, SİVRİCE".replace(" ", "").split(","),
"Erzincan": "ÇAYIRLI, İLİÇ, KEMAH, KEMALİYE, MERKEZ, OTLUKBELİ, REFAHİYE, TERCAN, ÜZÜMLÜ".replace(" ", "").split(","),
"Erzurum": "AŞKALE, AZİZİYE, ÇAT, HINIS, HORASAN, İSPİR, KARAÇOBAN, KARAYAZI, KÖPRÜKÖY, NARMAN, OLTU, OLUR, PALANDÖKEN, PASİNLER, PAZARYOLU, ŞENKAYA, TEKMAN, TORTUM, UZUNDERE, YAKUTİYE".replace(" ", "").split(","),
"Eskişehir": "ALPU, BEYLİKOVA, ÇİFTELER, GÜNYÜZÜ, HAN, İNÖNÜ, MAHMUDİYE, MİHALGAZİ, MİHALIÇÇIK, ODUNPAZARI, SARICAKAYA, SEYİTGAZİ, SİVRİHİSAR, TEPEBAŞI".replace(" ", "").split(","),
"Gaziantep": "ARABAN, İSLAHİYE, KARKAMIŞ, NİZİP, NURDAĞI, OĞUZELİ, ŞAHİNBEY, ŞEHİTKAMİL, YAVUZELİ".replace(" ", "").split(","),
"Giresun": "ALUCRA, BULANCAK, ÇAMOLUK, ÇANAKÇI, DERELİ, DOĞANKENT, ESPİYE, EYNESİL, GÖRELE, GÜCE, KEŞAP, MERKEZ, PİRAZİZ, ŞEBİNKARAHİSAR, TİREBOLU, YAĞLIDERE".replace(" ", "").split(","),
"Gümüşhane": "KELKİT, KÖSE, KÜRTÜN, MERKEZ, ŞİRAN, TORUL".replace(" ", "").split(","),
"Hakkari": " ÇUKURCA, DERECİK, MERKEZ, ŞEMDİNLİ, YÜKSEKOVA".replace(" ", "").split(","),
"Hatay": "ALTINÖZÜ, ANTAKYA, ARSUZ, BELEN, DEFNE, DÖRTYOL, ERZİN, HASSA, İSKENDERUN, KIRIKHAN, KUMLU, PAYAS, REYHANLI, SAMANDAĞ, YAYLADAĞI".replace(" ", "").split(","),
"Iğdır": "ARALIK, KARAKOYUNLU, MERKEZ, TUZLUCA".replace(" ", "").split(","),
"Isparta": "AKSU, ATABEY, EĞİRDİR, GELENDOST, GÖNEN, KEÇİBORLU, MERKEZ, SENİRKENT, SÜTÇÜLER, ŞARKİKARAAĞAÇ, ULUBORLU, YALVAÇ, YENİŞARBADEMLİ".replace(" ", "").split(","),
"İstanbul": "ADALAR, ARNAVUTKÖY, ATAŞEHİR, AVCILAR, BAĞCILAR, BAHÇELİEVLER, BAKIRKÖY, BAŞAKŞEHİR, BAYRAMPAŞA, BEŞİKTAŞ, BEYKOZ, BEYLİKDÜZÜ, BEYOĞLU, BÜYÜKÇEKMECE, ÇATALCA, ÇEKMEKÖY, ESENLER, ESENYURT, EYÜPSULTAN, FATİH, GAZİOSMANPAŞA, GÜNGÖREN, KADIKÖY, KAĞITHANE, KARTAL, KÜÇÜKÇEKMECE, MALTEPE, PENDİK, SANCAKTEPE, SARIYER, SİLİVRİ, SULTANBEYLİ, SULTANGAZİ, ŞİLE, ŞİŞLİ, TUZLA, ÜMRANİYE, ÜSKÜDAR, ZEYTİNBURNU".replace(" ", "").split(","),
"İzmir": " ALİAĞA, BALÇOVA, BAYINDIR, BAYRAKLI, BERGAMA, BEYDAĞ, BORNOVA, BUCA, ÇEŞME, ÇİĞLİ, DİKİLİ, FOÇA, GAZİEMİR, GÜZELBAHÇE, KARABAĞLAR, KARABURUN, KARŞIYAKA, KEMALPAŞA, KINIK, KİRAZ, KONAK, MENDERES, MENEMEN, NARLIDERE, ÖDEMİŞ, SEFERİHİSAR, SELÇUK, TİRE, TORBALI, URLA".replace(" ", "").split(","),
"Kahramanmaraş": "AFŞİN, ANDIRIN, ÇAĞLAYANCERİT, DULKADİROĞLU, EKİNÖZÜ, ELBİSTAN, GÖKSUN, NURHAK, ONİKİŞUBAT, PAZARCIK, TÜRKOĞLU".replace(" ", "").split(","),
"Karabük": "EFLANİ, ESKİPAZAR, MERKEZ, OVACIK, SAFRANBOLU, YENİCE".replace(" ", "").split(","),
"Karaman": "YRANCI, BAŞYAYLA, ERMENEK, KAZIMKARABEKİR, MERKEZ, SARIVELİLER".replace(" ", "").split(","),
"Kars": "AKYAKA, ARPAÇAY, DİGOR, KAĞIZMAN, MERKEZ, SARIKAMIŞ, SELİM, SUSUZ".replace(" ", "").split(","),
"Kastamonu": "ABANA, AĞLI, ARAÇ, AZDAVAY, BOZKURT, CİDE, ÇATALZEYTİN, DADAY, DEVREKANİ, DOĞANYURT, HANÖNÜ, İHSANGAZİ, İNEBOLU, KÜRE, MERKEZ, PINARBAŞI, SEYDİLER, ŞENPAZAR, TAŞKÖPRÜ, TOSYA".replace(" ", "").split(","),
"Kayseri": "AKKIŞLA, BÜNYAN, DEVELİ, FELAHİYE, HACILAR, İNCESU, KOCASİNAN, MELİKGAZİ, ÖZVATAN, PINARBAŞI, SARIOĞLAN, SARIZ, TALAS, TOMARZA, YAHYALI, YEŞİLHİSAR".replace(" ", "").split(","),
"Kırıkkale": " BAHŞILI, BALIŞEYH, ÇELEBİ, DELİCE, KARAKEÇİLİ, KESKİN, MERKEZ, SULAKYURT, YAHŞİHAN".replace(" ", "").split(","),
"Kırklareli": "BABAESKİ, DEMİRKÖY, KOFÇAZ, LÜLEBURGAZ, MERKEZ, PEHLİVANKÖY, PINARHİSAR, VİZE".replace(" ", "").split(","),
"Kırşehir": "KÇAKENT, AKPINAR, BOZTEPE, ÇİÇEKDAĞI, KAMAN, MERKEZ, MUCUR".replace(" ", "").split(","),
"Kilis": "ELBEYLİ, MERKEZ, MUSABEYLİ, POLATELİ".replace(" ", "").split(","),
"Kocaeli": "BAŞİSKELE, ÇAYIROVA, DARICA, DERİNCE, DİLOVASI, GEBZE, GÖLCÜK, İZMİT, KANDIRA, KARAMÜRSEL, KARTEPE, KÖRFEZ".replace(" ", "").split(","),
"Konya": "AHIRLI, AKÖREN, AKŞEHİR, ALTINEKİN, BEYŞEHİR, BOZKIR, CİHANBEYLİ, ÇELTİK, ÇUMRA, DERBENT, DEREBUCAK, DOĞANHİSAR, EMİRGAZİ, EREĞLİ, GÜNEYSINIR, HADİM, HALKAPINAR, HÜYÜK, ILGIN, KADINHANI, KARAPINAR, KARATAY, KULU, MERAM, SARAYÖNÜ, SELÇUKLU, SEYDİŞEHİR, TAŞKENT, TUZLUKÇU, YALIHÜYÜK, YUNAK".replace(" ", "").split(","),
"Kütahya": "ALTINTAŞ, ASLANAPA, ÇAVDARHİSAR, DOMANİÇ, DUMLUPINAR, EMET, GEDİZ, HİSARCIK, MERKEZ, PAZARLAR, SİMAV, ŞAPHANE, TAVŞANLI".replace(" ", "").split(","),
"Malatya": "AKÇADAĞ, ARAPGİR, ARGUVAN, BATTALGAZİ, DARENDE, DOĞANŞEHİR, DOĞANYOL, HEKİMHAN, KALE, KULUNCAK, PÜTÜRGE, YAZIHAN, YEŞİLYURT".replace(" ", "").split(","),
"Manisa": "AHMETLİ, AKHİSAR, ALAŞEHİR, DEMİRCİ, GÖLMARMARA, GÖRDES, KIRKAĞAÇ, KÖPRÜBAŞI, KULA, SALİHLİ, SARIGÖL, SARUHANLI, SELENDİ, SOMA, ŞEHZADELER, TURGUTLU, YUNUSEMRE".replace(" ", "").split(","),
"Mardin": "ARTUKLU, DARGEÇİT, DERİK, KIZILTEPE, MAZIDAĞI, MİDYAT, NUSAYBİN, ÖMERLİ, SAVUR, YEŞİLLİ".replace(" ", "").split(","),
    "Mersin": "AKDENİZ, ANAMUR, AYDINCIK, BOZYAZI, ÇAMLIYAYLA, ERDEMLİ, GÜLNAR, MEZİTLİ, MUT, SİLİFKE, TARSUS, TOROSLAR, YENİŞEHİR".replace(" ", "").split(","),
    "Muğla": "BODRUM, DALAMAN, DATÇA, FETHİYE, KAVAKLIDERE, KÖYCEĞİZ, MARMARİS, MENTEŞE, MİLAS, ORTACA, SEYDİKEMER, ULA, YATAĞAN".replace(" ", "").split(","),
    "Muş": " BULANIK, HASKÖY, KORKUT, MALAZGİRT, MERKEZ, VARTO".replace(" ", "").split(","),
    "Nevşehir": "ACIGÖL, AVANOS, DERİNKUYU, GÜLŞEHİR, HACIBEKTAŞ, KOZAKLI, MERKEZ, ÜRGÜP".replace(" ", "").split(","),
    "Niğde": "ALTUNHİSAR, BOR, ÇAMARDI, ÇİFTLİK, MERKEZ, ULUKIŞLA".replace(" ", "").split(","),
    "Ordu": "AKKUŞ, ALTINORDU, AYBASTI, ÇAMAŞ, ÇATALPINAR, ÇAYBAŞI, FATSA, GÖLKÖY, GÜLYALI, GÜRGENTEPE, İKİZCE, KABADÜZ, KABATAŞ, KORGAN, KUMRU, MESUDİYE, PERŞEMBE, ULUBEY, ÜNYE".replace(" ", "").split(","),
    "Osmaniye": "BAHÇE, DÜZİÇİ, HASANBEYLİ, KADİRLİ, MERKEZ, SUMBAS, TOPRAKKALE".replace(" ", "").split(","),
    "Rize": "ARDEŞEN, ÇAMLIHEMŞİN, ÇAYELİ, DEREPAZARI, FINDIKLI, GÜNEYSU, HEMŞİN, İKİZDERE, İYİDERE, KALKANDERE, MERKEZ, PAZAR".replace(" ", "").split(","),
    "Sakarya": "ADAPAZARI, AKYAZI, ARİFİYE, ERENLER, FERİZLİ, GEYVE, HENDEK, KARAPÜRÇEK, KARASU, KAYNARCA, KOCAALİ, PAMUKOVA, SAPANCA, SERDİVAN, SÖĞÜTLÜ, TARAKLI".replace(" ", "").split(","),
    "Samsun": "19 MAYIS,ALAÇAM,ASARCIK,ATAKUM,AYVACIK,BAFRA,CANİK,ÇARŞAMBA,HAVZA,İLKADIM,KAVAK,LADİK,SALIPAZARI,TEKKEKÖY,TERME,VEZİRKÖPRÜ, YAKAKENT".split(","),
    "Siirt": "BAYKAN, ERUH, KURTALAN, MERKEZ, PERVARİ, ŞİRVAN, TİLLO".replace(" ", "").split(","),
    "Sinop": "AYANCIK, BOYABAT, DİKMEN, DURAĞAN, ERFELEK, GERZE, MERKEZ, SARAYDÜZÜ, TÜRKELİ".replace(" ", "").split(","),
    "Sivas": "AKINCILAR, ALTINYAYLA, DİVRİĞİ, DOĞANŞAR, GEMEREK, GÖLOVA, GÜRÜN, HAFİK, İMRANLI, KANGAL, KOYULHİSAR, MERKEZ, SUŞEHRİ, ŞARKIŞLA, ULAŞ, YILDIZELİ, ZARA".replace(" ", "").split(","),
    "Şanlıurfa": "AKÇAKALE, BİRECİK, BOZOVA, CEYLANPINAR, EYYÜBİYE, HALFETİ, HALİLİYE, HARRAN, HİLVAN, KARAKÖPRÜ, SİVEREK, SURUÇ, VİRANŞEHİR".replace(" ", "").split(","),
    "Şırnak": "BEYTÜŞŞEBAP, CİZRE, GÜÇLÜKONAK, İDİL, MERKEZ, SİLOPİ, ULUDERE".replace(" ", "").split(","),
"Tekirdağ": "ÇERKEZKÖY, ÇORLU, ERGENE, HAYRABOLU, KAPAKLI, MALKARA, MARMARAEREĞLİSİ, MURATLI, SARAY, SÜLEYMANPAŞA, ŞARKÖY".replace(" ", "").split(","),
    "Tokat": "ALMUS, ARTOVA, BAŞÇİFTLİK, ERBAA, MERKEZ, NİKSAR, PAZAR, REŞADİYE, SULUSARAY, TURHAL, YEŞİLYURT, ZİLE".replace(" ", "").split(","),
    "Trabzon": "AKÇAABAT, ARAKLI, ARSİN, BEŞİKDÜZÜ, ÇARŞIBAŞI, ÇAYKARA, DERNEKPAZARI, DÜZKÖY, HAYRAT, KÖPRÜBAŞI, MAÇKA, OF, ORTAHİSAR, SÜRMENE, ŞALPAZARI, TONYA, VAKFIKEBİR, YOMRA".replace(" ", "").split(","),
    "Tunceli": "ÇEMİŞGEZEK, HOZAT, MAZGİRT, MERKEZ, NAZIMİYE, OVACIK, PERTEK, PÜLÜMÜR".replace(" ", "").split(","),
    "Uşak": "BANAZ, EŞME, KARAHALLI, MERKEZ, SİVASLI, ULUBEY".replace(" ", "").split(","),
    "Van": "BAHÇESARAY, BAŞKALE, ÇALDIRAN, ÇATAK, EDREMİT, ERCİŞ, GEVAŞ, GÜRPINAR, İPEKYOLU, MURADİYE, ÖZALP, SARAY, TUŞBA".replace(" ", "").split(","),
    "Yalova": "ALTINOVA, ARMUTLU, ÇINARCIK, ÇİFTLİKKÖY, MERKEZ, TERMAL".replace(" ", "").split(","),
    "Yozgat": "AKDAĞMADENİ, AYDINCIK, BOĞAZLIYAN, ÇANDIR, ÇAYIRALAN, ÇEKEREK, KADIŞEHRİ, MERKEZ, SARAYKENT, SARIKAYA, SORGUN, ŞEFAATLİ, YENİFAKILI, YERKÖY".replace(" ", "").split(","),
    "Zonguldak": "ALAPLI, ÇAYCUMA, DEVREK, EREĞLİ, GÖKÇEBEY, KİLİMLİ, KOZLU, MERKEZ".replace(" ", "").split(","),

}


class ScrapData(object):

    def load_districts(self):
        city = self.city.currentText()
        self.district.clear()
        self.district.addItem("ALL")
        self.district.addItems(districts[city])

    def scrap_button(self):
        city = self.city.currentText().replace("İ","i").lower().replace("ı","i").replace("ü","u").replace("ö","o").replace("ş","s").replace("ğ","g").replace("ç","c").replace(" ","-").lower()
        district = self.district.currentText().replace("İ","i").lower().replace("ı","i").replace("ü","u").replace("ö","o").replace("ş","s").replace("ğ","g").replace("ç","c").replace(" ","-").lower()
        url = "https://www.sahibinden.com/satilik-daire/"
        if district != "all":
            url += city+"-"+district
        else:
            url += city
        program = Scraping(url,city)
        try:
            program.program()
        except selenium.common.exceptions.NoSuchWindowException:
            program.close_file()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(-10, -10, 821, 621))
        self.background.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));")
        self.background.setText("")
        self.background.setObjectName("background")
        self.city = QtWidgets.QComboBox(Form)
        self.city.setGeometry(QtCore.QRect(350, 180, 201, 30))
        self.city.setObjectName("city")
        city_list = ['Adana', 'Adıyaman', 'Afyonkarahisar', 'Ağrı', 'Aksaray', 'Amasya', 'Ankara', 'Antalya', 'Ardahan',
                     'Artvin', 'Aydın', 'Balıkesir', 'Bartın', 'Batman', 'Bayburt', 'Bilecik', 'Bingöl', 'Bitlis',
                     'Bolu',
                     'Burdur', 'Bursa', 'Çanakkale', 'Çankırı', 'Çorum', 'Denizli', 'Diyarbakır', 'Düzce', 'Edirne',
                     'Elazığ',
                     'Erzincan', 'Erzurum', 'Eskişehir', 'Gaziantep', 'Giresun', 'Gümüşhane', 'Hakkâri', 'Hatay',
                     'Iğdır',
                     'Isparta', 'istanbul', 'İzmir', 'Kahramanmaraş', 'Karabük', 'Karaman', 'Kars', 'Kastamonu',
                     'Kayseri',
                     'Kilis', 'Kırıkkale', 'Kırklareli', 'Kırşehir', 'Kocaeli', 'Konya', 'Kütahya', 'Malatya', 'Manisa',
                     'Mardin', 'Mersin', 'Muğla', 'Muş', 'Nevşehir', 'Niğde', 'Ordu',
                     'Osmaniye', 'Rize', 'Sakarya', 'Samsun', 'Şanlıurfa', 'Siirt', 'Sinop', 'Sivas', 'Şırnak',
                     'Tekirdağ',
                     'Tokat', 'Trabzon', 'Tunceli', 'Uşak', 'Van', 'Yalova', 'Yozgat', 'Zonguldak']
        self.city.addItems(city_list)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(220, 310, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.district = QtWidgets.QComboBox(Form)
        self.district.setGeometry(QtCore.QRect(350, 310, 201, 30))
        self.district.setObjectName("district")
        self.scrap_data_button = QtWidgets.QPushButton(Form)
        self.scrap_data_button.setGeometry(QtCore.QRect(330, 390, 160, 60))
        self.scrap_data_button.setStyleSheet("QPushButton{\n"
"font-size:18px;\n"
"border-radius:10px;\n"
"background:rgba(85, 98, 112, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,107,107,255);\n"
"}\n"
"")
        self.scrap_data_button.setObjectName("button1")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(330, 80, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.scrap_data_button.clicked.connect(self.scrap_button)
        self.load_district_button = QtWidgets.QPushButton(Form)
        self.load_district_button.setGeometry(QtCore.QRect(230, 250, 321, 21))
        self.load_district_button.setStyleSheet("QPushButton{\n"
"font-size:18px;\n"
"border-radius:10px;\n"
"background:rgba(85, 98, 112, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,107,107,255);\n"
"}\n"
"")
        self.load_district_button.setObjectName("button1_2")
        self.load_district_button.clicked.connect(self.load_districts)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Scrap Data", "Scrap Data"))
        self.label.setText(_translate("Form", "City"))
        self.label_2.setText(_translate("Form", "District"))
        self.scrap_data_button.setText(_translate("Form", "Scrap Data"))
        self.label_3.setText(_translate("Form", "Scrap Data"))
        self.load_district_button.setText(_translate("Form", "Load Districts"))
        Form.setWindowIcon(QIcon("logo.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ScrapData()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
