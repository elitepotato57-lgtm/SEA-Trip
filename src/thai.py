# ================= THAILAND DEEP DATA (researched Nov 2026) =================
# Loaded by data.py. Pins are approximate (ap=True): the app snaps each one to Google's exact spot the first time it's opened.
_existing = {p["n"].lower() for p in places}
def _ok(n):
    if n.lower() in _existing: return False
    _existing.add(n.lower()); return True
def TG(id, n, city, lat, lng, p=None, cur="THB", r=None, rs=None, rc=None, s=(), t=("Hostel",), d=None, src=(), tips=(), pu=None):
    if not _ok(n): return
    add(c="gaff", id=id, n=n, cc="TH", city=city, lat=lat, lng=lng, p=list(p) if p else None, cur=cur if p else None,
        pu=pu or (DORM if "Hostel" in t else "room, per night, from"), r=r, rs=rs, rc=rc, s=list(s), t=list(t), d=d, src=list(src), tips=list(tips), ap=True)
def TM(id, n, city, lat, lng, p=None, s=(), best=None, tips=(), src=(), t=("Street food",), pu="per dish, typical", cur="THB"):
    if not _ok(n): return
    add(c="munch", id=id, n=n, cc="TH", city=city, lat=lat, lng=lng, p=list(p) if p else None, cur=cur if p else None, pu=pu,
        s=list(s), t=list(t), best=best, tips=list(tips), src=list(src), verified=bool(src) and bool(p), ap=True)
def TC(id, n, city, lat, lng, t, s=(), p=None, cost=None, best=None, busy=None, tips=(), src=(), cur="THB"):
    if not _ok(n): return
    add(c="cool", id=id, n=n, cc="TH", city=city, lat=lat, lng=lng, t=list(t), p=list(p) if p else None, cur=cur if p else None, pu="entry",
        s=list(s), cost=cost, best=best, busy=busy, tips=list(tips), src=list(src), verified=bool(src), ap=True)
NEW_CITIES = []

# ---------------- BANGKOK ----------------
NEW_CITIES += [["Bangkok", 13.7563, 100.5018]]
B = "Bangkok"
NM = S("Nomadic Matt", "https://www.nomadicmatt.com/travel-blogs/best-hostels-bangkok/")
HGK = S("Hostelgeeks", "https://hostelgeeks.com/best-hostels-in-thailand-backpacking/")
KSR = S("Khaosanroad.com", "https://www.khaosanroad.com/articles/best-bangkok-party-hostels-2026")
GOB = S("Go Backpacking", "https://gobackpacking.com/travel-guides/thailand/best-hostels-bangkok/")
PYT_B = S("Pickyourtrail", "https://pickyourtrail.com/tourism/thailand/best-hostels-in-bangkok")
TG("g-bkk-lubd-siam", "Lub d Bangkok Siam", B, 13.7466, 100.5290, p=[350, 400], r=8.6, rs="Google (4.3 of 5, 740+ reviews)",
   s=["Next to National Stadium BTS, steps from Siam Square and MBK", "Big social hostel with co-working space, bar and lots of events"],
   src=[NM, S("Pickyourtrail", "https://pickyourtrail.com/best-hostels-in-thailand"), S("Feastography", "https://feastography.squarespace.com/blog/budget-hostels-bangkok")])
TG("g-bkk-madmonkey", "Mad Monkey Hostel Bangkok", B, 13.7612, 100.4960, p=[450, 900], r=9.3, rs="Hostelworld (via Best Party Hostels)",
   s=["Bangkok’s best-known party hostel, by Rambuttri and Khao San Road", "Small pool, lively bar, daily events and cheap tours"],
   tips=["Not for light sleepers", "No free breakfast"],
   src=[KSR, S("Best Party Hostels", "https://bestpartyhostels.pages.dev/asia/south-east-asia/thailand/bangkok"), S("Nomads Nation", "https://nomadsnation.com/best-party-hostels-in-bangkok"), NM])
TG("g-bkk-nappark", "NapPark Hostel @ Khao San", B, 13.7595, 100.4985, p=[420],
   s=["One of the most-recommended backpacker hostels near Khao San Road", "Popular with couples as well as solo travellers"],
   src=[S("Feastography", "https://feastography.squarespace.com/blog/budget-hostels-bangkok"), HGK])
TG("g-bkk-here", "Here Hostel", B, 13.7630, 100.4985,
   s=["Near the Grand Palace and the Old Town temples", "Social but chill, with good facilities"],
   src=[KSR, GOB, PYT_B])
TG("g-bkk-onceagain", "Once Again Hostel", B, 13.7533, 100.5040,
   s=["Old Town, close to Chinatown and the temples", "Picked as the best hostel in Bangkok by Hostelgeeks; very social"],
   src=[HGK, GOB, PYT_B])
TG("g-bkk-slumber", "Slumber Party Hostel Bangkok", B, 13.7425, 100.5530, p=[12, 18], cur="USD", r=8.4, rs="Guest rating 4.2 of 5 (This Hotel)",
   s=["Sukhumvit Soi 1, party hostel with nightly pub crawls", "Good for solo travellers who want to meet people"],
   src=[S("This Hotel", "https://thishotel.com/?p=15278"), S("Nomads Nation", "https://nomadsnation.com/best-party-hostels-in-bangkok"), GOB])
TG("g-bkk-bodega", "Bodega Bangkok Party Hostel", B, 13.7590, 100.4970,
   s=["Right in the Khao San Road area", "Rated the top party hostel in Bangkok by two backpacker guides"],
   tips=["Expect noise late into the night"], src=[GOB, S("Nomads Nation", "https://nomadsnation.com/best-party-hostels-in-bangkok"), KSR])
TG("g-bkk-bedstation", "Bed Station Hostel Ratchathewi", B, 13.7518, 100.5318,
   s=["Stylish, design-led hostel by Ratchathewi BTS", "Comfy dorms, good for solo travellers; 24-hour reception"],
   src=[PYT_B, HGK])
TG("g-bkk-yard", "The Yard Hostel", B, 13.7795, 100.5440,
   s=["Eco-friendly hostel in leafy, local Ari", "Quiet nights and good cafés nearby; book early as Ari has few hostels"],
   src=[PYT_B, S("Hostelz", "https://www.hostelz.com/where-to-stay-in-bangkok-for-the-first-time")])
TG("g-bkk-barnbed", "Barn & Bed Hostel", B, 13.7440, 100.5170,
   s=["Top of Hostelgeeks’ Bangkok list", "Calm, well-run hostel"], src=[HGK])
TG("g-bkk-hom", "Hom Hostel & Cooking Club", B, 13.7330, 100.5715,
   s=["Picked as the best hostel in Sukhumvit", "Runs Thai cooking classes in-house"],
   src=[S("Southeast Asia Backpacker", "https://southeastasiabackpacker.com/review-isanook-residence-bangkok-a-hub-for-flashpackers-digital-nomads")])
TG("g-bkk-niras", "Niras Bankoc Cultural Hostel", B, 13.7525, 100.5030,
   s=["Old Town hostel in a restored shophouse", "Recommended for a quiet night"], src=[GOB])
TG("g-bkk-hide", "Hide Bangkok Hostel", B, 13.7530, 100.5370,
   s=["Hostelz’s top pick in Bangkok", "Good for solo travellers and digital nomads"],
   src=[S("Hostelz", "https://www.hostelz.com/where-to-stay-in-bangkok-solo-traveler")])
TG("g-bkk-ddinn", "D&D Inn", B, 13.7589, 100.4968, t=("Hotel",),
   s=["Hotel right on Khao San Road with a rooftop pool", "Named the best place to stay on Khao San itself"],
   src=[S("Southeast Asia Backpacker", "https://southeastasiabackpacker.com/review-isanook-residence-bangkok-a-hub-for-flashpackers-digital-nomads")])
TG("g-bkk-lubd-silom", "Lub d Bangkok Silom", B, 13.7247, 100.5265,
   s=["Silom branch of Lub d, by Surasak BTS", "Calmer than Khao San, close to Silom’s night markets and bars"],
   src=[S("Mad Monkey", "https://madmonkeyhostels.com/cheap-hostels-in-bangkok/")])

AU = S("Asia Undiscovered", "https://www.asiaundiscovered.com/bangkok-street-food/")
TJ = S("TableJourney", "https://tablejourney.com/thailand/street-food/")
TM("m-bkk-thipsamai", "Thip Samai Pad Thai", B, 13.7527, 100.5047, p=[60, 120], t=("Restaurant",),
   s=["Bangkok’s most famous pad thai, on Mahachai Road in the Old Town", "Try the ‘superb’ version wrapped in thin omelette"],
   best="Evenings, 5 pm to midnight", tips=["Closed Wednesdays", "Expect a queue"],
   src=[AU, S("Pickyourtrail", "https://pickyourtrail.com/tourism/thailand/best-street-food-in-bangkok"), S("Durango Herald", "https://www.durangoherald.com/?p=104460")])
TM("m-bkk-jayfai", "Raan Jay Fai", B, 13.7526, 100.5045, p=[800], t=("Restaurant",), pu="crab omelette",
   s=["The street stall with a Michelin star, famous for crab omelette and drunken noodles", "Chef cooks over charcoal in ski goggles"],
   tips=["Cash only", "Queue from late morning; opening days vary, so check before you go", "Much pricier than normal street food"],
   src=[TJ, S("Durango Herald", "https://www.durangoherald.com/?p=104460"), S("Thai Holiday Guide", "https://www.thaiholidayguide.com/best-restaurants-bangkok/")])
TM("m-bkk-faitalu", "Pad Thai Fai Ta Lu", B, 13.7550, 100.5020,
   s=["Cheaper, shorter-queue alternative to Thip Samai nearby", "Some say the pad thai is better"], src=[AU])
TM("m-bkk-jokprince", "Jok Prince", B, 13.7240, 100.5150, p=[70],
   s=["Michelin Bib Gourmand rice congee with pork and century egg", "Charoen Krung, near the river"],
   best="Breakfast, 6 am to 1 pm (also opens again in the evening)", src=[AU])
TM("m-bkk-goang", "Go-Ang Pratunam Chicken Rice", B, 13.7508, 100.5420, p=[60],
   s=["Bib Gourmand khao man gai (chicken rice), the pink-sign stall is the original", "Opposite the mall in Pratunam"],
   best="6 am to 2 pm, then 5 pm to midnight", tips=["From BTS Chit Lom it’s a 15-minute walk or a ฿30 motorbike taxi"], src=[AU, S("Tagthai", "https://www.tagthai.com/explore/p/michelin-guide-thailand-2026")])
TM("m-bkk-ortorkor", "Or Tor Kor Market", B, 13.8020, 100.5480, p=[90, 200], t=("Market",),
   s=["Upmarket fresh market and food court next to Chatuchak, where chefs shop", "Som tam, grilled chicken, curry plates and fruit"],
   best="Daily, 6 am to 8 pm", tips=["MRT Kamphaeng Phet exit 3"],
   src=[AU, S("TableJourney", "https://tablejourney.com/thailand/bangkok/budget-eating/polo-fried-chicken-budget/"), S("Khaosanroad.com", "https://www.khaosanroad.com/articles/bangkok-street-food-guide")])
TM("m-bkk-jeho", "Jeh O Chula", B, 13.7390, 100.5240,
   s=["Bib Gourmand late-night spot famous for its giant tom yum noodle pots", "A Bangkok late-night institution"],
   best="Late night", tips=["Queues build after 10 pm"],
   src=[S("The Poor Traveler", "https://www.thepoortraveler.net/?p=54990"), S("Waug", "https://www.waug.com/en/magazines/1764")])
TM("m-bkk-naiek", "Nai Ek Roll Noodle", B, 13.7410, 100.5085,
   s=["Bib Gourmand peppery rolled-noodle soup on Yaowarat Road, Chinatown"], best="Evenings",
   src=[S("Pickyourtrail", "https://pickyourtrail.com/tourism/thailand/best-street-food-in-bangkok")])
TM("m-bkk-apsorn", "Krua Apsorn", B, 13.7560, 100.5020, t=("Restaurant",),
   s=["Old Town shophouse cooking royal Thai dishes; the crab omelette and curries are favourites"],
   src=[S("Traveller", "https://www.traveller.com.au/travel-tips--advice-for-thailand-20-reasons-to-love-bangkok-h0obel")])

YTG = S("Your Thai Guide", "https://yourthaiguide.com/bangkok-big-list-of-entry-fees")
TC("c-bkk-watpho", "Wat Pho (Reclining Buddha)", B, 13.7465, 100.4927, ["Temples"],
   s=["The 46-metre gold Reclining Buddha, and the birthplace of Thai massage", "Get a massage at the temple’s own school"],
   p=[300], best="Daily 8 am to 7:30 pm; early is coolest", tips=["Cover shoulders and knees"], src=[YTG])
TC("c-bkk-watarun", "Wat Arun (Temple of Dawn)", B, 13.7437, 100.4888, ["Temples", "Views"],
   s=["Riverside temple covered in porcelain, climbable for river views", "Lit up beautifully at night from across the river"],
   p=[100], best="Sunset from the other bank", tips=["Fee is from older sources, may have gone up", "Cross on the cheap river ferry from Tha Tien pier"],
   src=[S("Wanderon", "https://wanderon.in/blogs/best-places-to-visit-in-bangkok"), S("Rajadamnern", "https://rajadamnern.com/?p=9140")])
TC("c-bkk-jimthompson", "Jim Thompson House", B, 13.7491, 100.5286, ["Museums"],
   s=["Six teak houses and a garden, home of the American who revived Thai silk and vanished in 1967"],
   p=[250], best="Daily 9 am to 6 pm, guided tours all day", tips=["Near National Stadium BTS; allow an hour"],
   src=[YTG, S("Khaosanroad.com", "https://www.khaosanroad.com/articles/what-to-do-in-bangkok")])
TC("c-bkk-mahanakhon", "King Power Mahanakhon SkyWalk", B, 13.7234, 100.5283, ["Views"],
   s=["Thailand’s highest observation deck at 314 m, with a glass floor"],
   p=[25, 31], cur="USD", best="Sunset (pricier slot)", tips=["Cheaper booked online in advance", "Open 10 am to 7 pm"],
   src=[S("Shipped Away", "https://shippedaway.com/bangkok-travel-guide"), S("Klook", "https://www.klook.com/destination/c4-bangkok/?aid=55947")])
TC("c-bkk-rajadamnern", "Muay Thai at Rajadamnern Stadium", B, 13.7582, 100.5100, ["Nightlife"],
   s=["Thailand’s oldest Muay Thai stadium, fights most evenings", "Lively crowd and betting; very atmospheric"],
   p=[1500, 4500], best="Evenings from about 7 pm", tips=["Ringside costs most; the upper seats are fine"],
   src=[S("Rajadamnern", "https://rajadamnern.com/?p=9140"), YTG])
TC("c-bkk-lumphini", "Lumphini Park", B, 13.7314, 100.5414, ["Views"],
   s=["Bangkok’s big green park, with giant monitor lizards by the lakes"], cost="Free", best="Early morning or late afternoon",
   src=[S("Travel Triangle", "https://traveltriangle.com/blog/?p=95623")])
TC("c-bkk-khaosan", "Khao San Road at night", B, 13.7589, 100.4975, ["Nightlife"],
   s=["The famous backpacker street: bars, buckets, street food and chaos"], cost="Free", best="After 9 pm",
   tips=["Watch for tuk-tuk and ‘closed temple’ scams nearby"], src=[S("Hostelz", "https://www.hostelz.com/where-to-stay-in-bangkok-solo-traveler")])
TC("c-bkk-ladmayom", "Khlong Lat Mayom Floating Market", B, 13.7630, 100.4100, ["Markets"],
   s=["Local-feeling floating market on the Thonburi side, less touristy than Damnoen Saduak"], cost="Free to enter", best="Weekends only",
   src=[YTG])
TC("c-bkk-chaophraya", "Chao Phraya river boats", B, 13.7193, 100.5135, ["Excursions", "Views"],
   s=["Hop the river boats between the temples, Chinatown and Sathorn, skipping the traffic"], cost="Cheap, a few dozen baht (not checked)",
   best="Late afternoon light", src=[S("Hostelworld", "https://www.hostelworld.com/hostels/p/337930/cozy-lab/")])

# ---------------- CHIANG MAI ----------------
CM = "Chiang Mai"
CMU20 = S("Chiang Mai hostels under $20 (2026)", "https://kualalumpur-4bs.pages.dev/blog/chiang-mai-best-hostels-under-20/")
HZP = S("Hostelz", "https://www.hostelz.com/party-hostels-in-chiang-mai"); HZY = S("Hostelz", "https://www.hostelz.com/youth-hostels-in-chiang-mai")
BPW = S("Backpackers Wanderlust", "https://www.backpackerswanderlust.com/best-hostels-in-chiang-mai/")
TG("g-cm-stamps", "Stamps Backpackers", CM, 18.7880, 98.9930, p=[8, 12], cur="USD", r=9.2, rs="Hostelworld",
   s=["Old City near Tha Phae Gate", "Very social, with pool parties"], src=[CMU20, S("Passport and Stamps", "https://passportandstamps.com/?p=16447")])
TG("g-cm-banilah", "Banilah Hostel", CM, 18.7900, 98.9880, p=[10, 15], cur="USD", r=9.0, rs="Hostelworld",
   s=["Old City; clean, quiet and female-friendly"], src=[CMU20])
