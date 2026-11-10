import json

CHK = "Nov 2026"

rates = {
  "GBP": {"v": 1, "note": "home currency"},
  "THB": {"v": 45.0, "note": "checked early Nov 2026 (sources ranged 44–45)"},
  "USD": {"v": 1.34, "note": "checked 4 Nov 2026"},
  "VND": {"v": 34500, "note": "checked Oct 2026"},
  "KHR": {"v": 5370, "note": "estimated from the dollar rate"},
  "LAK": {"v": 29000, "note": "estimated from the dollar rate"},
  "MYR": {"v": 5.65, "note": "estimated from the dollar rate"},
  "SGD": {"v": 1.73, "note": "estimated from the dollar rate"},
  "IDR": {"v": 22000, "note": "estimated from the dollar rate"},
}

rate_sources = [
  ["Wise", "https://wise.com/us/currency-converter/gbp-to-thb-rate"],
  ["Pluang", "https://pluang.com/en/tools/currency-converter/gbp-thb"],
  ["CurrencyConvert", "https://currencyconvert.online/gbp/vnd/125000000000"],
  ["MoneyExchangeRate", "https://moneyexchangerate.org/currencyexchange/gbp/usd/201"],
]

countries = {
  "TH": {"name": "Thailand", "flag": "🇹🇭", "cur": "THB", "alt": [], "lang": "th", "langName": "Thai", "c": [13.2, 100.6], "z": 5.5},
  "KH": {"name": "Cambodia", "flag": "🇰🇭", "cur": "USD", "alt": ["KHR"], "lang": "km", "langName": "Khmer", "c": [12.4, 104.9], "z": 6.5},
  "VN": {"name": "Vietnam", "flag": "🇻🇳", "cur": "VND", "alt": [], "lang": "vi", "langName": "Vietnamese", "c": [15.8, 106.6], "z": 5.5},
  "LA": {"name": "Laos", "flag": "🇱🇦", "cur": "LAK", "alt": [], "lang": "lo", "langName": "Lao", "c": [19.3, 102.6], "z": 6.5},
  "MY": {"name": "Malaysia", "flag": "🇲🇾", "cur": "MYR", "alt": [], "lang": "ms", "langName": "Malay", "c": [3.9, 101.8], "z": 6.5},
  "SG": {"name": "Singapore", "flag": "🇸🇬", "cur": "SGD", "alt": [], "lang": "en", "langName": "English (widely spoken)", "c": [1.33, 103.83], "z": 11},
  "ID": {"name": "Indonesia", "flag": "🇮🇩", "cur": "IDR", "alt": [], "lang": "id", "langName": "Indonesian", "c": [-8.45, 115.2], "z": 9},
}

rides = {
  "TH": "Grab and Bolt both work in the cities and on the big islands, and Bolt is often a little cheaper. With tuk-tuks, agree the price before you get in. In Bangkok taxis, ask for the meter and get out if they refuse. Motorbike taxis in orange vests are quick for short hops. On the islands, shared pickups (songthaews) run set routes, so confirm the fare first.",
  "KH": "Grab and PassApp work in Phnom Penh and Siem Reap and show the price upfront. Tuk-tuks are cheap for short rides, so agree the price first, in dollars or riel. For Angkor, lots of people hire one tuk-tuk driver for the whole day.",
  "VN": "Grab and Xanh SM (the green electric taxis and bikes) show prices upfront. If you hail a street taxi, stick to Mai Linh or Vinasun and make sure the meter is running. Motorbike taxis (xe ôm) are fine, just agree the price first.",
  "LA": "Ride apps are limited. LOCA works in Vientiane, but elsewhere it’s tuk-tuks and shared songthaews. Agree the price before you set off and expect to share.",
  "MY": "Grab is the default in Kuala Lumpur and Penang and is usually cheaper than street taxis. KL’s trains (LRT, MRT and monorail) are cheap and easy.",
  "SG": "Public transport is excellent, and you can tap in with a contactless card. Grab, Gojek and TADA all work, and metered taxis are honest.",
  "ID": "Gojek and Grab are cheap in Bali, but some spots don’t allow app pickups, so walk a bit further away if a driver cancels. Scooter hire is common; only ride if you’re confident and insured.",
}

def S(label, url): return [label, url]

HZ_BKK = S("Hostelz (Hostelworld data)", "https://www.hostelz.com/best-hostels-in-bangkok-for-solo-female-travelers")
places = []
def add(**k):
    k.setdefault("ap", False); k.setdefault("t", []); k.setdefault("p", None); k.setdefault("cur", None)
    k.setdefault("pu", ""); k.setdefault("r", None); k.setdefault("rs", None); k.setdefault("rc", None)
    k.setdefault("s", []); k.setdefault("d", None); k.setdefault("tips", []); k.setdefault("best", None)
    k.setdefault("busy", None); k.setdefault("src", []); k.setdefault("chk", CHK); k.setdefault("verified", bool(k.get("src")))
    places.append(k)

DORM = "dorm bed, per night, from"

# ---------------- GAFFS (researched Nov 2026) ----------------
def gaff(**k):
    k.setdefault("t", ["Hostel"]); k.setdefault("pu", DORM); k.setdefault("ap", True)
    add(c="gaff", **k)
NC = None
HW = "https://www.hostelworld.com"
gaff(id="g-line-bkk", n="Line Bangkok Hostel", cc="TH", city="Bangkok", lat=13.7605, lng=100.4995,
     p=[10.02], cur="USD", r=9.6, rs="Hostelworld (via Hostelz)",
     s=["About an 8-minute walk from Khao San Road, on a quiet street", "Reviewers rave about how comfy and private the dorm beds are"],
     d={"breakfast": "Not listed by the hostel", "privacy": "Dorms (including a 4-bed female dorm) and private rooms",
        "beds": "4-bed dorms with large single beds rather than bunks, per reviews", "toilet": "Shared dorm bathrooms with hot, powerful showers; private rooms have their own",
        "room": "Air-con, two-level lockers, linen and towels provided, adults only"},
     src=[HZ_BKK, S("Booking.com", "https://www.booking.com/hotel/th/line-bangkok-hostel.html?aid=391214"), S("Hostelworld", HW + "/de/jugendherbergen/p/325887/line-bangkok-hostel/"), S("Dinogo", "https://dinogo.com/hotels/5619-line-bangkok-boutique-hostel")])
gaff(id="g-nbhd-bkk", n="Bangkok Neighborhood Hostel", cc="TH", city="Bangkok", lat=13.7465, lng=100.4985,
     p=[10.79], cur="USD", r=9.6, rs="Hostelworld (via Hostelz)",
     s=["Old Town, about 3 minutes from Sam Yot MRT and 1 km from Wat Pho", "Quiet, away from the party streets"],
     d={"breakfast": "Not listed by the hostel", "privacy": "Dorms (including female-only) and private rooms",
        "beds": "Bunks with privacy curtains", "toilet": "Shared bathrooms with showers and bidets",
        "room": "Air-con, shared kitchen, work desks, adults only (18+)"},
     src=[S("Hostelz", "https://www.hostelz.com/best-hostels-bangkok"), S("Hostelworld", HW + "/hostels/p/328758/bangkok-neighborhood-hostel/"), S("Booking.com (via easyJet)", "https://hotels.easyjet.com/hotel/th/bangkok-neighborhood-hostel.en-gb.html?aid=356980")])
gaff(id="g-common-cnx", n="The Common Hostel", cc="TH", city="Chiang Mai", lat=18.7930, lng=98.9822,
     r=8.9, rs="Backpackers Wanderlust",
     s=["Old Town on Singharat Road, 7 minutes’ walk from Wat Phra Singh", "Free coffee and drinking water"],
     d={"breakfast": "Included, an Asian buffet that reviewers rate (one older guide says otherwise)", "privacy": "Mixed and female dorms, plus private doubles",
        "beds": "Big bunks (single or queen-size), with a curtain on every bunk", "toilet": "Shared bathrooms for dorms (one reviewer called them basic); private doubles have their own",
        "room": "Air-con, terrace, games room, 18+"},
     src=[S("Backpackers Wanderlust", "https://www.backpackerswanderlust.com/best-hostels-in-chiang-mai/"), S("Hostelworld", HW + "/hostels/p/273677/the-common-hostel/"), S("Booking.com (via TAP)", "https://hotels.flytap.com/hotel/th/slow-poke-poshtel-by-bed.en-gb.html?aid=304142"), S("Travelocity", "https://www.travelocity.ca/Chiang-Mai-Hotels-The-Common-Hostel.h16580636.Hotel-Reviews")])
gaff(id="g-family2-cnx", n="Family Home 2 (Absolute House by Joe)", cc="TH", city="Chiang Mai", lat=18.780386, lng=98.98813, ap=False,
     p=[7.51], cur="USD", r=9.7, rs="Hostelworld (via Hostelz)", rc=1579,
     s=["2 minutes’ walk from Chiang Mai Gate", "Very social, run by a welcoming family"],
     d={"breakfast": "Available, may cost extra", "privacy": "Dorms only, no private rooms",
        "beds": "Bunk dorms; every bed has its own locker, light and plug", "toilet": NC,
        "room": "Air-con and fans, balconies, pool table, PS5 and Wii, adults only"},
     src=[S("Hostelz", "https://www.hostelz.com/party-hostels-in-chiang-mai"), S("Hostelworld", HW + "/hosteldetails.php/Family-Home-2-Absolute-House-by-Joe/Chiang-Mai/285223"), S("Expedia", "https://expedia.com.sg/Chiang-Mai-Hotels-Family-Home-2-Chiangmai-Adults-Only.h23002231.Hotel-Information"), S("Sembo (location)", "https://www.sembo.com/d/hotel-780032_family_home_2_chiangmai_adults_only_hostel_chiang_mai")])
gaff(id="g-makad-cnx", n="Makad Rooftop Hostel", cc="TH", city="Chiang Mai", lat=18.7905, lng=99.0005,
     p=[4.89], cur="USD", r=9.2, rs="Hostelworld", rc=91,
     s=["Hidden inside Chinatown next to Warorot Market, near the river", "Rooftop with great views, good for meeting people"],
     d={"breakfast": "Not listed by the hostel", "privacy": "Dorms and private rooms (doubles and family rooms)",
        "beds": "Bunks; top-floor dorms mean lots of stairs", "toilet": "Shared bathroom described as OK by reviewers; private rooms have their own",
        "room": "Air-con, rooftop bar"},
     src=[S("Hostelworld", HW + "/hostels/p/330495/makad-rooftop-hostel/"), S("Hostelworld listings", HW + "/bed-and-breakfasts/asia/thailand/chiang-mai/p/3/"), S("Hostelz", "https://www.hostelz.com/party-hostels-in-chiang-mai")])
gaff(id="g-baanmaisak-pai", n="Baan Mai Sak Hostel", cc="TH", city="Pai", lat=19.3605, lng=98.4400,
     p=[6], cur="USD", pu="6-bed dorm, per night, from", r=9.1, rs="Booking.com (via ViaMichelin)", rc=335,
     s=["Picked as the best hostel in Pai for a quiet night", "300 m from the bus station, 400 m from Walking Street"],
     d={"breakfast": "Not listed (there’s a shared kitchen)", "privacy": "Mixed and female dorms",
        "beds": "6-bed dorms", "toilet": "Shared hot-water bathrooms outside the rooms, in an outdoor block",
        "room": "Air-con, small lockers, linen and towels, hammocks; quiet, not a party hostel"},
     src=[S("Go Backpacking", "https://gobackpacking.com/travel-guides/thailand/best-hostels-pai/"), S("Hostelz", "https://www.hostelz.com/best-hostels-pai"), S("Booking.com (via easyJet)", "https://hotels.easyjet.com/hotel/th/baan-mai-sak.en-gb.html"), S("ViaMichelin", "https://www.viamichelin.pl/maps/hotels/poi/pai-58130-snisb4ov")])
