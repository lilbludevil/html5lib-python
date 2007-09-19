# borrowed from feedvalidator, original copyright license is
#
# Copyright (c) 2002-2006, Sam Ruby, Mark Pilgrim, Joseph Walton, and Phil Ringnalda
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

isoLang = \
    {'aa': 'Afar',
     'ab': 'Abkhazian',
     'ae': 'Avestan',
     'af': 'Afrikaans',
     'ak': 'Akan',
     'am': 'Amharic',
     'an': 'Aragonese',
     'ar': 'Arabic',
     'as': 'Assamese',
     'av': 'Avaric',
     'ay': 'Aymara',
     'az': 'Azerbaijani',
     'ba': 'Bashkir',
     'be': 'Byelorussian',
     'bg': 'Bulgarian',
     'bh': 'Bihari',
     'bi': 'Bislama',
     'bm': 'Bambara',
     'bn': 'Bengali;Bangla',
     'bo': 'Tibetan',
     'br': 'Breton',
     'bs': 'Bosnian',
     'ca': 'Catalan',
     'ce': 'Chechen',
     'ch': 'Chamorro',
     'co': 'Corsican',
     'cr': 'Cree',
     'cs': 'Czech',
     'cu': 'Church Slavic',
     'cv': 'Chuvash',
     'cy': 'Welsh',
     'da': 'Danish',
     'de': 'German',
     'dv': 'Divehi',
     'dz': 'Dzongkha',
     'ee': 'Ewe',
     'el': 'Greek',
     'en': 'English',
     'eo': 'Esperanto',
     'es': 'Spanish',
     'et': 'Estonian',
     'eu': 'Basque',
     'fa': 'Persian (Farsi)',
     'ff': 'Fulah',
     'fi': 'Finnish',
     'fj': 'Fiji',
     'fo': 'Faroese',
     'fr': 'French',
     'fy': 'Frisian, Western',
     'ga': 'Irish',
     'gd': 'Scots Gaelic',
     'gl': 'Galician',
     'gn': 'Guarani',
     'gu': 'Gujarati',
     'gv': 'Manx',
     'ha': 'Hausa',
     'he': 'Hebrew',
     'hi': 'Hindi',
     'ho': 'Hiri Motu',
     'hr': 'Croatian',
     'ht': 'Haitian',
     'hu': 'Hungarian',
     'hy': 'Armenian',
     'hz': 'Herero',
     'ia': 'Interlingua',
     'id': 'Indonesian',
     'ie': 'Interlingue',
     'ig': 'Igbo',
     'ii': 'Sichuan Yi',
     'ik': 'Inupiak',
     'io': 'Ido',
     'is': 'Icelandic',
     'it': 'Italian',
     'iu': 'Inuktitut',
     'ja': 'Japanese',
     'jv': 'Javanese',
     'ka': 'Georgian',
     'kg': 'Kongo',
     'ki': 'Kikuyu; Gikuyu',
     'kj': 'Kuanyama; Kwanyama',
     'kk': 'Kazakh',
     'kl': 'Greenlandic',
     'km': 'Cambodian',
     'kn': 'Kannada',
     'ko': 'Korean',
     'kr': 'Kanuri',
     'ks': 'Kashmiri',
     'ku': 'Kurdish',
     'kv': 'Komi',
     'kw': 'Cornish',
     'ky': 'Kirghiz',
     'la': 'Latin',
     'lb': 'Letzeburgesch; Luxembourgish',
     'lg': 'Ganda',
     'li': 'Limburgan; Limburger, Limburgish',
     'ln': 'Lingala',
     'lo': 'Lao',
     'lt': 'Lithuanian',
     'lu': 'Luba-Katanga',
     'lv': 'Latvian',
     'mg': 'Malagasy',
     'mh': 'Marshallese',
     'mi': 'Maori',
     'mk': 'Macedonian',
     'ml': 'Malayalam',
     'mn': 'Mongolian',
     'mo': 'Moldavian',
     'mr': 'Marathi',
     'ms': 'Malay',
     'mt': 'Maltese',
     'my': 'Burmese',
     'na': 'Nauru',
     'nb': 'Norwegian Bokmal',
     'nd': 'Ndebele, North',
     'ne': 'Nepali',
     'ng': 'Ndonga',
     'nl': 'Dutch',
     'nn': 'Norwegian Nynorsk',
     'no': 'Norwegian',
     'nr': 'Ndebele, South',
     'nv': 'Navaho; Navajo',
     'ny': 'Chewa; Chichewa; Nyanha',
     'oc': 'Occitan',
     'oj': 'Ojibwa',
     'om': 'Afan (Oromo)',
     'or': 'Oriya',
     'os': 'Ossetian; Ossetic',
     'pa': 'Punjabi',
     'pi': 'Pali',
     'pl': 'Polish',
     'ps': 'Pushto',
     'pt': 'Portuguese',
     'qu': 'Quechua',
     'rm': 'Rhaeto-Romance',
     'rn': 'Kurundi',
     'ro': 'Romanian',
     'ru': 'Russian',
     'rw': 'Kinyarwanda',
     'sa': 'Sanskrit',
     'sc': 'Sardinian',
     'sd': 'Sindhi',
     'se': 'Northern Sami',
     'sg': 'Sangho',
     'sh': 'Serbo-Croatian',
     'si': 'Singhalese',
     'sk': 'Slovak',
     'sl': 'Slovenian',
     'sm': 'Samoan',
     'sn': 'Shona',
     'so': 'Somali',
     'sq': 'Albanian',
     'sr': 'Serbian',
     'ss': 'Swati',
     'st': 'Sotho, Southern',
     'su': 'Sundanese',
     'sv': 'Swedish',
     'sw': 'Swahili',
     'ta': 'Tamil',
     'te': 'Telugu',
     'tg': 'Tajik',
     'th': 'Thai',
     'ti': 'Tigrinya',
     'tk': 'Turkmen',
     'tl': 'Tagalog',
     'tn': 'Tswana',
     'to': 'Tonga',
     'tr': 'Turkish',
     'ts': 'Tsonga',
     'tt': 'Tatar',
     'tw': 'Twi',
     'ty': 'Tahitian',
     'ug': 'Uigur',
     'uk': 'Ukrainian',
     'ur': 'Urdu',
     'uz': 'Uzbek',
     've': 'Venda',
     'vi': 'Vietnamese',
     'vo': 'Volapuk',
     'wa': 'Walloon',
     'wo': 'Wolof',
     'xh': 'Xhosa',
     'yi': 'Yiddish',
     'yo': 'Yoruba',
     'za': 'Zhuang',
     'zh': 'Chinese',
     'zu': 'Zulu',
     'x' : 'a user-defined language',
     'xx': 'a user-defined language',
     
     'abk': 'Abkhazian',
     'ace': 'Achinese',
     'ach': 'Acoli',
     'ada': 'Adangme',
     'ady': 'Adygei',
     'ady': 'Adyghe',
     'aar': 'Afar',
     'afh': 'Afrihili',
     'afr': 'Afrikaans',
     'afa': 'Afro-Asiatic (Other)',
     'ain': 'Ainu',
     'aka': 'Akan',
     'akk': 'Akkadian',
     'alb': 'Albanian',
     'sqi': 'Albanian',
     'gws': 'Alemanic',
     'ale': 'Aleut',
     'alg': 'Algonquian languages',
     'tut': 'Altaic (Other)',
     'amh': 'Amharic',
     'anp': 'Angika',
     'apa': 'Apache languages',
     'ara': 'Arabic',
     'arg': 'Aragonese',
     'arc': 'Aramaic',
     'arp': 'Arapaho',
     'arn': 'Araucanian',
     'arw': 'Arawak',
     'arm': 'Armenian',
     'hye': 'Armenian',
     'rup': 'Aromanian',
     'art': 'Artificial (Other)',
     'asm': 'Assamese',
     'ast': 'Asturian',
     'ath': 'Athapascan languages',
     'aus': 'Australian languages',
     'map': 'Austronesian (Other)',
     'ava': 'Avaric',
     'ave': 'Avestan',
     'awa': 'Awadhi',
     'aym': 'Aymara',
     'aze': 'Azerbaijani',
     'ast': 'Bable',
     'ban': 'Balinese',
     'bat': 'Baltic (Other)',
     'bal': 'Baluchi',
     'bam': 'Bambara',
     'bai': 'Bamileke languages',
     'bad': 'Banda',
     'bnt': 'Bantu (Other)',
     'bas': 'Basa',
     'bak': 'Bashkir',
     'baq': 'Basque',
     'eus': 'Basque',
     'btk': 'Batak (Indonesia)',
     'bej': 'Beja',
     'bel': 'Belarusian',
     'bem': 'Bemba',
     'ben': 'Bengali',
     'ber': 'Berber (Other)',
     'bho': 'Bhojpuri',
     'bih': 'Bihari',
     'bik': 'Bikol',
     'byn': 'Bilin',
     'bin': 'Bini',
     'bis': 'Bislama',
     'byn': 'Blin',
     'nob': 'Bokmal, Norwegian',
     'bos': 'Bosnian',
     'bra': 'Braj',
     'bre': 'Breton',
     'bug': 'Buginese',
     'bul': 'Bulgarian',
     'bua': 'Buriat',
     'bur': 'Burmese',
     'mya': 'Burmese',
     'cad': 'Caddo',
     'car': 'Carib',
     'spa': 'Castilian',
     'cat': 'Catalan',
     'cau': 'Caucasian (Other)',
     'ceb': 'Cebuano',
     'cel': 'Celtic (Other)',
     'cai': 'Central American Indian (Other)',
     'chg': 'Chagatai',
     'cmc': 'Chamic languages',
     'cha': 'Chamorro',
     'che': 'Chechen',
     'chr': 'Cherokee',
     'nya': 'Chewa',
     'chy': 'Cheyenne',
     'chb': 'Chibcha',
     'nya': 'Chichewa',
     'chi': 'Chinese',
     'zho': 'Chinese',
     'chn': 'Chinook jargon',
     'chp': 'Chipewyan',
     'cho': 'Choctaw',
     'zha': 'Chuang',
     'chu': 'Church Slavic; Church Slavonic; Old Church Slavonic; Old Church Slavic; Old Bulgarian',
     'chk': 'Chuukese',
     'chv': 'Chuvash',
     'nwc': 'Classical Nepal Bhasa; Classical Newari; Old Newari',
     'cop': 'Coptic',
     'cor': 'Cornish',
     'cos': 'Corsican',
     'cre': 'Cree',
     'mus': 'Creek',
     'crp': 'Creoles and pidgins(Other)',
     'cpe': 'Creoles and pidgins, English-based (Other)',
     'cpf': 'Creoles and pidgins, French-based (Other)',
     'cpp': 'Creoles and pidgins, Portuguese-based (Other)',
     'crh': 'Crimean Tatar; Crimean Turkish',
     'scr': 'Croatian',
     'hrv': 'Croatian',
     'cus': 'Cushitic (Other)',
     'cze': 'Czech',
     'ces': 'Czech',
     'dak': 'Dakota',
     'dan': 'Danish',
     'dar': 'Dargwa',
     'day': 'Dayak',
     'del': 'Delaware',
     'din': 'Dinka',
     'div': 'Divehi',
     'doi': 'Dogri',
     'dgr': 'Dogrib',
     'dra': 'Dravidian (Other)',
     'dua': 'Duala',
     'dut': 'Dutch',
     'nld': 'Dutch',
     'dum': 'Dutch, Middle (ca. 1050-1350)',
     'dyu': 'Dyula',
     'dzo': 'Dzongkha',
     'efi': 'Efik',
     'egy': 'Egyptian (Ancient)',
     'eka': 'Ekajuk',
     'elx': 'Elamite',
     'eng': 'English',
     'enm': 'English, Middle (1100-1500)',
     'ang': 'English, Old (ca.450-1100)',
     'myv': 'Erzya',
     'epo': 'Esperanto',
     'est': 'Estonian',
     'ewe': 'Ewe',
     'ewo': 'Ewondo',
     'fan': 'Fang',
     'fat': 'Fanti',
     'fao': 'Faroese',
     'fij': 'Fijian',
     'fil': 'Filipino; Pilipino',
     'fin': 'Finnish',
     'fiu': 'Finno-Ugrian (Other)',
     'fon': 'Fon',
     'fre': 'French',
     'fra': 'French',
     'frm': 'French, Middle (ca.1400-1600)',
     'fro': 'French, Old (842-ca.1400)',
     'frs': 'Frisian, Eastern',
     'fry': 'Frisian, Western',
     'fur': 'Friulian',
     'ful': 'Fulah',
     'gaa': 'Ga',
     'gla': 'Gaelic',
     'glg': 'Gallegan',
     'lug': 'Ganda',
     'gay': 'Gayo',
     'gba': 'Gbaya',
     'gez': 'Geez',
     'geo': 'Georgian',
     'kat': 'Georgian',
     'ger': 'German',
     'deu': 'German',
     'nds': 'German, Low',
     'gmh': 'German, Middle High (ca.1050-1500)',
     'goh': 'German, Old High (ca.750-1050)',
     'gem': 'Germanic (Other)',
     'kik': 'Gikuyu',
     'gil': 'Gilbertese',
     'gon': 'Gondi',
     'gor': 'Gorontalo',
     'got': 'Gothic',
     'grb': 'Grebo',
     'grc': 'Greek, Ancient (to 1453)',
     'gre': 'Greek, Modern (1453-)',
     'ell': 'Greek, Modern (1453-)',
     'kal': 'Greenlandic; Kalaallisut',
     'grn': 'Guarani',
     'guj': 'Gujarati',
     'gwi': 'Gwich\'in',
     'hai': 'Haida',
     'hat': 'Haitian',
     'hau': 'Hausa',
     'haw': 'Hawaiian',
     'heb': 'Hebrew',
     'her': 'Herero',
     'hil': 'Hiligaynon',
     'him': 'Himachali',
     'hin': 'Hindi',
     'hmo': 'Hiri Motu',
     'hit': 'Hittite',
     'hmn': 'Hmong',
     'hun': 'Hungarian',
     'hup': 'Hupa',
     'iba': 'Iban',
     'ice': 'Icelandic',
     'isl': 'Icelandic',
     'ido': 'Ido',
     'ibo': 'Igbo',
     'ijo': 'Ijo',
     'ilo': 'Iloko',
     'smn': 'Inari Sami',
     'inc': 'Indic (Other)',
     'ine': 'Indo-European (Other)',
     'ind': 'Indonesian',
     'inh': 'Ingush',
     'ina': 'Interlingua (International Auxiliary Language Association)',
     'ile': 'Interlingue',
     'iku': 'Inuktitut',
     'ipk': 'Inupiaq',
     'ira': 'Iranian (Other)',
     'gle': 'Irish',
     'mga': 'Irish, Middle (900-1200)',
     'sga': 'Irish, Old (to 900)',
     'iro': 'Iroquoian languages',
     'ita': 'Italian',
     'jpn': 'Japanese',
     'jav': 'Javanese',
     'jrb': 'Judeo-Arabic',
     'jpr': 'Judeo-Persian',
     'kbd': 'Kabardian',
     'kab': 'Kabyle',
     'kac': 'Kachin',
     'kal': 'Kalaallisut',
     'xal': 'Kalmyk',
     'kam': 'Kamba',
     'kan': 'Kannada',
     'kau': 'Kanuri',
     'krc': 'Karachay-Balkar',
     'kaa': 'Kara-Kalpak',
     'krl': 'Karelian',
     'kar': 'Karen',
     'kas': 'Kashmiri',
     'csb': 'Kashubian',
     'kaw': 'Kawi',
     'kaz': 'Kazakh',
     'kha': 'Khasi',
     'khm': 'Khmer',
     'khi': 'Khoisan (Other)',
     'kho': 'Khotanese',
     'kik': 'Kikuyu',
     'kmb': 'Kimbundu',
     'kin': 'Kinyarwanda',
     'kir': 'Kirghiz',
     'tlh': 'Klingon; tlhIngan-Hol',
     'kom': 'Komi',
     'kon': 'Kongo',
     'kok': 'Konkani',
     'kor': 'Korean',
     'kos': 'Kosraean',
     'kpe': 'Kpelle',
     'kro': 'Kru',
     'kua': 'Kuanyama',
     'kum': 'Kumyk',
     'kur': 'Kurdish',
     'kru': 'Kurukh',
     'kut': 'Kutenai',
     'kua': 'Kwanyama',
     'lad': 'Ladino',
     'lah': 'Lahnda',
     'lam': 'Lamba',
     'lao': 'Lao',
     'lat': 'Latin',
     'lav': 'Latvian',
     'ltz': 'Letzeburgesch',
     'lez': 'Lezghian',
     'lim': 'Limburgan',
     'lin': 'Lingala',
     'lit': 'Lithuanian',
     'jbo': 'Lojban',
     'nds': 'Low German',
     'dsb': 'Lower Sorbian',
     'loz': 'Lozi',
     'lub': 'Luba-Katanga',
     'lua': 'Luba-Lulua',
     'lui': 'Luiseno',
     'smj': 'Lule Sami',
     'lun': 'Lunda',
     'luo': 'Luo (Kenya and Tanzania)',
     'lus': 'Lushai',
     'ltz': 'Luxembourgish',
     'mac': 'Macedonian',
     'mkd': 'Macedonian',
     'mad': 'Madurese',
     'mag': 'Magahi',
     'mai': 'Maithili',
     'mak': 'Makasar',
     'mlg': 'Malagasy',
     'may': 'Malay',
     'msa': 'Malay',
     'mal': 'Malayalam',
     'mlt': 'Maltese',
     'mnc': 'Manchu',
     'mdr': 'Mandar',
     'man': 'Mandingo',
     'mni': 'Manipuri',
     'mno': 'Manobo languages',
     'glv': 'Manx',
     'mao': 'Maori',
     'mri': 'Maori',
     'mar': 'Marathi',
     'chm': 'Mari',
     'mah': 'Marshallese',
     'mwr': 'Marwari',
     'mas': 'Masai',
     'myn': 'Mayan languages',
     'men': 'Mende',
     'mic': 'Micmac',
     'min': 'Minangkabau',
     'mwl': 'Mirandese',
     'mis': 'Miscellaneous languages',
     'moh': 'Mohawk',
     'mdf': 'Moksha',
     'mol': 'Moldavian',
     'mkh': 'Mon-Khmer (Other)',
     'lol': 'Mongo',
     'mon': 'Mongolian',
     'mos': 'Mossi',
     'mul': 'Multiple languages',
     'mun': 'Munda languages',
     'nah': 'Nahuatl',
     'nau': 'Nauru',
     'nav': 'Navaho; Navajo',
     'nde': 'Ndebele, North',
     'nbl': 'Ndebele, South',
     'ndo': 'Ndonga',
     'nap': 'Neapolitan',
     'nep': 'Nepali',
     'new': 'Newari',
     'nia': 'Nias',
     'nic': 'Niger-Kordofanian (Other)',
     'ssa': 'Nilo-Saharan (Other)',
     'niu': 'Niuean',
     'nog': 'Nogai',
     'non': 'Norse, Old',
     'nai': 'North American Indian (Other)',
     'frr': 'Northern Frisian',
     'sme': 'Northern Sami',
     'nso': 'Northern Sotho; Pedi; Sepedi',
     'nde': 'North Ndebele',
     'nor': 'Norwegian',
     'nob': 'Norwegian Bokmal',
     'nno': 'Norwegian Nynorsk',
     'nub': 'Nubian languages',
     'nym': 'Nyamwezi',
     'nya': 'Nyanja',
     'nyn': 'Nyankole',
     'nno': 'Nynorsk, Norwegian',
     'nyo': 'Nyoro',
     'nzi': 'Nzima',
     'oci': 'Occitan (post 1500)',
     'oji': 'Ojibwa',
     'ori': 'Oriya',
     'orm': 'Oromo',
     'osa': 'Osage',
     'oss': 'Ossetian; Ossetic',
     'oto': 'Otomian languages',
     'pal': 'Pahlavi',
     'pau': 'Palauan',
     'pli': 'Pali',
     'pam': 'Pampanga',
     'pag': 'Pangasinan',
     'pan': 'Panjabi',
     'pap': 'Papiamento',
     'paa': 'Papuan (Other)',
     'per': 'Persian',
     'fas': 'Persian',
     'peo': 'Persian, Old (ca.600-400)',
     'phi': 'Philippine (Other)',
     'phn': 'Phoenician',
     'pon': 'Pohnpeian',
     'pol': 'Polish',
     'por': 'Portuguese',
     'pra': 'Prakrit languages',
     'oci': 'Provencal',
     'pro': 'Provencal, Old (to 1500)',
     'pan': 'Punjabi',
     'pus': 'Pushto',
     'que': 'Quechua',
     'roh': 'Raeto-Romance',
     'raj': 'Rajasthani',
     'rap': 'Rapanui',
     'rar': 'Rarotongan',
     'qaa': 'Reserved for local use',
     'qtz': 'Reserved for local use',
     'roa': 'Romance (Other)',
     'rum': 'Romanian',
     'ron': 'Romanian',
     'rom': 'Romany',
     'run': 'Rundi',
     'rus': 'Russian',
     'sal': 'Salishan languages',
     'sam': 'Samaritan Aramaic',
     'smi': 'Sami languages (Other)',
     'smo': 'Samoan',
     'sad': 'Sandawe',
     'sag': 'Sango',
     'san': 'Sanskrit',
     'sat': 'Santali',
     'srd': 'Sardinian',
     'sas': 'Sasak',
     'nds': 'Saxon, Low',
     'sco': 'Scots',
     'gla': 'Scottish Gaelic',
     'sel': 'Selkup',
     'sem': 'Semitic (Other)',
     'nso': 'Sepedi; Northern Sotho; Pedi',
     'scc': 'Serbian',
     'srp': 'Serbian',
     'srr': 'Serer',
     'shn': 'Shan',
     'sna': 'Shona',
     'iii': 'Sichuan Yi',
     'scn': 'Sicilian',
     'sid': 'Sidamo',
     'sgn': 'Sign languages',
     'bla': 'Siksika',
     'snd': 'Sindhi',
     'sin': 'Sinhalese',
     'sit': 'Sino-Tibetan (Other)',
     'sio': 'Siouan languages',
     'sms': 'Skolt Sami',
     'den': 'Slave (Athapascan)',
     'sla': 'Slavic (Other)',
     'slo': 'Slovak',
     'slk': 'Slovak',
     'slv': 'Slovenian',
     'sog': 'Sogdian',
     'som': 'Somali',
     'son': 'Songhai',
     'snk': 'Soninke',
     'wen': 'Sorbian languages',
     'nso': 'Sotho, Northern',
     'sot': 'Sotho, Southern',
     'sai': 'South American Indian (Other)',
     'alt': 'Southern Altai',
     'sma': 'Southern Sami',
     'nbl': 'South Ndebele',
     'spa': 'Spanish',
     'srn': 'Sranan Tongo',
     'suk': 'Sukuma',
     'sux': 'Sumerian',
     'sun': 'Sundanese',
     'sus': 'Susu',
     'swa': 'Swahili',
     'ssw': 'Swati',
     'swe': 'Swedish',
     'gsw': 'Swiss German; Alemanic',
     'syr': 'Syriac',
     'tgl': 'Tagalog',
     'tah': 'Tahitian',
     'tai': 'Tai (Other)',
     'tgk': 'Tajik',
     'tmh': 'Tamashek',
     'tam': 'Tamil',
     'tat': 'Tatar',
     'tel': 'Telugu',
     'ter': 'Tereno',
     'tet': 'Tetum',
     'tha': 'Thai',
     'tib': 'Tibetan',
     'bod': 'Tibetan',
     'tig': 'Tigre',
     'tir': 'Tigrinya',
     'tem': 'Timne',
     'tiv': 'Tiv',
     'tlh': 'tlhIngan-Hol; Klingon',
     'tli': 'Tlingit',
     'tpi': 'Tok Pisin',
     'tkl': 'Tokelau',
     'tog': 'Tonga (Nyasa)',
     'ton': 'Tonga (Tonga Islands)',
     'tsi': 'Tsimshian',
     'tso': 'Tsonga',
     'tsn': 'Tswana',
     'tum': 'Tumbuka',
     'tup': 'Tupi languages',
     'tur': 'Turkish',
     'ota': 'Turkish, Ottoman (1500-1928)',
     'tuk': 'Turkmen',
     'tvl': 'Tuvalu',
     'tyv': 'Tuvinian',
     'twi': 'Twi',
     'udm': 'Udmurt',
     'uga': 'Ugaritic',
     'uig': 'Uighur',
     'ukr': 'Ukrainian',
     'umb': 'Umbundu',
     'und': 'Undetermined',
     'hsb': 'Upper Sorbian',
     'urd': 'Urdu',
     'uzb': 'Uzbek',
     'vai': 'Vai',
     'cat': 'Valencian',
     'ven': 'Venda',
     'vie': 'Vietnamese',
     'vol': 'Volapuk',
     'vot': 'Votic',
     'wak': 'Wakashan languages',
     'wal': 'Walamo',
     'wln': 'Walloon',
     'war': 'Waray',
     'was': 'Washo',
     'wel': 'Welsh',
     'cym': 'Welsh',
     'fry': 'Wester Frisian',
     'wol': 'Wolof',
     'xho': 'Xhosa',
     'sah': 'Yakut',
     'yao': 'Yao',
     'yap': 'Yapese',
     'yid': 'Yiddish',
     'yor': 'Yoruba',
     'ypk': 'Yupik languages',
     'znd': 'Zande',
     'zap': 'Zapotec',
     'zen': 'Zenaga',
     'zha': 'Zhuang',
     'zul': 'Zulu',
     'zun': 'Zuni' }

def isValidLangCode(value):
    if '-' in value:
        lang, sublang = value.split('-', 1)
    else:
        lang = value
    return isoLang.has_key(unicode.lower(unicode(lang)))