TG("g-cm-pak", "Pak Chiang Mai", CM, 18.7980, 98.9680, p=[12, 18], cur="USD", r=8.9, rs="Hostelworld",
   s=["In trendy Nimman, good for working remotely, with co-working space"], src=[CMU20])
TG("g-cm-littlebird", "A Little Bird Guesthouse", CM, 18.7880, 98.9810, p=[7, 12], cur="USD", t=("Guesthouse",), pu=DORM,
   s=["Old City near Wat Phra Singh", "Unassuming entrance but one of the best-value stays in town"], src=[CMU20])
TG("g-cm-laithai", "Lai Thai Guesthouse", CM, 18.7848, 98.9945, p=[8, 14], cur="USD", t=("Guesthouse",), pu=DORM,
   s=["Long-running guesthouse, popular for longer stays"], src=[CMU20])
TG("g-cm-madmonkey", "Mad Monkey Chiang Mai", CM, 18.7930, 98.9900, r=9.5, rs="Hostelworld (via Best Party Hostels)",
   s=["Chiang Mai’s top-rated party hostel", "Mixes the social scene with cultural trips"],
   src=[S("Best Party Hostels", "https://bestpartyhostels.pages.dev/asia/south-east-asia/thailand/chiang-mai"), S("Pickyourtrail", "https://pickyourtrail.com/best-hostels-in-thailand")])
TG("g-cm-hiddengarden", "Hidden Garden Hostel", CM, 18.7845, 98.9870, p=[14.12], cur="USD", r=9.5, rs="Hostelworld (via Hostelz)",
   s=["Picked as the best hostel in Chiang Mai by Hostelgeeks", "Leafy garden, relaxed atmosphere in the Old City"], src=[HZP, HGK])
TG("g-cm-makad", "Makad Rooftop Hostel", CM, 18.7885, 98.9895, p=[4.89], cur="USD", r=9.1, rs="Hostelworld (via Hostelz)",
   s=["Cheap beds and a rooftop to hang out on"], src=[HZP])
TG("g-cm-bigo", "Big & O’s House 2", CM, 18.7770, 98.9890, p=[6.25], cur="USD", r=9.5, rs="Backpackers Wanderlust",
   s=["Rated the best hostel for solo travellers", "Known for making guests feel like family"], src=[BPW, HZP])
TG("g-cm-onelife", "One Life Hostel", CM, 18.7895, 98.9930, p=[10.84, 12.21], cur="USD",
   s=["Chiang Mai’s best-known party hostel by Hostelz’s count"], src=[HZP, HZY])
TG("g-cm-hostelone", "Hostel One & Art Gallery", CM, 18.7845, 98.9900, r=9.5, rs="Backpackers Wanderlust",
   s=["Cosy, creative hostel on Ratchamanka Road in the Old City"], src=[BPW])
TG("g-cm-cabin", "The Cabin Backpackers Hostel & Bar", CM, 18.7870, 98.9830, r=9.0, rs="Backpackers Wanderlust",
   s=["Picked as the best cheap hostel, with its own bar"], src=[BPW])
TG("g-cm-angmo", "Angmo Hostel by Amaka", CM, 18.7880, 98.9860, p=[12.51], cur="USD", r=9.7, rs="Hostelworld (via Hostelz)",
   s=["One of the highest-rated hostels in the city"], src=[HZY])
TG("g-cm-familyhome2", "Family Home 2 (Absolute House by Joe)", CM, 18.7860, 98.9880, p=[7.51], cur="USD", r=9.7, rs="Hostelworld (via Hostelz)",
   s=["Homely, very highly rated and cheap"], src=[HZY])
TG("g-cm-yard", "The Yard Hostel Chiang Mai", CM, 18.7950, 98.9890, p=[15.86], cur="USD", r=9.6, rs="Hostelworld (via Hostelz)",
   s=["Si Phum, inside the Old City’s north side", "Garden hostel, calm and well kept"],
   src=[HZY, S("Booking.com (via easyJet)", "https://hotels.easyjet.com/hostels/city/th/chiang-mai.en-gb.html?aid=356980")])
TG("g-cm-baanlung", "Baan Lung Poshtel", CM, 18.7875, 98.9915, p=[11.56], cur="USD", r=9.6, rs="Hostelworld (via Hostelz)",
   s=["Upmarket ‘poshtel’ dorms"], src=[HZY])
TG("g-cm-whoopers", "Whoopers Hostel", CM, 18.7890, 98.9905, p=[3.01], cur="USD",
   s=["Harry Potter-themed social hostel", "Among the cheapest beds in the city"], tips=["The hostel asks you to read its description before booking"], src=[HZY])
TG("g-cm-lazygibbon", "Lazy Gibbon 2", CM, 18.7770, 98.9880, r=9.1, rs="Booking.com (1,878 reviews)",
   s=["Hai Ya, just south of the Old City; very well reviewed"], src=[S("Booking.com", "https://www.booking.com/hostels/city/th/chiang-mai.html?aid=328234")])

TJCM = S("TableJourney", "https://tablejourney.com/thailand/chiang-mai/cheap-eats/")
AFQ = S("Authentic Food Quest", "https://authenticfoodquest.com/best-authentic-khao-soi-chiang-mai/")
BYK = S("Byklo", "https://www.byklo.rent/en/blog/chiang-mai-street-food-guide/")
TM("m-cm-maesai", "Khao Soi Mae Sai", CM, 18.8010, 98.9800, p=[45, 80], t=("Restaurant",),
   s=["One of the city’s favourite khao soi shops, on Ratchaphuek Alley"], best="Mon to Sat, 8 am to 4 pm", tips=["Closed Sundays"],
   src=[AFQ, S("Cookly", "https://cookly.me/magazine/?p=2535"), TJCM])
TM("m-cm-khunyai", "Khao Soi Khun Yai", CM, 18.7990, 98.9850, p=[50, 90], t=("Restaurant",),
   s=["Long-loved khao soi spot north of the Old City (Chang Phueak area)"], best="Lunch", tips=["Sells out; go early"],
   src=[BYK, S("TableJourney", "https://tablejourney.com/thailand/chiang-mai/signature-dishes/"), S("2foodtrippers", "https://www.2foodtrippers.com/chiang-mai-food-guide/")])
TM("m-cm-cowboyhat", "Cowboy Hat Lady (Khao Kha Moo Chang Phueak)", CM, 18.7966, 98.9864, p=[40, 60],
   s=["Famous braised pork leg on rice with a soft egg, made famous by Anthony Bourdain", "At the Chang Phueak (north) gate night market"],
   best="Evenings from about 5 pm to midnight", tips=["Cash only"], src=[TJCM, S("2foodtrippers", "https://www.2foodtrippers.com/chiang-mai-food-guide/"), S("Travel Guides Tips", "https://travelguidestip.com/chiang-mai-food-guide/")])
TM("m-cm-changphueak", "Chang Phueak Gate Night Market", CM, 18.7965, 98.9866, p=[50, 65], t=("Market",),
   s=["Evening street-food cluster at the north gate: khao soi, pork leg rice, dim sum, smoothies"], best="Daily 5 pm to midnight",
   src=[BYK, S("Where Goes Rose", "https://www.wheregoesrose.com/chiang-mai-food-guide")])
TM("m-cm-lamduan", "Khao Soi Lam Duan Fa Ham", CM, 18.8020, 99.0020, t=("Restaurant",),
   s=["Classic khao soi shop on Faham Road with a daily queue"], best="Lunch", src=[BYK, S("2foodtrippers", "https://www.2foodtrippers.com/chiang-mai-food-guide/")])
TM("m-cm-lungprakit", "Khao Soi Lung Prakit Kad Kom", CM, 18.7790, 98.9880, t=("Restaurant",),
   s=["Inside Kad Kom market south of the moat; locals rate it among the best"], best="Mid-morning", tips=["Order a plate of naem crispy rice with it"], src=[TJCM])
TM("m-cm-spchicken", "SP Chicken", CM, 18.7870, 98.9810, t=("Restaurant",),
   s=["Old City favourite for gai yang (grilled chicken) and som tam, on Soi Samlarn 1"], best="Lunch", src=[BYK])
TM("m-cm-wualai", "Wualai Saturday Walking Street", CM, 18.7750, 98.9880, t=("Market",),
   s=["Saturday night market south of the Old City, known for its sai ua sausage grills"], best="Saturday evenings", src=[BYK])
TM("m-cm-nimmansoi", "Khao Soi Nimman", CM, 18.7975, 98.9675, t=("Restaurant",),
   s=["Popular khao soi in Nimman, Soi 7"], src=[S("2foodtrippers", "https://www.2foodtrippers.com/?p=11327")])
TM("m-cm-siriwattana", "Siri Wattana Market", CM, 18.8050, 98.9870, p=[30, 60], t=("Market",),
   s=["Local market for sai ua (northern herb sausage) and other northern snacks"], src=[S("Where Goes Rose", "https://www.wheregoesrose.com/chiang-mai-food-guide"), S("Pattaya Talk", "https://pattayatalk.com/things-to-do/chiang-mai-markets-food")])

TGT = S("Travel Guides Tips", "https://travelguidestip.com/things-to-do-in-chiang-mai/")
TC("c-cm-enp", "Elephant Nature Park", CM, 19.2150, 98.8590, ["Excursions"],
   s=["Widely seen as Chiang Mai’s most ethical elephant sanctuary, founded by conservationist Lek Chailert", "No riding; you watch, feed and learn"],
   p=[2500, 6000], best="Book well ahead", tips=["Half and full-day programmes; pickup included"],
   src=[S("Dimaak", "https://dimaak.com/blog/things-to-do-in-chiang-mai"), S("Pickyourtrail", "https://pickyourtrail.com/blog/things-to-do-in-chiang-mai")])
TC("c-cm-ejs", "Elephant Jungle Sanctuary", CM, 18.8770, 98.8380, ["Excursions"],
   s=["Popular no-riding sanctuary with feeding and mud baths"], p=[75], cur="USD", tips=["Avoid anywhere offering rides or shows"],
   src=[TGT, S("Gotripzi", "https://gotripzi.com/destinations/chiang-mai-th")])
TC("c-cm-chedluang", "Wat Chedi Luang", CM, 18.7869, 98.9867, ["Temples"],
   s=["Huge part-ruined 14th-century chedi in the middle of the Old City", "Free ‘monk chat’ tables daily, about 9 am to 6 pm"],
   cost="About 40 baht (some guides say free)", best="Morning", tips=["Cover shoulders and knees"],
   src=[S("Gecko Routes", "https://www.geckoroutes.com/blog/things-to-do-in-chiang-mai-thailand/"), S("Nomado", "https://www.nomadotravel.app/en/guides/things-to-do-in-chiang-mai")])
TC("c-cm-phrasingh", "Wat Phra Singh", CM, 18.7884, 98.9820, ["Temples"],
   s=["Classic Lanna temple holding northern Thailand’s most sacred Buddha image"], cost="About 20–40 baht",
   src=[S("Pattaya Talk", "https://pattayatalk.com/things-to-do/adventure-awaits-chiang-mai-activities"), S("Gotripzi", "https://gotripzi.com/destinations/chiang-mai-th")])
TC("c-cm-chiangman", "Wat Chiang Man", CM, 18.7942, 98.9893, ["Temples"],
   s=["Chiang Mai’s oldest temple, built in the 13th century; peaceful"], p=[20],
   src=[S("Gecko Routes", "https://www.geckoroutes.com/blog/things-to-do-in-chiang-mai-thailand/")])
TC("c-cm-cooking", "Thai cooking class", CM, 18.7880, 98.9870, ["Excursions"],
   s=["Half-day classes with a market visit, then you cook and eat 4–5 dishes", "Chiang Mai is the cheapest and best place in Thailand to do one"],
   p=[700, 1000], tips=["Most schools pick you up from your hostel"], src=[S("Departly", "https://departly.pages.dev/to/thailand/chiang-mai/"), S("A Backpacker’s World", "https://abackpackersworld.com/?p=78127")])
TC("c-cm-inthanon", "Doi Inthanon National Park", CM, 18.5880, 98.4870, ["Hikes", "Views", "Waterfalls"],
   s=["Thailand’s highest mountain, with waterfalls, twin royal pagodas and cloud-forest trails", "Usually done as a full-day tour"],
   cost="Park fee plus transport (not checked)", best="Early start, cool season", src=[TGT, S("Destinationless Travel", "https://destinationlesstravel.com/10-best-things-to-do-in-chiang-mai-thailand/")])
TC("c-cm-canyon", "Chiang Mai Grand Canyon", CM, 18.6960, 98.8930, ["Excursions"],
   s=["Old flooded quarry turned water park, with red cliffs and inflatables", "About 30 minutes from the city"],
   cost="Entry fee (not checked)", src=[S("Dimaak", "https://dimaak.com/blog/things-to-do-in-chiang-mai")])
TC("c-cm-nimman", "Nimman nightlife", CM, 18.7975, 98.9680, ["Nightlife"],
   s=["Nimmanhaemin Road’s bars, rooftops and clubs, the student and nomad night out"], cost="Free", best="After 9 pm",
   src=[S("Klook", "https://www-verify.klook.cn/en-NZ/blog/chiang-mai-attractions")])
TC("c-cm-nightbazaar", "Chiang Mai Night Bazaar", CM, 18.7853, 99.0000, ["Markets"],
   s=["Big nightly market east of the Old City for souvenirs and snacks"], cost="Free", best="Every evening",
   tips=["Bargain: start at 60–70% of the asking price"], src=[TGT])

# ---------------- PAI ----------------
PA = "Pai"
RA = S("Road Affair", "https://www.roadaffair.com/best-hostels-in-pai-thailand/")
JATW = S("Jones Around the World", "https://www.jonesaroundtheworld.com/?p=10986")
GOBP = S("Go Backpacking", "https://gobackpacking.com/travel-guides/thailand/best-hostels-pai/")
BPHP = S("Best Party Hostels", "https://bestpartyhostels.pages.dev/asia/south-east-asia/thailand/pai")
MMP = S("Mad Monkey", "https://madmonkeyhostels.com/blogs/blogs-travel-guide-thailand-travel-best-pai-hostels/")
TG("g-pai-commongrounds", "Common Grounds Pai", PA, 19.3595, 98.4415, p=[10], cur="USD", r=9.5, rs="Hostelworld (3,600+ reviews)", rc=3615,
   s=["About 50 m from Walking Street; won a 2026 Hostelworld Hoscar", "Very social, with canyon and waterfall trips, open mic and dance nights"],
   d={"breakfast": "Not listed", "privacy": "6-bed air-con dorms with lockers, plus loft-style privates for 2–3", "beds": "6-bed dorms", "toilet": "Not listed", "room": "Air-con; common area closes at 10 pm"},
   src=[S("Hostelworld", "https://www.hostelworld.com/hostels/asia/thailand/pai/f/couples/"), RA, GOBP])
TG("g-pai-circus", "The Famous Pai Circus Hostel", PA, 19.3530, 98.4520, p=[5.86, 6.78], cur="USD", r=8.6, rs="Hostelworld",
   s=["Pai’s legendary party hostel, set up by an English ex-circus performer", "Pool with mountain views, fire shows and circus skills"],
   src=[JATW, BPHP, S("Hostelworld", "https://www.hostelworld.com/hostels/p/91394/the-famous-pai-circus-hostel/")])
TG("g-pai-revolution", "Revolution Hostel Pai", PA, 19.3610, 98.4440, p=[7.6], cur="USD", r=9.5, rs="Hostelworld (2,000+ reviews)", rc=2038,
   s=["Very highly rated, about 600 m from the centre"], src=[S("Hostelworld", "https://www.hostelworld.com/hostels/asia/thailand/pai/f/party/"), JATW])
TG("g-pai-deejai", "Deejai Pai Backpackers", PA, 19.3620, 98.4470,
   s=["Friendly, sociable hostel with basketball, slackline and board games", "Recommended for couples"], src=[RA])
TG("g-pai-madmonkey", "Mad Monkey Hostel Pai", PA, 19.3540, 98.4525, s=["Mad Monkey’s Pai branch in Mae Hi, across the river"], src=[MMP])
TG("g-pai-spicypai", "Spicypai Backpackers", PA, 19.3560, 98.4500,
   s=["The classic Pai experience: bamboo huts among the fields", "Kitchen for guests; hosts Momo and Jojo"], src=[RA, MMP])
TG("g-pai-bodega", "Bodega Pai Party Hostel", PA, 19.3585, 98.4410, r=8.1, rs="Hostelworld (via Best Party Hostels)", s=["Party hostel close to the centre"], src=[BPHP, JATW])
TG("g-pai-nolo", "Nolo Hub Pai", PA, 19.3600, 98.4430, s=["Picked as the best hostel in Pai for solo travellers"], src=[RA])
TG("g-pai-suandoi", "Suandoi Backpacker Resort", PA, 19.3500, 98.4400, s=["Fun hostel surrounded by nature"], src=[RA])
TG("g-pai-buzzas", "Buzza’s Backpackers @ Pai Chan", PA, 19.3570, 98.4480, r=9.0, rs="Hostelz", s=["Resort-style hostel known for its food"], src=[S("Hostelz", "https://www.hostelz.com/party-hostels-in-pai"), MMP])
TG("g-pai-butterfly", "Butterfly Hostel", PA, 19.3590, 98.4425, p=[6.41], cur="USD", r=8.9, rs="Hostelz", s=["Social hostel for drinking and meeting people"], src=[S("Hostelz", "https://www.hostelz.com/party-hostels-in-pai")])
TG("g-pai-easyhouse", "Easy House Hostel", PA, 19.3605, 98.4435, p=[5.86], cur="USD", r=8.6, rs="Hostelworld", s=["Cheap and well reviewed"], src=[JATW])