gaff(id="g-moongarden-pai", n="Moon Garden Hostel", cc="TH", city="Pai", lat=19.3585, lng=98.4415,
     r=9.0, rs="Booking.com", rc=119,
     s=["Family-run wooden house 200 m from the night market and bus station"],
     d={"breakfast": "Free coffee and bananas, not a full breakfast", "privacy": "Dorms (including a 6-bed dorm)",
        "beds": "Beds with curtains (one reviewer said they’re thin)", "toilet": "Shared bathrooms, mostly outside, which reviewers call very clean; the 6-bed dorm has one upstairs",
        "room": "Air-con, fridge and kettle, linen and towels, garden"},
     src=[S("Booking.com", "https://www.booking.com/hostels/city/th/pai.html?aid=814024"), S("Booking.com (via TAP)", "https://hotels.flytap.com/hotel/th/moon-garden-hostel.en-gb.html?aid=304142"), S("ViaMichelin", "https://www.viamichelin.pl/maps/hotels/poi/pai-58130-f5c95803")])
gaff(id="g-tianming-samui", n="Tian Ming Hostel", cc="TH", city="Koh Samui", lat=9.5390, lng=100.0590,
     p=[10.35], cur="USD", r=9.5, rs="Hostelworld (via Hostelz)",
     s=["About 7 minutes’ walk to Chaweng Beach", "Staff get a lot of praise"],
     d={"breakfast": "Not listed by the hostel", "privacy": "Single-sex dorms (female or male) plus private ensuite rooms",
        "beds": "10-bed bunk dorms; reviewers say the top bunks wobble", "toilet": "Bathroom attached to each dorm; private rooms are ensuite",
        "room": "Air-con, daily housekeeping, shared fridge and microwave, terrace"},
     tips=["Cash only"],
     src=[S("Hostelz", "https://www.hostelz.com/best-hostels-koh-samui"), S("Hostelworld", HW + "/hostels/p/331079/tian-ming-hostel/"), S("Travelocity", "https://www.travelocity.ca/Koh-Samui-Hotels-Tian-Ming-Hostel.h113619893.Hotel-Reviews")])
gaff(id="g-kohabitat-samui", n="KoHabitat Samui", cc="TH", city="Koh Samui", lat=9.5430, lng=100.0410,
     p=[8.69], cur="USD", r=9.2, rs="Hostelworld (via Hostelz)",
     s=["In Bophut near Big C, about 12 minutes’ drive from Chaweng Beach"],
     d={"breakfast": "Not included", "privacy": "One 12-bed mixed dorm",
        "beds": "12 single beds, each with its own curtain", "toilet": "Two shared bathrooms, cleaned daily, with hairdryers",
        "room": "Air-con, no window in the dorm, shared kitchen, adults only"},
     tips=["Easiest with a scooter"],
     src=[S("Hostelz", "https://www.hostelz.com/best-hostels-koh-samui"), S("Trip.com", "https://nz.trip.com/hotels/koh-samui-hotel-detail-13665507/kohabitat-samui"), S("Travelocity", "https://www.travelocity.com/Koh-Samui-Hotels-KoHabitat-Samui-Adults-Only-Hostel.h28956002.Hotel-Reviews"), S("Wanderlog", "https://wanderlog.com/place/details/4766668")])
gaff(id="g-bunkhouse-kpg", n="Bunkhouse Koh Phangan", cc="TH", city="Koh Phangan", lat=9.7140, lng=100.0160,
     p=[12.97], cur="USD", r=9.8, rs="Hostelworld (via Hostelz)",
     s=["Opened in 2025 in Ban Tai, near Hard Road", "Praised for cleanliness and a friendly, social feel"],
     d={"breakfast": "Not included (free coffee, tea and biscuits)", "privacy": "8-bed mixed dorm and 8-bed female dorm",
        "beds": "Capsule-style bunks for privacy", "toilet": NC,
        "room": "Air-con, shared kitchen, adults only (18+)"},
     src=[S("Hostelz", "https://www.hostelz.com/party-hostels-in-koh-phangan"), S("Hostelworld", HW + "/hostels/p/331210/bunkhouse-koh-phangan/"), S("Trip.com", "https://ca.trip.com/hotels/koh-phangan-hotel-detail-127649914/bunkhouse-koh-phangan-co-ltd/")])
gaff(id="g-mbar-kpg", n="Mbar Haad Rin", cc="TH", city="Koh Phangan", lat=9.6772, lng=100.0640,
     p=[11.35], cur="USD", r=9.8, rs="Hostelworld (via Hostelz)",
     s=["Tiny party hostel in Haad Rin, home of the Full Moon Party", "4-minute walk to both Haad Rin beaches"],
     d={"breakfast": "Not included (free coffee and tea)", "privacy": "Two 6-bed mixed dorms",
        "beds": "Three bunk beds per dorm", "toilet": "Each dorm has its own bathroom",
        "room": "Lake views, one dorm has a balcony, daily housekeeping, bar and arcade downstairs"},
     tips=["Cash only", "Book well ahead around Full Moon dates"],
     src=[S("Hostelz", "https://www.hostelz.com/party-hostels-in-koh-phangan"), S("Expedia", "https://www.expedia.ae/Ko-Pha-Ngan-Hotels-MBAR-HOSTEL-HAAD-RIN.h106733777.Hotel-Information"), S("Travelocity", "https://travelocity.ca/Ko-Pha-Ngan-Hotels-MBAR-HOSTEL-HAAD-RIN.h106733777.Hotel-Information")])
gaff(id="g-dearly-tao", n="The Dearly Koh Tao", cc="TH", city="Koh Tao", lat=10.0700, lng=99.8300,
     p=[16], cur="USD", r=8.8, rs="HotelsCombined", rc=1463,
     s=["Flashpacker-style hostel and PADI dive resort in Chalok", "7 minutes’ walk to Chalok Baan Kao Bay"],
     d={"breakfast": "Free buffet breakfast, 7–10 am", "privacy": "4-bed mixed and 6-bed female dorms, plus private rooms",
        "beds": "4-bed dorms have two large bunks", "toilet": "4-bed dorms have two bathrooms; some private rooms share, deluxe rooms are ensuite",
        "room": "Air-con, pool (7 am–7 pm), restaurant, free beach shuttle"},
     src=[S("HotelsCombined", "https://www.hotelscombined.ae/Place/Ko_Pha_ngan-hostels.htm"), S("Travelocity", "https://www.travelocity.ca/Koh-Tao-Hotels-The-Dearly-Koh-Tao-Hostel.h87555868.Hotel-Information"), S("Expedia", "https://expedia.co.th/Koh-Tao-Hotels-The-Dearly-Koh-Tao-Hostel.h87555868.Hotel-Information"), S("South East Asia Backpacker", "https://southeastasiabackpacker.com/koh-tao-hostels/")])
gaff(id="g-indie-tao", n="Indie Hostel Koh Tao", cc="TH", city="Koh Tao", lat=10.0985, lng=99.8272,
     p=[13], cur="USD", r=7.6, rs="Booking.com (via ViaMichelin)", rc=709,
     s=["100 m from Sairee Beach, across from Choppers and Diza Bar", "Dive schools nearby give guests discounts"],
     d={"breakfast": "Not included; about 100 baht with coffee at the café downstairs", "privacy": "Dorms and compact private rooms",
        "beds": "Built-in wooden capsule bunks with curtains, reading lights and lockers", "toilet": "Shared bathrooms with rain showers",
        "room": "Air-con; towels cost extra"},
     tips=["Cash only", "The bar opposite plays music until about 1 am", "Some reviewers mention mould in rooms"],
     src=[S("Booking.com", "https://sp.booking.com/hotel/th/indie-hostel-koh-tao.html"), S("ViaMichelin", "https://www.viamichelin.pt/web/Hotel/Ko_Tao-84360-_-zfhhoy6b"), S("Wanderlog", "https://wanderlog.com/place/details/2846261"), S("South East Asia Backpacker", "https://southeastasiabackpacker.com/koh-tao-hostels/")])
gaff(id="g-nomads-aonang", n="Nomads Ao Nang", cc="TH", city="Ao Nang", lat=8.0440, lng=98.8170,
     p=[10.55], cur="USD", r=9.3, rs="Hostelz",
     s=["Ao Nang’s big party hostel, with daily trips and pub crawls", "700 m from Nopparat Thara Beach"],
     d={"breakfast": "Not listed by the hostel", "privacy": "Dorms only",
        "beds": "4-, 6- and 8-bed dorms", "toilet": "4-bed dorms have their own bathroom; in the 6-bed the toilet is outside",
        "room": "Air-con, pool, bar; ages 18–35; music stops at 11 pm"},
     tips=["Book the 4-bed dorm for an inside bathroom", "Cards only, no cash"],
     src=[S("Hostelz", "https://www.hostelz.com/best-hostels-krabi"), S("Booking.com (via easyJet)", "https://hotels.easyjet.com/hotel/th/nomads-ao-nang.en-gb.html"), S("Trip.com reviews", "https://id.trip.com/hotels/krabi-hotel-detail-105202381/nomads-ao-nang/review.html"), S("The Broke Backpacker", "https://thebrokebackpacker.com/best-hostels-in-krabi-thailand")])
gaff(id="g-kbunk-aonang", n="K-Bunk AoNang Center", cc="TH", city="Ao Nang", lat=8.0330, lng=98.8270,
     p=[7.90], cur="USD", r=9.0, rs="Hostelz",
     s=["Central Ao Nang, about 10 minutes’ walk to the beach", "Nightly bar crawls and its own tours"],
     d={"breakfast": "Paid, from the menu (guests rate it highly)", "privacy": "Dorms and private doubles",
        "beds": "8-bed mixed dorms with privacy curtains and reading lights", "toilet": "8-bed dorms have two bathrooms inside; private rooms are ensuite",
        "room": "Air-con, salt-water pool, free towels and shampoo, water refills"},
     tips=["200 baht cash damage deposit at check-in"],
     src=[S("Hostelz", "https://www.hostelz.com/hostels-in-ao-nang-with-private-rooms"), S("Hostelz", "https://www.hostelz.com/en/best-hostels-ao-nang"), S("Booking.com (via Citypass)", "https://hotels.citypass.com/hotel/th/the-moment-hostel.en-gb.html"), S("Booking.com", "https://suite.booking.com/hotel/th/the-moment-hostel.zh-cn.html")])
gaff(id="g-slumber-phiphi", n="Slumber Party Phi Phi", cc="TH", city="Koh Phi Phi", lat=7.7405, lng=98.7700,
     r=8.5, rs="Hostelworld", rc=272,
     s=["Party hostel 5 minutes’ walk from Ton Sai and Loh Dalum beaches"],
     d={"breakfast": "Not included (food at the bar-restaurant)", "privacy": "4-, 6- and 8-bed mixed dorms, a 6-bed female dorm, plus private rooms",
        "beds": "Bunks with curtains", "toilet": "Shared bathrooms outside the rooms, with bidets",
        "room": "Air-con, bar, restaurant, daily events, 18+"},
     tips=["Reviews are very mixed, including some very bad recent ones, so read the latest before booking"],
     src=[S("Hostelworld", HW + "/hostels/p/317384/slumber-party-phi-phi/"), S("Hostelworld listings", HW + "/bed-and-breakfasts/asia/thailand/koh-phi-phi/f/kitchen/"), S("Trip.com", "https://nz.trip.com/hotels/phi-phi-islands-hotel-detail-129726368/slumber-party-phi-phi"), S("Expedia", "https://expedia.com.au/Ko-Phi-Phi-Hotels-Slumber-Party-Phi-Phi.h102500868.Hotel-Reviews")])
gaff(id="g-lubd-patong", n="Lub d Phuket Patong", cc="TH", city="Phuket", lat=7.8975, lng=98.2965,
     p=[350, 500], cur="THB", r=8.4, rs="Booking.com (via Travel Guides Tip)",
     s=["One of the very few beachfront hostels in Patong, on Thaweewong Road", "5 minutes’ walk from Bangla Road, but quiet inside"],
     d={"breakfast": "Not included", "privacy": "Dorms and private rooms (privates about 900–1,400 baht)",
        "beds": NC, "toilet": NC, "room": "Pool"},
     src=[S("Travel Guides Tip", "https://travelguidestip.com/?p=297"), S("Phuket 101", "https://www.phuket101.net/best-hostels-in-phuket/")])
