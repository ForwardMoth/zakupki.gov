passwd = "test"
database = "test_notice"


all_regions = ["Adygeya_Resp", "Altayskii__krai", "Arhangelskaya_obl", "Astrahanskaya_obl",
           "Bashkortostan_Resp", "Belgorodskaya_obl", "Brianskaya_obl","Chechenskaya_Resp", "Cheliabinskaya_obl",
           "Chuvashskaya_Respublika", "Dagestan_Resp", "Habarovskii_krai", "Hakasiia_Resp",
           "Hanty-Mansiiskii_AO_Iugra_AO", "Ivanowskaya_obl",
           "Jaroslavskaya_obl", "Kabardino-Balkarskaya_Resp", "Kaliningradskaya_obl",
           'Kaluzhskaya_obl', 'Karachaevo-Cherkesskaya_Resp',  'Kemerowskaya_obl',
           'Kirowskaya_obl',  'Kostromskaya_obl', 'Krasnodarskii_krai', 'Krasnoyarskii_krai', 'Krym_Resp',
           'Kurganskaya_obl', 'Kurskaya_obl', 'Leningradskaya_obl', 'Lipetckaya_obl',
           'Marii_El_Resp', 'Mordoviya_Resp', 'Moskovskaya_obl', 'Moskva', 'Murmanskaya_obl',
           'Nizhegorodskaya_obl', 'Novgorodskaya_obl', 'Novosibirskaya_obl', 'Omskaya_obl', 'Orenburgskaya_obl',
           'Orlovskaya_obl', 'Penzenskaya_obl', 'Permskii_krai',  'Pskovskaya_obl', 'Rostovskaya_obl',
           'Ryazanskaya_obl', 'Samarskaya_obl', 'Sankt-Peterburg',
           'Saratovskaya_obl', 'Sevastopol', 'Severnaia_Osetiya_Alaniia_Resp', 'Smolenskaya_obl', 'Stavropolskii_krai',
           'Sverdlovskaya_obl', 'Tambovskaya_obl', 'Tatarstan_Resp', 'Tiumenskaya_obl',  'Tulskaya_obl',
           'Tverskaya_obl',  'Udmurtskaya_Resp', 'Ulianovskaya_obl', 'Vladimirskaya_obl', 'Volgogradskaya_obl',
           'Vologodskaya_obl', 'Voronezhskaya_obl']





notice_directories = ['purchaseNotice', 'purchaseNoticeAE', 'purchaseNoticeAE94', 'purchaseNoticeAESMBO',
                      'purchaseNoticeEP', 'purchaseNoticeIS', 'purchaseNoticeKESMBO', 'purchaseNoticeOA',
                      'purchaseNoticeOK', 'purchaseNoticeZK', 'purchaseNoticeZKESMBO',
                      'purchaseNoticeZPESMBO']

# not included regions

# "Baikonur_g", "Altay_Resp",  "Evreiskaya_Aobl", "Irkutskaya_obl_Ust-Ordynskii_Buriatskii_okrug", 'Magadanskaya_obl',
# 'Nenetckii_AO', 'Primorskii_krai',  'Sahalinskaya_obl', 'Tyva_Resp', 'Zabaikalskii_krai',
# 'Zabaikalskii_krai_Aginskii_Buriatskii_okrug', 'Kamchatskii_krai', "Amurskaya_obl", "Chukotskii_AO",
# 'Saha_Jakutiya_Resp', "Buryatiya_Resp", "Irkutskaya_obl", 'Tomskaya_obl', "Jamalo-Nenetckii_AO", "Ingushetiya_Resp",
# "Kalmykiya_Resp", 'Komi_Resp', 'Kareliya_Resp',


# all_regions = ["Adygeya_Resp", "Altay_Resp", "Altayskii__krai", "Amurskaya_obl", "Arhangelskaya_obl", "Astrahanskaya_obl",
#            "Baikonur_g", "Bashkortostan_Resp", "Belgorodskaya_obl", "Brianskaya_obl", "Buryatiya_Resp",
#            "Chechenskaya_Resp", "Cheliabinskaya_obl", "Chukotskii_AO", "Chuvashskaya_Respublika", "Dagestan_Resp",
#            "Evreiskaya_Aobl", "Habarovskii_krai", "Hakasiia_Resp", "Hanty-Mansiiskii_AO_Iugra_AO", "Ingushetiya_Resp",
#            "Irkutskaya_obl", "Irkutskaya_obl_Ust-Ordynskii_Buriatskii_okrug", "Ivanowskaya_obl", "Jamalo-Nenetckii_AO",
#            "Jaroslavskaya_obl", "Kabardino-Balkarskaya_Resp", "Kaliningradskaya_obl", "Kalmykiya_Resp",
#            'Kaluzhskaya_obl', 'Kamchatskii_krai', 'Karachaevo-Cherkesskaya_Resp', 'Kareliya_Resp', 'Kemerowskaya_obl',
#            'Kirowskaya_obl', 'Komi_Resp', 'Kostromskaya_obl', 'Krasnodarskii_krai', 'Krasnoyarskii_krai', 'Krym_Resp',
#            'Kurganskaya_obl', 'Kurskaya_obl', 'Leningradskaya_obl', 'Lipetckaya_obl', 'Magadanskaya_obl',
#            'Marii_El_Resp', 'Mordoviya_Resp', 'Moskovskaya_obl', 'Moskva', 'Murmanskaya_obl', 'Nenetckii_AO',
#            'Nizhegorodskaya_obl', 'Novgorodskaya_obl', 'Novosibirskaya_obl', 'Omskaya_obl', 'Orenburgskaya_obl',
#            'Orlovskaya_obl', 'Penzenskaya_obl', 'Permskii_krai', 'Primorskii_krai', 'Pskovskaya_obl', 'Rostovskaya_obl',
#            'Ryazanskaya_obl', 'Saha_Jakutiya_Resp', 'Sahalinskaya_obl', 'Samarskaya_obl', 'Sankt-Peterburg',
#            'Saratovskaya_obl', 'Sevastopol', 'Severnaia_Osetiya_Alaniia_Resp', 'Smolenskaya_obl', 'Stavropolskii_krai',
#            'Sverdlovskaya_obl', 'Tambovskaya_obl', 'Tatarstan_Resp', 'Tiumenskaya_obl', 'Tomskaya_obl', 'Tulskaya_obl',
#            'Tverskaya_obl', 'Tyva_Resp', 'Udmurtskaya_Resp', 'Ulianovskaya_obl', 'Vladimirskaya_obl', 'Volgogradskaya_obl',
#            'Vologodskaya_obl', 'Voronezhskaya_obl', 'Zabaikalskii_krai', 'Zabaikalskii_krai_Aginskii_Buriatskii_okrug']