MMR = S("Mad Monkey", "https://madmonkeyhostels.com/post/cheap-pai-restaurants")
WLP = S("Wanderlog", "https://wanderlog.com/list/geoCategory/93797")
HCP = S("Hotels.com", "https://co.hoteles.com/go/thailand/best-restaurants-pai")
TM("m-pai-charlielek", "Charlie & Lek", PA, 19.3605, 98.4405, p=[40, 120], t=("Restaurant",),
   s=["Pai’s favourite cheap Thai restaurant; great khao soi, massaman and papaya pad thai", "Google 4.6 from 1,300+ reviews; also runs cooking classes"],
   best="Lunch or dinner", tips=["Closed Sundays (per one guide)"], src=[MMR, WLP, S("Mad Monkey", "https://madmonkeyhostels.com/blogs/blogs-travel-guide-thailand-travel-best-pai-restaurants/")])
TM("m-pai-omgarden", "Om Garden Cafe", PA, 19.3585, 98.4450, p=[150], t=("Cafe",), pu="breakfast with a drink",
   s=["Leafy garden café on Rat Damrong Road, Google 4.7 from 1,600+ reviews", "Great for breakfast and a quiet laptop session"], best="Breakfast to late afternoon",
   src=[WLP, S("Visit Thailand Today", "https://www.visitthailandtoday.com/top-lists/best-restaurants-pai")])
TM("m-pai-nas", "Na’s Kitchen", PA, 19.3592, 98.4425, p=[60, 100], t=("Restaurant",),
   s=["No-frills spot cooking big portions of Thai and northern Thai food", "Pad thai from ฿60, soups from ฿100"], tips=["Na doesn’t always open every day"],
   src=[MMR, S("Lonely Planet", "https://www-lonelyplanet-com-57e2.imagizer.com/thailand/mae-hong-son-province/pai/restaurants")])
TM("m-pai-larpkhom", "Larp Khom Huay Poo", PA, 19.3720, 98.4380, t=("Restaurant",),
   s=["Local northern Thai spot just north of town, famous for larb (minced meat salad)"], best="Daily 9 am to 8 pm",
   src=[HCP, S("Lonely Planet", "https://www-lonelyplanet-com-57e2.imagizer.com/thailand/mae-hong-son-province/pai/restaurants")])
TM("m-pai-zisters", "Khao Soi Zister’s", PA, 19.3590, 98.4400, t=("Restaurant",),
   s=["Casual spot well known for its khao soi, plus juices and coffee"], best="Daily 9 am to 4:30 pm", src=[HCP])
TM("m-pai-ganesh", "Ganesh Bar & Restaurant", PA, 19.3560, 98.4440, t=("Restaurant",),
   s=["Simple but superb Thai food; some say the best khao soi in Pai"], best="Mon to Sat, 3 pm to midnight",
   src=[S("Mad Monkey", "https://madmonkeyhostels.com/blogs/blogs-travel-guide-thailand-travel-best-pai-restaurants/"), S("Hotels.com", "https://nl.hotels.com/go/thailand/best-restaurants-pai")])
TM("m-pai-duang", "Duang Restaurant", PA, 19.3598, 98.4412, p=[40], t=("Restaurant",),
   s=["Run by deaf and hard-of-hearing Thai staff, just off Walking Street", "Khao soi for about ฿40"], src=[S("Go To Thailand", "https://gotothailand.com/pai")])
TM("m-pai-twosisters", "Two Sisters Restaurant", PA, 19.3520, 98.4530, t=("Restaurant",), s=["Highly rated (4.8) family restaurant in Mae Hi"],
   src=[S("Visit Thailand Today", "https://www.visitthailandtoday.com/top-lists/best-restaurants-pai")])
TM("m-pai-blueox", "The Blue Ox", PA, 19.3600, 98.4430, t=("Restaurant",), s=["BBQ, khao soi and northern-hill-tribe fusion dishes"],
   src=[S("Mad Monkey", "https://madmonkeyhostels.com/blogs/blogs-travel-guide-thailand-travel-best-pai-restaurants/")])

TBF = S("The Backpacking Family", "https://thebackpackingfamily.com/?p=2197")
TC("c-pai-thamlod", "Tham Lod Cave", PA, 19.5660, 98.2790, ["Excursions", "Hikes"],
   s=["One of northern Thailand’s biggest caves, with a river you cross on bamboo rafts and ancient coffins", "About an hour from Pai, near Soppong"],
   cost="200 baht wildlife-sanctuary day pass, plus about 600 baht for a guide per group of up to 3",
   best="Late afternoon, when thousands of swifts fly in", tips=["Wear shoes with grip; the rocks are wet", "The same day pass covers Pam Bok waterfall and Sai Ngam hot spring"],
   src=[TBF, S("The Manduls", "https://themanduls.com/?p=18564"), S("Dimaak", "https://dimaak.com/blog/things-to-do-in-pai-thailand")])
TC("c-pai-yunlai", "Yun Lai Viewpoint", PA, 19.3620, 98.4110, ["Views"],
   s=["Sunrise over the misty Pai valley, above the Chinese village", "Google 4.4 from nearly 4,900 reviews"], p=[20],
   best="Sunrise, November to February", tips=["Entry includes a cup of tea"],
   src=[S("Go To Thailand", "https://gotothailand.com/10-reasons-to-visit-pai/"), S("Visit Thailand Today", "https://www.visitthailandtoday.com/destinations/pai")])
TC("c-pai-pambok", "Pam Bok Waterfall", PA, 19.3390, 98.4000, ["Waterfalls"],
   s=["Waterfall at the end of a narrow rock gorge, about 8 km from town", "Deep enough to jump into"],
   cost="Covered by the 200 baht wildlife-sanctuary day pass", src=[TBF, S("Dimaak", "https://dimaak.com/blog/things-to-do-in-pai-thailand")])
TC("c-pai-mopaeng", "Mo Paeng Waterfall", PA, 19.3870, 98.3970, ["Waterfalls"],
   s=["Multi-level waterfall you can slide down, near Yun Lai"], cost="Free (not checked)", src=[S("Dimaak", "https://dimaak.com/blog/things-to-do-in-pai-thailand")])
TC("c-pai-bamboo", "Bamboo Bridge (Boon Ko Ku So)", PA, 19.3270, 98.3880, ["Views"],
   s=["800 m bamboo walkway across the rice fields to a forest temple"], cost="Free (older source)",
   src=[S("The Blond Travels", "https://www.theblondtravels.com/places-see-pai"), S("Salt in our Hair", "https://www.saltinourhair.com/thailand/pai")])
TC("c-pai-thapai", "Tha Pai Hot Springs", PA, 19.3050, 98.4720, ["Excursions"],
   s=["Natural hot springs in a national park, about 8 km from town"], p=[300], best="Early morning",
   src=[S("Global Gallivanting", "https://www.global-gallivanting.com/?p=15944"), S("Solo Guides", "https://sologuides.com/pai")])
TC("c-pai-whitebuddha", "White Buddha (Wat Phra That Mae Yen)", PA, 19.3540, 98.4580, ["Temples", "Views"],
   s=["Big white Buddha looking over Pai, up a long staircase; great sunset views"], cost="Free",
   tips=["Cover shoulders and knees; scarves for hire at the entrance"], src=[S("Go To Thailand", "https://gotothailand.com/pai/"), S("Walfos", "https://walfosbrand.com/blogs/thailand/best-things-to-do-places-pai")])
TC("c-pai-landsplit", "The Land Split", PA, 19.3350, 98.4050, ["Excursions"],
   s=["A farm where an earthquake split the ground; the owner offers homegrown snacks and drinks"], cost="Donation",
   src=[S("Go To Thailand", "https://gotothailand.com/pai/"), S("The Backpacking Family", "https://thebackpackingfamily.com/pai-itinerary-one-week-thailand-travel/")])
TC("c-pai-saingam", "Sai Ngam Hot Spring", PA, 19.4300, 98.3600, ["Excursions"],
   s=["Warm, crystal-clear jungle hot-spring river on the way to Tham Lod"], cost="Covered by the 200 baht day pass",
   src=[TBF, S("Go To Thailand", "https://gotothailand.com/pai/")])

# ---------------- KOH SAMUI ----------------
KS = "Koh Samui"
BPHS = S("Best Party Hostels", "https://bestpartyhostels.pages.dev/asia/south-east-asia/thailand/koh-samui")
BKS = S("Booking.com", "https://www.booking.com/hostels/city/th/koh-samui.html")
TG("g-ks-lubd", "Lub d Koh Samui Chaweng Beach", KS, 9.5340, 100.0610, r=9.4, rs="Hostelworld (via Best Party Hostels)",
   s=["Beachfront party hostel on Chaweng with a pool, DJ sets and beer pong", "Picked as Samui’s best overall hostel by The Broke Backpacker"],
   tips=["Pricier than most hostels"], src=[BPHS, S("The Broke Backpacker", "https://www.thebrokebackpacker.com/?p=58957"), S("Expedia", "https://mob.expedia.ae/Koh-Samui-Hostels.d6035013-aaHostels.Travel-Guide-Accommodation")])
TG("g-ks-socialtel", "SocialTel Samui", KS, 9.5300, 100.0600, s=["Chaweng Beach; the flashpacker pick, a step up from a basic hostel"], src=[S("The Broke Backpacker", "https://www.thebrokebackpacker.com/?p=58957")])
TG("g-ks-rock", "The Rock Samui Poshtel Lamai Beach", KS, 9.4700, 100.0450, r=9.0, rs="Booking.com (164 reviews)", s=["Upmarket hostel in Lamai, calmer than Chaweng"],
   src=[S("Booking.com", "https://www.booking.com/hostels/city/th/ko-samui.html?aid=819619")])
TG("g-ks-p168", "P168 Hostel Samui", KS, 9.5300, 100.0570, r=8.6, rs="HotelsCombined (972 reviews)", s=["Chaweng; one of the best-reviewed budget beds on the island"],
   src=[S("HotelsCombined", "https://www.hotelscombined.co.uk/Place/Koh_Samui-hostels.htm"), BKS])
TG("g-ks-chillinnlamai", "Chill Inn Lamai Hostel & Beach Cafe", KS, 9.4680, 100.0460, r=8.4, rs="Booking.com (333 reviews)",
   s=["Lamai, with a pool, garden and its own beach area", "Social events and daily activities"], src=[S("Booking.com (via Routard)", "https://hotel.routard.com/hostels/city/th/koh-samui.en-gb.html?aid=304142"), BPHS])
TG("g-ks-chillinnchaweng", "Chill Inn Chaweng Hostel and Cafe", KS, 9.5310, 100.0590, r=8.6, rs="Booking.com (115 reviews)", s=["Chaweng branch of Chill Inn"], src=[BKS])
TG("g-ks-badmonkey", "Bad Monkey Samui Hostel", KS, 9.5320, 100.0600, r=8.0, rs="Booking.com (225 reviews)", s=["Chaweng, right in the nightlife area"], src=[BKS])
TG("g-ks-ushostel", "Us Hostel Samui", KS, 9.5550, 100.0300, r=9.6, rs="Expedia (11 reviews)", s=["Bophut, near Fisherman’s Village", "Garden, bar and restaurant; family feel"],
   src=[S("Expedia", "https://mob.expedia.ae/Koh-Samui-Hostels.d6035013-aaHostels.Travel-Guide-Accommodation"), S("Booking.com (via Routard)", "https://hotel.routard.com/hostels/city/th/koh-samui.en-gb.html?aid=304142")])
TG("g-ks-nomadstay", "Nomad Stay Hostel", KS, 9.5290, 100.0580, r=9.5, rs="Booking.com (20 reviews)", s=["Chaweng hostel with a co-working space"], src=[BKS])
TG("g-ks-monkey", "Monkey Samui Hostel", KS, 9.5310, 100.0560, s=["One of the cheapest beds on the island", "Guests love Hippo, the resident French bulldog"],
   src=[S("Expedia", "https://mob.expedia.ae/Koh-Samui-Hostels.d6035013-aaHostels.Travel-Guide-Accommodation"), S("HotelsCombined", "https://www.hotelscombined.com/Place/Koh_Samui-hostels.htm")])

THG = S("Thai Holiday Guide", "https://www.thaiholidayguide.com/best-restaurants-koh-samui/")
TGS = S("Travel Guides Tips", "https://travelguidestip.com/?p=2513")
HCS = S("Hotels.com", "https://en.hoteles.com/go/thailand/places-koh-samui-locals-love-to-eat")
TM("m-ks-fishermans", "Fisherman’s Village Friday Walking Street", KS, 9.5600, 100.0270, p=[50, 150], t=("Market",),
   s=["Samui’s best market: hundreds of stalls through Bophut’s old fishing village"], best="Friday evenings", tips=["A few restaurants nearby charge tourists double; check prices"],
   src=[TGS, S("12Go", "https://12go.com/en/thailand/koh-samui/tours"), S("Travel Arbitrage", "https://www.travelarbitrage.net/en/blog/koh-samui-attraction-tickets-friends-budget-2026/")])
TM("m-ks-nathon", "Nathon Sunday Market", KS, 9.5340, 99.9360, t=("Market",),
   s=["The most local market on the island, almost all Thai shoppers", "Best prices for grilled seafood and Thai desserts"], best="Sunday", src=[TGS])
TM("m-ks-chawengbazaar", "Chaweng Night Bazaar food stalls", KS, 9.5350, 100.0600, t=("Market",),
   s=["The cheap place to eat in pricey Chaweng"], best="Evenings", src=[THG])
TM("m-ks-lamaimarket", "Lamai Night Market", KS, 9.4700, 100.0440, t=("Market",), s=["Night market in Lamai for cheap eats and people-watching"],
   src=[S("Lub d", "https://lubd.com/scoop/backpacking-koh-samui-how-to-travel-cheap-and-have-the-best-time/"), S("Pickyourtrail", "https://pickyourtrail.com/tourism/thailand/things-to-do-in-koh-samui")])
TM("m-ks-greenbird", "Green Bird Restaurant", KS, 9.5330, 100.0610, t=("Restaurant",),
   s=["Chaweng Beach Road favourite with locals and budget travellers", "Try the fried basil and chilli with seafood"], src=[HCS])
TM("m-ks-surat", "Surat Restaurant", KS, 9.5370, 100.0620, t=("Restaurant",), s=["Tiny Thai eatery on Chaweng’s Soi Green Mango"],
   src=[S("Hotels.com", "https://el.hotels.com/see/go/thailand/places-koh-samui-locals-love-to-eat")])
TM("m-ks-noodlesoup", "Noodle Soup & Food", KS, 9.4800, 100.0400, t=("Restaurant",), s=["Does exactly what it says, on Road 4169 in Maret near Lamai"],
   src=[S("Hotels.com", "https://el.hotels.com/see/go/thailand/places-koh-samui-locals-love-to-eat")])
TM("m-ks-kruabophut", "Krua Bophut", KS, 9.5600, 100.0280, t=("Restaurant",), s=["One of the best overall restaurants in Fisherman’s Village"], src=[THG])
TM("m-ks-sabeinglae", "Sabeinglae", KS, 9.4550, 100.0350, t=("Restaurant",), s=["Seafood restaurant near Lamai, a local favourite"], src=[THG])
TM("m-ks-bangpo", "Bang Po seafood restaurants", KS, 9.5700, 99.9600, t=("Restaurant",), s=["Row of seafood restaurants on the quiet north-west coast, for a proper seafood dinner"],
   src=[S("Thai Holiday Guide", "https://www.thaiholidayguide.com/best-food-koh-samui/")])
TM("m-ks-lamaishops", "Lamai local shops (inland strip)", KS, 9.4720, 100.0420, p=[150], t=("Street food",), pu="filling lunch",
   s=["Chicken-rice shops, noodle stalls and curry places on the main street inland from the beach"], src=[THG])

TGK = S("Travel Guides Tips", "https://travelguidestip.com/best-things-to-do-in-koh-samui/")
TC("c-ks-angthong", "Ang Thong National Marine Park", KS, 9.6300, 99.6800, ["Excursions", "Diving", "Views"],
   s=["42 limestone islands: kayaking, snorkelling, the Emerald Lake and a steep viewpoint hike", "Full-day boat trips from Samui"],
   p=[1200, 1800], best="January to September", busy="Tours sell out in peak season",
   tips=["The park usually closes from about 1 November to mid-December for the monsoon, so check before booking", "Some tours add a 300–500 baht park fee"],
   src=[TGK, S("Travel Arbitrage", "https://www.travelarbitrage.net/en/blog/koh-samui-attraction-tickets-friends-budget-2026/"), S("Hanoi Voyage", "https://hanoivoyage.com/en/blog/visit-koh-samui-top-things-to-do.html")])
TC("c-ks-bigbuddha", "Big Buddha Temple (Wat Phra Yai)", KS, 9.5700, 100.0600, ["Temples", "Views"],
   s=["12-metre golden Buddha on a little island joined by a causeway, with views to Koh Phangan"], cost="Free", tips=["Cover shoulders and knees"],
   src=[S("Full Moon Party Thailand", "https://fullmoonparty-thailand.com/koh-samui-guide"), S("Hanoi Voyage", "https://hanoivoyage.com/en/blog/visit-koh-samui-top-things-to-do.html")])