gaff(id="g-aekkeko-hkt", n="Aekkeko Hostel", cc="TH", city="Phuket Town", lat=7.8850, lng=98.3880,
     p=[8.84], cur="USD", r=9.1, rs="Hostelworld (via Hostelz)",
     s=["Ranked #1 in Phuket Town on Hostelz’s list"],
     tips=["Room details couldn’t be confirmed online yet, so check the listing"],
     src=[S("Hostelz", "https://www.hostelz.com/best-hostels-in-phuket-city-for-solo-female-travelers")])
gaff(id="g-onederz-rep", n="Onederz Hostel Siem Reap", cc="KH", city="Siem Reap", lat=13.3530, lng=103.8555,
     p=[6.47], cur="USD", r=9.6, rs="Hostelworld (via Hostelz)",
     s=["Next to Angkor Night Market, 3 minutes’ walk to Pub Street"],
     d={"breakfast": "Paid (English breakfast 6:30 am–noon); early sunrise breakfast for Angkor trips", "privacy": "Mixed dorms, a 4-bed female dorm, and private twins, doubles and triples",
        "beds": "Bunk dorms", "toilet": "Showers with bidets; private rooms are ensuite",
        "room": "Air-con, outdoor pool, restaurant and bar, daily housekeeping; cards accepted"},
     src=[S("Hostelz", "https://www.hostelz.com/party-hostels-in-siem-reap"), S("Lastminute", "https://www.lastminute.com.au/Siem-Reap-Hotels-Onederz-Hostel-Siem-Reap.h15050908.Hotel-Information"), S("Ebookers", "https://www.ebookers.fi/Siem-Reap-Hotellit-Onederz-Hostel-Siem-Reap.h15050908.hotellitiedot"), S("South East Asia Backpacker", "https://southeastasiabackpacker.com/siem-reap-hostel/")])
gaff(id="g-pub-rep", n="Siem Reap Pub Hostel", cc="KH", city="Siem Reap", lat=13.3535, lng=103.8545,
     p=[4.50], cur="USD", pu="12-bed dorm, per night, from", r=9.6, rs="Along Dusty Roads", rc=3818,
     s=["Quiet side street, 1 minute from the night market and 4 from Pub Street", "Private doubles and twins from about $17"],
     d={"breakfast": "Paid, cooked to order 6–10 am", "privacy": "Dorms (the cheapest are split by gender) and private rooms",
        "beds": "4-bed and 12-bed dorms; every bed has a locker", "toilet": "Showers with bidets; private rooms are ensuite",
        "room": "Air-con, in-room safe, pool with a bar"},
     tips=["Hostelworld says pay in cash on arrival"],
     src=[S("Along Dusty Roads", "https://www.alongdustyroads.com/posts/best-hostels-in-siem-reap"), S("Hostelworld", HW + "/hostels/p/266721/siem-reap-pub-hostel/"), S("Ebookers", "https://ebookers.fi/Siem-Reap-Hotellit-Siem-Reap-Pub-Hostel.h16424764.hotellitiedot")])
gaff(id="g-madmonkey-pnh", n="Mad Monkey Phnom Penh", cc="KH", city="Phnom Penh", lat=11.5630, lng=104.9260,
     p=[10], cur="USD", r=8.8, rs="Expedia",
     s=["Well-known party hostel on Street 242", "Reviewers praise the staff and the parties"],
     d={"breakfast": "Sources disagree: Booking.com lists it as included, others say about $9, so check your rate", "privacy": "Mixed dorms of 4 to 12 beds, a 6-bed female dorm, plus private rooms",
        "beds": "Each bed has a reading light, plug, blanket and locker (bring a padlock)", "toilet": "Each dorm has its own bathroom with a hot shower",
        "room": "Air-con, curtains, pool, rooftop bar; some dorms have no window; 18+"},
     src=[S("Mad Monkey", "https://madmonkeyhostels.com/booking/?city=51"), S("Booking.com (via TAP)", "https://hotels.flytap.com/hotel/kh/mad-monkey-hostel-phnom-penh-phnom-penh.en-gb.html?aid=304142"), S("Trip.com", "https://nz.trip.com/hotels/phnom-penh-hotel-detail-22088747/mad-monkey-hostel-phnom-penh"), S("Expedia", "https://mob.expedia.ae/Cambodia-Hostels.d29-aaHostels.Travel-Guide-Accommodation")])
gaff(id="g-onederz-pnh", n="Onederz Phnom Penh", cc="KH", city="Phnom Penh", lat=11.5745, lng=104.9270,
     p=[15], cur="USD", pu="per night, from", r=9.0, rs="cozycozy", rc=8077,
     s=["Riverside on Street 110, 3 minutes from the night market", "Rooftop pool and bar over the river, free walking tour"],
     d={"breakfast": "Paid, cooked to order, about $2.50–4", "privacy": "4- and 6-bed dorms, mixed or female-only, plus private rooms",
        "beds": "Full curtains, reading light, charging points and big lockers", "toilet": "Shared bathrooms outside the dorms, with showers and toilets separate; private rooms are ensuite",
        "room": "Air-con, lift"},
     src=[S("Hostelworld", HW + "/hostels/p/274433/onederz-phnom-penh/"), S("Wotif", "https://www.wotif.com/Phnom-Penh-Hotels-Onederz-Phnom-Penh.h124029717.Hotel-Information"), S("Booking.com (via TAP)", "https://hotels.flytap.com/hotel/kh/waterview-guesthouse.en-gb.html?aid=304142"), S("cozycozy", "https://cozycozy.com/us/cambodia-hostels")])
gaff(id="g-hideout-sgn", n="The Hideout Hostel", cc="VN", city="Ho Chi Minh City", lat=10.7676, lng=106.6927,
     p=[7.54], cur="USD", r=9.1, rs="Budget Your Trip (91%)",
     s=["On Pham Ngu Lao, the backpacker street in District 1", "Party hostel with free beers at the rooftop bar and pub crawls three nights a week"],
     d={"breakfast": "Free, cooked to order", "privacy": "Dorms and private rooms (from about $19)",
        "beds": NC, "toilet": NC, "room": "Air-con, lift, bar"},
     tips=["Scores elsewhere are lower (7.6 to 7.9 on Expedia and Kayak)", "3% surcharge on card payments"],
     src=[S("Budget Your Trip", "https://www.budgetyourtrip.com/vietnam-article/best-party-hostels-in-vietnam/21"), S("Expedia", "https://expedia.com.ph/Ho-Chi-Minh-City-Hotels-The-Hideout.h23615329.Hotel-Information"), S("Kayak", "https://www.kayak.com.ph/Ho-Chi-Minh-City-Hotels-The-Hideout.2476991.ksp"), S("Culture Trip", "https://theculturetrip.com/articles/the-10-best-hostels-in-ho-chi-minh-city")])
gaff(id="g-rooftops-sgn", n="Saigon Rooftops Hostel", cc="VN", city="Ho Chi Minh City", lat=10.7630, lng=106.6950,
     p=[10.70], cur="USD", r=9.5, rs="Hostelworld (via Hostelz)",
     s=["Big hostel (around 178 beds) with four rooftop terraces", "District 1, Co Giang area"],
     d={"breakfast": "Free breakfast buffet", "privacy": "Dorms and private rooms",
        "beds": "Large dorms", "toilet": "Dorms have their own bathrooms with bidets",
        "room": "Air-con, a free beer each night on the rooftop, free water refills, daily cleaning"},
     src=[S("Hostelz", "https://www.hostelz.com/en/youth-hostels-in-ho-chi-minh-city"), S("Hostelworld", HW + "/hostels/p/322563/saigon-rooftops-hostel/"), S("Booking.com (via Webbanve)", "https://hotels.webbanve.net/hotel/vn/saigon-rooftops-hostel-ho-chi-minh.html"), S("The Broke Backpacker", "https://www.thebrokebackpacker.com/?p=32714")])
gaff(id="g-dom-hoian", n="Dom Hostel and Bar", cc="VN", city="Hoi An", lat=15.8810, lng=108.3290,
     p=[12], cur="USD", pu="per night, from", r=9.3, rs="Booking.com (via Priceline)",
     s=["58 Ba Trieu Street, 7 minutes’ walk to the Japanese Bridge"],
     d={"breakfast": "Free local breakfast, 7:30–9 am", "privacy": "6-bed men-only and women-only dorms",
        "beds": "Three bunks per dorm, big cabinets (bring a padlock)", "toilet": "Each dorm has its own bathroom",
        "room": "Air-con, blackout curtains, desk, daily housekeeping"},
     src=[S("Priceline", "https://h.priceline.com/hostels/country/vn.en-gb.html"), S("Wotif", "https://www.wotif.com/Da-Nang-Hotels-Dom-Hostel-And-Bar.h119760662.Hotel-Information"), S("Hotels.com", "https://nz.hotels.com/ho3833341184"), S("Expedia", "https://www.expedia.co.jp/en/Da-Nang-Hotels-Dom-Hostel-And-Bar.h119760662.Hotel-Information")])
gaff(id="g-ancient-hoian", n="Hoi An Ancient Town Hostel & Bar", cc="VN", city="Hoi An", lat=15.8790, lng=108.3240,
     p=[17], cur="USD", pu="per night, from", r=9.1, rs="Booking.com (via Priceline)",
     s=["7 minutes’ walk to the Japanese Covered Bridge", "Free bikes"],
     d={"breakfast": "Free breakfast, 7:30–9 am (buffet, Asian or vegetarian)", "privacy": "6-bed men-only and women-only dorms, plus a 4-bed female dorm",
        "beds": "Bunks", "toilet": "Dorms have their own bathroom",
        "room": "Air-con, darts, restaurant"},
     src=[S("Priceline", "https://h.priceline.com/hostels/country/vn.en-gb.html"), S("Hotels.com", "https://uk.hotels.com/ho3833347776/hoi-an-ancient-town-hostel-bar"), S("ViaMichelin", "https://www.viamichelin.pl/maps/hotels/poi/hoi_an-560000-9bde3f2c"), S("Booking.com (via eDreams)", "https://hotels.edreams.co.uk/hostels/city/vn/hoi-an.en-gb.html?aid=304142")])
gaff(id="g-wanderlust-han", n="Hanoi Wanderlust Hostel & Travel", cc="VN", city="Hanoi", lat=21.0315, lng=105.8485,
     p=[5.34], cur="USD", r=9.7, rs="Hostelworld (via Hostelz)",
     s=["47–49 Hang Bong Street in the Old Quarter", "Newer building with a lift and a rooftop bar"],
     d={"breakfast": "Guests praise it; check whether your rate includes it", "privacy": "Dorms, including a female-only dorm",
        "beds": NC, "toilet": "Big bathrooms, per reviews", "room": NC},
     tips=["A couple of reviews mention mould in a ground-floor female dorm, so ask for an upper floor"],
     src=[S("Hostelz", "https://www.hostelz.com/en/best-hostels-hanoi"), S("Hostelworld", HW + "/hostels/p/331927/hanoi-wanderlust-hostel-and-travel/"), S("Hostelworld reviews", HW + "/ru/khostely/p/331927/hanoi-wanderlust-hostel-and-travel/"), S("Booking.com (via eDreams)", "https://hotels.edreams.co.uk/hotel/vn/hanoi-wanderlust-hostel-amp-travel.en-gb.html?aid=304142")])
