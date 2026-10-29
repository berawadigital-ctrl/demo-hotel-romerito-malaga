# Contenido de la demo Hotel Romerito (Malaga) (es/ca/en/fr). Hechos de hotelromerito.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Doble con balcón y Twin con terraza','Familiar, Triple y Cuádruple','Individual y Adaptada'],'ca':['Doble amb balcó i Twin amb terrassa','Familiar, Triple i Quàdruple','Individual i Adaptada'],'en':['Double with balcony and Twin with terrace','Family, Triple and Quadruple','Single and Accessible'],'fr':['Double avec balcon et Twin avec terrasse','Familiale, Triple et Quadruple','Individuelle et Adaptée']}
RD={
'es':['La doble con cama de 150 cm y balcón con vistas al patio andaluz con fuente; la twin con dos camas individuales y terraza privada.','La familiar con cama de 135 cm y una individual; la triple con tres camas de 105 cm y la cuádruple con cuatro.','La individual con cama de 105 cm, y la adaptada, sin barreras y con baño amplio para personas con movilidad reducida.'],
'ca':['La doble amb llit de 150 cm i balcó amb vistes al pati andalús amb font; la twin amb dos llits individuals i terrassa privada.','La familiar amb llit de 135 cm i un d\'individual; la triple amb tres llits de 105 cm i la quàdruple amb quatre.','La individual amb llit de 105 cm, i l\'adaptada, sense barreres i amb bany ampli per a persones amb mobilitat reduïda.'],
'en':['The double with a 150 cm bed and a balcony overlooking the Andalusian patio with its fountain; the twin with two single beds and a private terrace.','The family room with a 135 cm bed plus a single; the triple with three 105 cm beds and the quadruple with four.','The single with a 105 cm bed, and the accessible room, barrier-free with a large bathroom for people with reduced mobility.'],
'fr':['La double avec lit de 150 cm et balcon donnant sur le patio andalou et sa fontaine ; la twin avec deux lits simples et terrasse privée.','La familiale avec lit de 135 cm et un lit simple ; la triple avec trois lits de 105 cm et la quadruple avec quatre.','L\'individuelle avec lit de 105 cm, et l\'adaptée, sans obstacles et avec grande salle de bain pour les personnes à mobilité réduite.']}
ART={
'hero':('arches',9601,['#f1e6d6','#e7b98a','#b5562f','#7a2f17','#4a1c0d']),
'intro':('waves',9602,['#2e5e4e','#f1c48c','#f8e2bd','#3f7a66','#2e5e4e','#1b3a30']),
'r1':('columns',9611,['#eef0ec','#f7f8f5','#c0663a','#7a2f17','#4a1c0d']),
'r2':('hills',9612,['#e5ede8','#f1ead6','#efc07c','#a6c0a1','#7b9f86','#527763']),
'r3':('skyline',9613,['#7a2f17','#e8a46a','#f6d5a4','#1f4d40','#1a4036','#112b24']),
'g1':('arches',9621,['#f0e4d3','#e4b585','#b2532c','#7a2f17','#4a1c0d']),
'g2':('waves',9622,['#28574a','#efc086','#f6dfb8','#38735f','#28574a','#173329']),
'g3':('columns',9623,['#ecefea','#f5f7f3','#bd6337','#7a2f17','#4a1c0d']),
'g4':('hills',9624,['#e2ebe5','#efe8d2','#edbd78','#a3bd9e','#789c83','#4f7460']),
'g5':('skyline',9625,['#7a2f17','#e5a166','#f5d3a0','#1d493d','#183c33','#102822']),
'g6':('arches',9626,['#eee2d0','#e1b281','#af5029','#7a2f17','#4a1c0d'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Romerito · Hotel con patio andaluz en Málaga',see_rooms='Ver habitaciones',hero_k='Málaga',hero_t='Su hotel con acento malagueño',hero_s='Patio andaluz con fuente, gimnasio gratuito y parada de la línea 20 de autobús en la misma puerta.',
 intro_t='Un patio andaluz a 10-15 minutos del aeropuerto',intro_p1='El hotel está en la calle Espacio, a unos 6 km del centro histórico y a apenas 1 km del Palacio de Ferias y Congresos y del Auditorio Municipal.',
 intro_p2='99 habitaciones de 8 tipos con aire acondicionado, calefacción y wifi gratis, recepción 24/7 y un restaurante abierto al público los 365 días del año.',
 stats=['Patio andaluz','Gimnasio gratuito','Recepción 24/7','Bus 20 en la puerta'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Dobles, twin, familiares, triples, cuádruples, individuales y adaptadas. Entrada desde las 14:00 y salida hasta las 12:00.',
 svcs=['Wifi de alta velocidad en todo el hotel','Gimnasio de uso gratuito','Restaurante abierto los 365 días','Salón para eventos','Parada del bus 20 frente al hotel','Habitaciones adaptadas','Garaje privado cubierto (de pago)','Patio andaluz con fuente'],
 loc_p='C/ Espacio, 48-50 · 29006 Málaga. A unos 6 km del centro y a 10-15 minutos en coche del aeropuerto.',
 chips=['¿Qué habitaciones tiene?','¿Tiene parking?','¿Cómo llego al centro?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Romerito · Hotel amb pati andalús a Màlaga',see_rooms='Veure habitacions',hero_k='Màlaga',hero_t='El seu hotel amb accent malagueny',hero_s='Pati andalús amb font, gimnàs gratuït i parada de la línia 20 d\'autobús a la mateixa porta.',
 intro_t='Un pati andalús a 10-15 minuts de l\'aeroport',intro_p1='L\'hotel és al carrer Espacio, a uns 6 km del centre històric i a tot just 1 km del Palau de Fires i Congressos i de l\'Auditori Municipal.',
 intro_p2='99 habitacions de 8 tipus amb aire condicionat, calefacció i wifi gratis, recepció 24/7 i un restaurant obert al públic els 365 dies de l\'any.',
 stats=['Pati andalús','Gimnàs gratuït','Recepció 24/7','Bus 20 a la porta'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Dobles, twin, familiars, triples, quàdruples, individuals i adaptades. Entrada des de les 14:00 i sortida fins a les 12:00.',
 svcs=['Wifi d\'alta velocitat a tot l\'hotel','Gimnàs d\'ús gratuït','Restaurant obert els 365 dies','Saló per a esdeveniments','Parada del bus 20 davant l\'hotel','Habitacions adaptades','Garatge privat cobert (de pagament)','Pati andalús amb font'],
 loc_p='C/ Espacio, 48-50 · 29006 Màlaga. A uns 6 km del centre i a 10-15 minuts en cotxe de l\'aeroport.',
 chips=['Quines habitacions té?','Té pàrquing?','Com arribo al centre?','Com es reserva?']),
'en':dict(title='Hotel Romerito · Hotel with an Andalusian patio in Málaga',see_rooms='See the rooms',hero_k='Málaga',hero_t='Your hotel with a Málaga accent',hero_s='Andalusian patio with a fountain, free gym and a line 20 bus stop right at the door.',
 intro_t='An Andalusian patio 10-15 minutes from the airport',intro_p1='The hotel is on Calle Espacio, about 6 km from the historic centre and barely 1 km from the Trade Fair and Congress Centre and the Municipal Auditorium.',
 intro_p2='99 rooms of 8 types with air conditioning, heating and free wifi, 24/7 reception and a restaurant open to the public 365 days a year.',
 stats=['Andalusian patio','Free gym','24/7 reception','Bus 20 at the door'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Doubles, twins, family, triple, quadruple, single and accessible rooms. Check-in from 14:00 and check-out until 12:00.',
 svcs=['High-speed wifi throughout the hotel','Free gym','Restaurant open 365 days','Events room','Bus 20 stop opposite the hotel','Accessible rooms','Private covered garage (paid)','Andalusian patio with fountain'],
 loc_p='C/ Espacio, 48-50 · 29006 Málaga. About 6 km from the centre and 10-15 minutes by car from the airport.',
 chips=['What rooms does it have?','Is there parking?','How do I get to the centre?','How do I book?']),
'fr':dict(title='Hotel Romerito · Hôtel avec patio andalou à Malaga',see_rooms='Voir les chambres',hero_k='Malaga',hero_t='Votre hôtel à l\'accent de Malaga',hero_s='Patio andalou avec fontaine, salle de sport gratuite et arrêt de la ligne de bus 20 juste devant la porte.',
 intro_t='Un patio andalou à 10-15 minutes de l\'aéroport',intro_p1='L\'hôtel se trouve rue Espacio, à environ 6 km du centre historique et à peine 1 km du Palais des Foires et Congrès et de l\'Auditorium municipal.',
 intro_p2='99 chambres de 8 types avec climatisation, chauffage et wifi gratuit, réception 24h/24 et 7j/7 et un restaurant ouvert au public 365 jours par an.',
 stats=['Patio andalou','Salle de sport gratuite','Réception 24h/24','Bus 20 devant la porte'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Doubles, twin, familiales, triples, quadruples, individuelles et adaptées. Arrivée à partir de 14h00 et départ jusqu\'à 12h00.',
 svcs=['Wifi haut débit dans tout l\'hôtel','Salle de sport gratuite','Restaurant ouvert 365 jours','Salle pour événements','Arrêt du bus 20 face à l\'hôtel','Chambres adaptées','Garage privé couvert (payant)','Patio andalou avec fontaine'],
 loc_p='C/ Espacio, 48-50 · 29006 Malaga. À environ 6 km du centre et à 10-15 minutes en voiture de l\'aéroport.',
 chips=['Quelles chambres a-t-il ?','Y a-t-il un parking ?','Comment aller au centre ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://www.hotelromerito.com/bookingstep1/'; REN='https://www.hotelromerito.com/en/bookingstep1/'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':REN,'fr':REN})
D=dict(name='Hotel Romerito',ac='#6b3a1f',ac2='#2f6b5a',ac2_a11y='#235246',book=BOOK,around=[],foot=FOOT,
 address='C/ Espacio, 48-50 · 29006 Málaga',phones=['+34 952 36 35 48'],emails=['info@hotelromerito.com'],maps='Hotel Romerito, Calle Espacio 48, Málaga',t=T)
META=dict(repo='demo-hotel-romerito-malaga',name='Hotel Romerito',legal_name='Hotel El Romerito, S.L.',registry_ids=['CIF B92714005','Registro de Turismo de Andalucía H/MA/01678'],
 url='https://www.hotelromerito.com/',domain='hotelromerito.com',municipality='Málaga',province='Málaga',sector='hotel con patio andaluz junto al Palacio de Ferias de Málaga',
 read_at='2026-10-29T14:54:00+01:00',created_at='2026-10-29T14:54:00+01:00',built_at='2026-10-29T15:05:00+01:00',audit_date='2026-10-29T14:52:00+01:00',
 rating=dict(value=4.2,coincide=['telefono','web'],date='2026-10-29T10:23:36+01:00',url='https://www.google.com/maps/place/Hotel+Romerito/@36.6992261,-4.4791506,17z/data=!4m13!1m2!2m1!1sHotel+El+Romerito+M%C3%A1laga!3m9!1s0xd72f756235766db:0x5c0b914d6f7d5979!5m2!4m1!1i2!8m2!3d36.6992261!4d-4.4746445!15sChlIb3RlbCBFbCBSb21lcml0byBNw6FsYWdhkgEFaG90ZWzgAQA!16s%2Fg%2F1tdcn9ql'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas del propio hotel (hotelromerito.com/bookingstep1, pagina del propio dominio que carga el componente de tarifas de Mirai del hotel, data-mirai-id 518696040; version /en/ para ingles y frances); la demo no construye ningun motor.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Tiene habitaciones para familias?','K02'),('¿Tiene habitación adaptada?','K03'),('¿Dónde está?','K04'),('¿Tiene parking?','K05'),('¿A qué distancia está el aeropuerto?','K06'),('¿Tiene restaurante?','K07'),('¿Hay gimnasio?','K08'),('¿A qué hora es el check-in?','K09'),('¿Tienen salón para eventos?','K10'),('¿Cómo reservo?','K11'),('¿Quién es el titular?','K12'),('¿Hay wifi?','K13'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K11'),('¿Tienen spa?',None),('¿Admiten mascotas?',None)],
'ca':[('Quines habitacions té?','K01'),('Té habitacions per a famílies?','K02'),('Té habitació adaptada?','K03'),('On és?','K04'),('Té pàrquing?','K05'),('A quina distància és l\'aeroport?','K06'),('Té restaurant?','K07'),('Hi ha gimnàs?','K08'),('A quina hora és el check-in?','K09'),('Teniu saló per a esdeveniments?','K10'),('Com reservo?','K11'),('Qui és el titular?','K12'),('Hi ha wifi?','K13'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K11'),('Teniu spa?',None),('Admeteu mascotes?',None)],
'en':[('What rooms does it have?','K01'),('Are there family rooms?','K02'),('Is there an accessible room?','K03'),('Where is it?','K04'),('Is there parking?','K05'),('How far is the airport?','K06'),('Is there a restaurant?','K07'),('Is there a gym?','K08'),('What time is check-in?','K09'),('Do you have an events room?','K10'),('How do I book?','K11'),('Who is the owner?','K12'),('Is there wifi?','K13'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K11'),('Do you have a spa?',None),('Are pets allowed?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Y a-t-il des chambres familiales ?','K02'),('Y a-t-il une chambre adaptée ?','K03'),('Où est-il ?','K04'),('Y a-t-il un parking ?','K05'),('À quelle distance est l\'aéroport ?','K06'),('Y a-t-il un restaurant ?','K07'),('Y a-t-il une salle de sport ?','K08'),('À quelle heure est l\'arrivée ?','K09'),('Avez-vous une salle pour événements ?','K10'),('Comment réserver ?','K11'),('Qui est le titulaire ?','K12'),('Y a-t-il le wifi ?','K13'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K11'),('Avez-vous un spa ?',None),('Les animaux sont-ils admis ?',None)]}