TC("c-ks-namuang", "Na Muang Waterfalls", KS, 9.4660, 99.9800, ["Waterfalls", "Hikes"],
   s=["Waterfall 1 is easy to reach; Waterfall 2 is a 20–30 minute jungle walk and quieter"], cost="Waterfall 1 free; Waterfall 2 about 30–100 baht",
   best="9 am to 5:30 pm", src=[S("Nomadasaurus", "https://www.nomadasaurus.com/koh-samui-itinerary/"), S("Travel Arbitrage", "https://www.travelarbitrage.net/en/blog/koh-samui-attraction-tickets-friends-budget-2026/")])
TC("c-ks-plailaem", "Wat Plai Laem", KS, 9.5730, 100.0700, ["Temples"], s=["Lakeside temple with a striking 18-armed statue of Guanyin, near Big Buddha"],
   cost="Free; donations welcome", src=[S("Pattaya Talk", "https://pattayatalk.com/things-to-do/embrace-the-spirit-of-ko-samui")])
TC("c-ks-secretgarden", "Secret Buddha Garden", KS, 9.4950, 100.0010, ["Views", "Excursions"], s=["Jungle hilltop garden of statues built by a local farmer"], p=[80],
   best="10 am to 5 pm", tips=["Steep road; take a jeep tour if you’re not confident on a scooter"], src=[S("Hanoi Voyage", "https://hanoivoyage.com/en/blog/visit-koh-samui-top-things-to-do.html")])
TC("c-ks-elephants", "Samui Elephant Sanctuary", KS, 9.5550, 100.0450, ["Excursions"], s=["Ethical sanctuary visit: feeding, bathing and a mud walk"], p=[1500, 2000],
   tips=["Sells out in peak season"], src=[TGK])
TC("c-ks-pubcrawl", "Koh Samui Pub Crawl", KS, 9.5320, 100.0600, ["Nightlife"], s=["Guided night out around Chaweng’s bars and clubs"], p=[800], best="Thursdays and Saturdays", src=[BPHS])
TC("c-ks-chaweng", "Chaweng Beach", KS, 9.5300, 100.0640, ["Beaches", "Nightlife"], s=["Samui’s busiest beach and party strip, lovely at sunrise"], cost="Free",
   src=[S("Lub d", "https://lubd.com/scoop/backpacking-koh-samui-how-to-travel-cheap-and-have-the-best-time/")])
TC("c-ks-lamai", "Lamai Beach and Hin Ta Hin Yai rocks", KS, 9.4440, 100.0420, ["Beaches"], s=["Relaxed beach with the famous ‘Grandfather and Grandmother’ rock formations"], cost="Free", src=[BPHS])

# ---------------- KOH PHANGAN ----------------
KP = "Koh Phangan"
BPHK = S("Best Party Hostels", "https://bestpartyhostels.pages.dev/asia/south-east-asia/thailand/koh-phangan")
HZK = S("Hostelz", "https://hostelz.com/best-hostels-koh-phangan")
HWFM = S("Hostelworld", "https://www.hostelworld.com/blog/?p=127181")
BKP = S("Booking.com", "https://www.booking.com/hostels/region/th/ko-pha-ngan.html")
FMTIP = "Haad Rin dorms climb to about £8–12 a night around the Full Moon, versus about £3 in Thong Sala; book a week or more ahead"
TG("g-kp-mbar", "MBar Hostel Haad Rin", KP, 9.6770, 100.0640, r=9.8, rs="Hostelworld (Booking.com 9.6 from 320 reviews)",
   s=["Steps from the Full Moon Party beach; Hostelz’s overall top pick", "Party hostel with its own bar and nightclub; staff get rave reviews"],
   tips=[FMTIP], src=[BPHK, HZK, BKP])
TG("g-kp-hideout", "Hideout Hostel", KP, 9.6780, 100.0660, r=9.3, rs="Hostelworld (via Best Party Hostels)",
   s=["Haad Rin, a 5-minute walk from the Full Moon beach, with a pool"], tips=[FMTIP], src=[BPHK])
TG("g-kp-wanderlust", "The Wanderlust Hostel", KP, 9.7000, 100.0400, r=8.9, rs="Hostelworld (via Best Party Hostels)",
   s=["Party hostel whose energy builds through Full Moon week"], src=[BPHK])
TG("g-kp-baankai", "Baan Kai Hostel", KP, 9.6990, 100.0480, p=[5.93], cur="USD", r=9.5, rs="Hostelz",
   s=["Hostelz’s top-rated hostel on the island", "Good for solo travellers and partygoers"], src=[HZK])
TG("g-kp-sogood", "So Good Haad Rin Hostel", KP, 9.6775, 100.0650, r=9.1, rs="Hostelz", s=["Best-rated hostel in Haad Rin by Hostelz’s scoring"],
   tips=[FMTIP], src=[S("Hostelz", "https://www.hostelz.com/best-hostels-haad-rin")])
TG("g-kp-shiralea", "Shiralea Backpackers Resort", KP, 9.7050, 100.0150, s=["Bungalow-style backpacker resort with a pool", "Picked as the best for female solo travellers"], src=[HZK])
TG("g-kp-kikos", "Kiko’s Hostel", KP, 9.7100, 100.0000, p=[189], s=["Thong Sala; guests call it the best hostel on the island"], tips=["Cash only"], src=[S("Hostelz", "https://www.hostelz.com/hostels/Thailand/Koh-Phangan")])
TG("g-kp-nomadhouse", "The Nomad House", KP, 9.7150, 100.0050, s=["Bangkrak Beach near Thong Sala; social, with a shuttle bus to the Full Moon Party"], src=[HWFM, S("Hostelz", "https://www.hostelz.com/hostels/Thailand/Koh-Phangan/safe-hostels")])
TG("g-kp-echo", "Echo Beach Hostel", KP, 9.6950, 100.0300, s=["Beachfront hammocks and bean bags; popular for the Full Moon"], src=[HWFM])
TG("g-kp-roadtrip", "Roadtrip Phangan", KP, 9.6765, 100.0655, s=["About 100 m from Haad Rin beach, under a minute to the party"], tips=[FMTIP], src=[HWFM])
TG("g-kp-lingling", "Lingling Hostel", KP, 9.6772, 100.0648, s=["Centre of Haad Rin with a big common area, bar and Full Moon pre-parties", "Guests praise the friendly staff"], tips=[FMTIP],
   src=[S("Hostelworld", "https://www.hostelworld.com/hostels/p/329196/lingling-hostel/")])
TG("g-kp-moonhouse", "Moon House Beach Hostel", KP, 9.6768, 100.0652, r=8.9, rs="Booking.com (105 reviews)", s=["Haad Rin; one reviewer recommends the jacket potatoes"], tips=[FMTIP], src=[BKP])
TG("g-kp-propaganda", "PROpaganda Hostel", KP, 9.7110, 100.0010, r=8.2, rs="Booking.com (689 reviews)", s=["Thong Sala; ‘home away from home’ according to reviewers"], src=[BKP])
TG("g-kp-10club", "The 10 Club Hostel", KP, 9.7105, 100.0005, s=["Thong Sala; rated ‘wonderful’ from 600+ Booking.com reviews"], src=[BKP])
TG("g-kp-madmonkey", "Mad Monkey Hostel Koh Phangan", KP, 9.6960, 100.0320, s=["Mad Monkey’s Phangan hostel with a pool"], src=[HWFM])

BPFK = S("The Backpacking Family", "https://thebackpackingfamily.com/?p=3713")
ALK = S("Amazing Lanta", "https://amazinglanta.com/places-to-eat-on-koh-phangan/")
G12K = S("12Go", "https://12go.asia/en/thailand/koh-phangan/food")
TM("m-kp-foodcourt", "Phangan Food Court", KP, 9.7095, 100.0000, p=[100, 300], s=["Lots of variety in one place, a short walk from Thong Sala pier"], best="10:30 am to 11 pm", src=[BPFK])
TM("m-kp-fisherman", "Fisherman’s Restaurant & Bar", KP, 9.6950, 100.0250, t=("Restaurant",),
   s=["The island’s best-known seafood spot: pick your fish and one of 12 sauces"], src=[S("Fodor’s", "https://cdn.fodors.com/world/asia/thailand/the-gulf-coast-beaches/places/koh-phangan/restaurants"), G12K, ALK])
TM("m-kp-mateo", "Mateo Muslim Restaurant", KP, 9.6990, 100.0480, t=("Restaurant",), s=["Cheap Thai food right on the beach at Baan Kai"], src=[G12K])
TM("m-kp-myfriend", "My Friend Restaurant", KP, 9.6775, 100.0645, t=("Restaurant",), s=["Cheap Thai eatery in Haad Rin"], src=[G12K])
TM("m-kp-jipshop", "Jip Shop", KP, 9.7975, 100.0730, t=("Restaurant",), s=["Popular Thai restaurant near Thong Nai Pan Noi"], src=[ALK])
TM("m-kp-alex", "Alex Restaurant", KP, 9.7780, 99.9750, t=("Restaurant",), s=["Cheap, simple Thai restaurant a short walk from Haad Salad"], src=[ALK])
TM("m-kp-homemade", "Phangan Homemade", KP, 9.7150, 100.0050, t=("Cafe",), s=["Garden café just outside Thong Sala, famous for its homemade ice cream; good Thai food too"], src=[ALK])
TM("m-kp-julien", "Julien’s Bakery", KP, 9.7100, 100.0000, t=("Cafe",), s=["Hidden-gem bakery in Thong Sala"], src=[BPFK])
TM("m-kp-kaif", "Kaif", KP, 9.7880, 100.0010, p=[100, 200], t=("Cafe",), s=["Chaloklum café for a proper cooked breakfast and coffee"], src=[BPFK])
TM("m-kp-vintage", "Vintage Burgers", KP, 9.7090, 100.0020, t=("Restaurant",), s=["Juicy burgers 550 m from Thong Sala pier, handy before a ferry"],
   src=[S("Hotels.com", "https://www.hotels.com/go/thailand/great-koh-phangan-restaurants")])
TM("m-kp-seafoodbbq", "Haad Rin seafood barbecues", KP, 9.6772, 100.0655, t=("Restaurant",), s=["Beachfront restaurants with all-you-can-eat seafood barbecues; choose from the catch on display"], src=[G12K])

GRK = S("Gecko Routes", "https://www.geckoroutes.com/thailand/things-to-do-in-koh-phangan-thailand/")
BPHG = S("Best Party Hostels", "https://bestpartyhostels.pages.dev/blog/full-moon-party-koh-phangan-guide")
for _p in places:
    if _p["id"] == "c-fullmoon":
        _p["tips"] = list(_p.get("tips") or []) + ["2026 dates include 24 December, plus a New Year’s Eve countdown party on 31 December; it runs 6 pm to 6 am",
            "Shared songthaews back to Thong Sala run all night, about $5–10, pricier after 3 am"]
        _p["src"] = list(_p.get("src") or []) + [S("Bangkok Airways blog", "https://blog.bangkokair.com/en/full-moon-party-koh-phangan-guide/"), BPHG]
TC("c-kp-halfmoon", "Half Moon Festival", KP, 9.7100, 100.0350, ["Nightlife"], s=["Jungle party with techno and house in a purpose-built arena in Baan Tai, smaller than the Full Moon"],
   cost="Ticketed (not checked)", best="About two weeks after each Full Moon", src=[BPHG, S("St Christopher’s", "https://st-christophers.co.uk/travel-blog/things-to-do-on-koh-phangan-thailand")])
TC("c-kp-jungle", "Jungle Experience", KP, 9.6850, 100.0600, ["Nightlife"], s=["Monthly electronic music event in the hills above Haad Rin"], cost="Ticketed (not checked)",
   best="The week before the Full Moon", src=[BPHG])
TC("c-kp-bottle", "Bottle Beach (Haad Khuad)", KP, 9.7930, 100.0400, ["Beaches"], s=["Secluded north-coast beach, reached by boat or a rough road; some of the island’s best swimming"], cost="Free",
   src=[GRK, BPHG])
TC("c-kp-phasawan", "Pha Sawan Viewpoint", KP, 9.7880, 100.0380, ["Views", "Hikes"], s=["Clifftop viewpoint over the north coast above Bottle Beach; the trail gets steep near the top"],
   cost="Free (not checked)", src=[S("Bangkok Airways blog", "https://blog.bangkokair.com/?p=20390"), S("Takeoff", "https://takeoff.to/destinations/koh-phangan")])
TC("c-kp-phaeng", "Phaeng Waterfall and Dom Sila Viewpoint", KP, 9.7400, 100.0300, ["Waterfalls", "Hikes", "Views"],
   s=["The island’s biggest waterfall in the jungle, with a steep path up to the Dom Sila viewpoint"], cost="Park fee may apply (not checked)",
   src=[S("Holidify", "https://www.holidify.com/places/koh-pha-ngan/sightseeing-and-things-to-do.html"), GRK])
TC("c-kp-thansadet", "Than Sadet Waterfall", KP, 9.7550, 100.0650, ["Waterfalls"], s=["Huge granite boulders and freshwater swimming pools"], cost="Free (not checked)",
   src=[S("Holidify", "https://www.holidify.com/places/koh-pha-ngan/sightseeing-and-things-to-do.html")])
TC("c-kp-tnpnoi", "Thong Nai Pan Noi Beach", KP, 9.7980, 100.0720, ["Beaches"], s=["Calm, pretty bay on the north-east coast with good snorkelling"], cost="Free",
   src=[BPHG, S("Takeoff", "https://takeoff.to/destinations/koh-phangan")])
TC("c-kp-secretbeach", "Haad Son (Secret Beach)", KP, 9.7550, 99.9750, ["Beaches", "Views"], s=["West-coast beach known for sunsets; Haad Salad next door is good for snorkelling"], cost="Free", src=[GRK])

# ---------------- PHUKET ----------------
PK = "Phuket"
BPHPK = S("Best Party Hostels", "https://bestpartyhostels.pages.dev/asia/south-east-asia/thailand/phuket")
BKPK = S("Booking.com", "https://www.booking.com/hostels/region/th/phuket.en-gb.html")
PKTIP = "Shared songthaews run between Phuket Town and Patong, Kata and Karon for 30–50 baht; tuk-tuks ask 200–400"
TG("g-pk-madmonkey", "Mad Monkey Phuket", PK, 7.8930, 98.2970, r=9.4, rs="Hostelworld (via Best Party Hostels)", s=["Phuket’s top-rated party hostel, with organised parties"], src=[BPHPK])
TG("g-pk-slumberkata", "Slumber Party Surf Kata Phuket", PK, 7.8200, 98.2990, r=8.0, rs="Hostelworld (via Best Party Hostels)", s=["Party hostel in Kata, with surf in the rainy season"], tips=[PKTIP], src=[BPHPK])
TG("g-pk-sweettlemon", "Sweett Lemon Hostel", PK, 7.8960, 98.3000, p=[15.83], cur="USD", r=9.6, rs="Hostelz", s=["The top-rated hostel in Patong by Hostelz’s scoring"], src=[S("Hostelz", "https://www.hostelz.com/best-hostels-phuket-patong-beach")])
TG("g-pk-bookabed", "Book a Bed Poshtel", PK, 7.8860, 98.3880, r=8.8, rs="Hostelworld (850 reviews)", rc=850,
   s=["Phuket Town ‘poshtel’; Hostelgeeks’ pick for the best hostel in Phuket"], tips=[PKTIP], src=[S("Hostelworld", "https://www.hostelworld.com/hostels/asia/thailand/phuket/d/phuket-town/"), HGK])
TG("g-pk-dorm", "The Dorm Hostel", PK, 7.8870, 98.3900, r=8.3, rs="Hostelworld (281 reviews)", s=["Phuket Town, with free breakfast"],
   src=[S("Hostelworld", "https://www.hostelworld.com/hostels/asia/thailand/phuket/p/2/"), S("Hostelz", "https://hostelz.com/hostels/Thailand/Phuket-City")])
TG("g-pk-sinokata", "Sino Hostel @ Kata", PK, 7.8210, 98.3000, s=["Dorm-only hostel close to Kata Beach"], src=[S("Hostelworld", "https://www.hostelworld.com/hostels/asia/thailand/phuket/p/2/")])
TG("g-pk-inest", "iNest Poshtel", PK, 7.8200, 98.3010, r=9.1, rs="Cozycozy (938 reviews)", s=["Kata Beach poshtel, close to Karon and Kata Noi beaches"], src=[S("Cozycozy", "https://www.cozycozy.com/gb/phuket-hostels")])
TG("g-pk-sleepystation", "Sleepy Station Hostel", PK, 7.8400, 98.2990, r=9.6, rs="Expedia (23 reviews)", s=["Karon; small and very well rated"], src=[S("Expedia", "https://www.expedia.com/es/Pa-Khlok-Hostales.d6230957-aaHostales.Guia-Viajes-Alojamiento")])
TG("g-pk-kuha", "Kuha Phuket Old Town", PK, 7.8840, 98.3870, s=["Old Town, walking distance to the markets and street art"], src=[S("Cozycozy", "https://www.cozycozy.com/nz/phuket-hostels")])
TG("g-pk-shunli", "Shunli Hotel", PK, 7.8850, 98.3890, t=("Hotel",), r=9.7, rs="Booking.com (1,000+ reviews)", s=["Old Town; guests rave about the comfy beds"], src=[BKPK])
TG("g-pk-beanstay", "Beanstay Hostel", PK, 7.8855, 98.3875, r=9.2, rs="Booking.com", s=["Adults-only Old Town hostel with a garden and terrace"], src=[BKPK])
TG("g-pk-purr", "Purr", PK, 7.8830, 98.3900, r=9.1, rs="Booking.com", s=["Phuket Town; one guest called it the best hostel in the Old Town"], src=[BKPK])
TG("g-pk-finkata", "Fin Hostel Phuket Kata", PK, 7.8190, 98.3005, s=["Picked as the best hostel for beach lovers"], src=[S("Pickyourtrail", "https://pickyourtrail.com/tourism/thailand/best-hostels-in-phuket")])