gaff(id="g-oqview-han", n="Old Quarter View Hanoi Hostel", cc="VN", city="Hanoi", lat=21.0360, lng=105.8525,
     p=[11.41], cur="USD", r=9.4, rs="Hostelworld (via Hostelz)",
     s=["Down a quiet alley just off Ta Hien Street", "Scores 9.8 on Booking.com too"],
     d={"breakfast": "To order, about 50,000 dong", "privacy": "Mixed dorms of 4, 6, 12 and 18 beds, plus a 6-bed female dorm",
        "beds": "Curtain, light and plug by each bed; big lockers and lockable cabinets", "toilet": "Shared bathrooms with showers and bidets",
        "room": "Air-con, blackout curtains, in-room safe, free walking tour, no lift"},
     src=[S("Hostelz", "https://www.hostelz.com/best-hostels-in-hanoi-for-solo-female-travelers"), S("Hotels.com", "https://ca.hotels.com/ho1457263264/old-quarter-view-hanoi-hostel-hanoi-vietnam"), S("Booking.com (via Odeon)", "https://proxy.odeonbeds.com/hotel/vn/old-quarter-view-hanoi-hostel.html"), S("Wanderlog", "https://wanderlog.com/place/details/108179")])
gaff(id="g-littlecharm-han", n="Little Charm Hanoi Hostel", cc="VN", city="Hanoi", lat=21.0335, lng=105.8495,
     p=[7.21], cur="USD", r=8.9, rs="Hostelworld (via Hostelz)",
     s=["44 Hang Bo in the Old Quarter, 6 minutes’ walk to Hoan Kiem Lake", "Indoor pool"],
     d={"breakfast": "Paid, cooked to order 7–10 am (some rates include it)", "privacy": "6- and 8-bed mixed dorms, plus 6-bed women-only dorms",
        "beds": "Large bunks", "toilet": "Dorms have their own bathroom",
        "room": "Air-con, blackout curtains, in-room safe, indoor pool (8 am–8 pm), no lift"},
     src=[S("Hostelz", "https://www.hostelz.com/best-hostels-in-hanoi-for-solo-female-travelers"), S("Ebookers", "https://ebookers.ie/Hanoi-Hotels-Little-Charm-Hanoi-Hostel.h32134112.Hotel-Information"), S("Trip.com", "https://ph.trip.com/hotels/hanoi-hotel-detail-26595412/little-charm-hanoi-hostel"), S("Travelmyth", "https://www.travelmyth.co.uk/Hanoi/Hotels/Little-Charm-Hanoi-Hostel_tmid2300143")])
gaff(id="g-lpbackpackers-lpq", n="Luang Prabang Backpackers", cc="LA", city="Luang Prabang", lat=19.8870, lng=102.1360,
     p=[5.87], cur="USD", r=9.6, rs="Hostelworld (via Hostelz)",
     s=["Big site with a billiards table"],
     tips=["Room details couldn’t be confirmed online yet, so check the listing"],
     src=[S("Hostelz", "https://www.hostelz.com/youth-hostels-in-luang-prabang")])
gaff(id="g-sabai-lpq", n="Sabai Sabai Backpackers Hostel", cc="LA", city="Luang Prabang", lat=19.8890, lng=102.1370,
     p=[6.13], cur="USD",
     s=["Town centre, under 1 km from Mount Phousi", "Free instant coffee and water all day"],
     d={"breakfast": "Included (basic, per reviews)", "privacy": "4-, 6- and 10-bed mixed dorms, a 6-bed female dorm, plus private rooms",
        "beds": "Lockers above the beds", "toilet": "Dorms have their own bathroom with a bidet",
        "room": "Air-con and fan, billiards, shared kitchen"},
     src=[S("Hostelworld", HW + "/hostels/p/327631/sabai-sabai-luang-prabang-hostel/"), S("Hostelworld (room types)", HW + "/zh/lushe/p/327631/sabai-sabai-luang-prabang-hostel/"), S("Booking.com (via Vliegwinkel)", "https://hotel.vliegwinkel.nl/hotel/la/sabai-sabai-backpackers-hostel.en-gb.html"), S("Hostelz", "https://www.hostelz.com/youth-hostels-in-luang-prabang")])
gaff(id="g-madmonkey-lpq", n="Mad Monkey Luang Prabang", cc="LA", city="Luang Prabang", lat=19.8780, lng=102.1350,
     p=[8.82], cur="USD", r=8.7, rs="Hostelworld (via Hostelz)",
     s=["Pool with sunset views, nightly events", "You can book a whole 6- or 8-bed dorm for your group"],
     d={"breakfast": "Not included", "privacy": "6-, 8- and 12-bed mixed dorms, a 12-bed female dorm, and whole dorms to book privately",
        "beds": "Bunks (some king-bed options) with reading lights, plugs and lockers", "toilet": "Dorms have their own bathroom with a bidet",
        "room": "Air-con, pool (1.8 m deep), bar, daily housekeeping, adults only, quiet hours enforced"},
     tips=["Mad Monkey’s own site listed beds at $13–14 a night"],
     src=[S("Hostelz", "https://www.hostelz.com/youth-hostels-in-luang-prabang"), S("Mad Monkey", "https://madmonkeyhostels.com/luang-prabang/"), S("Hotels.com", "https://uk.hotels.com/ho1418934688/mad-monkey-luang-prabang-hostel-adults-only-luang-prabang-laos"), S("Smartours", "https://smartours.com/property/mad-monkey-luang-prabang/BC-2158583")])
gaff(id="g-sunshine-kul", n="Sunshine Bedz Hostel", cc="MY", city="Kuala Lumpur", lat=3.1468, lng=101.7105,
     p=[5.25, 10.54], cur="USD", pu="bed, per night, from", r=9.4, rs="Hostelworld (via Hostelz)", rc=10479,
     s=["On Bukit Bintang Walk, 2 minutes from Bukit Bintang station", "Family-run and social, with events and pub crawls"],
     d={"breakfast": "Simple breakfast (toast, tea or coffee) on Hostelworld bookings; other sites charge for it", "privacy": "4- and 6-bed dorms, a female-only dorm, plus private rooms",
        "beds": "Bunks with curtains, their own light and a locker", "toilet": "Shared bathrooms with showers and bidets",
        "room": "Air-con, kitchen, bar, no lift"},
     src=[S("Hostelz", "https://www.hostelz.com/it/ostelli-per-feste-a-kuala-lumpur"), S("Hostelworld", HW + "/hostels/p/46914/sunshine-bedz-kl/"), S("Expedia", "https://www.expedia.co.nz/Kuala-Lumpur-Hotels-Sunshine-Bedz-Hostel-Kuala-Lumpur.h31532116.Hotel-Reviews"), S("Hostelz", "https://www.hostelz.com/en/best-hostels-kuala-lumpur")])
gaff(id="g-nonee-kul", n="Nonee Guesthouse Chinatown", cc="MY", city="Kuala Lumpur", lat=3.1430, lng=101.6980, t=["Guesthouse"],
     p=[29], cur="MYR", r=9.8, rs="Hostelworld",
     s=["Homely guesthouse in Chinatown", "A favourite with solo female travellers"],
     tips=["Room details couldn’t be confirmed online yet, so check the listing"],
     src=[S("Thatch guide (Hostelworld ratings)", "https://thatch.co/guide/23w64t30m9hk1/view"), S("Hostelz", "https://hostelz.com/best-hostels-in-kuala-lumpur-for-solo-female-travelers")])
gaff(id="g-atelier-sin", n="Atelier Hostel", cc="SG", city="Singapore", lat=1.2825, lng=103.8440,
     p=[11.52], cur="USD",
     s=["Chinatown, close to the MRT", "Café downstairs doubles as a place to work"],
     d={"breakfast": "Included (simple)", "privacy": NC, "beds": NC, "toilet": NC, "room": NC},
     src=[S("Indie Traveller", "https://www.indietraveller.co/best-hostels-in-singapore"), S("Hostelz", "https://hostelz.com/hostels/Singapore/Singapore-City/chinatown")])
gaff(id="g-wink-sin", n="Wink at Mosque Street", cc="SG", city="Singapore", lat=1.2838, lng=103.8455,
     s=["Chinatown capsule hostel that feels more like a boutique hotel", "Self check-in"],
     d={"breakfast": "Included", "privacy": NC, "beds": "Capsule-style pods", "toilet": NC, "room": NC},
     tips=["Singapore is pricey: the guide put average dorms around €40"],
     src=[S("Indie Traveller", "https://www.indietraveller.co/best-hostels-in-singapore")])
gaff(id="g-roomates-cgg", n="Roomates Canggu", cc="ID", city="Canggu", lat=-8.6545, lng=115.1315,
     p=[4.64], cur="USD", r=9.0, rs="Expedia",
     s=["7 minutes’ walk to Batu Bolong Beach", "Coworking café, pool and rooftop jacuzzi"],
     d={"breakfast": "Paid, cooked to order (about 171,000 rupiah)", "privacy": "4- and 6-bed mixed dorms, plus doubles and twins",
        "beds": "Solid concrete bunks that don’t squeak, with thick curtains, lights, plugs and lockers (bring a padlock)", "toilet": "Dorms are generally spotless; a few private rooms have had musty ensuites",
        "room": "Air-con; strict quiet hours; no outside alcohol"},
     tips=["Breakage deposit is paid in cash (rupiah)"],
     src=[S("Hostelz", "https://www.hostelz.com/en/hostels/Indonesia/Canggu/safe-hostels"), S("Ebookers", "https://www.ebookers.ie/Canggu-Hotels-RooMates-Canggu.h89582284.Hotel-Information"), S("Ebookers", "https://www.ebookers.fi/Canggu-Hotellit-Roomates-Hostel-Canggu.h89582284.hotellitiedot"), S("Roomer", "https://www.roomertravel.com/featured/roomates-hostel-canggu-by-ini-vie-hospitality.h1319038")])
gaff(id="g-lushy-cgg", n="Lushy Hostels", cc="ID", city="Pererenan (Canggu)", lat=-8.6460, lng=115.1180,
     r=9.0, rs="Booking.com", rc=1626,
     s=["Named Asia’s Best Hostel 2025 by Hostelworld", "10 minutes’ walk from Echo Beach; pool, bar, coworking, free yoga"],
     d={"breakfast": "Guests mention breakfast as part of the stay; check your rate", "privacy": "Mixed dorms and private rooms",
        "beds": "Curtains, lockers by the plug, personal safe", "toilet": "8-bed dorms have 3 toilets and 3 showers inside; separate men’s and women’s shared bathrooms too",
        "room": "Air-con, daily events"},
     src=[S("What’s New Indonesia", "https://whatsnewindonesia.com/bali/ultimate-guide/stay/best-hostels-bali-unveiling-unique-sanctuaries-travelers"), S("Booking.com", "https://www.booking.com/hostels/city/id/canggu.html?aid=315330"), S("Tiket.com", "https://www.tiket.com/hotel/indonesia/lushy-hostel-canggu-610001696550930829"), S("Booking.com (via Routard)", "https://hotel.routard.com/hostels/city/id/seminyak.html?aid=304142")])
gaff(id="g-pillow-ubd", n="Pillow Inn Ubud", cc="ID", city="Ubud", lat=-8.510572, lng=115.258367, ap=False,
     p=[22], cur="USD", r=7.9, rs="Booking.com", rc=558,
     s=["Jalan Bisma, central Ubud", "Free yoga and a free ‘chasing waterfalls’ trip"],
     d={"breakfast": "Included", "privacy": "12-bed mixed dorm, a female dorm, plus private rooms",
        "beds": "Pods with a curtain, safe, mirror, reading lamp and a big locker underneath", "toilet": "Shared bathrooms; recent reviews say they could be cleaner",
        "room": "Air-con, two pools including a rooftop one, rooftop bar"},
     tips=["Its Hostelworld score is much lower (5.4 from 884 reviews), so read the latest reviews first"],
     src=[S("Hostelworld", HW + "/hostels/p/285497/pillow-inn-ubud/"), S("Hostelworld listings", HW + "/bed-and-breakfasts/asia/indonesia/ubud/p/3/"), S("Booking.com", "https://www.booking.com/hostels/city/id/ubud.html?aid=925665"), S("Hostelgeeks", "https://hostelgeeks.com/best-hostels-in-ubud-bali-indonesia/"), S("Travelmyth (location)", "https://www.travelmyth.co.uk/Ubud/Hotels/Pillow-Inn-Ubud_tmid2057982")])

