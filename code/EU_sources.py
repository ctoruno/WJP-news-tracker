import pandas as pd

# Newspapers
newspapers = {
    "Austria":[
        {
            "country": "Austria",
            "newspaper_name": "Kronen Zeitung",
            "location": "Vienna",
            "editorial": "right",
            "url": "https://www.krone.at/",
            "justification": "Highest circulation in Austria, populist tone, significant influence on public opinion."
        },
        {
            "country": "Austria",
            "newspaper_name": "Der Standard",
            "location": "Vienna",
            "editorial": "center-left",
            "url": "https://derstandard.at/",
            "justification": "Influential voice for liberal-intellectual discourse, strong investigative journalism."
        },
        {
            "country": "Austria",
            "location": "Vienna",
            "newspaper_name": "Die Presse",
            "url": "https://diepresse.com/",
            "editorial": "centre-right",
            "justification": "Established paper with strong political and economic coverage, respected for its neutrality."
        },
        {
            "country": "Austria",
            "newspaper_name": "Salzburger Nachrichten",
            "location": "Salzburg",
            "editorial": "center-right",
            "url": "https://www.salzburg24.at/",
            "justification": "Leading regional paper with strong influence in western Austria, focus on local politics and business."
        },
        {
            "country": "Austria",
            "newspaper_name": "Kurier",
            "location": "Vienna",
            "editorial": "center",
            "url": "https://kurier.at/",
            "justification": "Large readership, focus on social and cultural issues, appeal to diverse demographics."
        },
        {
            "country": "Austria",
            "newspaper_name": "Kleine Zeitung",
            "location": "Graz",
            "editorial": "center-right",
            "url": "https://www.kleinezeitung.at/",
            "justification": "Leading regional paper in southern Austria, strong coverage of local and national news."
        },
        {
            "country": "Austria",
            "newspaper_name": "Neues Volksblatt",
            "location": "Linz",
            "editorial": "center-right",
            "url": "https://www.nachrichten.at/",
            "justification": "Dominant paper in Upper Austria, focus on regional politics and business."
        },
        {
            "country": "Austria",
            "newspaper_name": "Wiener Zeitung",
            "location": "Vienna",
            "editorial": "neutral",
            "url": "https://www.wienerzeitung.at/",
            "justification": "Official newspaper of Austria, focus on legal and political matters, respected for its neutrality."
        },
        {
            "country": "Austria",
            "newspaper_name": "Vorarlberger Nachrichten",
            "location": "Dornbirn",
            "editorial": "center-right",
            "url": "https://www.vn.at/",
            "justification": "Leading paper in Vorarlberg, strong influence on local and regional politics."
        },
        {
            "country": "Austria",
            "newspaper_name": "Tiroler Tageszeitung",
            "location": "Innsbruck",
            "url": "https://www.tt.com/",
            "editorial": "center-right",
            "justification": "Leading paper in Tyrol, focus on regional politics and tourism."
        }
    ],
    "Belgium":[
        {
            "country": "Belgium",
            "newspaper_name": "Het Laatste Nieuws",
            "location": "Antwerp",
            "editorial": "center-right",
            "url": "https://www.hln.be/",
            "justification": "Belgium's highest-circulation daily newspaper, with strong regional presence and influence on public opinion."
        },
        {
            "country": "Belgium",
            "newspaper_name": "Le Soir",
            "location": "Brussels",
            "editorial": "center-left",
            "url": "https://www.lesoir.be/",
            "justification": "Leading French-language daily, known for its in-depth analyses and influence on political discourse."
        },
        {
            "country": "Belgium",
            "newspaper_name": "De Standaard",
            "location": "Brussels",
            "editorial": "center-right",
            "url": "https://www.standaard.be/",
            "justification": "Respected quality newspaper with strong focus on international and economic news, shaping business and political circles."
        },
        {
            "country": "Belgium",
            "newspaper_name": "De Morgen",
            "location": "Ghent",
            "editorial": "center-left",
            "url": "https://www.demorgen.be/",
            "justification": "Influential liberal daily, known for its investigative journalism and progressive stance on social issues."
        },
        {
            "country": "Belgium",
            "newspaper_name": "La Libre Belgique",
            "location": "Brussels",
            "url": "https://www.lalibre.be/",
            "justification": "Historically significant French-language daily, offering conservative perspective and contributing to intellectual debate."
        },
        {
            "country": "Belgium",
            "newspaper_name": "Het Nieuwsblad",
            "location": "Hasselt",
            "editorial": "center",
            "url": "https://www.nieuwsblad.be/",
            "justification": "Second-highest circulation daily, with a broad readership and focus on regional news, influencing local public opinion."
        },
        {
            "country": "Belgium",
            "newspaper_name": "L'Echo",
            "location": "Brussels",
            "url": "https://www.lecho.be/",
            "justification": "Leading business newspaper, with in-depth coverage of financial markets and significant influence on economic decisions."
        },
        {
            "country": "Belgium",
            "location": "Brussels",
            "newspaper_name": "De Tijd",
            "url": "https://www.tijd.be/",
            "justification": "Respected financial daily, offering conservative economic analysis and shaping business discourse in Flemish region."
        },
        {
            "country": "Belgium",
            "location": "Brussels",
            "newspaper_name": "The Brussels Times",
            "url": "https://www.brusselstimes.com/",
            "justification": "Only major English-language daily, providing international perspective on Belgian news and influencing European policy discussions."
        },
        {
            "country": "Belgium",
            "location": "Liège",
            "newspaper_name": "La Meuse",
            "url": "https://www.lameuse.be/",
            "justification": "Major French-language daily in Wallonia, with strong regional focus and significant influence on local politics and public opinion."
        }
    ],
    "Croatia": [
        {
            "country": "Croatia",
            "newspaper_name": "Jutarnji list",
            "location": "Zagreb",
            "editorial": "Center-left",
            "url": "https://www.jutarnji.hr/",
            "justification": "Croatia's oldest daily newspaper with high print circulation, influential online presence, and a strong editorial voice."
        },
        {
            "country": "Croatia",
            "newspaper_name": "Večernji list",
            "location": "Zagreb",
            "editorial": "Center-left",
            "url": "https://www.vecernji.hr/",
            "justification": "Long-standing daily with in-depth analyses, high circulation, and a strong online presence."
        },
        {
            "country": "Croatia",
            "newspaper_name": "24sata",
            "location": "Zagreb",
            "editorial": "Tabloid",
            "url": "https://www.24sata.hr/",
            "justification": "Most popular tabloid with high online readership, known for catchy headlines and accessibility."
        },
        {
            "country": "Croatia",
            "newspaper_name": "Novi list",
            "location": "Rijeka",
            "editorial": "Center",
            "url": "https://www.novilist.hr/",
            "justification": "Leading regional newspaper with a focus on investigative journalism and a moderate political stance."
        },
        {
            "country": "Croatia",
            "newspaper_name": "Slobodna Dalmacija",
            "location": "Split",
            "editorial": "Center",
            "url": "https://slobodnadalmacija.hr/",
            "justification": "Influential regional daily with a strong focus on tourism, culture, and history."
        },
        {
            "country": "Croatia",
            "newspaper_name": "Glas Slavonije",
            "location": "Osijek",
            "editorial": "Center-left",
            "url": "https://www.glas-slavonije.hr/",
            "justification": "Respected regional newspaper known for investigative reporting and a focus on agriculture and local sports."
        },
        {
            "country": "Croatia",
            "newspaper_name": "Glas Istre",
            "location": "Pula",
            "editorial": "Center-right",
            "url": "https://www.glasistre.hr/",
            "justification": "Leading regional newspaper with diverse editorial voices and a focus on regional news, politics, and economy."
        },
        {
            "country": "Croatia",
            "newspaper_name": "Index.hr",
            "location": "Zagreb",
            "editorial": "Independent",
            "url": "https://www.index.hr/",
            "justification": "Influential online news portal with high traffic and a reputation for independent reporting and critical commentary."
        }
    ],
    "Czechia": [
        {
            "country": "Czechia",
            "newspaper_name": "Blesk",
            "location": "Prague",
            "editorial": "Tabloid",
            "url": "https://www.blesk.cz/",
            "justification": "Highest circulation, focusing on celebrities and sensational news, influences broader public opinion."
        },
        {
            "country": "Czechia",
            "location": "Prague",
            "editorial": "Center-right",
            "url": "https://www.lidovky.cz/",
            "justification": "Renowned for investigative journalism and strong political influence, especially among older generations."
        },
        {
            "country": "Czechia",
            "location": "Prague",
            "editorial": "Center-left",
            "url": "https://www.ceskenovinky.cz/",
            "justification": "Wide readership, known for covering social issues and offering diverse perspectives."
        },
        {
            "country": "Czechia",
            "location": "Prague",
            "editorial": "Center-right",
            "url": "https://www.mf dnes.cz/",
            "url_2": "https://www.idnes.cz/",
            "justification": "Large reach with both print and online platforms, offers balanced coverage across politics, economy, and culture."
        },
        {
            "country": "Czechia",
            "location": "Prague",
            "editorial": "Center-left",
            "url": "https://zpravy.aktualne.cz/",
            "justification": "Respected for in-depth analysis and commentary, influential among political and business elites."
        },
        {
            "country": "Czechia",
            "location": "Prague",
            "editorial": "Center-right",
            "url": "https://www.seznamzpravy.cz/",
            "justification": "Strong online presence, popular for investigative reporting and political satire."
        },
        {
            "country": "Czechia",
            "location": "Prague",
            "editorial": "Center-right",
            "url": "https://www.echo24.cz/",
            "justification": "Focuses on business and economic news, influential in financial circles and policy debates."
        },
        {
            "country": "Czechia",
            "location": "Prague",
            "editorial": "Center-left",
            "url": "https://denikn.cz/",
            "justification": "Renowned for intellectual essays and critical journalism, popular among cultural and academic circles."
        },
        {
            "country": "Czechia",
            "location": "Prague",
            "editorial": "Center-right",
            "url": "https://www.irozhlas.cz/",
            "justification": "Leading public radio station with online news portal, strong regional presence and focus on local issues."
        },
        {
            "country": "Czechia",
            "location": "Prague",
            "editorial": "Independent",
            "url": "https://ct24.ceskatelevize.cz/",
            "justification": "Public television news portal, offers balanced coverage and enjoys high trust among viewers."
        }
    ],
    "Cyprus": [
        {
            "country": "Cyprus",
            "newspaper_name": "Politis (Πολίτης)",
            "location": "Nicosia",
            "editorial": "Center-right",
            "url": "https://www.politis.com.cy/",
            "image": "https://upload.wikimedia.org/wikipedia/en/2/26/Politis_newspaper_Cyprus.jpg",
            "justification": "Leading daily with high circulation and readership, known for strong investigative journalism and influence on political discourse."
        },
        {
            "country": "Cyprus",
            "newspaper_name": "Phileleftheros (Φιλελεύθερος)",
            "location": "Nicosia",
            "editorial": "Center-left",
            "url": "https://www.philenews.com/",
            "image": "https://upload.wikimedia.org/wikipedia/en/4/41/Phileleftheros_newspaper_Cyprus.jpg",
            "justification": "Renowned for in-depth analysis and political commentary, influential amongst educated middle-class and political elites."
        },
        {
            "country": "Cyprus",
            "newspaper_name": "Simerini (Σημερινή)",
            "location": "Nicosia",
            "editorial": "Center-right",
            "url": "https://www.simerini.com/",
            "image": "https://upload.wikimedia.org/wikipedia/en/f/fe/Simerini_newspaper_Cyprus.jpg",
            "justification": "Popular daily with large readership, particularly among older generations, focuses on traditional values and national issues."
        },
        {
            "country": "Cyprus",
            "newspaper_name": "Haravghi (Χαραυγή)",
            "location": "Nicosia",
            "editorial": "Left-wing",
            "url": "https://www.haravghi.net/",
            "image": "https://upload.wikimedia.org/wikipedia/en/3/3c/Haravghi_newspaper_Cyprus.jpg",
            "justification": "Leading voice of the Cypriot left, known for its strong stances on social justice, worker's rights, and the Cyprus dispute."
        },
        {
            "country": "Cyprus",
            "newspaper_name": "Alithia (Αλήθεια)",
            "location": "Limassol",
            "editorial": "Center",
            "url": "https://www.alithia.com.cy/",
            "image": "https://upload.wikimedia.org/wikipedia/en/1/10/Alithia_newspaper_Cyprus.jpg",
            "justification": "Respected regional newspaper with strong presence in Limassol, known for balanced coverage and focus on local issues."
        }
    ],
    "Denmark": [
        {
            "country": "Denmark",
            "newspaper_name": "Politiken",
            "location": "Copenhagen",
            "editorial": "center-left",
            "url": "https://politiken.dk/",
            "justification": "Largest daily readership in Denmark (501,000 weekly readers in 2022), strong investigative journalism, historically influential in shaping Danish political discourse."
        },
        {
            "country": "Denmark",
            "newspaper_name": "Jyllands-Posten",
            "location": "Aarhus",
            "editorial": "center-right",
            "url": "https://jyllands-posten.dk/",
            "justification": "Second largest daily readership (435,000 weekly readers in 2022), significant regional influence, known for in-depth analyses and investigative reporting."
        },
        {
            "country": "Denmark",
            "newspaper_name": "Berlingske",
            "location": "Copenhagen",
            "editorial": "center-right",
            "url": "https://www.berlingske.dk/",
            "justification": "Leading business newspaper, influential in economic and political circles, strong digital presence."
        },
        {
            "country": "Denmark",
            "newspaper_name": "Ekstra Bladet",
            "location": "Copenhagen",
            "editorial": "populist",
            "url": "https://ekstrabladet.dk/",
            "justification": "Highest circulation tabloid newspaper, significant reach among working-class demographics, known for controversial and sensational headlines."
        },
        {
            "country": "Denmark",
            "newspaper_name": "Information",
            "location": "Copenhagen",
            "editorial": "center-left",
            "url": "https://www.information.dk/",
            "justification": "Leading intellectual newspaper, influential in cultural and academic circles, known for in-depth analyses and critical commentary."
        },
        {
            "country": "Denmark",
            "newspaper_name": "B.T.",
            "location": "Copenhagen",
            "editorial": "center-right",
            "url": "https://www.bt.dk/",
            "justification": "Popular tabloid newspaper with a strong online presence, known for its focus on entertainment and celebrity news."
        },
        {
            "country": "Denmark",
            "newspaper_name": "Kristeligt Dagblad",
            "location": "Copenhagen",
            "editorial": "center-right",
            "url": "https://www.kristeligt-dagblad.dk/",
            "justification": "Leading Christian newspaper, influential in religious and ethical debates, known for its focus on social and cultural issues."
        },
        {
            "country": "Denmark",
            "newspaper_name": "Weekendavisen",
            "location": "Copenhagen",
            "editorial": "center-left",
            "url": "https://www.weekendavisen.dk/",
            "justification": "Highly respected weekly newspaper, known for its in-depth articles and insightful commentary on political and cultural issues."
        },
        {
            "country": "Denmark",
            "newspaper_name": "Fyens Stiftstidende",
            "location": "Odense",
            "editorial": "center",
            "url": "https://www.fyens.dk/",
            "justification": "Leading regional newspaper in Funen, strong influence in local politics and business, known for its focus on regional news and issues."
        },
        {
            "country": "Denmark",
            "newspaper_name": "Århus Stiftstidende",
            "location": "Aarhus",
            "url": "https://www.stiften.dk/",
            "justification": "Leading regional newspaper in Jutland, strong influence in local politics and business, known for its focus on regional news and issues."
        }
    ],
    "Estonia": [
        {
            "country": "Estonia",
            "newspaper_name": "Postimees",
            "location": "Tallinn",
            "editorial": "center-right",
            "url": "https://www.postimees.ee/",
            "justification": "Largest daily readership (266,000 daily readers in 2023), strong investigative journalism, dominant market position, online presence across multiple platforms."
        },
        {
            "country": "Estonia",
            "newspaper_name": "Õhtuleht",
            "location": "Tallinn",
            "editorial": "populist",
            "url": "https://www.ohtuleht.ee/",
            "justification": "Second largest daily readership (209,000 daily readers in 2023), focus on sensational news and human-interest stories, significant reach among younger demographics."
        },
        {
            "country": "Estonia",
            "newspaper_name": "Eesti Päevaleht",
            "location": "Tallinn",
            "editorial": "center-left",
            "url": "https://www.epl.ee/",
            "justification": "Third largest daily readership (125,000 daily readers in 2023), respected for its in-depth analyses and coverage of political and social issues."
        },
        {
            "country": "Estonia",
            "newspaper_name": "Äripäev",
            "location": "Tallinn",
            "url": "https://www.aripaev.ee/",
            "justification": "Leading business newspaper, influential in economic circles, strong online presence, provides comprehensive coverage of the Estonian economy."
        },
        {
            "country": "Estonia",
            "newspaper_name": "Sirp",
            "location": "Tallinn",
            "url": "https://www.sirp.ee/",
            "justification": "Longest-running cultural newspaper, respected for its critical commentary on social, cultural, and political issues, provides a platform for diverse voices."
        }
    ],
    "Finland": [
        {
            "country": "Finland",
            "newspaper_name": "Helsingin Sanomat",
            "location": "Helsinki",
            "editorial": "center-right",
            "url": "https://www.hs.fi/",
            "justification": "Largest circulation (both print and digital), strong investigative journalism, historical influence shaping Finnish public discourse, influential among elites and opinion leaders."
        },
        {
            "country": "Finland",
            "location": "Helsinki",
            "newspaper_name": "Ilta-Sanomat",
            "url": "https://www.is.fi/",
            "justification": "Second largest circulation (both print and digital), strong focus on breaking news and popular topics, significant reach across demographics, known for sensational headlines."
        },
        {
            "country": "Finland",
            "location": "Tampere",
            "newspaper_name": "Aamulehti",
            "url": "https://www.aamulehti.fi/",
            "justification": "Third largest circulation (both print and digital), strong regional influence in western Finland, respected for in-depth reporting and analysis."
        },
        {
            "country": "Finland",
            "location": "Helsinki",
            "newspaper_name": "Hufvudstadsbladet",
            "url": "https://hbl.fi/",
            "justification": "Leading Swedish-language newspaper, influential among the Swedish-speaking minority, respected for its focus on cultural and political issues."
        },
        {
            "country": "Finland",
            "location": "Helsinki",
            "newspaper_name": "Helsingin Uutiset",
            "url": "https://www.helsinginuutiset.fi/",
            "justification": "Free paper focusing on local news and human-interest stories, significant reach in Helsinki metropolitan area, known for its investigative journalism."
        },
        {
            "country": "Finland",
            "location": "Helsinki",
            "newspaper_name": "Kauppalehti",
            "url": "https://www.kauppalehti.fi/",
            "justification": "Leading business newspaper, influential in economic circles and policy debates, respected for its financial reporting and analysis."
        },
        {
            "country": "Finland",
            "location": "Oulu",
            "newspaper_name": "Kaleva",
            "url": "https://www.kaleva.fi/",
            "justification": "Leading newspaper in northern Finland, strong regional influence, respected for its focus on local issues and investigative journalism."
        },
        {
            "country": "Finland",
            "location": "Helsinki",
            "newspaper_name": "Turun Sanomat",
            "url": "https://www.ts.fi/",
            "justification": "Leading newspaper in southwestern Finland, respected for its comprehensive coverage of regional news and in-depth analyses."
        },
        {
            "country": "Finland",
            "location": "Helsinki",
            "newspaper_name": "Suomen Kuvalehti",
            "url": "https://suomenkuvalehti.fi/",
            "justification": "Weekly news magazine with cultural and social focus, popular among intellectuals and opinion leaders, respected for its high-quality journalism and insightful commentary."
        },
        {
            "country": "Finland",
            "location": "Helsinki",
            "newspaper_name": "Iltalehti",
            "url": "https://www.iltalehti.fi/",
            "justification": "Popular online tabloid with a large reach, especially among younger demographics, known for its focus on entertainment and celebrity news, has expanded into investigative journalism."
        }
    ],
    "France": [
        {
            "country": "France",
            "newspaper_name": "Le Monde",
            "location": "Paris",
            "editorial": "center-left",
            "url": "https://www.lemonde.fr/",
            "justification": "Renowned national daily, considered the French newspaper of record, strong journalistic integrity, influential among intellectuals and elites."
        },
        {
            "country": "France",
            "location": "Paris",
            "newspaper_name": "Le Figaro",
            "url": "https://www.lefigaro.fr/",
            "justification": "National daily with center-right leaning, respected for its analytical reporting and strong business section, significant reach among conservative audience."
        },
        {
            "country": "France",
            "location": "Paris",
            "newspaper_name": "Libération",
            "url": "https://www.liberation.fr/",
            "justification": "National daily known for its left-wing stance and investigative journalism, influential in cultural and political debates, known for its critical commentary."
        },
        {
            "country": "France",
            "location": "Paris",
            "newspaper_name": "Les Échos",
            "url": "https://www.lesechos.fr/",
            "justification": "Leading financial newspaper, highly influential in economic circles, respected for its in-depth analyses and market data, strong digital presence."
        },
        {
            "country": "France",
            "location": "Paris",
            "newspaper_name": "Le Parisien",
            "url": "https://www.leparisien.fr/",
            "justification": "Highest circulation national daily, popular tabloid format, covers local and national news with a focus on human-interest stories, significant reach across demographics."
        },
        {
            "country": "France",
            "location": "Paris",
            "newspaper_name": "Mediapart",
            "url": "https://www.mediapart.fr/",
            "justification": "Leading online investigative journalism platform, known for its critical analyses of political and social issues, influential among left-wing circles and intellectuals."
        },
        {
            "country": "France",
            "location": "Paris",
            "newspaper_name": "L'Express",
            "url": "https://www.lexpress.fr/",
            "justification": "Weekly news magazine with center-right leaning, focuses on in-depth political and social analyses, respected for its investigative features and commentary."
        },
        {
            "country": "France",
            "location": "Paris",
            "newspaper_name": "La Croix",
            "url": "https://www.la-croix.com/",
            "justification": "Leading Catholic newspaper, respected for its ethical and social commentary, influences debates on religion, bioethics, and cultural issues."
        },
        {
            "country": "France",
            "location": "Rennes",
            "newspaper_name": "Ouest-France",
            "url": "https://www.ouest-france.fr/",
            "justification": "Highest circulation regional daily, dominant influence in western France, focuses on local news with national coverage of major events."
        },
        {
            "country": "France",
            "location": "Lyon",
            "newspaper_name": "Le Progrès",
            "url": "https://www.leprogres.fr/",
            "justification": "Leading regional daily in eastern France, influential in Lyon and surrounding areas, respected for its in-depth reporting and local investigative journalism."
        }
    ],    
    "Germany": [
        {
            "country": "Germany",
            "newspaper_name": "Bild",
            "location": "Berlin",
            "editorial": "Center-right",
            "url": "https://www.bild.de/",
            "justification": "Highest circulation in Germany, strong tabloid presence, influences public opinion."
        },
        {
            "country": "Germany",
            "newspaper_name": "Süddeutsche Zeitung",
            "location": "Munich",
            "editorial": "Center-left/Left-liberal",
            "url": "https://www.sueddeutsche.de/",
            "justification": "Renowned for investigative journalism, respected for in-depth analysis, influential across demographics."
        },
        {
            "country": "Germany",
            "newspaper_name": "Frankfurter Allgemeine Zeitung (FAZ)",
            "location": "Frankfurt am Main",
            "editorial": "Center-right/Moderately conservative to liberal",
            "url": "https://www.faz.net/aktuell/",
            "justification": "Highly respected for quality journalism and commentary, strong influence on political discourse."
        },
        {
            "country": "Germany",
            "newspaper_name": "Die Zeit",
            "location": "Hamburg",
            "editorial": "Center-left",
            "url": "https://www.zeit.de/english/index",
            "justification": "Weekly newspaper known for in-depth features and intellectual essays, influential amongst cultural and political elites."
        },
        {
            "country": "Germany",
            "newspaper_name": "Der Spiegel",
            "location": "Hamburg",
            "editorial": "Center-left",
            "url": "https://www.spiegel.de/international/",
            "justification": "Leading investigative magazine, known for critical reporting and uncovering political scandals."
        },
        {
            "country": "Germany",
            "newspaper_name": "Handelsblatt",
            "location": "Düsseldorf",
            "editorial": "Center-right",
            "url": "https://www.handelsblatt.com/",
            "justification": "Leading business newspaper, influential in economic circles and policy debates."
        },
        {
            "country": "Germany",
            "newspaper_name": "Berliner Morgenpost",
            "location": "Berlin",
            "editorial": "Center-right",
            "url": "https://www.morgenpost.de/",
            "justification": "Largest regional newspaper in Berlin, strong local influence and readership."
        },
        {
            "country": "Germany",
            "newspaper_name": "Südwest Presse",
            "location": "Ulm",
            "editorial": "Center-right",
            "url": "https://www.swp.de/",
            "justification": "Leading regional newspaper in southwestern Germany, influential in Baden-Württemberg."
        },
        {
            "country": "Germany",
            "newspaper_name": "Frankfurter Rundschau",
            "location": "Frankfurt am Main",
            "editorial": "Center-left",
            "url": "https://www.fr.de/",
            "justification": "Renowned for investigative journalism and social commentary, strong presence in Frankfurt/Rhine-Main region."
        },
        {
            "country": "Germany",
            "newspaper_name": "taz, die tageszeitung",
            "location": "Berlin",
            "editorial": "Left-wing",
            "url": "https://taz.de/",
            "justification": "Leading left-wing daily, influential in intellectual and political circles, known for strong editorial stance."
        }
    ],
    "Greece": [
        {
            "country": "Greece",
            "newspaper_name": "Kathimerini",
            "location": "Athens",
            "editorial": "center-left",
            "url": "https://www.kathimerini.com/",
            "justification": "Largest daily readership, strong investigative journalism, historical influence shaping Greek political discourse."
        },
        {
            "country": "Greece",
            "newspaper_name": "Ta Nea",
            "location": "Athens",
            "editorial": "center-left",
            "url": "https://www.tanea.gr/",
            "justification": "Second largest daily readership, critical commentary, investigative reporting, prominent role in Greek history."
        },
        {
            "country": "Greece",
            "newspaper_name": "Ethnos",
            "location": "Athens",
            "editorial": "center-left",
            "url": "https://www.ethnos.gr/",
            "justification": "Historically significant, strong investigative journalism, support for democracy during junta, critical stance towards conservative governments."
        },
        {
            "country": "Greece",
            "newspaper_name": "Proto Thema",
            "location": "Athens",
            "editorial": "center-right",
            "url": "https://www.protothema.gr/",
            "justification": "Significant circulation, focus on current events, political coverage, reach and influence despite criticism."
        },
        {
            "country": "Greece",
            "newspaper_name": "Avgi",
            "location": "Athens",
            "editorial": "left-wing",
            "url": "https://www.avgi.gr/",
            "justification": "Loyal readership, critical analyses of economic and social issues, strong stance against government policies, consistent voice for leftist ideologies."
        },
        {
            "country": "Greece",
            "newspaper_name": "Documento",
            "url": "https://www.documentonews.gr/",
            "justification": "Left-wing weekly, prominent investigative journalism, tackling political scandals and corruption, critical counterpoint to mainstream media."
        },
        {
            "country": "Greece",
            "newspaper_name": "Eleftherotypia",
            "location": "Athens",
            "editorial": "center-left",
            "url": "https://www.eleftherotypia.gr/",
            "justification": "Long history, prominent voice, critical analyses, independent voice despite declining readership."
        },
        {
            "country": "Greece",
            "newspaper_name": "Naftemporiki",
            "location": "Athens",
            "editorial": "independent",
            "url": "https://www.naftemporiki.gr/",
            "justification": "Leading business and economic daily, strong online presence, valuable resource for investors and business professionals."
        },
        {
            "country": "Greece",
            "newspaper_name": "I Kathimerini",
            "location": "Athens",
            "editorial": "center-left",
            "url": "https://www.ikatimerini.gr/",
            "justification": "Sister publication to Kathimerini, Sunday newspaper, in-depth analyses, cultural commentary, critical perspectives."
        },
        {
            "country": "Greece",
            "newspaper_name": "To Vima",
            "location": "Athens",
            "editorial": "center-left",
            "url": "https://www.tovima.gr/",
            "justification": "Sunday newspaper, strong reputation, in-depth articles, diverse topics, critical perspectives on Greek politics and society."
        }
    ],
    "Hungary": [
        {
            "country": "Hungary",
            "newspaper_name": "Magyar Nemzet",
            "location": "Budapest",
            "editorial": "pro-government, right-wing",
            "url": "https://www.magyarnemzet.hu/",
            "justification": "Largest circulation daily newspaper in Hungary, closely associated with the current government and its policies, influential among conservative readers."
        },
        {
            "country": "Hungary",
            "newspaper_name": "Népszava",
            "location": "Budapest",
            "editorial": "left-wing",
            "url": "https://nepszava.hu/",
            "justification": "Second largest circulation daily, leading voice for the opposition and left-wing views, known for its critical reporting on the government."
        },
        {
            "country": "Hungary",
            "newspaper_name": "Origo",
            "location": "Budapest",
            "url": "https://www.origo.hu/",
            "justification": "Leading online news portal, reaches a wide audience across the political spectrum, known for its mix of news, entertainment, and lifestyle content."
        },
        {
            "country": "Hungary",
            "newspaper_name": "Index.hu",
            "location": "Budapest",
            "url": "https://index.hu/",
            "justification": "Popular independent online news portal, known for its investigative journalism and critical commentary on political and social issues."
        },
        {
            "country": "Hungary",
            "newspaper_name": "Telex",
            "location": "Budapest",
            "url": "https://telex.hu/",
            "justification": "Online news platform launched by former journalists of Index.hu, known for its independent and critical reporting, enjoys strong support among younger demographics."
        },
        {
            "country": "Hungary",
            "newspaper_name": "HVG",
            "location": "Budapest",
            "editorial": "center-right",
            "url": "https://hvg.hu/",
            "justification": "Weekly political and business magazine, known for its in-depth analyses and investigative reporting, influential among business and political circles."
        },
        {
            "country": "Hungary",
            "newspaper_name": "Magyar Hírlap",
            "location": "Budapest",
            "editorial": "pro-government, center-right",
            "url": "https://magyarhirlap.hu/",
            "justification": "Daily newspaper with strong ties to the government, known for its conservative editorial stance and focus on national issues."
        },
        {
            "country": "Hungary",
            "newspaper_name": "Blikk",
            "location": "Budapest",
            "editorial": "populist",
            "url": "https://www.blikk.hu/",
            "justification": "Highest circulation tabloid newspaper, known for its sensational headlines and focus on entertainment and celebrity news, reaches a large audience across demographics."
        },
        {
            "country": "Hungary",
            "newspaper_name": "Átlátszó",
            "location": "Budapest",
            "url": "https://atlatszo.hu/",
            "justification": "Prominent investigative journalism platform, focused on uncovering corruption and holding power accountable, shares Népszabadság's commitment to fact-checking and in-depth reporting."
        },
        {
            "country": "Hungary",
            "newspaper_name": "Magyar Idők",
            "location": "Budapest",
            "editorial": "pro-government, right-wing",
            "url": "https://magyaridok.hu/",
            "justification": "Daily newspaper known for its strong support of the government and its policies, often publishes controversial articles and opinions."
        }
    ],
    "Ireland": [
        {
            "country": "Ireland",
            "newspaper_name": "Irish Independent",
            "location": "Dublin",
            "editorial": "center-right",
            "url": "https://www.independent.ie/",
            "justification": "Highest daily print circulation, strong investigative journalism, dominant market position, online presence across multiple platforms, historical influence shaping Irish public discourse."
        },
        {
            "country": "Ireland",
            "newspaper_name": "Irish Times",
            "location": "Dublin",
            "editorial": "center-left",
            "url": "https://www.irishtimes.com/",
            "justification": "Respected for in-depth analyses and coverage of political and social issues, influential among intellectuals and elites, historical significance shaping Irish journalism."
        },
        {
            "country": "Ireland",
            "newspaper_name": "Irish Examiner",
            "location": "Cork",
            "location": "center-right",
            "url": "https://www.irishexaminer.com/",
            "justification": "Leading regional daily in southern Ireland, respected for independent voice and strong regional coverage, established history in Irish journalism."
        },
        {
            "country": "Ireland",
            "newspaper_name": "Irish Daily Mail",
            "location": "Dublin",
            "url": "https://www.dailymail.ie/",
            "justification": "Second highest daily print circulation, focus on breaking news and popular topics, significant reach across demographics, known for sensational headlines."
        },
        {
            "country": "Ireland",
            "newspaper_name": "Irish Sun",
            "location": "Dublin",
            "url": "https://www.thesun.ie/",
            "justification": "Highest circulation tabloid, popular among working-class readers, focus on entertainment and celebrity news, significant reach and influence."
        },
        {
            "country": "Ireland",
            "newspaper_name": "The Journal",
            "url": "https://www.thejournal.ie/",
            "justification": "Leading online news platform, known for innovative journalism and breaking news coverage, significant reach among younger demographics."
        },
        {
            "country": "Ireland",
            "location": "Galway",
            "newspaper_name": "Galway Advertiser",
            "url": "https://www.advertiser.ie/",
            "justification": "Leading daily newspaper in western Ireland, respected for its independent voice and strong regional coverage, balances Dublin-centric focus, offers different perspective on national issues."
        },
        {
            "country": "Ireland",
            "newspaper_name": "Sunday Independent",
            "location": "Dublin",
            "editorial": "center-right",
            "url": "https://www.independent.ie/sunday-independent/",
            "justification": "Weekly newspaper known for its strong investigative journalism, often tackling political and social scandals, offers distinct perspective compared to daily papers, complements existing focus on investigative reporting."
        },
        {
            "country": "Ireland",
            "newspaper_name": "Dublin Gazette",
            "location": "Dublin",
            "url": "https://www.gov.ie/gazeda/",
            "justification": "Official state gazette, publishes legal notices and government announcements, historical record of Irish legislation and official actions."
        },
        {
            "country": "Ireland",
            "newspaper_name": "Meath Chronicle",
            "location": "Navan",
            "url": "https://www.meathchronicle.ie/",
            "justification": "Example of strong regional newspaper outside Dublin, influential in Meath and surrounding areas, reflects diversity of voices in Irish media landscape."
        }
    ], 
    "Italy": [
        {
            "country": "Italy",
            "newspaper_name": "Corriere della Sera",
            "location": "Milan",
            "editorial": "center-left",
            "url": "https://www.corriere.it/",
            "justification": "Largest daily readership, strong investigative journalism, historical influence shaping Italian political discourse, national reach and online presence."
        },
        {
            "country": "Italy",
            "newspaper_name": "La Repubblica",
            "location": "Rome",
            "editorial": "center-left",
            "url": "https://www.repubblica.it/",
            "justification": "Second largest daily readership, critical commentary and investigative reporting, prominent historical role during political shifts, respected across Italy."
        },
        {
            "country": "Italy",
            "newspaper_name": "Il Sole 24 Ore",
            "location": "Milan",
            "editorial": "independent",
            "url": "https://www.ilsole24ore.com/",
            "justification": "Leading business and economic daily, in-depth analyses and valuable resource for investors, strong influence in financial circles and economic policy debates."
        },
        {
            "country": "Italy",
            "newspaper_name": "Avvenire",
            "location": "Milan",
            "editorial": "Catholic",
            "url": "https://www.avvenire.it/",
            "justification": "Leading Catholic newspaper, influential among religious communities, voice for Catholic perspectives on social and political issues, historical significance representing Christian values."
        },
        {
            "country": "Italy",
            "location": "Turin",
            "newspaper_name": "La Stampa",
            "editorial": "center-left",
            "url": "https://www.lastampa.it/",
            "justification": "Respected for in-depth analyses and cultural commentary, historical significance in shaping Northern Italian journalism, known for independent voice and critical perspectives."
        },
        {
            "country": "Italy",
            "newspaper_name": "Il Messaggero",
            "location": "Rome",
            "url": "https://www.ilmessaggero.it/",
            "justification": "Significant readership in Rome and central Italy, focus on regional news and national politics, historical importance shaping Roman public discourse."
        },
        {
            "country": "Italy",
            "location": "Bologna",
            "newspaper_name": "Il Resto del Carlino",
            "url": "https://www.ilrestodelcarlino.it/",
            "justification": "Leading daily in northern Italy, strong regional coverage, influential in Emilia-Romagna and neighboring regions, historical prominence in Italian journalism."
        },
        {
            "country": "Italy",
            "location": "Naples",
            "newspaper_name": "Il Mattino",
            "url": "https://www.ilmattino.it/",
            "justification": "Main newspaper in southern Italy, significant regional influence, voice for southern issues and perspectives, historical role in shaping Neapolitan journalism."
        },
        {
            "country": "Italy",
            "newspaper_name": "L'Espresso",
            "location": "Rome",
            "url": "https://www.espresso.repubblica.it/",
            "justification": "Respected weekly news magazine, known for investigative journalism and critical analyses, focuses on politics, social issues, and cultural commentary, influences national debates."
        },
        {
            "country": "Italy",
            "location": "Milan",
            "newspaper_name": "La Verità",
            "editorial": "right-wing",
            "url": "https://www.laverita.info/",
            "justification": "Controversial right-wing newspaper known for its strong opinions and critical perspectives on Italian politics and society, offers alternative viewpoint and influences right-wing debates."
        },
        {
            "country": "Italy",
            "newspaper_name": "Il Foglio",
            "location": "Rome",
            "editorial": "center-right",
            "url": "https://www.ilfoglio.it/",
            "justification": "Prominent center-right daily known for its political commentary, critical analyses, and intellectual essays, offers distinct voice in Italian political discourse, influential among conservative and liberal circles."
        }
    ],
    "Latvia": [
        {
            "country": "Latvia",
            "newspaper_name": "Diena",
            "location": "Riga",
            "editorial": "center-left",
            "url": "https://www.diena.lv/",
            "justification": "Largest daily readership, high-quality journalism, historical impact shaping Latvian political discourse, strong online presence."
        },
        {
            "country": "Latvia",
            "newspaper_name": "Latvijas Avīze",
            "location": "Riga",
            "editorial": "center-right",
            "url": "https://www.la.lv/",
            "justification": "Second largest daily readership, respected for in-depth analyses and critical commentary, historical importance during Latvian independence movement."
        },
        {
            "country": "Latvia",
            "newspaper_name": "Neatkarīgā Rīta Avīze",
            "location": "Riga",
            "editorial": "center-left",
            "url": "https://nra.lv/",
            "justification": "Leading investigative reporting, critical stance towards government policies, loyal readership, distinct voice in Latvian media landscape."
        },
        {
            "country": "Latvia",
            "newspaper_name": "Delfi.lv",
            "location": "Riga",
            "url": "https://www.delfi.lv/",
            "url": "https://www.tvnet.lv/",
            "justification": "Most visited online news portal, owned by Estonian media group Ekspress Grupp, broad reach across demographics, mix of news, entertainment, and lifestyle content."
        },
        {
            "country": "Latvia",
            "newspaper_name": "Ir",
            "location": "Riga",
            "editorial": "independent",
            "url": "https://www.ir.lv/",
            "justification": "Respected daily newspaper known for intellectual commentary, critical analyses, and focus on cultural and social issues, influential among opinion leaders, offers distinct voice in Latvian media landscape."
        }
    ],
    "Netherlands": [
        {
            "country": "Netherlands",
            "newspaper_name": "Algemeen Dagblad",
            "location": "Rotterdam",
            "editorial": "center-right",
            "url": "https://www.ad.nl/",
            "justification": "Highest daily circulation, strong regional presence, historical influence shaping Dutch journalism, investigative reporting, online reach."
        },
        {
            "country": "Netherlands",
            "newspaper_name": "Telegraaf",
            "location": "Amsterdam",
            "editorial": "populist",
            "url": "https://www.telegraaf.nl/",
            "justification": "Second highest daily circulation, popular tabloid format, focus on sensational headlines and entertainment, significant reach across demographics."
        },
        {
            "country": "Netherlands",
            "newspaper_name": "NRC Handelsblad",
            "location": "Rotterdam",
            "editorial": "center-left",
            "url": "https://www.nrc.nl/",
            "justification": "Respected for in-depth analyses and critical commentary, influential among intellectuals and political elites, established history in Dutch journalism."
        },
        {
            "country": "Netherlands",
            "newspaper_name": "Volkskrant",
            "location": "Amsterdam",
            "editorial": "center-left",
            "url": "https://www.volkskrant.nl/",
            "justification": "Significant readership, focus on investigative journalism and social issues, respected voice in Dutch media landscape, online presence."
        },
        {
            "country": "Netherlands",
            "newspaper_name": "Trouw",
            "location": "Amsterdam",
            "editorial": "center-left",
            "url": "https://www.trouw.nl/",
            "justification": "Leading Christian newspaper, respected for balanced reporting and ethical stance, influential among religious communities, historical significance."
        },
        {
            "country": "Netherlands",
            "newspaper_name": "Het Parool",
            "location": "Amsterdam",
            "editorial": "center-left",
            "url": "https://www.parool.nl/",
            "justification": "Strong focus on Amsterdam news and politics, loyal local readership, online presence, historical role shaping Amsterdam discourse."
        },
        {
            "country": "Netherlands",
            "newspaper_name": "De Limburger",
            "location": "Heerlen",
            "url": "https://www.limburger.nl/",
            "justification": "Leading regional newspaper in southern Limburg, strong local influence, respected voice for regional perspectives and issues."
        },
        {
            "country": "Netherlands",
            "newspaper_name": "Het Financieele Dagblad",
            "location": "Amsterdam",
            "editorial": "independent",
            "url": "https://www.fd.nl/",
            "justification": "Leading business and financial newspaper, in-depth analyses and valuable resource for investors, strong influence in economic circles and policy debates."
        }
    ],
    "Portugal": [
        {
            "country": "Portugal",
            "newspaper_name": "Público",
            "location": "Lisbon",
            "editorial": "center-left",
            "url": "https://www.publico.pt/",
            "justification": "Highest quality journalism, respected for in-depth analyses and investigative reporting, historical influence shaping Portuguese public discourse, strong online presence."
        },
        {
            "country": "Portugal",
            "newspaper_name": "Expresso",
            "location": "Lisbon",
            "editorial": "independent",
            "url": "https://www.expresso.pt/",
            "justification": "Leading daily print circulation, strong investigative journalism, critical analyses, online reach across demographics, historical role in Portuguese journalism."
        },
        {
            "country": "Portugal",
            "newspaper_name": "Jornal de Notícias",
            "location": "Porto",
            "location": "center-right",
            "url": "https://www.jn.pt/",
            "justification": "Second highest daily print circulation, strong regional influence in northern Portugal, popular among older demographics, historical presence in Portuguese media."
        },
        {
            "country": "Portugal",
            "newspaper_name": "Observador",
            "location": "Lisbon",
            "url": "https://observador.pt/",
            "justification": "Leading online news platform, known for innovative journalism and breaking news coverage, strong influence among younger demographics, critical perspective."
        },
        {
            "country": "Portugal",
            "newspaper_name": "Diário de Notícias",
            "location": "Lisbon",
            "location": "center-left",
            "url": "https://www.dn.pt/",
            "justification": "Significant readership in southern Portugal, respected for balanced reporting and cultural coverage, historical role shaping Lisbon discourse."
        },
        {
            "country": "Portugal",
            "location": "Lisbon",
            "newspaper_name": "Correio da Manhã",
            "url": "https://www.cmjornal.pt/",
            "justification": "(Tabloid, consider replacing with investigative option like Visão or Sábado)"
        },
        {
            "country": "Portugal",
            "newspaper_name": "Visão",
            "location": "Lisbon",
            "url": "https://visao.pt/",
            "justification": "Weekly magazine known for strong investigative journalism, uncovering political and social scandals, influential among opinion leaders, complements daily news coverage."
        },
        {
            "country": "Portugal",
            "newspaper_name": "Sábado",
            "location": "Lisbon",
            "url": "https://www.sabado.pt/",
            "justification": "Weekly magazine known for investigative reporting and in-depth analyses, focus on politics, economy, and cultural issues, influential among intellectuals and elites."
        },
        {
            "country": "Portugal",
            "location": "Lisbon",
            "newspaper_name": "Sol",
            "url": "https://www.sol.pt/",
            "justification": "(Tabloid, consider replacing with regional option like Diário de Aveiro or Público.pt regional editions)"
        },
        {
            "country": "Portugal",
            "newspaper_name": "Diário de Aveiro",
            "location": "Aveiro",
            "url": "https://www.diarioaveiro.pt/",
            "justification": "Leading regional newspaper in central Portugal, respected for local coverage and commentary, strong historical presence in regional journalism."
        }
        ]
}

test = pd.DataFrame(newspapers["Germany"])