TGPF = S("Travel Guides Tips", "https://travelguidestip.com/?p=177")
TFK = S("Travelfika", "https://www.travelfika.com/tourism/phuket")
TM("m-pk-sundaywalk", "Lard Yai Sunday Walking Street", PK, 7.8845, 98.3885, p=[300, 600], t=("Market",), pu="food budget for the evening",
   s=["Thalang Road closes to traffic for street food, crafts and live music among the old shophouses", "Try moo hong (braised pork belly), gaeng som and kanom jeen"],
   best="Sundays 4 pm to 10 pm; arrive by 5 pm", src=[TGPF, S("The Thaiger", "https://thethaiger.com/travel/phuket-travel/things-to-do-phuket-every-type-traveller"), S("Gotripzi", "https://www.gotripzi.com/destinations/phuket-th")])
TM("m-pk-locktien", "Lock Tien food court", PK, 7.8848, 98.3878, p=[40, 80],
   s=["Old Town food court for Phuket’s Hokkien-style specialities: mee Hokkien noodles, oh-aew ice dessert and steamed buns"],
   src=[S("Thai Holiday Guide", "https://archived-bricks.thaiholidayguide.com/?p=22396")])
TM("m-pk-chillva", "Chillva Market", PK, 7.8960, 98.3940, t=("Market",), s=["Hip container market with live music, vintage clothes and food"], best="Mon to Sat, 5 pm to 11 pm", src=[TFK])
TM("m-pk-naka", "Naka Weekend Market", PK, 7.8630, 98.3730, t=("Market",), s=["Phuket’s biggest market, with a long street-food alley"], best="Sat and Sun, 4 pm to 11 pm",
   src=[TFK, S("The Thaiger", "https://thethaiger.com/travel/phuket-travel/things-to-do-phuket-every-type-traveller")])
TM("m-pk-indy", "Indy Market", PK, 7.8870, 98.3900, t=("Market",), s=["Smaller, local night market near the Old Town with good Thai snacks"], best="Mon to Sat, 5 pm to 10 pm", src=[TFK])
TM("m-pk-raya", "Raya House", PK, 7.8860, 98.3885, t=("Restaurant",), s=["Peranakan (Thai-Chinese) cooking in an old house on Dibuk Road"],
   src=[S("The Thaiger", "https://thethaiger.com/travel/phuket-travel/things-to-do-phuket-every-type-traveller")])
TM("m-pk-tukabkhao", "Tu Kab Khao", PK, 7.8835, 98.3895, t=("Restaurant",), s=["Phuket regional dishes in a restored shophouse on Phang Nga Road"],
   src=[S("The Thaiger", "https://thethaiger.com/travel/phuket-travel/things-to-do-phuket-every-type-traveller")])
TM("m-pk-meehokkien", "Old Town mee Hokkien stalls", PK, 7.8842, 98.3882, p=[50], s=["Charcoal-wok Hokkien noodles, Phuket’s signature dish, in the Old Town"],
   src=[S("Aifly", "https://aifly.one/?p=23462")])

AIF = S("Aifly", "https://aifly.one/?p=23462")
TC("c-pk-bigbuddha", "Big Buddha Phuket", PK, 7.8278, 98.3125, ["Temples", "Views"], s=["45-metre white marble Buddha on Nakkerd Hill with views over the island", "Reopened in 2026 after a two-year closure"],
   cost="Free; donations welcome", tips=["Cover shoulders and knees"], src=[AIF, S("Royal Caribbean", "https://www.royalcaribbean.com/inspire/things-to-do-in-phuket")])
TC("c-pk-phangnga", "Phang Nga Bay and James Bond Island", PK, 8.2750, 98.5010, ["Excursions", "Views"],
   s=["Limestone karsts, sea-cave kayaking and the stilt village of Koh Panyi", "James Bond Island is from The Man with the Golden Gun"],
   p=[1400, 1900], best="Go early to beat the crowds", src=[AIF, S("Phuket 101", "https://www.phuket101.net/things-to-do-in-phuket"), S("Klook", "https://www-verify.klook.cn/en-US/city/7-phuket-things-to-do")])
TC("c-pk-phiphitrip", "Phi Phi Islands day trip from Phuket", PK, 7.8580, 98.4004, ["Excursions", "Beaches", "Diving"],
   s=["Speedboat day trips to Maya Bay, Viking Cave and Monkey Beach, leaving Rassada Pier about 8 am"], p=[1400, 2400],
   tips=["Maya Bay has a daily visitor cap and no swimming", "Book a day ahead"], src=[AIF, S("Thai Holiday Guide", "https://archived-bricks.thaiholidayguide.com/?p=22396")])
TC("c-pk-promthep", "Promthep Cape", PK, 7.7620, 98.3050, ["Views"], s=["Phuket’s famous sunset viewpoint on the southern tip"], cost="Free", best="Arrive 45 minutes before sunset",
   src=[S("Pickyourtrail", "https://pickyourtrail.com/tourism/thailand/phuket"), S("Royal Caribbean", "https://www.royalcaribbean.com/inspire/things-to-do-in-phuket")])
TC("c-pk-oldtown", "Old Phuket Town", PK, 7.8840, 98.3880, ["Museums", "Views"], s=["Colourful Sino-Portuguese shophouses, street art and cafés along Thalang Road, Dibuk Road and Soi Romanee"],
   cost="Free", best="Golden hour", src=[AIF, S("Pickyourtrail", "https://pickyourtrail.com/tourism/thailand/places-to-visit-in-phuket")])
TC("c-pk-thaihua", "Thai Hua Museum", PK, 7.8850, 98.3870, ["Museums"], s=["The best introduction to Phuket’s Peranakan and tin-mining history"], p=[200], src=[AIF])
TC("c-pk-chalong", "Wat Chalong", PK, 7.8460, 98.3370, ["Temples"], s=["Phuket’s largest and most important temple"], cost="Free",
   src=[S("Travelfika", "https://www.travelfika.com/tourism/phuket"), S("JFTB", "https://www.jftb-real-estate-phuket.com/blog/what-to-do-in-phuket-2025.html")])
TC("c-pk-bangla", "Bangla Road", PK, 7.8935, 98.2970, ["Nightlife"], s=["Patong’s neon nightlife strip of bars and clubs"], cost="Free to walk", best="After 10 pm",
   tips=["Grab pickups are often blocked near Bangla after midnight", "Cocktails are overpriced; stick to bottled beer"], src=[BPHPK, S("Nomado", "https://www.nomadotravel.app/en/guides/things-to-do-in-phuket")])
TC("c-pk-naiharn", "Nai Harn Beach", PK, 7.7780, 98.3040, ["Beaches"], s=["One of Phuket’s prettiest, calmer beaches near Promthep Cape"], cost="Free",
   src=[S("Royal Caribbean", "https://www.royalcaribbean.com/inspire/things-to-do-in-phuket"), S("Thai Holiday Guide", "https://archived-bricks.thaiholidayguide.com/?p=22396")])
TC("c-pk-freedom", "Freedom Beach", PK, 7.8740, 98.2770, ["Beaches"], s=["Secluded beach south of Patong, reached by longtail boat or a steep path"], cost="Free (boat extra)",
   src=[S("Thai Holiday Guide", "https://archived-bricks.thaiholidayguide.com/?p=22396")])

# ---------------- KRABI TOWN, AO NANG, RAILAY ----------------
NEW_CITIES += [["Railay", 8.0110, 98.8380], ["Krabi Town", 8.0863, 98.9063]]
AN, KT, RL = "Ao Nang", "Krabi Town", "Railay"
HZKB = S("Hostelz", "https://www.hostelz.com/best-hostels-krabi")
HWKB = S("Hostelworld", "https://www.hostelworld.com/hostels/asia/thailand/krabi/")
VTTAN = S("Visit Thailand Today", "https://www.visitthailandtoday.com/guides/things-to-do-in-ao-nang")
GTK = S("Gotripzi", "https://www.gotripzi.com/destinations/krabi-th/cost")
EXK = S("Expats Thai", "https://expatsthai.pages.dev/cities/krabi/things-to-do")
TG("g-an-nomads", "Nomads Ao Nang Beach", AN, 8.0390, 98.8150, p=[10.55], cur="USD", r=9.7, rs="Hostelworld (3,400+ reviews)", rc=3427,
   s=["Ao Nang’s top-rated hostel and the area’s party pick"], src=[HWKB, HZKB])
TG("g-an-kbunk", "K-Bunk AoNang Center", AN, 8.0330, 98.8240, p=[3.38], cur="USD", r=9.0, rs="Hostelz", s=["Central, cheap and social; Hostelz’s best hostel in Ao Nang"],
   src=[HZKB, S("Hostelz", "https://hostelz.com/youth-hostels-in-ao-nang")])
TG("g-an-base", "Base Ao Nang Beachfront", AN, 8.0300, 98.8180, p=[16.26], cur="USD", r=9.4, rs="Hostelz", s=["Right on the beachfront"], src=[HZKB])
TG("g-an-hangover", "Hangover Aonang", AN, 8.0345, 98.8230, p=[10.28], cur="USD", r=9.0, rs="Hostelz", s=["Near Ao Nang’s bars, shops and restaurants"], src=[HZKB])
TG("g-an-seabeach", "Sea Beach Hostel & Club", AN, 8.0315, 98.8195, r=8.9, rs="Hostelz", s=["Beachfront hostel with its own club"], src=[HZKB, S("Hostelworld", "https://www.hostelworld.com/hostels/asia/thailand/krabi/d/ao-nang/")])
TG("g-an-sleeper", "Sleeper Hostel", AN, 8.0360, 98.8250, r=8.3, rs="Hostelworld (728 reviews)", s=["Popular, well-reviewed Ao Nang hostel"], src=[S("Hostelworld", "https://www.hostelworld.com/hostels/asia/thailand/krabi/d/ao-nang/")])
TG("g-an-popin", "Pop In Hostel", AN, 8.0350, 98.8220, p=[8], cur="USD", s=["Newer Ao Nang hostel from the team behind Pak-Up in Krabi Town"], src=[S("Hostelworld", "https://www.hostelworld.com/hostels/asia/thailand/krabi/d/ao-nang/")])
TG("g-an-irest", "iRest Ao Nang", AN, 8.0365, 98.8235, r=8.6, rs="Hostelworld (166 reviews)", s=["Quieter pick in Ao Nang"], src=[HWKB])
TG("g-kt-pakup", "Pak-Up Hostel", KT, 8.0620, 98.9170, p=[12, 15], cur="USD",
   s=["Krabi Town’s benchmark backpacker hostel", "Rooftop bar with ฿70-ish beers; the tour desk books Railay trips for about $18"],
   src=[S("Travel Guides Tips", "https://travelguidestip.com/best-hotels-in-krabi/"), S("Krabi Nature", "https://krabinature.com/krabi-on-a-budget-save-money-and-enjoy-paradise")])
TG("g-kt-talardkao", "Talardkao Balcony", KT, 8.0640, 98.9150, p=[12.33], cur="USD", r=8.9, rs="Hostelz", s=["Top-rated hostel in Krabi Town, mixing Thai style and modern comforts"], src=[HZKB])
TG("g-kt-tan", "TAN Hostel x Cafe", KT, 8.0655, 98.9160, p=[10.27], cur="USD", s=["Helpful staff and a café downstairs"], src=[HZKB])
TG("g-kt-play", "Play Poshtel", KT, 8.0700, 98.9100, p=[14], cur="USD", s=["Stylish, design-led poshtel in Krabi Town"], src=[HWKB])

TM("m-an-landmark", "Ao Nang Landmark Night Market", AN, 8.0470, 98.8050, p=[60, 150], t=("Market",), s=["Ao Nang’s nightly food market opposite Nopparat Thara Beach; Google 4.4 from 7,800 reviews"],
   best="Daily 5 pm to 11 pm", src=[VTTAN, GTK])
TM("m-kt-walking", "Krabi Town Weekend Walking Street", KT, 8.0640, 98.9150, p=[30, 120], t=("Market",), s=["Maharaj Road fills with street food, crafts and live music"],
   best="Friday to Sunday evenings", src=[S("Thailand Boat Tickets", "https://thailandboattickets.com/en/guides/to-do-in-krabi"), GTK])
TM("m-kt-nightmarket", "Krabi Town night market", KT, 8.0610, 98.9180, p=[50, 80], t=("Market",), s=["Authentic local night market; pad thai about ฿57, mango sticky rice about ฿76"], best="Evenings",
   src=[S("Skyscanner", "https://www.skyscanner.com/destinations/advice/things-to-do-in-krabi"), S("Gotripzi", "https://gotripzi.com/destinations/krabi-th")])

TC("c-kt-tigercave", "Tiger Cave Temple (Wat Tham Suea)", KT, 8.1260, 98.9230, ["Temples", "Hikes", "Views"],
   s=["1,237 steep steps to a golden Buddha and huge views; Google 4.6 from 13,900 reviews"], cost="Free", best="Start at 6 am, before the heat",
   tips=["Bring water", "Watch out for monkeys stealing snacks", "Cover shoulders and knees"], src=[VTTAN, EXK, S("Krabi Nature", "https://krabinature.com/krabi-on-a-budget-save-money-and-enjoy-paradise")])
TC("c-an-4islands", "Krabi 4 Islands tour", AN, 8.0320, 98.8200, ["Excursions", "Beaches", "Diving"],
   s=["Phra Nang Cave, Tup Island, Chicken Island and Koh Poda, with snorkelling and lunch"], p=[800, 1800],
   tips=["Longtail is cheaper (฿800–1,200) than speedboat (฿1,200–1,800)", "Check whether the ~฿200 national park fee is included"], src=[EXK, GTK])
TC("c-an-hong", "Hong Islands tour", AN, 8.0800, 98.6800, ["Excursions", "Diving"], s=["Emerald lagoon ringed by cliffs, with kayaking and snorkelling; quieter than the 4 Islands"],
   tips=["The ~฿300 national park fee is often not included"], src=[EXK, GTK, VTTAN])
TC("c-kt-emerald", "Emerald Pool and Hot Springs", KT, 7.9260, 99.2670, ["Waterfalls", "Excursions"], s=["Jungle pool of clear green water, plus a walk to the Blue Pool and warm hot-spring streams", "About 60 km from Ao Nang"],
   p=[400], best="Arrive early", src=[S("The Manduls", "https://themanduls.com/?p=18691"), EXK])
TC("c-rl-railay", "Railay and Phra Nang Cave Beach", RL, 8.0060, 98.8380, ["Beaches", "Views"],
   s=["Car-free peninsula of limestone cliffs, reached only by boat", "Phra Nang Cave Beach is a 10-minute walk from Railay West"], cost="Longtail from Ao Nang ฿100 each way",
   best="Before 10 am, before tour boats arrive", tips=["Boats cost about ฿50 more after 6 pm"], src=[VTTAN, GTK, S("Gotripzi", "https://gotripzi.com/destinations/krabi-th")])
TC("c-rl-climbing", "Railay rock climbing", RL, 8.0110, 98.8380, ["Excursions", "Hikes"], s=["One of the world’s great sport-climbing spots, with 700+ routes and beginner courses"],
   cost="Courses and guides vary (not checked)", src=[EXK])
TC("c-an-monkeytrail", "Monkey Trail to Pai Plong Beach", AN, 8.0280, 98.8100, ["Hikes", "Beaches"], s=["Short jungle-and-boardwalk trail from Ao Nang to a quiet beach"], cost="Free",
   best="Early morning", src=[VTTAN])
TC("c-an-dragoncrest", "Dragon Crest (Khao Ngon Nak) viewpoint", AN, 8.0530, 98.7860, ["Hikes", "Views"], s=["Tough jungle hike to a famous cliff-edge viewpoint over the coast"],
   cost="Park fee (not checked)", best="Start early", src=[VTTAN, S("The Manduls", "https://themanduls.com/things-to-do-in-krabi/")])
TC("c-an-sunset", "Ao Nang Beach sunset", AN, 8.0320, 98.8180, ["Beaches", "Views"], s=["Long beach facing the limestone islands, best in the hour before sunset"], cost="Free", src=[VTTAN])

# ---------------- KOH PHI PHI ----------------
PP = "Koh Phi Phi"
VTTP = S("Visit Thailand Today", "https://www.visitthailandtoday.com/guides/things-to-do-in-koh-phi-phi")
VTTPG = S("Visit Thailand Today", "https://www.visitthailandtoday.com/guides/koh-phi-phi-guide")
PPTIP = "Phi Phi is pricey for Thailand: dorms average about $19 a night"
TG("g-pp-bluehorizon", "Blue Horizon Hostel by Blue Flow", PP, 7.7400, 98.7700, r=8.0, rs="Booking.com (149 reviews)", s=["Comfy beds and a perfect location, say guests"], tips=[PPTIP],
   src=[S("Booking.com (via Priceline)", "https://h.priceline.com/hostels/city/th/phi-phi-don.en-gb.html")])