# ---------------- MUNCH (prices are typical ranges, not verified) ----------------
def munch(id, n, cc, city, lat, lng, p, cur, s, best=None, tips=None):
    add(id=id, c="munch", n=n, cc=cc, city=city, lat=lat, lng=lng, t=["Street food"], p=p, cur=cur, pu="per dish, typical",
        s=s, best=best, tips=tips or [], verified=False)
munch("m-yaowarat", "Yaowarat Road street food", "TH", "Bangkok", 13.7400, 100.5100, [50, 200], "THB",
      ["Bangkok’s Chinatown, packed with stalls after dark"], best="Evenings")
munch("m-khaosan", "Khao San Road stalls", "TH", "Bangkok", 13.7589, 100.4975, [50, 100], "THB",
      ["Cheap pad thai and snacks on the backpacker strip"], best="Late night")
munch("m-cnx-gate", "Chiang Mai Gate Night Market", "TH", "Chiang Mai", 18.7803, 98.9874, [30, 80], "THB",
      ["Locals’ favourite food market at the south gate of the Old Town"], best="Evenings")
munch("m-cnx-sunday", "Sunday Walking Street", "TH", "Chiang Mai", 18.7880, 98.9890, [20, 80], "THB",
      ["Huge Sunday market along Ratchadamnoen Road with loads of food stalls"], best="Sunday from late afternoon", tips=["Gets very crowded after dark"])
munch("m-pai-walking", "Pai Walking Street", "TH", "Pai", 19.3586, 98.4405, [20, 80], "THB",
      ["Nightly street of food stalls through the middle of town"], best="Every evening")
munch("m-thongsala", "Thong Sala Night Market", "TH", "Koh Phangan", 9.7110, 99.9925, [40, 150], "THB",
      ["Main food market near the ferry pier"], best="Evenings")
munch("m-fisherman", "Fisherman’s Village Night Market", "TH", "Koh Samui", 9.5570, 100.0290, [50, 200], "THB",
      ["Weekly walking street in Bophut with lots of food"], best="Friday evenings")
munch("m-phuket-sunday", "Phuket Town Sunday Walking Street", "TH", "Phuket", 7.8842, 98.3887, [30, 100], "THB",
      ["Sunday market in the old town, known locally as Lard Yai"], best="Sunday evenings")
munch("m-krabi-night", "Krabi Town night market", "TH", "Krabi Town", 8.0617, 98.9170, [30, 100], "THB",
      ["Weekend walking street in Krabi Town"], best="Weekend evenings")
munch("m-psarchas", "Old Market (Psar Chas)", "KH", "Siem Reap", 13.3547, 103.8559, [1, 3], "USD",
      ["Cheap local dishes next to Pub Street"], best="Lunch or evening")
munch("m-russian", "Russian Market (Toul Tom Poung)", "KH", "Phnom Penh", 11.5397, 104.9175, [1.5, 4], "USD",
      ["Market food court with cheap noodle and rice dishes"], best="Lunch")
munch("m-benthanh", "Ben Thanh Market area", "VN", "Ho Chi Minh City", 10.7725, 106.6980, [40000, 100000], "VND",
      ["Pho, broken rice and banh mi around District 1’s big market"], best="Daytime")
munch("m-banhmiphuong", "Banh Mi Phuong", "VN", "Hoi An", 15.8794, 108.3319, [30000, 50000], "VND",
      ["Famous banh mi shop in the old town"], best="Any time, expect a queue")
munch("m-buncha", "Bun Cha Huong Lien", "VN", "Hanoi", 21.0185, 105.8526, [50000, 120000], "VND",
      ["Bun cha spot made famous by a 2016 presidential visit"], best="Lunch")
munch("m-lpq-night", "Luang Prabang night market food alley", "LA", "Luang Prabang", 19.8885, 102.1355, [30000, 60000], "LAK",
      ["Food alley off the night market, known for cheap buffet plates"], best="Evenings")
munch("m-alor", "Jalan Alor", "MY", "Kuala Lumpur", 3.1456, 101.7087, [8, 30], "MYR",
      ["KL’s best-known night food street in Bukit Bintang"], best="Evenings")
munch("m-maxwell", "Maxwell Food Centre", "SG", "Singapore", 1.2803, 103.8447, [4, 8], "SGD",
      ["Classic hawker centre in Chinatown"], best="Lunch")
munch("m-gianyar", "Gianyar Night Market", "ID", "Gianyar (near Ubud)", -8.5410, 115.3265, [15000, 50000], "IDR",
      ["Local night market about 30 minutes from Ubud"], best="Evenings")

# ---------------- COOL ----------------
def cool(id, n, cc, city, lat, lng, t, s, p=None, cur=None, cost=None, best=None, busy=None, tips=None, src=None):
    add(id=id, c="cool", n=n, cc=cc, city=city, lat=lat, lng=lng, t=t, p=p, cur=cur, pu="entry", s=s,
        cost=cost, best=best, busy=busy, tips=tips or [], src=src or [], verified=bool(src))
cool("c-grandpalace", "Grand Palace", "TH", "Bangkok", 13.7500, 100.4913, ["Temples"],
     ["Thailand’s most famous royal complex, with the Temple of the Emerald Buddha"], p=[500], cur="THB",
     best="Go early", busy="Very busy from late morning", tips=["Cover shoulders and knees or you’ll be turned away"],
     src=[S("TourRadar itinerary", "https://www.tourradar.com/t/62732")])
cool("c-chatuchak", "Chatuchak Weekend Market", "TH", "Bangkok", 13.7999, 100.5508, ["Markets"],
     ["Enormous weekend market with thousands of stalls"], cost="Free to enter", best="Weekend mornings", busy="Hot and packed by midday")
cool("c-doisuthep", "Doi Suthep temple and Monk’s Trail", "TH", "Chiang Mai", 18.8048, 98.9217, ["Temples", "Hikes", "Views"],
     ["Golden hilltop temple overlooking Chiang Mai", "The Monk’s Trail is a free forest hike up towards it"],
     cost="Small entry fee (not checked)", best="Early morning", tips=["Bring water for the hike"])
cool("c-stickyfalls", "Bua Tong Sticky Waterfall", "TH", "Chiang Mai", 19.0630, 99.0792, ["Waterfalls"],
     ["Waterfall you can climb up, because the limestone isn’t slippery"], cost="Free (not checked)", best="Weekdays")
cool("c-paicanyon", "Pai Canyon", "TH", "Pai", 19.3180, 98.4570, ["Views", "Hikes"],
     ["Narrow ridges and drop-offs just outside town"], cost="Free (not checked)", best="Sunset", busy="Busiest at sunset", tips=["Edges are steep; watch your footing"])
cool("c-fullmoon", "Full Moon Party", "TH", "Koh Phangan", 9.6760, 100.0650, ["Nightlife", "Beaches"],
     ["All-night beach party on Haad Rin, once a month"], cost="Entry fee (amount not checked)", best="Full moon night", busy="Tens of thousands of people")
cool("c-tao-diving", "Learn to dive on Koh Tao", "TH", "Koh Tao", 10.0990, 99.8270, ["Diving"],
     ["One of the most popular places in the world to do an Open Water course"], cost="Paid, price varies by school", best="Course takes about 3 to 4 days")
cool("c-johnsuwan", "John-Suwan Viewpoint", "TH", "Koh Tao", 10.0555, 99.8255, ["Views", "Hikes"],
     ["Short, steep scramble to a view over two bays"], cost="Small entry fee (not checked)", best="Sunrise or late afternoon")
cool("c-bigbuddha-samui", "Big Buddha (Wat Phra Yai)", "TH", "Koh Samui", 9.5703, 100.0600, ["Temples"],
     ["Giant golden Buddha on a little islet linked by a causeway"], cost="Free (not checked)", tips=["Cover shoulders and knees"])
cool("c-railay", "Railay Beach", "TH", "Krabi", 8.0110, 98.8380, ["Beaches", "Hikes"],
     ["Cliff-backed beaches only reachable by boat", "Famous for rock climbing"], cost="Longtail boat from Ao Nang (price not checked)", best="Go early")
cool("c-tigercave", "Tiger Cave Temple", "TH", "Krabi", 8.1259, 98.9264, ["Temples", "Hikes", "Views"],
     ["About 1,260 steps up to a hilltop shrine and view"], cost="Free (not checked)", best="Early, before the heat")
cool("c-phiphiview", "Phi Phi Viewpoint", "TH", "Koh Phi Phi", 7.7465, 98.7750, ["Views", "Hikes"],
     ["The classic view over the island’s two bays"], cost="Small entry fee (not checked)", best="Sunset")
cool("c-bigbuddha-phuket", "Big Buddha Phuket", "TH", "Phuket", 7.8275, 98.3128, ["Temples", "Views"],
     ["Huge white marble Buddha with views across the island"], cost="Free, donations welcome (not checked)")
cool("c-angkor", "Angkor Archaeological Park", "KH", "Siem Reap", 13.4125, 103.8670, ["Temples"],
     ["Angkor Wat, Bayon, Ta Prohm and dozens more temples"], p=[37, 72], cur="USD",
     cost="$37 for 1 day, $62 for 3 days, $72 for 7 days", best="Sunrise at Angkor Wat", busy="Sunrise is the busiest moment",
     tips=["Only buy passes from Angkor Enterprise, the official seller", "A 3-day pass can be used on any 3 days within 10"],
     src=[S("Hello Angkor", "https://helloangkor.com/angkor-ticket-prices/")])
cool("c-tuolsleng", "Tuol Sleng Genocide Museum (S-21)", "KH", "Phnom Penh", 11.5494, 104.9178, ["Museums"],
     ["Former Khmer Rouge prison, now a museum; heavy but important"], cost="Paid (amount not checked)", tips=["The audio guide is well worth it"])
cool("c-bokor", "Bokor Mountain", "KH", "Kampot", 10.6250, 104.0300, ["Views", "Excursions"],
     ["Mountain road with old colonial ruins and big views, popular by motorbike"], cost="Not checked", best="Clear mornings")
cool("c-cuchi", "Cu Chi Tunnels", "VN", "Ho Chi Minh City", 11.1440, 106.4630, ["Excursions", "Museums"],
     ["Wartime tunnel network about 2 hours from the city"], cost="Paid, often booked as a tour (not checked)", best="Morning")
cool("c-hoian-old", "Hoi An Ancient Town", "VN", "Hoi An", 15.8770, 108.3270, ["Views", "Markets"],
     ["Lantern-lit old town on the river"], cost="Ticket for some sights (amount not checked)", best="After dark", busy="Busy every evening")
cool("c-trangan", "Trang An boat trip", "VN", "Ninh Binh", 20.2560, 105.8930, ["Excursions", "Views"],
     ["Rowing boats through caves and limestone karsts"], cost="Paid (amount not checked)", best="Morning")
cool("c-halong", "Ha Long Bay cruise", "VN", "Ha Long", 20.9101, 107.1839, ["Excursions"],
     ["Day or overnight boat trips among thousands of islands"], cost="Varies a lot by boat (not checked)")
cool("c-hoankiem", "Hoan Kiem Lake", "VN", "Hanoi", 21.0285, 105.8522, ["Views"],
     ["The lake at the heart of Hanoi", "The streets around it go pedestrian at weekends"], cost="Free", best="Weekend evenings")
cool("c-kuangsi", "Kuang Si Falls", "LA", "Luang Prabang", 19.7490, 101.9930, ["Waterfalls"],
     ["Turquoise tiered pools you can swim in"], cost="Small entry fee (not checked)", best="Morning, before tour groups")
cool("c-phousi", "Mount Phousi", "LA", "Luang Prabang", 19.8910, 102.1380, ["Views", "Temples"],
     ["Hill in the middle of town with a temple and sunset view"], cost="Small entry fee (not checked)", best="Sunset", busy="Crowded at sunset")
cool("c-batu", "Batu Caves", "MY", "Kuala Lumpur", 3.2379, 101.6840, ["Temples", "Hikes"],
     ["Hindu cave temple up 272 rainbow-painted steps"], cost="Free to enter the main cave (not checked)", tips=["Dress code applies"])