TG("g-pp-blueflow", "Blue Flow Hostel", PP, 7.7405, 98.7710, s=["Phi Phi’s best-known party hostel by Hostelz’s count"], tips=[PPTIP], src=[S("Hostelz", "https://hostelz.com/hostels/Thailand/Ko-Phi-Phi")])
TG("g-pp-view", "The View Hostel", PP, 7.7420, 98.7725, s=["A minute’s walk from Loh Dalam Bay"], tips=[PPTIP], src=[S("Expedia", "https://www.expedia.co.kr/en/Ko-Phi-Phi-Hotels-The-View-Hostel.h122416107.Hotel-Information")])
TG("g-pp-nacha", "Nacha Hostel", PP, 7.7395, 98.7695, s=["Budget hostel on Phi Phi Don"], tips=[PPTIP], src=[S("Booking.com", "https://www.booking.com/hostels/city/th/phi-phi-don.html?aid=340993")])
TG("g-pp-paradise", "Phi Phi Paradise Hostel", PP, 7.7410, 98.7690, p=[7.5], cur="USD", s=["The cheapest bed on the island by Hostelz’s count"], src=[S("Hostelz", "https://hostelz.com/hostels/Thailand/Ko-Phi-Phi")])

TC("c-pp-lehcircuit", "Phi Phi Leh boat trip (Maya Bay and Pileh Lagoon)", PP, 7.6780, 98.7660, ["Excursions", "Beaches", "Diving"],
   s=["Half-day longtail loop: Maya Bay (from The Beach), the cliff-enclosed Pileh Lagoon, Viking Cave and snorkel stops"], p=[1200, 1500],
   best="Take the 7 am boat, before the Phuket speedboats arrive about 10 am", tips=["Plus a ฿400 national park fee in cash; keep the ticket, it’s valid all day", "No swimming at Maya Bay"],
   src=[VTTP, VTTPG, S("Go Asia", "https://goasia.cc/en/article/phi-phi-islands")])
TC("c-pp-viewpoint", "Phi Phi Viewpoint", PP, 7.7440, 98.7780, ["Views", "Hikes"], s=["Hot, steep climb to the classic view over Phi Phi Don’s twin bays; Google 4.8 from 5,400 reviews"], p=[30],
   best="Sunrise or sunset", tips=["Viewpoint 3 is a little higher and quieter"], src=[S("Go Asia", "https://goasia.cc/en/article/phi-phi-islands"), VTTPG])
TC("c-pp-longbeach", "Long Beach and Shark Point", PP, 7.7290, 98.7830, ["Beaches", "Diving"], s=["White-sand beach with blacktip reef sharks to snorkel with just offshore"], cost="Free",
   best="Morning", src=[VTTP])
TC("c-pp-bamboo", "Bamboo Island", PP, 7.8200, 98.7650, ["Beaches", "Excursions"], s=["Peaceful little island with powdery sand, on many day tours"], cost="Tour or boat hire (not checked)",
   src=[S("Travel and Destinations", "https://www.travelanddestinations.com/?p=5613")])
TC("c-pp-monkey", "Monkey Beach", PP, 7.7560, 98.7860, ["Beaches"], s=["Small beach full of monkeys, a stop on most tours"], cost="On tours", tips=["Hold on to bags, cameras and drinks; the monkeys steal"],
   src=[S("Travel and Destinations", "https://www.travelanddestinations.com/?p=5613")])
TC("c-pp-diving", "Diving on Phi Phi", PP, 7.7395, 98.7685, ["Diving"], s=["Some of Thailand’s best-value diving, with courses for beginners"], cost="Courses vary (not checked)", src=[VTTPG])
TC("c-pp-nightlife", "Loh Dalam beach bars", PP, 7.7425, 98.7720, ["Nightlife"], s=["Phi Phi’s famously wild nightlife: fire shows, buckets and beach parties"], cost="Free to walk",
   src=[S("Nomadic Matt", "https://www.nomadicmatt.com/?p=7115")])

# ---------------- KOH LANTA ----------------
NEW_CITIES += [["Koh Lanta", 7.6250, 99.0400]]
LT = "Koh Lanta"
EXT = S("Explorer Tom", "https://explorertom.com/en/?p=63773")
CCL = S("Cozycozy", "https://www.cozycozy.com/en-ae/koh-lanta-hostels")
TG("g-lt-chaolay", "Lanta Chaolay", LT, 7.6550, 99.0350, r=9.0, rs="HotelsCombined (376 reviews)", s=["The island’s best-reviewed hostel on HotelsCombined"],
   src=[S("HotelsCombined", "https://www.hotelscombined.com/Place/Ko_Lanta-hostels.htm")])
TG("g-lt-aha", "Aha Lanta Cozy Hostel", LT, 7.4950, 99.0800, s=["Kantiang Bay in the quiet south, close to the national park"], src=[CCL])
TG("g-lt-sunnies", "Sunnies 24", LT, 7.5950, 99.0390, s=["Phra Ae, about 200 m from Long Beach"], src=[CCL])
TG("g-lt-bananaway", "Banana Way", LT, 7.6000, 99.0380, r=9.4, rs="Cozycozy (38 reviews)", s=["Small traveller’s lodge with air-con"], src=[CCL])
TG("g-lt-peacock", "Peacock Hostel", LT, 7.6270, 99.0400, s=["Cheap and clean, among local life in Saladan village"], src=[S("Hostelz", "https://www.hostelz.com/hostels/Thailand/koh-lanta")])
TG("g-lt-baanmook", "Baan Mook Anda Hostel", LT, 7.6100, 99.0370, s=["Hostel with a jacuzzi"], src=[CCL])
TM("m-lt-saladan", "Saladan Walking Street and Night Market", LT, 7.6290, 99.0380, t=("Market",), s=["Street-food stalls and night-market buzz in Lanta’s main village"],
   best="Every night in high season", tips=["Lots of Lanta closes from May to October"], src=[EXT, CCL])
TM("m-lt-oldtown", "Lanta Old Town eateries", LT, 7.5250, 99.1040, t=("Restaurant",), s=["Food shaped by Chinese, Muslim and Thai traditions in the old wooden shophouses"],
   best="Daytime", src=[EXT])
TC("c-lt-np", "Mu Ko Lanta National Park", LT, 7.4680, 99.0950, ["Hikes", "Beaches", "Views"], s=["Jungle trails, two beaches and an old lighthouse on the cliffs at Ta Noad Cape"], p=[200],
   best="8:30 am to 5:30 pm", tips=["Watch for monkeys"], src=[EXT, S("Expedia", "https://www.expedia.com.hk/Ko-Lanta.dx6035252")])
TC("c-lt-khlongchak", "Khlong Chak Waterfall", LT, 7.5230, 99.0960, ["Waterfalls", "Hikes"], s=["Jungle walk to a waterfall"], p=[40], tips=["Your national park ticket covers it on the same day; otherwise ฿200 + ฿40"], src=[EXT])
TC("c-lt-oldtown", "Lanta Old Town", LT, 7.5240, 99.1050, ["Museums", "Markets"], s=["Wooden shophouses, Chinese temples and handicrafts on the quiet east coast", "The Chao Leh Museum tells the sea-gypsy story"],
   cost="Free", best="Daytime; it empties out after dark", tips=["Be respectful around the Moken stilt-house community"],
   src=[S("Explorer Tom", "https://explorertom.com/en/koh-lanta-things-to-see-beaches/"), S("Expedia", "https://www.expedia.co.uk/Ko-Lanta.dx6035252")])
TC("c-lt-longbeach", "Long Beach (Phra Ae)", LT, 7.5950, 99.0370, ["Beaches"], s=["Lanta’s main beach, long and relaxed with beach bars"], cost="Free", src=[CCL, S("Agoda", "https://www.agoda.com/en-ie/city/koh-lanta-th.html")])

# ---------------- KOH TAO ----------------
KTO = "Koh Tao"
VTTT = S("Visit Thailand Today", "https://www.visitthailandtoday.com/guides/things-to-do-in-koh-tao")
THGT = S("Thai Holiday Guide", "https://www.thaiholidayguide.com/things-to-do-in-koh-tao/")
TAOTIP = "ATMs charge ฿250–350 per foreign-card withdrawal, so take out more at once"
TG("g-kt-savage", "Savage Hostel Koh Tao", KTO, 10.1000, 99.8280, r=8.6, rs="HotelsCombined (1,682 reviews)", s=["Rated the best hostel on Koh Tao by HotelsCombined"], tips=[TAOTIP],
   src=[S("HotelsCombined", "https://www.hotelscombined.ie/Place/Ko_Tao-hostels.htm")])
TG("g-kt-dearly", "The Dearly Koh Tao Hostel", KTO, 10.0890, 99.8270, r=9.0, rs="Cozycozy (2,500+ reviews)", s=["Hostel attached to a PADI 5-star dive resort; breakfast available"], tips=[TAOTIP],
   src=[S("Cozycozy", "https://www.cozycozy.com/au/ko-tao-hostels")])
TG("g-kt-revolution", "Revolution Koh Tao", KTO, 10.0960, 99.8290, s=["One of Koh Tao’s top hostels"], tips=[TAOTIP], src=[S("Cozycozy", "https://www.cozycozy.com/au/ko-tao-hostels")])
TG("g-kt-ddhut", "Dd Hut Koh Tao", KTO, 10.0950, 99.8300, s=["Budget hostel with breakfast available"], src=[S("Cozycozy", "https://www.cozycozy.com/ca/koh-tao-hostels")])
TC("c-kto-dive", "Learn to dive (Open Water course)", KTO, 10.0990, 99.8270, ["Diving"], s=["Koh Tao is where Thailand learns to dive; an Open Water certification takes about 3 days", "Famous sites include Chumphon Pinnacle, Twins, White Rock, Shark Island and Sail Rock"],
   cost="Varies by school; check what’s included", best="February to September for the clearest water", src=[THGT, VTTT, S("A Broken Backpack", "https://abrokenbackpack.com/?p=8241")])
TC("c-kto-nangyuan", "Koh Nang Yuan", KTO, 10.1170, 99.8140, ["Beaches", "Views", "Diving"], s=["Three islets joined by a sandbar, with a short climb to the famous viewpoint"], p=[250],
   best="First taxi boat of the morning", tips=["Taxi boats from Sairee cost about ฿100–150 each way", "Plastic bottles aren’t allowed"], src=[VTTT, S("Visit Thailand Today", "https://www.visitthailandtoday.com/guides/koh-tao-travel-guide")])
TC("c-kto-sharkbay", "Shark Bay", KTO, 10.0520, 99.8350, ["Diving", "Beaches"], s=["Snorkel with turtles and blacktip reef sharks"], cost="Free from the shore", best="Early morning", src=[VTTT, THGT])
TC("c-kto-johnsuwan", "John-Suwan Viewpoint", KTO, 10.0550, 99.8260, ["Views", "Hikes"], s=["Short, sweaty scramble to a view over the twin southern bays; Google 4.7 from 3,400 reviews"],
   cost="About ฿100, paid in two parts", best="Early morning or sunset, never midday", tips=["Wear proper shoes"], src=[VTTT, S("Go Backpacking", "https://gobackpacking.com/koh-tao-budget-cost/")])
TC("c-kto-freedom", "Freedom Beach", KTO, 10.0570, 99.8230, ["Beaches"], s=["Quiet beach below John-Suwan, calm even in high season"], p=[50], src=[VTTT, THGT])
TC("c-kto-tanote", "Tanote Bay", KTO, 10.0890, 99.8570, ["Beaches", "Diving"], s=["East-coast bay with a jump rock and great shore snorkelling"], cost="Free", src=[THGT, VTTT])
TC("c-kto-sairee", "Sairee Beach sunset and fire shows", KTO, 10.1000, 99.8270, ["Beaches", "Nightlife"], s=["Koh Tao’s main beach; sunset drinks, then fire shows at the bars"], cost="Free", best="Late afternoon onwards", src=[VTTT])
TC("c-kto-mango", "Mango Bay and Mango Viewpoint", KTO, 10.1220, 99.8380, ["Views", "Diving"], s=["Empty north-coast bay and viewpoint"], p=[100], tips=["About ฿100 by land"], src=[VTTT])
TC("c-kto-snorkeltrip", "Round-island snorkelling boat trip", KTO, 10.0870, 99.8270, ["Excursions", "Diving"], s=["Five bays in a day (Nang Yuan, Mango Bay, Hin Wong, Aow Leuk, Shark Bay), lunch and gear included"],
   cost="Tour price (not checked)", tips=["Check whether the Nang Yuan fee is included", "Book a day or two ahead in high season"], src=[S("Visit Thailand Today", "https://www.visitthailandtoday.com/guides/koh-tao-travel-guide"), VTTT])

# ---------------- CHIANG RAI ----------------
NEW_CITIES += [["Chiang Rai", 19.9105, 99.8406]]
CR = "Chiang Rai"
VTTCR = S("Visit Thailand Today", "https://www.visitthailandtoday.com/guides/chiang-rai-travel-guide")
DPCR = S("Departly", "https://departly.pages.dev/to/thailand/chiang-rai/")
TGCR = S("Travel Guides Tips", "https://travelguidestip.com/?p=14390")
TG("g-cr-saijai", "Saijai Cafe and Hostel", CR, 19.9085, 99.8320, s=["One of Chiang Rai’s most popular backpacker hostels: social, central but on a quiet street", "Walkable to the Night Bazaar and Walking Street"],
   src=[S("Global Gallivanting", "https://www.global-gallivanting.com/?p=35757")])
TC("c-cr-white", "White Temple (Wat Rong Khun)", CR, 19.8243, 99.7631, ["Temples"], s=["Dazzling all-white modern temple by artist Chalermchai Kositpipat, with pop-culture murals inside", "Entry now includes the Cave of Art"],
   p=[200], best="At the 8 am opening, before the tour vans", tips=["Fee doubled from ฿100 in January 2026", "Public bus from Bus Terminal 1 is about ฿20", "Cover shoulders and knees"],
   src=[VTTCR, S("Go2Thailand", "https://go2thailand-com.vercel.app/blog/chiang-rai-white-temple-entrance-fee-doubles-2026/"), TGCR])
TC("c-cr-blue", "Blue Temple (Wat Rong Suea Ten)", CR, 19.9230, 99.8410, ["Temples"], s=["Cobalt-blue temple in town, stunning in late-afternoon light"], cost="Free (donation)", best="Around 4 pm to sunset",
   src=[VTTCR, DPCR, S("Solo Guides", "https://sologuides.com/?p=6096")])
TC("c-cr-black", "Black House (Baan Dam Museum)", CR, 19.9920, 99.8600, ["Museums"], s=["Artist Thawan Duchanee’s dark, strange compound of buildings, bones and skins", "About 13 km north of town, the opposite way to the White Temple"],
   p=[80], tips=["Closes over lunch and reopens about 1 pm"], src=[DPCR, S("Sebastien Brousseau", "https://www.sebastienbrousseau.com/?p=29975"), TGCR])
TC("c-cr-huaypla", "Wat Huay Pla Kang", CR, 19.9480, 99.7960, ["Temples", "Views"], s=["Huge white Guanyin statue you can go up inside, with views over the valley"], cost="Not checked", src=[VTTCR])
TC("c-cr-clock", "Clock tower light show", CR, 19.9070, 99.8310, ["Nightlife"], s=["Golden clock tower by the White Temple’s artist, with a short light-and-music show"], cost="Free", best="7 pm, 8 pm and 9 pm", src=[VTTCR])
TC("c-cr-golden", "Golden Triangle and Chiang Saen", CR, 20.3540, 100.0830, ["Excursions", "Views"], s=["Where Thailand, Laos and Myanmar meet on the Mekong, with the old walled town of Chiang Saen"], cost="Transport or tour (not checked)", src=[VTTCR])
TM("m-cr-nightbazaar", "Chiang Rai Night Bazaar food court", CR, 19.9060, 99.8350, t=("Market",), s=["Big food court of shared tables by Bus Terminal 1, with live music most evenings"], best="Nightly from about 5 pm",
   src=[TGCR, VTTCR, S("Sebastien Brousseau", "https://www.sebastienbrousseau.com/?p=29975")])
TM("m-cr-walking", "Saturday Walking Street (Thanalai Road)", CR, 19.9100, 99.8300, t=("Market",), s=["Chiang Rai’s best evening market"], best="Saturdays, about 4 pm to 10 pm", src=[TGCR])

# ---------------- AYUTTHAYA ----------------
NEW_CITIES += [["Ayutthaya", 14.3532, 100.5689]]
AY = "Ayutthaya"
VTTAY = S("Visit Thailand Today", "https://www.visitthailandtoday.com/guides/bangkok-to-ayutthaya")
PTAY = S("Pattaya Talk", "https://pattayatalk.com/things-to-do/ayutthaya-a-photographers-paradise")
AYTIP = "A ฿220 combo ticket covers six temples (Mahathat, Ratchaburana, Phra Si Sanphet, Phra Ram, Chaiwatthanaram, Maheyong), cash only, valid 30 days"
TC("c-ay-mahathat", "Wat Mahathat", AY, 14.3570, 100.5675, ["Temples"], s=["The famous Buddha head held in the roots of a fig tree, among rows of ruined prangs"], p=[50],
   best="Early morning", tips=["Keep your head lower than the Buddha’s when taking photos", AYTIP], src=[PTAY, S("Thai Holiday Guide", "https://www.thaiholidayguide.com/things-to-do-in-ayutthaya/"), VTTAY])
TC("c-ay-sanphet", "Wat Phra Si Sanphet", AY, 14.3560, 100.5590, ["Temples"], s=["Three great chedis that held royal ashes; once the royal temple and the most photographed in Ayutthaya"], p=[50],
   best="Golden hour", tips=[AYTIP], src=[PTAY])
TC("c-ay-ratchaburana", "Wat Ratchaburana", AY, 14.3590, 100.5680, ["Temples", "Views"], s=["Tall prang you can climb, with old murals inside"], p=[50], tips=[AYTIP], src=[PTAY])
TC("c-ay-chaiwat", "Wat Chaiwatthanaram", AY, 14.3430, 100.5420, ["Temples", "Views"], s=["Riverside temple in Khmer style, like a mini Angkor Wat; the classic sunset photo"], p=[50],
   best="Late afternoon; the historical park closes at 6 pm", tips=[AYTIP], src=[PTAY, S("Thai Holiday Guide", "https://www.thaiholidayguide.com/things-to-do-in-ayutthaya/")])
TC("c-ay-cycle", "Cycling the historical park", AY, 14.3550, 100.5650, ["Excursions"], s=["Rent a bike to loop the ruins; the main temples are within easy cycling distance"], p=[50, 100],
   tips=["Price is per day", "From the station, take the ฿5 ferry across and rent a bike at the landing"], src=[S("Pattaya Talk", "https://pattayatalk.com/first-time/discover-ayutthaya-thailands-historic-gem"), VTTAY])
TC("c-ay-bangpain", "Bang Pa-In Palace", AY, 14.2320, 100.5790, ["Museums"], s=["Royal summer palace with European, Chinese and Thai pavilions"], p=[100],
   src=[S("Pattaya Talk", "https://pattayatalk.com/first-time/ayutthaya-adventure-in-ancient-ruins")])
TM("m-ay-boatnoodles", "Ayutthaya boat noodles", AY, 14.3540, 100.5660, p=[30, 60], s=["Small, rich bowls of kuay teow rua, Ayutthaya’s local speciality, from street vendors"],
   src=[S("Pattaya Talk", "https://pattayatalk.com/first-time/ayutthaya-the-ancient-city-awaits"), S("Pattaya Talk", "https://pattayatalk.com/things-to-do/ayutthaya-unveiled-secrets-of-the-past")])
TM("m-ay-rotisaimai", "Roti sai mai stalls", AY, 14.3560, 100.5700, p=[20, 30], t=("Street food",), pu="per pack", s=["Ayutthaya’s famous snack: candy floss wrapped in thin pancakes"],
   src=[S("Pattaya Talk", "https://pattayatalk.com/things-to-do/ayutthaya-unveiled-secrets-of-the-past")])
TM("m-ay-floating", "Ayutthaya Floating Market", AY, 14.3640, 100.5850, t=("Market",), s=["Touristy but fun market for boat noodles, coconut ice cream and snacks"], best="Daily 10 am to 8 pm",
   src=[S("Pattaya Talk", "https://pattayatalk.com/first-time/ayutthaya-adventure-in-ancient-ruins")])
TM("m-ay-nightmarket", "Ayutthaya Night Market", AY, 14.3440, 100.5440, t=("Market",), s=["New riverside night market near Wat Chaiwatthanaram (opened November 2025), where you can dress in traditional Thai costume"],
   tips=["Opening days can change; check locally"], src=[S("Bus Online Ticket", "https://www.busonlineticket.co.th/?p=35598"), S("Thai Holiday Guide", "https://www.thaiholidayguide.com/things-to-do-in-ayutthaya/")])
TM("m-ay-baankao", "Baan Kao Nhom", AY, 14.3550, 100.5690, t=("Cafe",), s=["Cosy café known for its boat noodles"], src=[S("Pattaya Talk", "https://pattayatalk.com/first-time/ayutthaya-adventure-in-ancient-ruins")])

# ---------------- KANCHANABURI ----------------
NEW_CITIES += [["Kanchanaburi", 14.0228, 99.5328]]
KB = "Kanchanaburi"
VTTKB = S("Visit Thailand Today", "https://www.visitthailandtoday.com/guides/kanchanaburi-travel-guide")
TRZ = S("Trazy", "https://blog.trazy.com/kanchanaburi-day-trip-things-to-do-in-kanchanaburi/")
TC("c-kb-erawan", "Erawan Falls", KB, 14.3680, 99.1440, ["Waterfalls", "Hikes"], s=["Seven tiers of turquoise pools you can swim in, about 70 km north of town"], p=[200],
   best="Arrive early, before the tour buses", tips=["Local bus from Kanchanaburi bus station is ฿60 each way, roughly hourly from 8 am"],
   src=[S("Thai National Parks", "https://static.thainationalparks.com/erawan-national-park/get-there"), S("Penang Travel Tips", "https://www.penang-traveltips.com/thailand/kanchanaburi.htm"), VTTKB])
TC("c-kb-bridge", "Bridge on the River Kwai", KB, 14.0410, 99.5030, ["Museums", "Views"], s=["The famous WWII bridge on the Death Railway, still in use; you can walk across"], cost="Free",
   best="Before 9 am or late afternoon", src=[VTTKB, S("Pickyourtrail", "https://pickyourtrail.com/tourism/thailand/things-to-do-in-kanchanaburi")])
TC("c-kb-train", "Death Railway train to Nam Tok", KB, 14.0405, 99.5040, ["Excursions", "Views"], s=["Ride the WWII railway over the Wampo viaduct (by Krasae Cave), about 2 hours to Nam Tok"], p=[100],
   tips=["The steam train rides no longer operate; this is the regular train"], src=[TRZ, VTTKB, S("Thai National Parks", "https://thainationalparks.com/erawan-national-park/get-there")])
TC("c-kb-hellfire", "Hellfire Pass", KB, 14.3550, 98.9550, ["Museums", "Hikes"], s=["Railway cutting hacked through rock by POWs, with a moving memorial museum and walking trail; Google 4.7 from 5,300 reviews"],
   cost="Not checked", best="Daily 9 am to 4 pm", src=[VTTKB, S("Pickyourtrail", "https://pickyourtrail.com/tourism/thailand/things-to-do-in-kanchanaburi")])
TC("c-kb-cemetery", "War Cemetery and Thailand–Burma Railway Centre", KB, 14.0300, 99.5260, ["Museums"], s=["The main POW cemetery, with the excellent railway museum beside it"], p=[160],
   tips=["The cemetery is free; ฿160 is for the Railway Centre"], src=[S("Expedia", "https://www.expedia.com.my/things-to-do/erawan-falls-and-river-kwai-kanchanaburi-nature-and-history-ride.a50786906.activity-details"), VTTKB])
TC("c-kb-jeath", "JEATH War Museum", KB, 14.0180, 99.5310, ["Museums"], s=["Small museum on the prisoners who built the Death Railway"], p=[40], best="8:30 am to 6 pm", src=[TRZ])
TC("c-kb-krasae", "Krasae Cave", KB, 14.1750, 99.3120, ["Views"], s=["Small cave shrine beside the railway at the dramatic ‘Dangerous Curve’ viaduct"], cost="Free", src=[TRZ])
TC("c-kb-saiyok", "Sai Yok National Park", KB, 14.4300, 98.8500, ["Waterfalls", "Excursions"], s=["Waterfalls and bamboo rafting on the Kwai Noi; often combined with Hellfire Pass"], cost="Park fee (not checked)",
   src=[S("Pickyourtrail", "https://pickyourtrail.com/tourism/thailand/things-to-do-in-kanchanaburi"), VTTKB])

# ---------------- KHAO SOK ----------------
NEW_CITIES += [["Khao Sok", 8.9130, 98.5290]]
KSO = "Khao Sok"
CTS = S("Couples Travel Stories", "https://couplestravelstories.ca/khao-sok-costs/")
TC("c-kso-park", "Khao Sok National Park trails", KSO, 8.9200, 98.5280, ["Hikes", "Waterfalls"], s=["Ancient rainforest with limestone cliffs; the main trail takes 3–4 hours, the harder Bangkok Trail up to 6"],
   p=[300], best="December to April (dry season)", tips=["Keep your ticket for same-day re-entry", "Wear covered shoes and repellent: leeches"],
   src=[CTS, S("Pattaya Talk", "https://pattayatalk.com/things-to-do/khao-sok-national-park-natures-masterpiece"), S("Siam Tickets", "https://siamtickets.com/?p=9593")])
TC("c-kso-cheowlan", "Cheow Lan Lake", KSO, 8.9690, 98.8160, ["Excursions", "Views"], s=["Emerald lake among jagged karsts, explored by longtail; an hour’s drive from Khao Sok village"], p=[1000, 2000],
   tips=["Plus a ฿40 pier ticket and the park fee if your tour doesn’t include it", "If you stay at the lake the day after visiting the HQ, you pay the park fee again"],
   src=[CTS, S("Pattaya Talk", "https://pattayatalk.com/things-to-do/unwind-in-khao-sok-a-tropical-paradise"), S("It’s Better in Thailand", "https://itsbetterinthailand.com/destinations/khao-sok/")])
TC("c-kso-floating", "Floating bungalow night on Cheow Lan", KSO, 8.9800, 98.8000, ["Excursions"], s=["Sleep in a raft house on the lake, with meals included; book ahead"], p=[2500], tips=["Price per night including meals"],
   src=[S("Pattaya Talk", "https://pattayatalk.com/things-to-do/khao-sok-a-journey-through-thailands-wild-side")])

# ---------------- HUA HIN ----------------
NEW_CITIES += [["Hua Hin", 12.5684, 99.9577]]
HH = "Hua Hin"
BYH = S("Byklo", "https://www.byklo.rent/en/blog/best-things-to-do-in-hua-hin/")
GAH = S("Go Asia", "https://goasia.cc/en/article/hua-hin-night-markets")
TG("g-hh-madpanda", "Mad Panda Hostel", HH, 12.5700, 99.9590, s=["Hua Hin’s backpacker hostel, beds from about €10–20"], src=[S("Hostelworld", "https://www.hostelworld.com/blog/?p=313779")])
TM("m-hh-chatchai", "Hua Hin Night Market (Chatchai)", HH, 12.5715, 99.9545, p=[40, 80], t=("Market",), s=["Classic street-food night market on Dechanuchit Road, two minutes from the railway station"],
   best="Daily about 5 pm to 11 pm; busiest 7 to 9 pm", src=[GAH, BYH])
TM("m-hh-cicada", "Cicada Market", HH, 12.5260, 99.9650, p=[60, 120], t=("Market",), s=["Arty weekend market with live bands, crafts and fusion food; Google 4.3 from 18,000 reviews"],
   best="Friday to Sunday, 4 pm to 11 pm", src=[S("Thai Holiday Guide", "https://www.thaiholidayguide.com/attraction/cicada-market/"), S("Visit Thailand Today", "https://www.visitthailandtoday.com/markets-shopping/hua-hin/cicada-market"), BYH])
TM("m-hh-tamarind", "Tamarind Market", HH, 12.5265, 99.9640, t=("Market",), s=["Food-focused market right next to Cicada"], best="Friday to Sunday evenings", src=[GAH, BYH])
TC("c-hh-beach", "Hua Hin Beach", HH, 12.5690, 99.9620, ["Beaches"], s=["Long town beach; Hua Hin is drier than most of the south thanks to its rain shadow"], cost="Free",
   src=[BYH, S("Go Asia", "https://goasia.cc/en/thailand/hua-hin")])
TC("c-hh-station", "Royal Hua Hin Railway Station", HH, 12.5675, 99.9515, ["Museums", "Views"], s=["One of Thailand’s oldest and prettiest stations, with its red-and-cream royal waiting pavilion"], cost="Free",
   src=[S("Hostelworld", "https://www.hostelworld.com/blog/?p=313779"), BYH])
TC("c-hh-takiab", "Khao Takiab", HH, 12.5160, 99.9800, ["Temples", "Views"], s=["Hilltop temple with a big standing Buddha, sea views and lots of monkeys"], cost="Free (not checked)", src=[BYH])
TC("c-hh-hinlekfai", "Khao Hin Lek Fai viewpoint", HH, 12.5800, 99.9350, ["Views"], s=["Hill park with viewpoints over the town, a short scooter ride from the centre"], cost="Free (not checked)", src=[BYH])
TC("c-hh-samroiyot", "Khao Sam Roi Yot National Park", HH, 12.2050, 99.9900, ["Excursions", "Hikes", "Beaches"], s=["About 65 km south: Phraya Nakhon Cave with its pavilion lit by sunbeams, beaches and viewpoints"],
   cost="Park fee (not checked)", src=[BYH])
TC("c-hh-palace", "Mrigadayavan Palace", HH, 12.6730, 99.9580, ["Museums"], s=["Elegant teak royal summer palace on stilts by the sea"], cost="Not checked",
   src=[S("Lambus", "https://lambus.com/discover/inspiration/66f432b523cafae2591a38ae")])

# ---------------- PATTAYA ----------------
NEW_CITIES += [["Pattaya", 12.9236, 100.8825]]
PY = "Pattaya"
PPTR = S("Pattaya Pointer", "https://pattayapointer.pages.dev/guides/pattaya-1-day-layover-guide")
GTPY = S("Gotripzi", "https://www.gotripzi.com/destinations/pattaya-th/cost")
PYTIP = "Baht buses on fixed routes cost about ฿10; use Grab for anything over ฿150"
TG("g-py-18coins", "18 Coins Cafe & Hostel", PY, 12.9300, 100.8800, s=["Boutique hostel and café; Pattaya’s hostels are pricier than most of Thailand"], tips=[PYTIP], src=[GTPY])
TC("c-py-sanctuary", "Sanctuary of Truth", PY, 12.9727, 100.8890, ["Temples", "Museums"], s=["Gigantic hand-carved wooden temple by the sea, under construction since 1981"], p=[500],
   best="8 am opening, before the heat; allow 90 minutes", src=[PPTR, S("Visit Thailand Today", "https://www.visitthailandtoday.com/destinations/pattaya")])
TC("c-py-kohlarn", "Koh Larn (Coral Island)", PY, 12.9200, 100.7800, ["Beaches", "Excursions"], s=["Island 7 km offshore with clear water and white sand that Pattaya Beach lacks"], p=[30, 40],
   tips=["Public ferry from Bali Hai Pier is ฿30–40 each way and takes 30–45 minutes; a speedboat is about ฿300", "Last ferry back is around 5:30–6 pm"],
   src=[PPTR, GTPY, S("Sebastien Brousseau", "https://www.sebastienbrousseau.com/pattaya-travel-guide/")])
TC("c-py-walking", "Walking Street", PY, 12.9270, 100.8720, ["Nightlife"], s=["Pattaya’s famous neon nightlife strip by Bali Hai Pier"], cost="Free", best="7 pm to 10 pm for food and atmosphere",
   tips=["Avoid the fixed-price taxi touts around Walking Street"], src=[PPTR, S("Pickyourtrail", "https://pickyourtrail.com/tourism/thailand/places-to-visit-in-pattaya")])
TC("c-py-bigbuddha", "Big Buddha Hill (Pattaya viewpoint)", PY, 12.9150, 100.8690, ["Temples", "Views"], s=["Golden Buddha on the hill between Pattaya and Jomtien, with views over the bay"], cost="Free",
   src=[S("Go To Thailand", "https://gotothailand.com/things-to-do-pattaya/")])
TC("c-py-jomtien", "Jomtien Beach", PY, 12.8800, 100.8740, ["Beaches"], s=["Longer, calmer beach south of central Pattaya"], cost="Free", src=[S("12Go", "https://12go.asia/en/travel/pattaya")])
TM("m-py-thepprasit", "Thepprasit Night Market", PY, 12.9030, 100.8840, t=("Market",), s=["Huge weekend night market, excellent for street food"], best="Thursday to Sunday, 5 pm to 11 pm",
   src=[S("Sebastien Brousseau", "https://www.sebastienbrousseau.com/pattaya-travel-guide/"), S("Go To Thailand", "https://gotothailand.com/things-to-do-pattaya/")])
TM("m-py-jomtienmarket", "Jomtien Night Market", PY, 12.8890, 100.8730, p=[51, 204], t=("Market",), s=["Cheap seafood and fruit shakes at sunset by Jomtien Beach"], src=[GTPY])
TM("m-py-kiss", "Kiss Food & Drink", PY, 12.9300, 100.8800, p=[82, 255], t=("Restaurant",), s=["Local chain open 24/7, the classic late-night feed after Walking Street"], src=[GTPY])

# ---------------- KOH CHANG ----------------
NEW_CITIES += [["Koh Chang", 12.0700, 102.2850]]
KC = "Koh Chang"
G2KC = S("Go2Thailand", "https://go2thailand-com.vercel.app/islands/koh-chang/")
BKC = S("Booking.com (via easyJet)", "https://hotels.easyjet.com/hostels/city/th/ko-chang-th.en-gb.html?aid=356980")
TG("g-kc-montview", "MontView Koh Chang", KC, 12.0000, 102.2720, r=9.1, rs="Booking.com (65 reviews)", s=["Small, very clean and good value"], src=[S("Booking.com (via Priceline)", "https://h.priceline.com/hostels/city/th/ko-chang-th.en-gb.html")])
TG("g-kc-junglefever", "Jungle Fever Koh Chang", KC, 11.9990, 102.2760, r=7.9, rs="Booking.com (135 reviews)", s=["About 10 minutes’ walk from Lonely Beach; the owners know the island’s best spots"],
   src=[BKC, S("Booking.com (via Priceline)", "https://h.priceline.com/hostels/city/th/ko-chang-th.en-gb.html")])