cool("c-gardens", "Gardens by the Bay Supertree Grove", "SG", "Singapore", 1.2816, 103.8636, ["Views"],
     ["Giant tree-like towers with a free evening light show"], cost="Outdoor gardens are free (not checked)", best="Evening light show")
cool("c-tegallalang", "Tegallalang Rice Terraces", "ID", "Ubud", -8.4339, 115.2789, ["Views", "Hikes"],
     ["Bali’s classic terraced rice fields"], cost="Small entry fee (not checked)", best="Early morning", busy="Busy by late morning")
cool("c-batur", "Mount Batur sunrise trek", "ID", "Kintamani", -8.2422, 115.3750, ["Hikes", "Views"],
     ["Pre-dawn climb up an active volcano for sunrise"], cost="Usually a guided tour (price not checked)", best="Leaves around 2 to 4 am")

# ---------------- TRANSPORT HUBS (map pins) ----------------
def hub(id, n, cc, city, lat, lng, s):
    add(id=id, c="move", n=n, cc=cc, city=city, lat=lat, lng=lng, t=["Hub"], s=s, verified=False)
hub("h-aphiwat", "Krung Thep Aphiwat Central Terminal", "TH", "Bangkok", 13.8047, 100.5413, ["Sleeper trains north to Chiang Mai and south towards the islands"])
hub("h-cnx-station", "Chiang Mai Railway Station", "TH", "Chiang Mai", 18.7847, 99.0170, ["Sleeper trains back to Bangkok"])
hub("h-maenam", "Mae Nam Pier", "TH", "Koh Samui", 9.5733, 100.0003, ["Lomprayah ferries to Koh Phangan, Koh Tao and the mainland"])
hub("h-thongsala", "Thong Sala Pier", "TH", "Koh Phangan", 9.7096, 99.9909, ["Ferries to Koh Tao and Koh Samui"])
hub("h-maehaad", "Mae Haad Pier", "TH", "Koh Tao", 10.0874, 99.8266, ["Ferries to Koh Phangan, Koh Samui and Chumphon"])
hub("h-rassada", "Rassada Pier", "TH", "Phuket", 7.8580, 98.4004, ["Ferries to Koh Phi Phi"])
hub("h-klongjilad", "Klong Jilad Pier", "TH", "Krabi Town", 8.0516, 98.9132, ["Ferries to Koh Phi Phi"])
hub("h-tonsai", "Tonsai Pier", "TH", "Koh Phi Phi", 7.7387, 98.7710, ["Ferries to Phuket, Krabi and Ao Nang"])
hub("h-gi-rep", "Giant Ibis bus stop", "KH", "Siem Reap", 13.3600, 103.8580, ["Buses to Phnom Penh, Bangkok and Ho Chi Minh City"])
hub("h-gi-pnh", "Giant Ibis bus stop", "KH", "Phnom Penh", 11.5625, 104.9290, ["Buses to Siem Reap, Kampot and Ho Chi Minh City"])
hub("h-pnl", "Pham Ngu Lao bus offices", "VN", "Ho Chi Minh City", 10.7675, 106.6930, ["International buses to Phnom Penh"])
hub("h-dad-station", "Da Nang Railway Station", "VN", "Da Nang", 16.0716, 108.2089, ["Trains up and down the coast"])
hub("h-han-station", "Hanoi Railway Station", "VN", "Hanoi", 21.0245, 105.8412, ["Trains south along the coast"])


WP = {"c-grandpalace":"Grand_Palace","c-chatuchak":"Chatuchak_Weekend_Market","c-doisuthep":"Wat_Phra_That_Doi_Suthep",
 "c-stickyfalls":"Bua_Tong_Waterfall","c-paicanyon":"Pai_Canyon","c-fullmoon":"Full_Moon_Party","c-tao-diving":"Ko_Tao",
 "c-bigbuddha-samui":"Wat_Phra_Yai","c-railay":"Railay_Beach","c-tigercave":"Wat_Tham_Suea_(Krabi)","c-phiphiview":"Phi_Phi_Islands",
 "c-bigbuddha-phuket":"Big_Buddha_(Phuket)","c-angkor":"Angkor_Wat","c-tuolsleng":"Tuol_Sleng_Genocide_Museum","c-bokor":"Bokor_Hill_Station",
 "c-cuchi":"Cu_Chi_tunnels","c-hoian-old":"Hoi_An","c-trangan":"Trang_An","c-halong":"Ha_Long_Bay","c-hoankiem":"Hoan_Kiem_Lake",
 "c-kuangsi":"Kuang_Si_Falls","c-phousi":"Mount_Phou_Si","c-batu":"Batu_Caves","c-gardens":"Gardens_by_the_Bay","c-tegallalang":"Tegallalang",
 "c-batur":"Mount_Batur","m-yaowarat":"Yaowarat_Road","m-khaosan":"Khaosan_Road","m-benthanh":"Ben_Thanh_Market","m-alor":"Jalan_Alor",
 "m-maxwell":"Maxwell_Food_Centre","h-aphiwat":"Krung_Thep_Aphiwat_Central_Terminal","h-cnx-station":"Chiang_Mai_railway_station",
 "h-han-station":"Hanoi_railway_station","h-dad-station":"Da_Nang_railway_station"}
for p in places:
    p["wp"] = WP.get(p["id"])

# ---------------- ROUTES ----------------
routes = []
def route(**k):
    k.setdefault("p", None); k.setdefault("cur", None); k.setdefault("dur", None); k.setdefault("op", None)
    k.setdefault("notes", []); k.setdefault("src", []); k.setdefault("chk", CHK); k.setdefault("live", None)
    k.setdefault("verified", bool(k.get("src")))
    routes.append(k)
route(id="r-bkk-cnx-train", cc=["TH"], a="Bangkok", b="Chiang Mai", mode="Train", dur="About 13 h, overnight", p=[941, 1041], cur="THB",
      op="State Railway of Thailand, train #9, 2nd-class sleeper", notes=["Leaves from Krung Thep Aphiwat Central Terminal", "Upper berths are cheaper than lower"],
      src=[S("Thailand Train guide", "https://thailandtrain.pages.dev/contentDetail/567")])
route(id="r-bkk-cnx-fly", cc=["TH"], a="Bangkok", b="Chiang Mai", mode="Flight", dur="1 h 5–25 min, plus airport time", p=[30, 75], cur="USD",
      op="Several budget airlines", src=[S("Visit Thailand Today", "https://www.visitthailandtoday.com/guides/chiang-mai-to-bangkok")])
route(id="r-cnx-pai", cc=["TH"], a="Chiang Mai", b="Pai", mode="Minivan", dur="About 3 h on a very twisty road",
      op="Several minivan companies", notes=["Hundreds of bends, so bring travel sickness tablets if you need them", "Price not checked yet"], verified=False)
route(id="r-bkk-surat-train", cc=["TH"], a="Bangkok", b="Surat Thani", mode="Train", dur="Overnight", p=[978], cur="THB",
      op="State Railway of Thailand, train #31, 2nd-class sleeper", notes=["Surat Thani is the jumping-off point for Koh Samui, Phangan and Tao"],
      src=[S("Thailand Train guide", "https://thailandtrain.pages.dev/contentDetail/567")])
route(id="r-bkk-tao-combo", cc=["TH"], a="Bangkok", b="Koh Tao", mode="Bus + ferry", op="Lomprayah joint ticket",
      notes=["One ticket covers the bus and the boat", "Lomprayah needs booking two days ahead", "Price not checked yet"],
      src=[S("12Go", "https://12go.asia/en/travel/bangkok/koh-tao?z=162257")], live="https://12go.asia/en/travel/bangkok/koh-tao?z=162257")
route(id="r-samui-phangan", cc=["TH"], a="Koh Samui", b="Koh Phangan", mode="Ferry", dur="About 30 min", p=[300, 400], cur="THB",
      op="Lomprayah high-speed catamaran", src=[S("Thailand Boat Tickets", "https://thailandboattickets.com/en/guides/lomprayah-ferry")])
route(id="r-phangan-tao", cc=["TH"], a="Koh Phangan", b="Koh Tao", mode="Ferry", dur="1½–1¾ h",
      op="Lomprayah or Seatran Discovery", notes=["From Thong Sala pier to Mae Haad on Koh Tao", "Price not checked yet"],
      src=[S("12Go", "https://12go.asia/en/travel/bangkok/koh-tao?z=162257")])
route(id="r-samui-tao", cc=["TH"], a="Koh Samui", b="Koh Tao", mode="Ferry", dur="About 2 h", p=[650, 750], cur="THB",
      op="Lomprayah", src=[S("Thailand Boat Tickets", "https://thailandboattickets.com/en/guides/lomprayah-ferry")])
route(id="r-gulf-andaman", cc=["TH"], a="Gulf islands", b="Krabi or Phuket", mode="Bus + ferry", op="Lomprayah, via Surat Thani",
      notes=["Lomprayah’s Surat Thani line links the Gulf islands with Phuket, Krabi and Koh Phi Phi", "Price not checked yet"],
      src=[S("Baolau", "https://www.baolau.com/ja/transportation/thailand/ferries/lom-lomprayah/")])
route(id="r-phiphi", cc=["TH"], a="Phuket or Krabi", b="Koh Phi Phi", mode="Ferry",
      notes=["From Rassada pier in Phuket Town or Klong Jilad pier in Krabi Town", "Smaller boats also run from Ao Nang", "Price not checked yet"],
      src=[S("Hostelz", "https://www.hostelz.com/hostels/Thailand/Ko-Phi-Phi/beach-hostels")])
route(id="r-hkt-pnh", cc=["TH", "KH"], a="Phuket", b="Phnom Penh", mode="Flight", notes=["Your planned jump into Cambodia", "Check flights live, prices not saved yet"], verified=False)
route(id="r-bkk-rep", cc=["TH", "KH"], a="Bangkok", b="Siem Reap", mode="Bus", dur="About 8 h", p=[28, 48], cur="USD",
      op="Giant Ibis", src=[S("Busbud", "https://riderexpress.busbud.com/en/bus-company/giant-ibis-transport")])
route(id="r-rep-pnh", cc=["KH"], a="Siem Reap", b="Phnom Penh", mode="Bus", dur="5½–7 h", p=[15], cur="USD",
      op="Giant Ibis (day buses)", notes=["Giant Ibis night sleeper buses cost $17–25", "Stops for a toilet break and lunch (lunch not included)"],
      src=[S("12Go", "https://12go.asia/en/travel/siem-reap/phnom-penh?z=16765768"), S("Move to Cambodia", "https://movetocambodia.com/phnom-penh/how-to-get-from-phnom-penh-to-siem-reap-and-vice-versa/comment-page-2/")],
      live="https://12go.asia/en/travel/siem-reap/phnom-penh?z=16765768")
route(id="r-pnh-kampot", cc=["KH"], a="Phnom Penh", b="Kampot", mode="Bus", p=[12], cur="USD", op="Giant Ibis",
      src=[S("Busbud", "https://busbud.com/en/bus-company/giant-ibis-transport")])
route(id="r-pnh-sgn", cc=["KH", "VN"], a="Phnom Penh", b="Ho Chi Minh City", mode="Bus", dur="5–8 h, including the border", p=[10, 15], cur="USD",
      op="Mekong Express, Sorya, Kumho Samco, Virak Buntham", notes=["Giant Ibis runs this route too, from about $31", "All buses cross at Bavet / Moc Bai"],
      src=[S("Hello Angkor", "https://helloangkor.com/phnom-penh-ho-chi-minh-vietnam-bus/"), S("Busbud", "https://busbud.com/en/bus-company/giant-ibis-transport")])
route(id="r-sgn-dalat", cc=["VN"], a="Ho Chi Minh City", b="Da Lat", mode="Bus", dur="6–7 h", p=[200000, 300000], cur="VND",
      op="Phuong Trang and others (sleeper bus)", src=[S("Vietnam Tourism", "https://www.vietnamtourism.com/de/was-kostet-ein-schlafbus-in-vietnam-der-grosse-kostenratgeber-fur-2026")])