TG("g-kc-99", "99Hostel & Bar Koh Chang", KC, 11.9985, 102.2715, r=7.8, rs="Booking.com (49 reviews)", s=["Hostel with a bar near Lonely Beach"], src=[BKC])
TG("g-kc-slumber", "Slumber Party Resort Koh Chang", KC, 11.9975, 102.2705, r=7.8, rs="Booking.com (57 reviews)", s=["Party hostel right on the beach"], src=[BKC])
TG("g-kc-habitat", "The Habitat Hostel Koh Chang", KC, 12.0010, 102.2730, s=["Budget hostel in the Lonely Beach area, where most backpackers stay"],
   src=[S("Expedia", "https://www.expedia.co.th/en/Ko-Chang-Hotels-The-Habitat-Hostel-Koh-Chang.h15255844.Hotel-Information"), S("Hostelz", "https://www.hostelz.com/hostels/Thailand/Ko-Chang")])
TC("c-kc-klongplu", "Klong Plu Waterfall", KC, 12.0510, 102.3270, ["Waterfalls"], s=["Koh Chang’s most popular waterfall, with a natural swimming pool a short walk from the car park"], p=[200], src=[G2KC])
TC("c-kc-lonely", "Lonely Beach", KC, 11.9980, 102.2700, ["Beaches", "Nightlife"], s=["The backpacker beach: cheap bungalows and beach bars"], cost="Free", src=[S("Thaiest", "https://thaiest.com/thailand/koh-chang"), S("Hostelz", "https://www.hostelz.com/hostels/Thailand/Ko-Chang")])
TC("c-kc-whitesand", "White Sand Beach", KC, 12.1340, 102.2780, ["Beaches"], s=["The island’s biggest, liveliest beach, still relaxed"], cost="Free", src=[G2KC, S("Con Mochila", "https://www.conmochila.com/en/wp-json/wp/v2/pages/8255")])
TC("c-kc-bangbao", "Bang Bao pier and lighthouse", KC, 11.9690, 102.3070, ["Views"], s=["Stilted fishing village pier full of seafood restaurants and shops"], cost="Free", src=[S("Ticket2Attraction", "https://www.ticket2attraction.com/blogs/koh-chang-koh-kood-attractions/")])
TC("c-kc-salakphet", "Salak Phet mangrove boardwalk", KC, 11.9830, 102.3800, ["Hikes", "Views"], s=["Boardwalk through the mangroves on the quiet south-east coast"], cost="Not checked", src=[S("Ticket2Attraction", "https://www.ticket2attraction.com/blogs/koh-chang-koh-kood-attractions/")])
TC("c-kc-snorkel", "Island snorkelling day trip (Koh Rang)", KC, 11.8000, 102.3900, ["Diving", "Excursions"], s=["Big-boat or speedboat trips to the marine-park islands around Koh Rang"], cost="Tour price (not checked)",
   src=[G2KC, S("Ticket2Attraction", "https://www.ticket2attraction.com/blogs/koh-chang-koh-kood-attractions/")])

# ---------------- KOH LIPE ----------------
NEW_CITIES += [["Koh Lipe", 6.4880, 99.3070]]
LP = "Koh Lipe"
THGL = S("Thai Holiday Guide", "https://www.thaiholidayguide.com/visit/koh-lipe/")
BAL = S("Bangkok Airways blog", "https://blog.bangkokair.com/en/phuket-to-koh-lipe-travel-essentials/")
LPTIP = "Prices roughly double from December to March and rooms sell out; book ahead. ATMs can run out of cash"
TC("c-lp-walking", "Lipe Walking Street", LP, 6.4880, 99.3040, ["Nightlife", "Markets"], s=["1 km car-free street linking Pattaya Beach and Sunrise Beach, packed with restaurants and bars"],
   cost="Free", best="6 pm to midnight", tips=[LPTIP, "It floods in heavy rain; bring waterproof sandals"], src=[BAL, THGL])
TC("c-lp-adang", "Koh Adang and Pha Chado viewpoint", LP, 6.5000, 99.2950, ["Hikes", "Views"], s=["Forest trail to an old pirate lookout with the classic view back over Koh Lipe; about 15 minutes by boat"],
   cost="Boat (not checked)", best="Early, before the heat", src=[BAL, THGL, S("Where Are Those Morgans", "https://wherearethosemorgans.com/?p=9966")])
TC("c-lp-sunrise", "Sunrise Beach", LP, 6.4930, 99.3110, ["Beaches"], s=["Long, calmer beach facing Koh Adang, five minutes from Walking Street"], cost="Free", src=[S("Where Are Those Morgans", "https://wherearethosemorgans.com/?p=9966")])
TC("c-lp-sunset", "Sunset Beach (Hat Pramong)", LP, 6.4830, 99.2990, ["Beaches", "Views"], s=["Quiet west-facing beach for sunset"], cost="Free", tips=["Island taxi about ฿50 per person"], src=[BAL])
TC("c-lp-hinngam", "Koh Hin Ngam", LP, 6.4500, 99.2600, ["Beaches", "Diving"], s=["Surreal beach of smooth black pebbles with good snorkelling just offshore"], cost="On boat tours (not checked)", src=[THGL])
TC("c-lp-snorkel", "Adang-Rawi snorkelling trip", LP, 6.4900, 99.2700, ["Diving", "Excursions"], s=["Longtail or speedboat snorkel stops around the marine park islands"], cost="Tour price (not checked)",
   tips=["Watch for jellyfish, the main hazard here"], src=[THGL, S("Takeoff", "https://takeoff.to/destinations/koh-lipe")])

# ---------------- SUKHOTHAI ----------------
NEW_CITIES += [["Sukhothai", 17.0070, 99.8230]]
SK = "Sukhothai"
GASK = S("Go Asia", "https://goasia.cc/en/article/sukhothai-historical-park")
SKTIP = "Each zone is ฿100, plus ฿10 to bring a bicycle in; there’s no combined ticket any more"
TG("g-sk-oldcity", "Old City Guesthouse", SK, 17.0180, 99.7080, t=("Guesthouse",), s=["Affordable rooms near the historical park, handy for sunrise and bike rental"],
   src=[S("Bus Online Ticket", "https://www.busonlineticket.co.th/?p=7937"), S("Bus Online Ticket", "https://www.busonlineticket.co.th/?p=35729")])
TG("g-sk-thaithai", "Thai Thai Sukhothai Guesthouse", SK, 17.0150, 99.7180, t=("Guesthouse",), s=["About 1 km from the park entrance, outside the old walls"], src=[S("Bus Online Ticket", "https://www.busonlineticket.co.th/?p=7937")])
TC("c-sk-central", "Sukhothai Historical Park, Central Zone", SK, 17.0170, 99.7040, ["Temples", "Museums"], s=["Thailand’s first capital: lotus-bud chedis and Buddhas reflected in ponds; a UNESCO site"], p=[100],
   best="Sunrise or late afternoon", tips=[SKTIP, "Bikes cost ฿30–50 a day at the entrance"], src=[GASK, S("Bangkok Airways blog", "https://blog.bangkokair.com/?p=968"), S("Wikivoyage", "https://kwx.liehendr.com/content/wikivoyage_en_all_maxi_2025-02/A/Sukhothai")])
TC("c-sk-sichum", "Wat Si Chum (North Zone)", SK, 17.0300, 99.6980, ["Temples"], s=["A giant seated Buddha peering through a narrow opening in a tall mondop"], p=[100], tips=[SKTIP], src=[GASK, S("Machu Picchu travel", "https://www.machupicchu.org/sukhothai-day-trip-from-chiang-mai-or-bangkok-2026-travel-planning-guide.htm")])
TC("c-sk-west", "West Zone ruins", SK, 17.0170, 99.6800, ["Temples", "Hikes"], s=["Quieter, forested hilltop ruins best reached by bike"], p=[100], tips=[SKTIP], src=[S("Sebastien Brousseau", "https://www.sebastienbrousseau.com/sukhothai-historical-park-guide/")])

# ================= NEW PLANNER HUBS AND CONNECTIONS =================
STATIONS.update({
 "ekkamai": ["Ekkamai (Eastern) Bus Terminal", 13.7197, 100.5846], "saitaimai": ["Southern Bus Terminal (Sai Tai Mai)", 13.7840, 100.3830],
 "huahinstn": ["Hua Hin Railway Station", 12.5675, 99.9515], "aonangbeach": ["Ao Nang beach longtail counter", 8.0320, 98.8200],
 "pakbarapier": ["Pak Bara pier", 6.8670, 99.7530], "lipebeach": ["Pattaya Beach, Koh Lipe", 6.4860, 99.3020], "thammachat": ["Ao Thammachat ferry pier", 12.1960, 102.2920],
 "northpattaya": ["North Pattaya Bus Terminal", 12.9500, 100.8970], "ayustn": ["Ayutthaya Railway Station", 14.3560, 100.5830], "kanstn": ["Kanchanaburi Railway Station", 14.0250, 99.5280],
 "thsbus": ["Sukhothai Bus Terminal", 17.0170, 99.8150], "thsair": ["Sukhothai Airport", 17.2380, 99.8180], "khaosokvillage": ["Khao Sok village", 8.9130, 98.5290]})
HUBS += [["ayu", "Ayutthaya", 14.3532, 100.5689, "Central", False], ["kan", "Kanchanaburi", 14.0228, 99.5328, "Central", False],
         ["huahin", "Hua Hin", 12.5684, 99.9577, "Gulf coast", False], ["pattaya", "Pattaya", 12.9236, 100.8825, "East coast", False],
         ["kohchang", "Koh Chang", 12.0700, 102.2850, "East coast", True], ["sukhothai", "Sukhothai", 17.0070, 99.8230, "North", False],
         ["khaosok", "Khao Sok", 8.9130, 98.5290, "Andaman coast", False], ["railay", "Railay", 8.0110, 98.8380, "Andaman coast", True],
         ["pakbara", "Pak Bara pier", 6.8670, 99.7530, "Andaman coast", False], ["lipe", "Koh Lipe", 6.4880, 99.3070, "Andaman islands", True]]
GO12.update({"ayu": "ayutthaya", "kan": "kanchanaburi", "huahin": "hua-hin", "pattaya": "pattaya", "kohchang": "koh-chang", "sukhothai": "sukhothai",
             "khaosok": "khao-sok", "pakbara": "pak-bara", "lipe": "koh-lipe"})
BOT = S("Bus Online Ticket", "https://www.busonlineticket.co.th/?p=35598")
BYKF = S("Byklo", "https://www.byklo.rent/en/blog/first-time-visiting-hua-hin-guide/")
EXTL = S("Explorer Tom", "https://explorertom.com/en/?p=63651")
E("bkk", "ayu", "Train", [0.75, 1.35], [70, 125], op="Rapid or express train", da="aphiwat", db="ayustn", notes=["Ordinary 3rd-class trains are cheaper and slower", "From the station, take the ฿5 ferry across to the old city"], src=[VTTAY, BOT])
E("bkk", "kan", "Train", [2.5, 3.5], [100], op="State Railway of Thailand", da=None, db="kanstn", notes=["The line crosses the River Kwai bridge", "Journey time not checked"], src=[VTTKB])
E("bkk", "kan", "Minivan", [2, 2.5], None, op="Minivan from the southern bus terminal", da="saitaimai", db=None, notes=["Price not checked"], src=[S("Thai National Parks", "https://thainationalparks.com/erawan-national-park/get-there")])
E("bkk", "huahin", "Train", [4, 4.5], [45, 150], op="State Railway of Thailand", da="aphiwat", db="huahinstn", notes=["Arrives at the historic royal station, 1 km from the beach"], src=[BYKF])
E("bkk", "huahin", "Minivan", [3, 3.5], [180, 300], op="Minivan", da="saitaimai", db=None, notes=["Also from Ekkamai and Victory Monument", "Not great with big luggage"], src=[BYKF, S("Takeoff", "https://takeoff.to/destinations/hua-hin")])
E("bkk", "pattaya", "Bus", [2, 2.5], [120, 250], op="Roong Reuang and others, about every 30–60 minutes", da="ekkamai", db="northpattaya", notes=["Last bus back to Bangkok about 9 pm"], src=[PPTR, S("Sebastien Brousseau", "https://www.sebastienbrousseau.com/pattaya-travel-guide/")])
E("bkkair", "pattaya", "Bus", [1.5, 2], [146], op="Airport bus", da="bkkair", db=None, src=[GTPY])
E("bkk", "kohchang", "Bus + ferry", [7, 7.5], [900], op="Khao San bus-and-ferry package (lunch and hotel transfer included)", da=None, db=None, notes=["Leaves about 5 am, arrives around noon"],
  src=[S("Ticket2Attraction", "https://www.ticket2attraction.com/blogs/koh-chang-koh-kood-attractions/")])
E("bkk", "kohchang", "Minivan", [4.5, 5.5], [400, 800], op="Minivan direct to the ferry pier", da=None, db="thammachat", notes=["Some fares include the ferry", "Only the Ao Thammachat ferry runs now (Centrepoint shut in 2024)", "Ferry fares rose in April 2026 with fuel costs"],
  src=[G2KC, S("It’s Better in Thailand", "https://itsbetterinthailand.com/destinations/koh-chang"), S("The Nation", "https://www.nationthailand.com/news/general/40064779")])
E("bkk", "kohchang", "Flight", [2.3, 2.9], [3000, 4550], op="Bangkok Airways to Trat, then shuttle and ferry", da="bkkair", db=None, notes=["Price includes the ฿500–550 airport shuttle and ferry"],
  src=[S("Thailand Boat Tickets", "https://thailandboattickets.com/en/destinations/koh-chang")])
E("bkk", "sukhothai", "Bus", [6, 7], [300, 550], op="Intercity and VIP buses", da="mochit", db="thsbus", notes=["Songthaews to the old city are about ฿30"], src=[GASK, S("Machu Picchu travel", "https://www.machupicchu.org/sukhothai-day-trip-from-chiang-mai-or-bangkok-2026-travel-planning-guide.htm")])
E("cnx", "sukhothai", "Bus", [5, 6], [300, 570], op="Intercity bus", da="arcade", db="thsbus", src=[S("Machu Picchu travel", "https://www.machupicchu.org/sukhothai-day-trip-from-chiang-mai-or-bangkok-2026-travel-planning-guide.htm"), S("Olsen Tours", "https://olsentours.com/sukhothai")])
E("bkk", "sukhothai", "Flight", [0.9, 1], [2000, 4000], op="Bangkok Airways", da="bkkair", db="thsair", src=[S("Sebastien Brousseau", "https://www.sebastienbrousseau.com/sukhothai-historical-park-guide/")])
E("urt", "khaosok", "Bus", [2, 2.5], [120, 350], op="Bus or van, 20+ departures a day", da=None, db="khaosokvillage", notes=["Local bus about ฿120; booked vans ฿300–350"],
  src=[S("Siam Tickets", "https://siamtickets.com/?p=9593"), S("Go Asia", "https://goasia.cc/how-to-get-from-surat-thani-to-khao-sok")])
E("krabi", "khaosok", "Minivan", [2.5, 4], [250, 400], op="Bus or shared minivan", da="kbibus", db="khaosokvillage", src=[S("Pattaya Talk", "https://pattayatalk.com/things-to-do/adventure-awaits-in-khao-soks-lush-rainforest")])
E("phuket", "khaosok", "Bus", [3, 4], [200, 400], op="Bus", da="hktbus", db="khaosokvillage", src=[S("Pattaya Talk", "https://pattayatalk.com/things-to-do/khao-sok-the-heart-of-thailands-wilderness")])
E("aonang", "railay", "Ferry", [0.17, 0.25], [100, 150], op="Longtail boat", da="aonangbeach", db=None, notes=["About ฿50 extra after 6 pm"], src=[VTTAN, GTK])
E("krabi", "railay", "Ferry", [0.5, 0.5], None, op="Longtail boat", da=None, db=None, notes=["About 30 minutes from Krabi Town; price not checked"],
  src=[S("Budget Your Trip", "https://www.budgetyourtrip.com/thailand-article/the-best-party-hostels-in-ao-nang-railay-beach-and-krabi/264")])
E("lanta", "lipe", "Ferry", [3, 3.25], [1700, 1750], op="Speedboat (high season only)", da="saladan", db="lipebeach", notes=["Departs about 10:30 and 13:30", "Plus a ฿200 national park fee"],
  src=[S("Koh Lipe Island", "https://www.kohlipeisland.org/koh-lanta-to-koh-lipe/"), EXTL])
E("phiphi", "lipe", "Ferry", [4, 4], [2450], op="Speedboat (high season)", da="tonsai", db="lipebeach", src=[EXTL])
E("phuket", "lipe", "Ferry", [5, 5], [2600], op="Speedboat (high season)", da="rassada", db="lipebeach", src=[EXTL])
E("pakbara", "lipe", "Ferry", [1.25, 2], [500, 700], op="Speedboat", da="pakbarapier", db="lipebeach", notes=["Plus a ฿200 national park fee", "Can be bumpy: waterproof your bag"],
  src=[S("Travelfish", "https://www.travelfish.org/koh-lipe-ferry-tickets-online.php"), S("12Go", "https://12go.asia/en/travel/pak-bara/koh-lipe?z=4089997")])
E("krabi", "pakbara", "Minivan", [3.5, 5], None, op="Minivan", da=None, db="pakbarapier", notes=["Vans run from Krabi Town and Trang to Pak Bara; time is an estimate"], verified=False,
  src=[S("Visit Thailand Today", "https://www.visitthailandtoday.com/guides/how-to-get-to-koh-lipe")])