route(id="r-sgn-hoian-bus", cc=["VN"], a="Ho Chi Minh City", b="Hoi An", mode="Bus", dur="18–20 h", p=[500000, 700000], cur="VND",
      op="Sleeper bus", notes=["Cheapest but a long, tiring ride"], src=[S("Hoiana", "https://hoiana.com/blog/how-to-get-to-hoi-an")])
route(id="r-sgn-dad-train", cc=["VN"], a="Ho Chi Minh City", b="Da Nang", mode="Train", dur="About 17½ h", p=[31], cur="USD",
      op="Vietnam Railways", notes=["Da Nang is about 30 km from Hoi An"], src=[S("Expatolife", "https://www.expatolife.com/ho-chi-minh-to-hoi-an-vietnam/")])
route(id="r-sgn-dad-fly", cc=["VN"], a="Ho Chi Minh City", b="Da Nang", mode="Flight", p=[25, 55], cur="USD",
      notes=["Price when booked 2–3 weeks ahead"], src=[S("Vietnam Tourism", "https://www.vietnamtourism.com/en/transport")])
route(id="r-dad-hoian", cc=["VN"], a="Da Nang", b="Hoi An", mode="Bus", p=[35000], cur="VND", op="Public bus LK02",
      src=[S("Jungle Boss", "https://junglebosstours.com/explorer/tourism-blog/hanoi-to-hoi-an")])
route(id="r-hue-hoian", cc=["VN"], a="Hue", b="Hoi An", mode="Bus", dur="3–4 h", p=[250000, 500000], cur="VND", op="Direct coach",
      src=[S("Vietnam Tourism", "https://www.vietnamtourism.com/en/overnight-bus-vs-train-in-vietnam-an-honest-comparison-for-every-major-route")])
route(id="r-dad-han-train", cc=["VN"], a="Da Nang", b="Hanoi", mode="Train", dur="About 15 h on train SE3", p=[45, 50], cur="USD",
      op="Vietnam Railways, soft sleeper", src=[S("9Rail guide", "https://9rail.pages.dev/guide/vietnam-train-travel-guide"), S("Jungle Boss", "https://junglebosstours.com/explorer/tourism-blog/hanoi-to-hoi-an")])
route(id="r-han-onward", cc=["VN", "MY", "ID"], a="Hanoi", b="Kuala Lumpur or Bali", mode="Flight", notes=["Your possible last leg", "Check flights live, prices not saved yet"], verified=False)

# rough route as described
trip = [
  [13.7563, 100.5018, "Bangkok", 0], [18.7883, 98.9853, "Chiang Mai", 0], [19.3590, 98.4400, "Pai", 0],
  [10.0950, 99.8400, "Koh Tao", 0], [9.7300, 100.0100, "Koh Phangan", 0], [9.5120, 100.0130, "Koh Samui", 0],
  [8.0320, 98.8200, "Ao Nang", 0], [7.7400, 98.7700, "Koh Phi Phi", 0], [7.8800, 98.3900, "Phuket", 0],
  [11.5564, 104.9282, "Phnom Penh", 1], [13.3633, 103.8564, "Siem Reap", 0], [10.7769, 106.7009, "Ho Chi Minh City", 0],
  [15.8800, 108.3300, "Hoi An", 0], [21.0285, 105.8542, "Hanoi", 0],
]
trip_maybe = [[21.0285, 105.8542], [3.1390, 101.6869], [21.0285, 105.8542], [-8.6500, 115.1300]]

cities = [
  ["Bangkok", 13.7563, 100.5018], ["Chiang Mai", 18.7883, 98.9853], ["Pai", 19.3590, 98.4400], ["Koh Tao", 10.0950, 99.8400],
  ["Koh Phangan", 9.7300, 100.0100], ["Koh Samui", 9.5120, 100.0130], ["Ao Nang", 8.0320, 98.8200], ["Koh Phi Phi", 7.7400, 98.7700],
  ["Phuket", 7.8800, 98.3900], ["Siem Reap", 13.3633, 103.8564], ["Phnom Penh", 11.5564, 104.9282], ["Kampot", 10.6100, 104.1800],
  ["Ho Chi Minh City", 10.7769, 106.7009], ["Da Lat", 11.9400, 108.4400], ["Hoi An", 15.8800, 108.3300], ["Hanoi", 21.0285, 105.8542],
  ["Luang Prabang", 19.8856, 102.1347], ["Kuala Lumpur", 3.1390, 101.6869], ["Singapore", 1.2900, 103.8500], ["Ubud", -8.5069, 115.2625], ["Canggu", -8.6500, 115.1300],
]

# ---------------- TRANSPORT NETWORK (Thailand, researched Nov 2026) ----------------
STATIONS = {
 "phayathai": ["Phaya Thai station (Airport Rail Link)", 13.7566, 100.5339], "aphiwat": ["Krung Thep Aphiwat Central Terminal", 13.8047, 100.5413],
 "mochit": ["Mo Chit Bus Terminal", 13.8124, 100.5495], "bkkair": ["Suvarnabhumi Airport", 13.6900, 100.7501], "dmk": ["Don Mueang Airport", 13.9126, 100.6067],
 "cnxstn": ["Chiang Mai Railway Station", 18.7847, 99.0170], "arcade": ["Chiang Mai Arcade Bus Terminal", 18.8059, 99.0167], "cnxair": ["Chiang Mai Airport", 18.7668, 98.9626],
 "paibus": ["Pai bus station", 19.3594, 98.4419], "ceibus": ["Chiang Rai Bus Terminal", 19.9070, 99.8320],
 "cjmstn": ["Chumphon Railway Station", 10.4987, 99.1747], "cjmpier": ["Lomprayah Pier, Chumphon", 10.4510, 99.2830],
 "urtstn": ["Surat Thani Railway Station (Phun Phin)", 9.1062, 99.2320], "urtair": ["Surat Thani Airport", 9.1326, 99.1356], "donsak": ["Donsak ferry piers", 9.3290, 99.6920],
 "samuipier": ["Samui piers (Nathon, Mae Nam or Lipa Noi)", 9.5345, 99.9360], "usm": ["Samui Airport", 9.5478, 100.0623],
 "thongsala": ["Thong Sala Pier", 9.7096, 99.9909], "maehaad": ["Mae Haad Pier", 10.0874, 99.8266],
 "klongjilad": ["Klong Jilad Pier", 8.0516, 98.9132], "kbibus": ["Krabi Bus Terminal", 8.1080, 98.9070], "kbv": ["Krabi Airport", 8.0986, 98.9862],
 "nopparat": ["Nopparat Thara Pier", 8.0450, 98.8050], "tonsai": ["Tonsai Pier", 7.7387, 98.7710], "rassada": ["Rassada Pier", 7.8580, 98.4004],
 "hktbus": ["Phuket Bus Terminal 2", 7.9030, 98.3940], "hkt": ["Phuket Airport", 8.1132, 98.3169], "saladan": ["Saladan Pier (or hotel pickup)", 7.6280, 99.0390],
 "hotel": ["Hotel pickup", None, None],
}
HUBS = [
 ["bkk", "Bangkok", 13.7466, 100.5393, "Bangkok", False], ["bkkair", "Suvarnabhumi Airport (BKK)", 13.6900, 100.7501, "Bangkok", False],
 ["dmk", "Don Mueang Airport (DMK)", 13.9126, 100.6067, "Bangkok", False],
 ["cnx", "Chiang Mai", 18.7883, 98.9853, "North", False], ["pai", "Pai", 19.3590, 98.4400, "North", False], ["cei", "Chiang Rai", 19.9105, 99.8406, "North", False],
 ["cjm", "Chumphon", 10.4930, 99.1800, "Gulf coast", False], ["urt", "Surat Thani", 9.1382, 99.3215, "Gulf coast", False],
 ["samui", "Koh Samui", 9.5120, 100.0130, "Gulf islands", True], ["phangan", "Koh Phangan", 9.7300, 100.0100, "Gulf islands", True], ["tao", "Koh Tao", 10.0950, 99.8400, "Gulf islands", True],
 ["krabi", "Krabi Town", 8.0863, 98.9063, "Andaman coast", False], ["aonang", "Ao Nang", 8.0320, 98.8200, "Andaman coast", False],
 ["phiphi", "Koh Phi Phi", 7.7400, 98.7700, "Andaman islands", True], ["lanta", "Koh Lanta", 7.6250, 99.0400, "Andaman islands", False], ["phuket", "Phuket", 7.8804, 98.3923, "Andaman coast", False],
]
EDGES = []
def E(a, b, mode, dur, p=None, cur="THB", op=None, da=None, db=None, notes=None, src=None, verified=True):
    EDGES.append({"a": a, "b": b, "mode": mode, "dur": dur, "p": p, "cur": cur, "op": op, "da": da, "db": db, "notes": notes or [], "src": src or [], "verified": verified})
WEGO = S("Wego", "https://blog.wego.com/bangkok-airport-transfer/"); VTT_AIR = S("Visit Thailand Today", "https://www.visitthailandtoday.com/guides/bangkok-airport-to-city")
E("bkk", "bkkair", "Train", [0.5, 0.75], [45], op="Airport Rail Link", da="phayathai", db="bkkair", notes=["Runs about 05:30 to midnight", "Change to the BTS Skytrain at Phaya Thai"], src=[WEGO, S("Thai Holiday Guide", "https://www.thaiholidayguide.com/bangkok-airports-guide/")])
E("bkk", "bkkair", "Taxi", [0.75, 1.25], [400, 575], op="Metered taxi or Grab", da="hotel", db="bkkair", notes=["Includes the 50 baht airport surcharge and about 70–75 baht of expressway tolls", "Grab costs about the same"], src=[WEGO])
E("bkk", "dmk", "Train", [0.35, 0.6], [33], op="SRT Red Line, then MRT", da="aphiwat", db="dmk", notes=["Skywalk from the airport to the Red Line"], src=[VTT_AIR])
E("bkk", "dmk", "Bus", [0.5, 0.85], [30], op="Airport bus A1", da="mochit", db="dmk", notes=["Goes to Mo Chit BTS station"], src=[VTT_AIR, S("Go2Thailand", "https://go2thailand-com.vercel.app/blog/bangkok-airport-transfer-guide-2026/")])
E("bkk", "dmk", "Taxi", [0.5, 1], [250, 400], op="Metered taxi or Grab", da="hotel", db="dmk", notes=["Plus the 50 baht airport surcharge and tolls"], src=[VTT_AIR])
R2R_CNX = S("Rome2Rio", "https://www.rome2rio.com/s/Mochit-Terminal-Platform-3/Chiang-Mai")
E("bkk", "cnx", "Train", [11, 13], [941, 1041], op="State Railway of Thailand, 2nd-class sleeper (train #9)", da="aphiwat", db="cnxstn", notes=["Overnight; slower trains have seats from about 210 baht"], src=[S("Thailand Train guide", "https://thailandtrain.pages.dev/contentDetail/567"), R2R_CNX])
E("bkk", "cnx", "Bus", [10, 11], [550, 1006], op="Sombat Tour, Transport Co and others", da="mochit", db="arcade", notes=["Express about 704 baht, Super VIP about 1,006"], src=[R2R_CNX, S("Expatolife", "https://www.expatolife.com/bangkok-to-chiang-mai-thailand/")])
E("bkk", "cnx", "Flight", [1, 1.25], [949, 3000], op="AirAsia, Nok Air, Thai Lion Air and others", da="dmk", db="cnxair", notes=["Budget airlines fly from Don Mueang"], src=[S("The Thaiger", "https://thethaiger.com/travel/thailand-travel/the-essential-guide-to-domestic-flights-in-thailand")])
P12_PAI = S("12Go", "https://12go.asia/en/travel/chiang-mai/pai?z=15839495")
E("cnx", "pai", "Minivan", [3, 4.3], [150, 250], op="Prem Pracha or Aya Service", da="arcade", db="paibus", notes=["Departs about hourly through the day", "Hundreds of bends: take travel sickness tablets if you need them", "Riders say it’s about 200 baht at the station, a bit more online"], src=[P12_PAI, S("12Go (return)", "https://12go.asia/en/travel/pai/chiang-mai?z=15839495")])
E("cnx", "pai", "Taxi", [3, 3.5], [99, 101], cur="USD", op="Private car for up to 3", da="hotel", db="hotel", notes=["Price is for the whole car"], src=[S("12Go", "https://12go.asia/en/travel/pai/chiang-mai?z=16187692")])
E("cnx", "cei", "Bus", [3, 4], [250, 400], op="Green Bus Thailand", da="arcade", db="ceibus", src=[S("GoAsia", "https://goasia.cc/how-to-get-from-bangkok-to-chiang-rai")])
R2R_CJM = S("Rome2Rio", "https://www.rome2rio.com/s/Mochit/Chumphon")
E("bkk", "cjm", "Train", [8.5, 9.5], [150, 1400], op="State Railway of Thailand", da="aphiwat", db="cjmstn", notes=["Cheapest is a 3rd-class seat; sleepers cost more"], src=[R2R_CJM])
E("bkk", "cjm", "Bus", [6.5, 7.5], None, op="Tourist bus or minivan", da="mochit", db=None, notes=["Price not checked yet"], src=[S("North Vietnam guide", "https://north-vietnam.com/?p=79479")])
E("cjm", "tao", "Ferry", [1.5, 1.75], None, op="Lomprayah high-speed catamaran", da="cjmpier", db="maehaad", notes=["From about €11 on Omio", "Lomprayah also sells one ticket that covers the bus from Bangkok and this boat"], src=[S("Omio", "https://www.omio.com/ferries/chumphon/ko-tao-sii7b"), S("Thailand Boat Tickets", "https://thailandboattickets.com/en/guides/lomprayah-ferry")])
E("bkk", "urt", "Train", [10, 12], [978], op="State Railway of Thailand, 2nd-class sleeper (train #31)", da="aphiwat", db="urtstn", notes=["Overnight; journey time not checked"], src=[S("Thailand Train guide", "https://thailandtrain.pages.dev/contentDetail/567")])
E("bkk", "urt", "Flight", [1.1, 1.25], None, op="AirAsia or Nok Air", da="dmk", db="urtair", notes=["About 5 flights a day; usually much cheaper than flying to Samui", "Land before 3 pm if you want the last boat to Samui"], src=[S("Santorini Dave", "https://santorinidave.com/bangkok-to-koh-samui")])
E("urt", "samui", "Ferry", [1.5, 3], [230, 750], op="Raja, Seatran or Lomprayah", da="donsak", db="samuipier", notes=["Raja car ferry from 230 baht or Seatran from 350 (about 1.5 h) from Donsak, about an hour from town", "Lomprayah from about 650 baht", "Bus transfers from town, the station or the airport are often bundled in"], src=[S("Ferrygogo", "https://ferrygogo.com/?p=69835"), S("Siam Tickets", "https://siamtickets.com/?p=6267")])
E("urt", "phangan", "Ferry", [2.75, 4.5], [11, 48], cur="USD", op="Raja, Seatran or Lomprayah", da="donsak", db="thongsala", notes=["Raja from Donsak takes about 2.5 h; Lomprayah is the fastest"], src=[S("Direct Ferries", "https://www.directferries.com/surat_thani_city_koh_phangan_thong_sala_pier_ferry.htm"), S("Direct Ferries", "https://www.directferries.com/donsak_raja_ferry_port_koh_phangan_thong_sala_pier_ferry.htm")])
E("samui", "phangan", "Ferry", [0.5, 1.5], [230, 400], op="Lomprayah, Seatran or Raja", da="samuipier", db="thongsala", notes=["Lomprayah and Seatran take about 30 min; Raja is slower and cheaper"], src=[S("Ferrygogo", "https://ferrygogo.com/?p=69835"), S("Thailand Boat Tickets", "https://thailandboattickets.com/en/guides/lomprayah-ferry")])
E("phangan", "tao", "Ferry", [1, 1.75], None, op="Lomprayah or Seatran Discovery", da="thongsala", db="maehaad", notes=["Price not checked yet"], src=[S("Thailand Boat Tickets", "https://thailandboattickets.com/en/guides/lomprayah-ferry")])
E("samui", "tao", "Ferry", [1.5, 2], [600, 750], op="Seatran Discovery or Lomprayah", da="samuipier", db="maehaad", src=[S("Ferrygogo", "https://ferrygogo.com/?p=69835")])
E("bkk", "samui", "Flight", [1.1, 1.5], [3200], op="Bangkok Airways (the only airline)", da="bkkair", db="usm", notes=["From Suvarnabhumi; the priciest way to the islands"], src=[S("Santorini Dave", "https://santorinidave.com/bangkok-to-koh-samui"), S("Universal Traveller", "https://www.universal-traveller.com/?p=256272")])
E("cnx", "samui", "Flight", [1.75, 1.75], [5300], op="Bangkok Airways", da="cnxair", db="usm", notes=["Direct, so it skips Bangkok"], src=[S("Santorini Dave", "https://santorinidave.com/bangkok-to-koh-samui")])
E("phangan", "aonang", "Bus + ferry", [5, 8], [670, 1200], op="Raja, Seatran or Lomprayah joint ticket", da="thongsala", db="hotel", notes=["One ticket: ferry to Donsak, then bus or van across", "Raja about 670 baht, Seatran about 750, Lomprayah about 1,200", "Also stops in Krabi Town"], src=[S("The Backpacking Family", "https://thebackpackingfamily.com/koh-phangan-to-krabi-ao-nang-step-by-step-guide/"), S("12Go", "https://12go.asia/en/travel/Koh-Phangan/Ao-Nang-Beach-Krabi"), S("Inside Samui", "https://www.insidesamui.com/?p=656")])
E("samui", "aonang", "Bus + ferry", [4.5, 7], [670, 1200], op="Joint ferry and bus ticket", da="samuipier", db="hotel", notes=["Based on the Koh Phangan ticket, which calls at Samui on the way; check live"], verified=False)
E("samui", "phuket", "Flight", [0.85, 1], [2750, 7000], op="Bangkok Airways", da="usm", db="hkt", src=[S("Santorini Dave", "https://santorinidave.com/bangkok-to-koh-samui"), S("Rome2Rio", "https://www.rome2rio.com/s/Koh-Phangan/Phi-Phi-Ferry-Terminal")])
E("samui", "krabi", "Flight", [0.9, 1], [2750], op="Bangkok Airways", da="usm", db="kbv", src=[S("Santorini Dave", "https://santorinidave.com/bangkok-to-koh-samui")])
E("bkk", "krabi", "Flight", [1.4, 1.6], [23], cur="USD", op="AirAsia, Nok Air, Thai Lion Air", da="dmk", db="kbv", notes=["From Don Mueang; Krabi Airport is between Krabi Town and Ao Nang"], src=[S("The Koh Samui Guide", "https://thekohsamuiguide.com/thailand-travel-costs"), S("Lastminute", "https://www.lastminute.com/flights/r_bangkok--krabi")])
E("bkk", "phuket", "Flight", [1.25, 1.5], [928, 2500], op="AirAsia, Nok Air, Thai Lion Air and others", da="dmk", db="hkt", src=[S("The Thaiger", "https://thethaiger.com/travel/thailand-travel/the-essential-guide-to-domestic-flights-in-thailand")])
E("cnx", "phuket", "Flight", [1.5, 1.75], None, op="Limited direct flights", da="cnxair", db="hkt", notes=["Price not checked yet"], src=[S("Pickyourtrail", "https://pickyourtrail.com/blog/domestic-flights-in-thailand")])
E("krabi", "phiphi", "Ferry", [1, 2], [450], op="Andaman Wave Master, Songserm or Seatran", da="klongjilad", db="tonsai", notes=["Speedboats take about an hour but cost more"], src=[S("Baolau", "https://booking.baolau.com/en/s/Krabi/Koh-Phi-Phi/boat"), S("Direct Ferries", "https://www.directferries.com/koh_phi_phi_krabi_klong_jilad_pier_ferry.htm")])
E("aonang", "phiphi", "Ferry", [2.5, 3.5], [456, 950], op="Van and ferry ticket", da="hotel", db="tonsai", src=[S("Amazing Lanta", "https://amazinglanta.com/klong-muang-to-koh-phi-phi-ferry-transfer")])
E("phuket", "phiphi", "Ferry", [1, 2], [500, 1300], op="Andaman Wave Master and others", da="rassada", db="tonsai", src=[S("Rome2Rio", "https://www.rome2rio.com/s/Koh-Phangan/Phi-Phi-Ferry-Terminal")])
TP = S("Thai Pass", "https://www.thethaipass.com/articles/general/krabi-to-phuket")
E("krabi", "phuket", "Bus", [3, 3.5], [300, 375], op="Public bus", da="kbibus", db="hktbus", src=[TP])
E("krabi", "phuket", "Minivan", [2.5, 4], [300, 800], op="Shared minivan", da="hotel", db="hotel", notes=["Hotel drop-off costs more"], src=[S("Thai Pass", "https://www.thethaipass.com/articles/general/phuket-to-krabi")])
E("krabi", "phuket", "Ferry", [2, 3], [800, 1000], op="Ferry", da="klongjilad", db="rassada", src=[TP])
E("aonang", "phuket", "Ferry", [1, 2], [980], op="Speedboat or ferry", da="nopparat", db="rassada", src=[S("Thai Pass", "https://www.thethaipass.com/articles/general/phuket-to-krabi")])
VTT_LANTA = S("Visit Thailand Today", "https://www.visitthailandtoday.com/guides/koh-lanta-to-krabi")
E("lanta", "krabi", "Minivan", [2, 3], [380, 540], op="Shared minivan (car ferry included)", da="hotel", db=None, notes=["Hourly from about 06:00 to 16:00"], src=[VTT_LANTA])
E("lanta", "aonang", "Minivan", [3, 3], [470, 800], op="Shared minivan", da="hotel", db="hotel", src=[VTT_LANTA])
E("lanta", "phiphi", "Ferry", [0.75, 1], None, op="Ferry", da="saladan", db="tonsai", notes=["About €13 on Ferryscanner"], src=[S("Ferryscanner", "https://www.ferryscanner.com/zh/ferry-routes/ferry-krabi-town-all-ports-piers-koh-lanta-all-ports-piers")])
TAXI = {"meter": {"flag": 35, "bands": [[9, 6.5], [10, 7], [20, 8], [20, 8.5], [20, 9], [None, 10.5]]},
        "src": [S("Thaiest", "https://thaiest.com/en/thailand/bangkok/taxi"), S("Expat Focus", "https://www.expatfocus.com/thailand/guide/thailand-taxis-and-ride-hailing-services")]}
GO12 = {"bkk": "bangkok", "cnx": "chiang-mai", "pai": "pai", "cei": "chiang-rai", "cjm": "chumphon", "urt": "surat-thani", "samui": "koh-samui",
        "phangan": "koh-phangan", "tao": "koh-tao", "krabi": "krabi", "aonang": "ao-nang", "phiphi": "koh-phi-phi", "lanta": "koh-lanta", "phuket": "phuket"}
net = {"stations": STATIONS, "hubs": HUBS, "edges": EDGES, "taxi": TAXI, "go12": GO12}

exec(open("thai.py", encoding="utf-8").read())
cities += [c for c in NEW_CITIES if c[0] not in {x[0] for x in cities}]
data = {"net": net, "rates": rates, "rateSources": rate_sources, "countries": countries, "rides": rides, "places": places,
        "routes": routes, "trip": trip, "tripMaybe": trip_maybe, "cities": cities, "checked": CHK}
open("data.json", "w", encoding="utf-8").write(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
print(len(places), "places", len(routes), "routes")
from collections import Counter
print(Counter(p["c"] for p in places))
print(Counter(p["cc"] for p in places if p["c"]=="gaff"))
