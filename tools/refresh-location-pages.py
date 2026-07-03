from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCATION_DIR = ROOT / "service-location"


SERVICES = [
    (
        "../services/short-term-rental-cleaning-gpt.html",
        "Airbnb and VRBO cleaning",
        "Guest-ready turnovers for condos, cabins, townhomes, and short-term rentals.",
        "../assets/park-city-airbnb-vrbo-kitchen-island-turnover-cleaning-sun-ray.jpg",
        "Kitchen island cleaned for Airbnb and VRBO turnover service",
    ),
    (
        "../services/deep-cleaning-gpt.html",
        "Deep cleaning",
        "Detailed resets for kitchens, bathrooms, baseboards, buildup, and seasonal dust.",
        "../assets/summit-county-deep-cleaning-shower-detail-sun-ray.jpg",
        "Shower detail cleaned during a deep cleaning visit",
    ),
    (
        "../services/recurring-cleaning-gpt.html",
        "Recurring cleaning",
        "Weekly, biweekly, and monthly cleaning plans for full-time and part-time homes.",
        "../assets/midway-recurring-bedroom-cleaning-sun-ray.jpg",
        "Bedroom cleaned for recurring residential cleaning",
    ),
    (
        "../services/move-in-move-out-cleaning-gpt.html",
        "Move cleaning",
        "Move-in and move-out cleaning before walkthroughs, closings, unpacking, or guests.",
        "../assets/wasatch-county-move-in-entry-kitchen-cleaning-sun-ray.jpg",
        "Entry and kitchen cleaned for move-in or move-out cleaning",
    ),
]


PAGES = [
    {
        "slug": "park-city",
        "label": "Park City",
        "eyebrow": "Park City cleaning services",
        "title": "Park City House Cleaning, Airbnb Turnovers and Deep Cleaning | Sun Ray Cleaning",
        "description": "Park City house cleaning, Airbnb and VRBO turnovers, recurring cleaning, deep cleaning, and move cleaning for full-time homes, rentals, and second homes.",
        "h1": "Park City house cleaning for homes, rentals, and second homes.",
        "lead": "Sun Ray Cleaning helps Park City homeowners, hosts, property managers, and second-home owners keep luxury homes, condos, and rentals ready for daily life and guest arrivals.",
        "image": "job-gallery-2026-07/sun-ray-park-city-mountain-home-living-room-hero.webp",
        "image_alt": "Park City mountain home living room used as a Sun Ray Cleaning Services house cleaning hero image",
        "plan_title": "A cleaning plan built around Park City homes and guest schedules.",
        "plan_copy": "Park City properties often need more than a standard house clean. Ski-season dirt, summer guests, second-home gaps, and rental turnover windows all shape the right scope.",
        "plan": [
            "Recurring cleaning for full-time Park City residences and busy family homes.",
            "Airbnb and VRBO turnover cleaning for condos, townhomes, and vacation rentals.",
            "Deep cleaning before owner arrivals, seasonal visits, holidays, and post-ski resets.",
            "Move-in and move-out cleaning for homes, apartments, and property transitions.",
        ],
        "local_title": "Park City neighborhood pages",
        "local_copy": "Use the closest neighborhood page when the home, condo, or rental needs more specific local context.",
        "areas": [
            ("old-town-park-city", "Old Town Park City"),
            ("deer-valley", "Deer Valley"),
            ("canyons-village", "Canyons Village"),
            ("snyderville", "Snyderville"),
            ("park-meadows", "Park Meadows"),
            ("prospector", "Prospector"),
            ("kimball-junction", "Kimball Junction"),
            ("jeremy-ranch", "Jeremy Ranch"),
        ],
        "nearby": [
            ("old-town-park-city", "Old Town Park City"),
            ("deer-valley", "Deer Valley"),
            ("canyons-village", "Canyons Village"),
            ("snyderville", "Snyderville"),
            ("summit-county", "Summit County"),
            ("heber-city", "Heber City"),
        ],
        "faqs": [
            (
                "Does Sun Ray Cleaning handle Park City vacation rental turnovers?",
                "Yes. Sun Ray Cleaning provides Airbnb and VRBO turnover cleaning for Park City homes, condos, and rental properties, including guest-ready detail work and timing around arrivals.",
            ),
            (
                "Can Park City second-home owners schedule cleaning before they arrive?",
                "Yes. Share arrival timing, access details, home size, and priorities so Sun Ray can recommend a cleaning plan before owner visits or family stays.",
            ),
            (
                "What Park City neighborhoods does Sun Ray serve?",
                "Sun Ray serves Park City and nearby areas including Old Town Park City, Deer Valley, Canyons Village, Snyderville, Park Meadows, Prospector, Kimball Junction, and surrounding Summit County communities.",
            ),
        ],
    },
    {
        "slug": "snyderville",
        "label": "Snyderville",
        "eyebrow": "Snyderville cleaning services",
        "title": "Snyderville House Cleaning and Recurring Cleaning | Sun Ray Cleaning",
        "description": "Snyderville house cleaning, recurring cleaning, deep cleaning, move cleaning, and short-term rental support near Kimball Junction, Silver Creek, and Park City.",
        "h1": "Snyderville cleaning for residential and commuter-area homes.",
        "lead": "Sun Ray Cleaning serves Snyderville homes near Kimball Junction, Silver Creek, and Park City with practical cleaning plans for busy households, rentals, and move schedules.",
        "image": "summit-county-recurring-kitchen-cleaning-sun-ray.jpg",
        "image_alt": "Recurring kitchen cleaning for a Summit County home near Snyderville by Sun Ray Cleaning Services",
        "plan_title": "Reliable cleaning for Snyderville schedules and Summit County homes.",
        "plan_copy": "Snyderville residents often balance Park City work, family routines, pets, winter weather, and active households. Sun Ray builds quotes around the rooms, timing, and level of detail that matter most.",
        "plan": [
            "Recurring cleaning for kitchens, bathrooms, floors, bedrooms, and living areas.",
            "Deep cleaning for seasonal resets, post-construction dust, buildup, and guest prep.",
            "Move-in and move-out cleaning near Kimball Junction, Silver Creek, and nearby neighborhoods.",
            "Short-term rental and second-home cleaning support close to Park City and Canyons Village.",
        ],
        "local_title": "Nearby Snyderville service areas",
        "local_copy": "Snyderville connects naturally to Park City, Canyons Village, Kimball Junction, and surrounding Summit County pages.",
        "areas": [
            ("park-city", "Park City"),
            ("kimball-junction", "Kimball Junction"),
            ("canyons-village", "Canyons Village"),
            ("old-town-park-city", "Old Town Park City"),
            ("summit-county", "Summit County"),
            ("kamas", "Kamas"),
        ],
        "nearby": [
            ("park-city", "Park City"),
            ("summit-county", "Summit County"),
            ("canyons-village", "Canyons Village"),
            ("old-town-park-city", "Old Town Park City"),
            ("kamas", "Kamas"),
            ("oakley", "Oakley"),
        ],
        "faqs": [
            (
                "Does Sun Ray Cleaning serve Snyderville and Kimball Junction?",
                "Yes. Sun Ray Cleaning serves Snyderville, Kimball Junction, Silver Creek, Park City, and nearby Summit County communities.",
            ),
            (
                "Can I book recurring house cleaning in Snyderville?",
                "Yes. Weekly, biweekly, and monthly recurring cleaning can be quoted for Snyderville homes based on home size, condition, pets, and priorities.",
            ),
            (
                "Do Snyderville cleaning quotes include nearby Park City rentals?",
                "Sun Ray can quote homes, second homes, and rental properties near Snyderville, Canyons Village, and Park City when timing, access, and scope are clear.",
            ),
        ],
    },
    {
        "slug": "deer-valley",
        "label": "Deer Valley",
        "eyebrow": "Deer Valley cleaning services",
        "title": "Deer Valley Luxury Home Cleaning and Turnovers | Sun Ray Cleaning",
        "description": "Luxury home cleaning, second-home cleaning, deep cleaning, and guest-ready rental turnovers for Deer Valley homes, condos, and ski properties.",
        "h1": "Detailed Deer Valley cleaning for luxury homes and ski stays.",
        "lead": "Sun Ray Cleaning supports Deer Valley owners, hosts, and property managers with high-detail cleaning for luxury homes, second homes, ski condos, and guest-ready arrivals.",
        "image": "park-city-deep-cleaning-bathroom-detail-sun-ray.jpg",
        "image_alt": "Detailed bathroom cleaning for a Deer Valley luxury home by Sun Ray Cleaning Services",
        "plan_title": "High-detail cleaning for Deer Valley expectations.",
        "plan_copy": "Deer Valley homes often call for careful attention to bathrooms, kitchens, entry areas, guest rooms, and owner preferences. Sun Ray quotes the work based on the property and the outcome needed.",
        "plan": [
            "Second-home cleaning before owner arrivals, family visits, and ski-season stays.",
            "Guest-ready cleaning for luxury rentals, condos, townhomes, and mountain homes.",
            "Deep cleaning for bathrooms, kitchens, baseboards, dust, and high-use spaces.",
            "Recurring maintenance for owners who want the home kept polished between visits.",
        ],
        "local_title": "Deer Valley and nearby Park City pages",
        "local_copy": "Connect Deer Valley cleaning intent with Park City, Old Town, Canyons Village, and broader Summit County routes.",
        "areas": [
            ("park-city", "Park City"),
            ("old-town-park-city", "Old Town Park City"),
            ("canyons-village", "Canyons Village"),
            ("snyderville", "Snyderville"),
            ("summit-county", "Summit County"),
        ],
        "nearby": [
            ("park-city", "Park City"),
            ("old-town-park-city", "Old Town Park City"),
            ("canyons-village", "Canyons Village"),
            ("snyderville", "Snyderville"),
            ("summit-county", "Summit County"),
        ],
        "faqs": [
            (
                "Does Sun Ray Cleaning clean Deer Valley luxury homes?",
                "Yes. Sun Ray Cleaning can quote high-detail cleaning for Deer Valley luxury homes, second homes, condos, and guest-ready rentals.",
            ),
            (
                "Can Deer Valley cleaning be scheduled around guest arrivals?",
                "Yes. Share the arrival window, checkout time, access details, and priority rooms so Sun Ray can quote the right turnover or pre-arrival clean.",
            ),
            (
                "What services are most common for Deer Valley homes?",
                "Common requests include deep cleaning, recurring cleaning, second-home cleaning, short-term rental turnovers, and pre-arrival cleaning before ski trips or owner visits.",
            ),
        ],
    },
    {
        "slug": "canyons-village",
        "label": "Canyons Village",
        "eyebrow": "Canyons Village cleaning services",
        "title": "Canyons Village Condo and Vacation Rental Cleaning | Sun Ray Cleaning",
        "description": "Canyons Village condo cleaning, Airbnb and VRBO turnovers, ski-season cleaning, and guest-ready deep cleaning near Park City Mountain.",
        "h1": "Canyons Village condo and rental cleaning for guest-ready stays.",
        "lead": "Sun Ray Cleaning helps Canyons Village hosts, condo owners, and property managers keep rentals and second homes clean between ski trips, summer visits, and guest arrivals.",
        "image": "park-city-airbnb-vrbo-kitchen-island-turnover-cleaning-sun-ray.jpg",
        "image_alt": "Kitchen island cleaned for a Canyons Village Airbnb and VRBO turnover by Sun Ray Cleaning Services",
        "plan_title": "Turnover-ready cleaning for Canyons Village properties.",
        "plan_copy": "Canyons Village homes often need clean timing, clear access, ski-season entry detail, and polished kitchens and bathrooms before the next stay.",
        "plan": [
            "Airbnb and VRBO turnover cleaning for condos, townhomes, and vacation rentals.",
            "Guest-ready kitchen, bathroom, bedroom, and living area resets.",
            "Deep cleaning before peak season, after ski season, or between owner visits.",
            "Recurring or on-call cleaning for second homes near Park City Mountain.",
        ],
        "local_title": "Canyons Village and Park City links",
        "local_copy": "Use these nearby routes for related rental, second-home, and residential cleaning needs.",
        "areas": [
            ("park-city", "Park City"),
            ("snyderville", "Snyderville"),
            ("old-town-park-city", "Old Town Park City"),
            ("deer-valley", "Deer Valley"),
            ("kimball-junction", "Kimball Junction"),
            ("summit-county", "Summit County"),
        ],
        "nearby": [
            ("park-city", "Park City"),
            ("old-town-park-city", "Old Town Park City"),
            ("deer-valley", "Deer Valley"),
            ("snyderville", "Snyderville"),
            ("summit-county", "Summit County"),
        ],
        "faqs": [
            (
                "Does Sun Ray Cleaning handle Canyons Village condo turnovers?",
                "Yes. Sun Ray Cleaning provides condo and vacation rental turnover cleaning for Canyons Village properties near Park City Mountain.",
            ),
            (
                "Can Sun Ray Cleaning help during ski season?",
                "Yes. Ski-season cleaning can be quoted around guest timing, owner arrivals, mudrooms, entry areas, bathrooms, kitchens, and linen-ready presentation needs.",
            ),
            (
                "Do you clean both rentals and second homes in Canyons Village?",
                "Yes. Sun Ray can quote Airbnb and VRBO turnovers, second-home cleaning, recurring cleaning, deep cleaning, and move cleaning in Canyons Village.",
            ),
        ],
    },
    {
        "slug": "old-town-park-city",
        "label": "Old Town Park City",
        "eyebrow": "Old Town Park City cleaning services",
        "title": "Old Town Park City Airbnb, Condo and Historic Home Cleaning | Sun Ray Cleaning",
        "description": "Old Town Park City cleaning for Main Street-area condos, historic homes, Airbnb and VRBO turnovers, tight parking access, and guest-ready stays.",
        "h1": "Old Town Park City cleaning for historic homes and Main Street-area rentals.",
        "lead": "Sun Ray Cleaning helps Old Town Park City homeowners, hosts, and property managers keep historic homes, condos, and short-term rentals ready despite tight access, parking, stairs, and fast guest windows.",
        "image": "park-city-vrbo-living-room-turnover-cleaning-sun-ray.jpg",
        "image_alt": "Living room prepared for an Old Town Park City short-term rental turnover by Sun Ray Cleaning Services",
        "plan_title": "Cleaning built around Old Town access and guest turnover details.",
        "plan_copy": "Old Town Park City properties can have tight parking, stairs, older layouts, historic finishes, and short turnaround times. Sun Ray quotes the cleaning plan around the actual access and presentation needs.",
        "plan": [
            "Airbnb and VRBO cleaning for Main Street-area condos, townhomes, and historic homes.",
            "Pre-arrival and post-stay cleaning for owners, families, and guests.",
            "Deep cleaning for kitchens, bathrooms, bedrooms, floors, entry areas, and seasonal dust.",
            "Move-in and move-out cleaning for condos and homes near Old Town Park City.",
        ],
        "local_title": "Nearby Park City pages",
        "local_copy": "Old Town connects closely with Park City, Deer Valley, Canyons Village, Snyderville, and the Summit County hub.",
        "areas": [
            ("park-city", "Park City"),
            ("deer-valley", "Deer Valley"),
            ("canyons-village", "Canyons Village"),
            ("snyderville", "Snyderville"),
            ("summit-county", "Summit County"),
        ],
        "nearby": [
            ("park-city", "Park City"),
            ("deer-valley", "Deer Valley"),
            ("canyons-village", "Canyons Village"),
            ("snyderville", "Snyderville"),
            ("summit-county", "Summit County"),
        ],
        "faqs": [
            (
                "Does Sun Ray Cleaning serve Old Town Park City?",
                "Yes. Sun Ray Cleaning serves Old Town Park City homes, condos, and short-term rentals near Main Street and surrounding Park City neighborhoods.",
            ),
            (
                "Can Old Town cleaning account for tight parking or stairs?",
                "Yes. Include parking, access, stairs, entry instructions, and timing when requesting a quote so the cleaning plan reflects the property logistics.",
            ),
            (
                "Is Old Town Park City the main route instead of Old Town?",
                "Yes. The primary preview route is Old Town Park City, with the older Old Town route treated as a legacy redirect alias.",
            ),
        ],
    },
    {
        "slug": "heber-city",
        "label": "Heber City",
        "eyebrow": "Heber City cleaning services",
        "title": "Heber City House Cleaning, Move Cleaning and Deep Cleaning | Sun Ray Cleaning",
        "description": "Heber City house cleaning, move-in and move-out cleaning, deep cleaning, recurring cleaning, and vacation-home support near Red Ledges and Jordanelle.",
        "h1": "Heber City house cleaning for family homes, moves, and guest-ready spaces.",
        "lead": "Sun Ray Cleaning serves Heber City homes with recurring cleaning, deep cleaning, move cleaning, and vacation-home support near Red Ledges, Jordanelle, and the Heber Valley.",
        "image": "heber-city-residential-kitchen-cleaning-sun-ray.jpg",
        "image_alt": "Heber City residential kitchen cleaned by Sun Ray Cleaning Services",
        "plan_title": "Practical cleaning for Heber City homes and transitions.",
        "plan_copy": "Heber City cleaning needs range from family-home maintenance to move cleans, new-home resets, rental support, and seasonal guest prep around the Heber Valley.",
        "plan": [
            "Recurring cleaning for kitchens, bathrooms, bedrooms, floors, and main living areas.",
            "Move-in and move-out cleaning before walkthroughs, closings, or unpacking.",
            "Deep cleaning for seasonal resets, buildup, guest visits, and detailed home care.",
            "Vacation-home and short-term rental cleaning near Jordanelle, Red Ledges, and nearby areas.",
        ],
        "local_title": "Heber City and Wasatch County pages",
        "local_copy": "Connect Heber City searches with nearby Wasatch County and Heber Valley service pages.",
        "areas": [
            ("wasatch-county", "Wasatch County"),
            ("midway", "Midway"),
            ("daniel", "Daniel"),
            ("red-ledges", "Red Ledges"),
            ("jordanelle", "Jordanelle"),
            ("old-town-heber", "Old Town Heber"),
            ("heber-valley", "Heber Valley"),
        ],
        "nearby": [
            ("wasatch-county", "Wasatch County"),
            ("midway", "Midway"),
            ("daniel", "Daniel"),
            ("old-town-heber", "Old Town Heber"),
            ("red-ledges", "Red Ledges"),
            ("jordanelle", "Jordanelle"),
        ],
        "faqs": [
            (
                "Does Sun Ray Cleaning serve Heber City?",
                "Yes. Sun Ray Cleaning serves Heber City and nearby Wasatch County communities with recurring, deep, move, and short-term rental cleaning.",
            ),
            (
                "Can I book move-out cleaning in Heber City?",
                "Yes. Sun Ray can quote move-in and move-out cleaning for Heber City homes based on home size, condition, timing, and walkthrough needs.",
            ),
            (
                "Do you clean near Red Ledges and Jordanelle?",
                "Yes. Sun Ray Cleaning serves Heber City homes near Red Ledges, Jordanelle, Heber Valley, Midway, and surrounding Wasatch County areas.",
            ),
        ],
    },
    {
        "slug": "midway",
        "label": "Midway",
        "eyebrow": "Midway cleaning services",
        "title": "Midway House Cleaning, Cabin Cleaning and Vacation Home Cleaning | Sun Ray Cleaning",
        "description": "Midway house cleaning, vacation home cleaning, cabin cleaning, recurring cleaning, deep cleaning, and seasonal openings near Homestead and Interlaken.",
        "h1": "Midway cleaning for homes, cabins, and seasonal stays.",
        "lead": "Sun Ray Cleaning serves Midway homes, cabins, and vacation properties with recurring cleaning, deep cleaning, seasonal openings, and guest-ready support near Homestead and Interlaken.",
        "image": "midway-recurring-bedroom-cleaning-sun-ray.jpg",
        "image_alt": "Fresh bedroom cleaned for recurring residential cleaning in Midway Utah by Sun Ray Cleaning Services",
        "plan_title": "Warm, reliable cleaning for Midway homes and vacation properties.",
        "plan_copy": "Midway properties often need flexible support around family visits, cabins, ski trips, lake weekends, and seasonal openings or closings.",
        "plan": [
            "Recurring cleaning for full-time Midway homes and busy households.",
            "Cabin and vacation-home cleaning before owner arrivals or family weekends.",
            "Deep cleaning for spring openings, post-guest resets, and detailed seasonal care.",
            "Move-in and move-out cleaning for homes around Midway and the Heber Valley.",
        ],
        "local_title": "Midway and nearby Wasatch County pages",
        "local_copy": "These routes support Midway, Homestead, Interlaken, and nearby Wasatch County searches.",
        "areas": [
            ("wasatch-county", "Wasatch County"),
            ("heber-city", "Heber City"),
            ("daniel", "Daniel"),
            ("homestead", "Homestead"),
            ("interlaken", "Interlaken"),
            ("deer-creek", "Deer Creek"),
            ("swiss-mountain", "Swiss Mountain"),
        ],
        "nearby": [
            ("wasatch-county", "Wasatch County"),
            ("heber-city", "Heber City"),
            ("daniel", "Daniel"),
            ("homestead", "Homestead"),
            ("interlaken", "Interlaken"),
            ("deer-creek", "Deer Creek"),
        ],
        "faqs": [
            (
                "Does Sun Ray Cleaning serve Midway vacation homes and cabins?",
                "Yes. Sun Ray Cleaning serves Midway homes, cabins, and vacation properties with recurring, deep, move, and guest-ready cleaning.",
            ),
            (
                "Can I schedule a seasonal opening clean in Midway?",
                "Yes. Share the property condition, timing, access details, and priority rooms so Sun Ray can quote a seasonal opening or pre-arrival cleaning.",
            ),
            (
                "What areas near Midway are included?",
                "Sun Ray Cleaning serves Midway and nearby areas including Homestead, Interlaken, Deer Creek, Swiss Mountain, Heber City, Daniel, and Wasatch County.",
            ),
        ],
    },
    {
        "slug": "kamas",
        "label": "Kamas",
        "eyebrow": "Kamas cleaning services",
        "title": "Kamas House Cleaning, Ranch Home Cleaning and Deep Cleaning | Sun Ray Cleaning",
        "description": "Kamas house cleaning, rural home cleaning, ranch home cleaning, move cleaning, deep cleaning, and recurring cleaning across eastern Summit County.",
        "h1": "Kamas cleaning for rural homes, ranch properties, and everyday living.",
        "lead": "Sun Ray Cleaning serves Kamas households and rural Summit County properties with practical cleaning for kitchens, bathrooms, floors, move schedules, deep cleans, and recurring home care.",
        "image": "summit-county-recurring-kitchen-cleaning-sun-ray.jpg",
        "image_alt": "Recurring kitchen cleaning for a rural Kamas home in Summit County by Sun Ray Cleaning Services",
        "plan_title": "Cleaning support for Kamas homes and rural property needs.",
        "plan_copy": "Kamas homes can bring mudrooms, pets, outdoor gear, ranch traffic, guest visits, and longer drives into the cleaning plan. Sun Ray quotes the scope around the real property.",
        "plan": [
            "Recurring cleaning for kitchens, bathrooms, floors, bedrooms, and living spaces.",
            "Ranch and rural-home cleaning for active households and larger properties.",
            "Deep cleaning for dust, mudroom buildup, seasonal resets, and detailed home care.",
            "Move-in and move-out cleaning for Kamas and nearby eastern Summit County homes.",
        ],
        "local_title": "Kamas and eastern Summit County pages",
        "local_copy": "These links help connect Kamas with Oakley, Coalville, Park City, Snyderville, and Summit County service intent.",
        "areas": [
            ("summit-county", "Summit County"),
            ("oakley", "Oakley"),
            ("coalville", "Coalville"),
            ("park-city", "Park City"),
            ("snyderville", "Snyderville"),
        ],
        "nearby": [
            ("summit-county", "Summit County"),
            ("oakley", "Oakley"),
            ("coalville", "Coalville"),
            ("park-city", "Park City"),
            ("snyderville", "Snyderville"),
        ],
        "faqs": [
            (
                "Does Sun Ray Cleaning serve Kamas?",
                "Yes. Sun Ray Cleaning serves Kamas and nearby Summit County communities with recurring, deep, move, and rural residential cleaning.",
            ),
            (
                "Can Sun Ray Cleaning quote ranch or rural homes near Kamas?",
                "Yes. Share home size, rooms, surfaces, pets, access, timing, and current condition so Sun Ray can quote the right cleaning scope.",
            ),
            (
                "What cleaning services are available in Kamas?",
                "Common Kamas services include recurring house cleaning, deep cleaning, move-in and move-out cleaning, and detailed cleaning for rural or ranch-style homes.",
            ),
        ],
    },
    {
        "slug": "oakley",
        "label": "Oakley",
        "eyebrow": "Oakley cleaning services",
        "title": "Oakley House Cleaning, Ranch Home Cleaning and Recurring Cleaning | Sun Ray Cleaning",
        "description": "Oakley house cleaning, ranch home cleaning, recurring cleaning, deep cleaning, move cleaning, and rural residential cleaning in Summit County.",
        "h1": "Oakley cleaning for ranch homes, rural homes, and busy households.",
        "lead": "Sun Ray Cleaning serves Oakley homes with recurring cleaning, deep cleaning, move cleaning, and practical rural-home support for families, ranch properties, and active households.",
        "image": "summit-county-recurring-kitchen-cleaning-sun-ray.jpg",
        "image_alt": "Clean rural Summit County kitchen prepared for an Oakley recurring cleaning client by Sun Ray Cleaning Services",
        "plan_title": "Rural residential cleaning that fits Oakley homes.",
        "plan_copy": "Oakley homes may need extra attention to mudrooms, pet areas, kitchens, bathrooms, floors, and dust. Sun Ray quotes the cleaning around the real home and the level of detail needed.",
        "plan": [
            "Recurring cleaning for active households, family homes, and rural properties.",
            "Deep cleaning for dust, buildup, guest visits, seasonal resets, and detailed rooms.",
            "Move-in and move-out cleaning for homes around Oakley and Summit County.",
            "Flexible cleaning support for ranch homes, pets, entryways, and high-use areas.",
        ],
        "local_title": "Oakley and nearby Summit County pages",
        "local_copy": "Connect Oakley searches with Kamas, Coalville, Snyderville, Park City, and the county hub.",
        "areas": [
            ("summit-county", "Summit County"),
            ("kamas", "Kamas"),
            ("coalville", "Coalville"),
            ("snyderville", "Snyderville"),
            ("park-city", "Park City"),
        ],
        "nearby": [
            ("summit-county", "Summit County"),
            ("kamas", "Kamas"),
            ("coalville", "Coalville"),
            ("park-city", "Park City"),
            ("snyderville", "Snyderville"),
        ],
        "faqs": [
            (
                "Does Sun Ray Cleaning serve Oakley?",
                "Yes. Sun Ray Cleaning serves Oakley and nearby Summit County communities with house cleaning, deep cleaning, recurring cleaning, and move cleaning.",
            ),
            (
                "Can I request recurring cleaning for an Oakley rural home?",
                "Yes. Recurring cleaning can be quoted for Oakley homes based on room count, square footage, pets, access, condition, and preferred schedule.",
            ),
            (
                "Do Oakley quotes cover ranch-home details?",
                "Yes. Include mudrooms, pet areas, high-traffic floors, outbuildings if relevant, and priority rooms when requesting a rural or ranch-home cleaning quote.",
            ),
        ],
    },
    {
        "slug": "daniel",
        "label": "Daniel",
        "eyebrow": "Daniel cleaning services",
        "title": "Daniel Utah House Cleaning, Move Cleaning and Deep Cleaning | Sun Ray Cleaning",
        "description": "Daniel Utah house cleaning, rural home cleaning, move-in and move-out cleaning, deep cleaning, and recurring cleaning in the Heber Valley.",
        "h1": "Daniel cleaning for rural homes and Heber Valley households.",
        "lead": "Sun Ray Cleaning serves Daniel and the surrounding Heber Valley with residential cleaning, deep cleaning, move cleaning, and recurring home care for rural and family homes.",
        "image": "wasatch-county-residential-family-room-cleaning-sun-ray.jpg",
        "image_alt": "Bright family room cleaned for a Daniel Utah residential cleaning client by Sun Ray Cleaning Services",
        "plan_title": "Reliable cleaning for Daniel homes and Wasatch County routines.",
        "plan_copy": "Daniel homes often need flexible cleaning support around family schedules, rural access, pets, move timing, and bigger living spaces.",
        "plan": [
            "Recurring cleaning for kitchens, bathrooms, living areas, bedrooms, and floors.",
            "Deep cleaning for seasonal resets, dust, buildup, guest visits, and detailed home care.",
            "Move-in and move-out cleaning for Daniel and Heber Valley homes.",
            "Rural residential cleaning that accounts for access, pets, mudrooms, and high-use spaces.",
        ],
        "local_title": "Daniel and nearby Heber Valley pages",
        "local_copy": "Use these links to connect Daniel with Heber City, Midway, Center Creek, and Wasatch County.",
        "areas": [
            ("wasatch-county", "Wasatch County"),
            ("heber-city", "Heber City"),
            ("midway", "Midway"),
            ("center-creek", "Center Creek"),
            ("heber-valley", "Heber Valley"),
        ],
        "nearby": [
            ("wasatch-county", "Wasatch County"),
            ("heber-city", "Heber City"),
            ("midway", "Midway"),
            ("center-creek", "Center Creek"),
            ("heber-valley", "Heber Valley"),
        ],
        "faqs": [
            (
                "Does Sun Ray Cleaning serve Daniel, Utah?",
                "Yes. Sun Ray Cleaning serves Daniel and nearby Heber Valley communities with recurring, deep, move, and residential cleaning.",
            ),
            (
                "Can Daniel homes book deep cleaning or move cleaning?",
                "Yes. Daniel homeowners can request deep cleaning, move-in cleaning, move-out cleaning, recurring cleaning, and rural residential cleaning quotes.",
            ),
            (
                "What details help with a Daniel cleaning quote?",
                "Helpful details include square footage, bedrooms, bathrooms, service type, property access, pets, current condition, preferred timing, and priority rooms.",
            ),
        ],
    },
    {
        "slug": "coalville",
        "label": "Coalville",
        "eyebrow": "Coalville cleaning services",
        "title": "Coalville House Cleaning, Ranch Cleaning and Move Cleaning | Sun Ray Cleaning",
        "description": "Coalville house cleaning, ranch home cleaning, deep cleaning, recurring cleaning, and move cleaning for rural Summit County homes.",
        "h1": "Coalville cleaning for rural homes, ranch properties, and move-ready spaces.",
        "lead": "Sun Ray Cleaning serves Coalville homes and rural Summit County properties with deep cleaning, recurring cleaning, move cleaning, and practical residential support.",
        "image": "summit-county-recurring-kitchen-cleaning-sun-ray.jpg",
        "image_alt": "Clean Summit County kitchen prepared for a Coalville residential cleaning client by Sun Ray Cleaning Services",
        "plan_title": "Cleaning support for Coalville homes and rural property needs.",
        "plan_copy": "Coalville properties may need extra attention to dust, entryways, pet areas, mudrooms, large kitchens, and move timelines. Sun Ray quotes the work around the home and schedule.",
        "plan": [
            "Recurring cleaning for family homes, rural properties, and active households.",
            "Deep cleaning for seasonal resets, guest visits, buildup, and detailed rooms.",
            "Move-in and move-out cleaning for Coalville and surrounding Summit County homes.",
            "Ranch and rural-home cleaning support for kitchens, bathrooms, floors, and living areas.",
        ],
        "local_title": "Coalville and Summit County links",
        "local_copy": "Connect Coalville with Kamas, Oakley, Snyderville, Park City, and county-wide cleaning routes.",
        "areas": [
            ("summit-county", "Summit County"),
            ("kamas", "Kamas"),
            ("oakley", "Oakley"),
            ("snyderville", "Snyderville"),
            ("park-city", "Park City"),
        ],
        "nearby": [
            ("summit-county", "Summit County"),
            ("kamas", "Kamas"),
            ("oakley", "Oakley"),
            ("snyderville", "Snyderville"),
            ("park-city", "Park City"),
        ],
        "faqs": [
            (
                "Does Sun Ray Cleaning serve Coalville?",
                "Yes. Sun Ray Cleaning serves Coalville and nearby Summit County homes with recurring, deep, move, and rural residential cleaning.",
            ),
            (
                "Can Coalville ranch homes request cleaning?",
                "Yes. Share property access, room count, square footage, pets, mudrooms, condition, and timing so Sun Ray can quote rural or ranch-home cleaning accurately.",
            ),
            (
                "What Coalville services can be quoted?",
                "Coalville homeowners can request recurring cleaning, deep cleaning, move-in and move-out cleaning, and detailed home cleaning for rural properties.",
            ),
        ],
    },
    {
        "slug": "summit-county",
        "label": "Summit County",
        "eyebrow": "Summit County cleaning services",
        "title": "Summit County House Cleaning, Vacation Rental Cleaning and Luxury Cleaning | Sun Ray Cleaning",
        "description": "Summit County house cleaning, Airbnb and VRBO cleaning, luxury home cleaning, deep cleaning, recurring cleaning, and move cleaning for Park City, Snyderville, Kamas, Oakley, and Coalville.",
        "h1": "Summit County cleaning from Park City to Kamas, Oakley, and Coalville.",
        "lead": "Sun Ray Cleaning serves Summit County homeowners, hosts, second-home owners, luxury-home owners, and rural households with residential cleaning, rental turnovers, deep cleaning, recurring cleaning, and move cleaning.",
        "image": "summit-county-deep-cleaning-shower-detail-sun-ray.jpg",
        "image_alt": "Shower detail deep cleaning for a Summit County home by Sun Ray Cleaning Services",
        "plan_title": "A county-wide cleaning hub for Summit County searches.",
        "plan_copy": "Summit County includes ski homes, vacation rentals, commuter neighborhoods, ranch properties, family homes, and rural residences. The best quote starts with location, home type, scope, and timing.",
        "plan": [
            "Park City and Snyderville cleaning for rentals, second homes, condos, and residential clients.",
            "Kamas, Oakley, and Coalville cleaning for rural homes, ranch properties, moves, and recurring care.",
            "Deep cleaning, luxury-home cleaning, and seasonal resets for ski homes, mountain homes, and high-use spaces.",
            "Airbnb and VRBO turnover cleaning for guest-ready Summit County stays.",
        ],
        "local_title": "Summit County location pages",
        "local_copy": "These primary pages make the requested Summit County locations easy to find from the county hub.",
        "areas": [
            ("park-city", "Park City"),
            ("snyderville", "Snyderville"),
            ("deer-valley", "Deer Valley"),
            ("canyons-village", "Canyons Village"),
            ("old-town-park-city", "Old Town Park City"),
            ("kamas", "Kamas"),
            ("oakley", "Oakley"),
            ("coalville", "Coalville"),
        ],
        "nearby": [
            ("park-city", "Park City"),
            ("snyderville", "Snyderville"),
            ("deer-valley", "Deer Valley"),
            ("canyons-village", "Canyons Village"),
            ("old-town-park-city", "Old Town Park City"),
            ("kamas", "Kamas"),
            ("oakley", "Oakley"),
            ("coalville", "Coalville"),
        ],
        "faqs": [
            (
                "What Summit County areas does Sun Ray Cleaning serve?",
                "Sun Ray Cleaning serves Summit County areas including Park City, Snyderville, Deer Valley, Canyons Village, Old Town Park City, Kamas, Oakley, Coalville, and nearby communities.",
            ),
            (
                "Does Summit County service include both rentals and full-time homes?",
                "Yes. Sun Ray can quote Airbnb and VRBO turnovers, second-home cleaning, recurring residential cleaning, deep cleaning, and move cleaning across Summit County.",
            ),
            (
                "How should I request a Summit County cleaning quote?",
                "Share your city or neighborhood, bedrooms, bathrooms, square footage, service type, timing, access details, pets, and priority rooms for the most accurate quote.",
            ),
        ],
    },
    {
        "slug": "wasatch-county",
        "label": "Wasatch County",
        "eyebrow": "Wasatch County cleaning services",
        "title": "Wasatch County House Cleaning, Move Cleaning and Vacation Home Cleaning | Sun Ray Cleaning",
        "description": "Wasatch County house cleaning, vacation home cleaning, deep cleaning, recurring cleaning, and move cleaning for Heber City, Midway, Daniel, and the Heber Valley.",
        "h1": "Wasatch County cleaning for Heber City, Midway, Daniel, and nearby homes.",
        "lead": "Sun Ray Cleaning serves Wasatch County homes, cabins, vacation properties, and rural residences with recurring cleaning, deep cleaning, move cleaning, and guest-ready support.",
        "image": "wasatch-county-residential-family-room-cleaning-sun-ray.jpg",
        "image_alt": "Bright Wasatch County family room cleaned for a residential client by Sun Ray Cleaning Services",
        "plan_title": "A county hub for Heber Valley and Wasatch County cleaning.",
        "plan_copy": "Wasatch County cleaning can mean family-home maintenance, cabin openings, Red Ledges and Jordanelle-area homes, move cleans, deep cleans, and short-term rental support.",
        "plan": [
            "Heber City cleaning for family homes, moves, deep cleans, recurring service, and guest prep.",
            "Midway cleaning for homes, cabins, seasonal openings, and vacation properties.",
            "Daniel and rural Wasatch County cleaning for larger homes, pets, mudrooms, and move schedules.",
            "Deep cleaning, recurring cleaning, move cleaning, and short-term rental support across the county.",
        ],
        "local_title": "Wasatch County location pages",
        "local_copy": "These primary pages make the requested Wasatch County locations easy to find from the county hub.",
        "areas": [
            ("heber-city", "Heber City"),
            ("midway", "Midway"),
            ("daniel", "Daniel"),
            ("red-ledges", "Red Ledges"),
            ("jordanelle", "Jordanelle"),
            ("heber-valley", "Heber Valley"),
            ("old-town-heber", "Old Town Heber"),
            ("center-creek", "Center Creek"),
        ],
        "nearby": [
            ("heber-city", "Heber City"),
            ("midway", "Midway"),
            ("daniel", "Daniel"),
            ("red-ledges", "Red Ledges"),
            ("jordanelle", "Jordanelle"),
            ("heber-valley", "Heber Valley"),
        ],
        "faqs": [
            (
                "What Wasatch County areas does Sun Ray Cleaning serve?",
                "Sun Ray Cleaning serves Wasatch County areas including Heber City, Midway, Daniel, Heber Valley, Red Ledges, Jordanelle, Old Town Heber, and Center Creek.",
            ),
            (
                "Can Wasatch County homes book move cleaning?",
                "Yes. Sun Ray Cleaning can quote move-in and move-out cleaning for Wasatch County homes based on home size, condition, timing, and walkthrough needs.",
            ),
            (
                "Does Sun Ray Cleaning serve vacation homes in Wasatch County?",
                "Yes. Sun Ray can quote vacation-home, cabin, second-home, and short-term rental cleaning across Heber City, Midway, Daniel, and nearby Wasatch County areas.",
            ),
        ],
    },
]


def area_links(items: list[tuple[str, str]], prefix: str = "../service-location/") -> str:
    return "".join(
        f'<a href="{prefix}{escape(slug)}-gpt.html">{escape(label)}<span>View local page</span></a>'
        for slug, label in items
    )


def pill_links(items: list[tuple[str, str]], prefix: str = "../service-location/") -> str:
    return "".join(
        f'<a href="{prefix}{escape(slug)}-gpt.html">{escape(label)}</a>'
        for slug, label in items
    )


def service_cards() -> str:
    return "".join(
        f'<a class="info-card" href="{escape(href)}"><img class="card-image" src="{escape(image)}" alt="{escape(alt)}"><h3>{escape(title)}</h3><p>{escape(copy)}</p></a>'
        for href, title, copy, image, alt in SERVICES
    )


def faq_markup(faqs: list[tuple[str, str]]) -> str:
    return "".join(
        f'<details><summary>{escape(question)}</summary><div class="answer">{escape(answer)}</div></details>'
        for question, answer in faqs
    )


def quote_modal() -> str:
    return """<div class="modal-backdrop" data-quote-modal aria-hidden="true">
  <div class="quote-modal" role="dialog" aria-modal="true" aria-labelledby="quote-modal-title">
    <button class="modal-close" type="button" data-close-quote aria-label="Close quote form">x</button>
    <div class="quote-modal-inner">
      <aside class="quote-modal-copy">
        <p class="eyebrow">Get a transparent quote</p>
        <h2 id="quote-modal-title">Tell us what your home needs.</h2>
        <p>Share your city or neighborhood, home size, timing, and priorities. Sun Ray uses those details to give a practical quote without surprise add-ons.</p>
        <ul class="check-list">
          <li><div><strong>No-surprise pricing</strong><span>Quotes are based on real rooms, condition, and service type.</span></div></li>
          <li><div><strong>Eco and pet-safe options</strong><span>Helpful for families, hosts, and second homes.</span></div></li>
          <li><div><strong>Open daily</strong><span>Call or text (801) 604-2189 for faster help.</span></div></li>
        </ul>
      </aside>
      <div class="quote-modal-form">
        <form class="quote-form" name="Sun Ray GPT Quote Request" data-name="Sun Ray GPT Quote Request" method="post" action="#">
          <div class="field-grid">
            <label class="field">First name<input name="first-name" type="text" autocomplete="given-name" required placeholder="Jane"></label>
            <label class="field">Phone<input name="phone" type="tel" autocomplete="tel" required placeholder="(801) 555-0123"></label>
            <label class="field">Email optional<input name="email" type="email" autocomplete="email" placeholder="you@example.com"></label>
            <label class="field">City or neighborhood<input name="service-area" type="text" required placeholder="Park City, Heber, Midway..."></label>
            <label class="field">Service type<select name="service-type" required><option value="">Choose one</option><option>Recurring cleaning</option><option>Deep clean</option><option>Move-in / move-out</option><option>Airbnb / VRBO turnover</option><option>Not sure yet</option></select></label>
            <label class="field">Home size<input name="home-size" type="text" required placeholder="3 bed / 2 bath or 2,000 sq ft"></label>
            <label class="field full">Preferred timing<input name="preferred-timing" type="text" placeholder="This week, next turnover, before move-in..."></label>
            <label class="field full">Notes<textarea name="notes" placeholder="Pets, access, current condition, guest timing, product preferences..."></textarea></label>
          </div>
          <div class="form-note">Webflow-ready form markup. In this static preview, call or text (801) 604-2189 for live scheduling.</div>
          <div class="form-success" role="status">Thanks. Your quote request was received.</div>
          <div class="form-error" role="alert">Something went wrong. Please call or text (801) 604-2189.</div>
          <div class="form-actions"><button class="button button-yellow" type="submit">Request my quote</button><a class="button button-outline" href="sms:+18016042189">Text instead</a></div>
        </form>
      </div>
    </div>
  </div>
</div>"""


def header(current: str, root_prefix: str = "../") -> str:
    return f"""<div class="utility-bar"><div class="container"><span>Female-owned, locally operated cleaning for Summit and Wasatch County homes</span><a href="tel:+18016042189">Call or text (801) 604-2189</a></div></div>
<header class="site-header"><div class="container nav-row"><a class="brand" href="{root_prefix}index-gpt.html" aria-label="Sun Ray Cleaning home"><img src="{root_prefix}assets/logo-nav.png" alt="Sun Ray Cleaning Services"></a><nav class="nav-links" aria-label="Main navigation"><div class="nav-item"><a class="nav-drop-toggle" href="{root_prefix}services-gpt.html">Services</a><div class="nav-dropdown"><a href="{root_prefix}services-gpt.html"><strong>All services</strong><span>Residential cleaning service hub</span></a><a href="{root_prefix}services/short-term-rental-cleaning-gpt.html"><strong>Airbnb &amp; VRBO cleaning</strong><span>Guest-ready turnovers for Park City rentals</span></a><a href="{root_prefix}services/recurring-cleaning-gpt.html"><strong>Recurring cleaning</strong><span>Weekly, biweekly and monthly home care</span></a><a href="{root_prefix}services/deep-cleaning-gpt.html"><strong>Deep cleaning</strong><span>Detailed resets for kitchens, baths and buildup</span></a><a href="{root_prefix}services/move-in-move-out-cleaning-gpt.html"><strong>Move-in/out cleaning</strong><span>Move-ready cleaning for homes and rentals</span></a></div></div><div class="nav-item"><a class="nav-drop-toggle" href="{root_prefix}service-areas-gpt.html" aria-current="{current}">Service areas</a><div class="nav-dropdown"><a href="{root_prefix}service-areas-gpt.html"><strong>All service areas</strong><span>County, city and neighborhood hub</span></a><a href="{root_prefix}service-location/summit-county-gpt.html"><strong>Summit County</strong><span>Park City, Snyderville, Kamas and more</span></a><a href="{root_prefix}service-location/wasatch-county-gpt.html"><strong>Wasatch County</strong><span>Heber City, Midway, Daniel and more</span></a><a href="{root_prefix}service-location/park-city-gpt.html"><strong>Park City</strong><span>Old Town Park City, Deer Valley, Canyons Village</span></a><a href="{root_prefix}service-location/heber-city-gpt.html"><strong>Heber City</strong><span>Red Ledges, Jordanelle, Timber Lakes</span></a><a href="{root_prefix}service-location/midway-gpt.html"><strong>Midway</strong><span>Interlaken, Homestead, Deer Creek</span></a></div></div><a href="{root_prefix}blog-gpt.html">Blog</a><a href="{root_prefix}specials-gpt.html">Specials</a><a href="{root_prefix}about-gpt.html">About</a><a href="{root_prefix}contact-gpt.html">Contact</a></nav><a class="button button-yellow" href="{root_prefix}contact-gpt.html#quote-form" data-open-quote>Get a quote</a></div></header>"""


def footer(root_prefix: str = "../") -> str:
    return f"""<footer class="site-footer"><div class="container footer-grid"><div><img src="{root_prefix}assets/logo-nav.png" alt="Sun Ray Cleaning Services"><p>Female-owned, locally operated residential cleaning for Summit County, Wasatch County, Park City, Heber City, Midway and nearby Utah communities.</p></div><div><h3>Services</h3><a href="{root_prefix}services-gpt.html">Services overview</a><a href="{root_prefix}services/short-term-rental-cleaning-gpt.html">Short-term rentals</a><a href="{root_prefix}services/recurring-cleaning-gpt.html">Recurring cleaning</a><a href="{root_prefix}services/deep-cleaning-gpt.html">Deep cleaning</a><a href="{root_prefix}services/move-in-move-out-cleaning-gpt.html">Move-in/out cleaning</a></div><div><h3>Areas</h3><a href="{root_prefix}service-areas-gpt.html">Service areas hub</a><a href="{root_prefix}service-location/summit-county-gpt.html">Summit County</a><a href="{root_prefix}service-location/wasatch-county-gpt.html">Wasatch County</a><a href="{root_prefix}service-location/park-city-gpt.html">Park City</a><a href="{root_prefix}service-location/snyderville-gpt.html">Snyderville</a><a href="{root_prefix}service-location/old-town-park-city-gpt.html">Old Town Park City</a></div><div><h3>Blog</h3><a href="{root_prefix}blog-gpt.html">Blog home</a><a href="{root_prefix}blog/complete-guide-airbnb-vrbo-cleaning-park-city-2026-gpt.html">Complete Guide to Airbnb &amp; VRBO Cleaning in Park City</a><a href="{root_prefix}blog/how-much-does-airbnb-cleaning-cost-park-city-gpt.html">How Much Does Airbnb Cleaning Cost in Park City?</a><a href="{root_prefix}blog/post-ski-season-deep-clean-park-city-rental-owners-gpt.html">Post-Ski-Season Deep Clean Checklist</a></div><div><h3>Contact</h3><a href="{root_prefix}specials-gpt.html">Specials</a><a href="{root_prefix}discounts-gpt.html">Discounts</a><a href="{root_prefix}contact-gpt.html">Get a quote</a><a href="tel:+18016042189">(801) 604-2189</a><a href="sms:+18016042189">Text Sun Ray</a><span>Open daily, 7:30 AM - 8:30 PM</span></div></div><div class="container footer-bottom">Sun Ray Cleaning Services. Local residential cleaning with no-surprise quotes.</div></footer>"""


def page_html(page: dict[str, object]) -> str:
    plan_items = "".join(f"<li>{escape(item)}</li>" for item in page["plan"])
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="../assets/favicon/favicon.ico" sizes="any">
  <link rel="icon" type="image/svg+xml" href="../assets/favicon/favicon.svg">
  <link rel="apple-touch-icon" href="../assets/favicon/apple-touch-icon.png">
  <link rel="manifest" href="../assets/favicon/site.webmanifest">
  <meta name="theme-color" content="#1f3a68">
  <title>{escape(page["title"])}</title>
  <meta name="description" content="{escape(page["description"])}">
  <meta name="robots" content="noindex, follow">
  <meta property="og:title" content="{escape(page["title"])}">
  <meta property="og:description" content="{escape(page["description"])}">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="../styles-gpt.css">
</head>
<body>
{header("page")}
<main>
  <section class="page-hero">
    <div class="container page-hero-grid">
      <div>
        <div class="breadcrumb"><a href="../index-gpt.html">Home</a><span>/</span><a href="../service-areas-gpt.html">Service areas</a><span>/</span><span>{escape(page["label"])}</span></div>
        <p class="eyebrow">{escape(page["eyebrow"])}</p>
        <h1>{escape(page["h1"])}</h1>
        <p class="lead">{escape(page["lead"])}</p>
        <div class="hero-actions"><a class="button button-yellow" href="../contact-gpt.html#quote-form" data-open-quote>Get a quote</a><a class="button button-outline" href="sms:+18016042189">Text (801) 604-2189</a></div>
      </div>
      <div class="page-hero-media"><img src="../assets/{escape(page["image"])}" alt="{escape(page["image_alt"])}"></div>
    </div>
  </section>

  <section class="section">
    <div class="container split">
      <div>
        <p class="eyebrow">Local cleaning plan</p>
        <h2>{escape(page["plan_title"])}</h2>
        <p>{escape(page["plan_copy"])}</p>
        <ul class="check-list">{plan_items}</ul>
      </div>
      <div class="info-card">
        <h3>Best fit services</h3>
        <p>Share the location, service type, home size, timing, pets, access details, and current condition. Sun Ray will match the quote to the real cleaning need.</p>
        <div class="pill-row"><a href="../services/recurring-cleaning-gpt.html">Recurring</a><a href="../services/deep-cleaning-gpt.html">Deep clean</a><a href="../services/short-term-rental-cleaning-gpt.html">Turnovers</a><a href="../services/move-in-move-out-cleaning-gpt.html">Move clean</a></div>
      </div>
    </div>
  </section>

  <section class="section section-cream">
    <div class="container">
      <div class="section-head center"><p class="eyebrow">Nearby pages</p><h2>{escape(page["local_title"])}</h2><p>{escape(page["local_copy"])}</p></div>
      <div class="area-list">{area_links(page["areas"])}</div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center"><p class="eyebrow">Services in {escape(page["label"])}</p><h2>Popular cleaning services for this area.</h2></div>
      <div class="grid-2">{service_cards()}</div>
    </div>
  </section>

  <section class="section section-cream">
    <div class="container split">
      <div>
        <p class="eyebrow">Service area links</p>
        <h2>Nearby Sun Ray Cleaning pages.</h2>
        <p>These internal links keep the main city, neighborhood, and county pages connected for visitors, Google, and AI-search crawlers.</p>
      </div>
      <div class="info-card"><h3>Related locations</h3><div class="pill-row">{pill_links(page["nearby"])}</div></div>
    </div>
  </section>

  <section class="section section-cream" data-gpt-faq>
    <div class="container">
      <div class="section-head center"><p class="eyebrow">Cleaning FAQs</p><h2>{escape(page["label"])} cleaning questions.</h2></div>
      <div class="faq">{faq_markup(page["faqs"])}</div>
    </div>
  </section>

  <section class="section section-navy cta-band">
    <div class="container">
      <p class="eyebrow">Ready for local cleaning?</p>
      <h2>Get a quote for your {escape(page["label"])} home.</h2>
      <p>Share your city or neighborhood, home size, service type, timing, access notes, and cleaning priorities so Sun Ray can recommend the right plan.</p>
      <div class="cta-actions"><a class="button button-yellow" href="../contact-gpt.html#quote-form" data-open-quote>Get a quote</a><a class="button button-white" href="tel:+18016042189">Call (801) 604-2189</a></div>
    </div>
  </section>
</main>
{footer()}
{quote_modal()}
<script src="../quote-modal-gpt.js"></script>
</body>
</html>
"""


def service_area_hub() -> str:
    summit = [
        ("park-city", "Park City"),
        ("snyderville", "Snyderville"),
        ("deer-valley", "Deer Valley"),
        ("canyons-village", "Canyons Village"),
        ("old-town-park-city", "Old Town Park City"),
        ("kamas", "Kamas"),
        ("oakley", "Oakley"),
        ("coalville", "Coalville"),
    ]
    wasatch = [
        ("heber-city", "Heber City"),
        ("midway", "Midway"),
        ("daniel", "Daniel"),
        ("red-ledges", "Red Ledges"),
        ("jordanelle", "Jordanelle"),
        ("heber-valley", "Heber Valley"),
        ("old-town-heber", "Old Town Heber"),
        ("center-creek", "Center Creek"),
    ]
    all_primary = [
        ("park-city", "Park City"),
        ("snyderville", "Snyderville"),
        ("deer-valley", "Deer Valley"),
        ("canyons-village", "Canyons Village"),
        ("old-town-park-city", "Old Town Park City"),
        ("heber-city", "Heber City"),
        ("midway", "Midway"),
        ("kamas", "Kamas"),
        ("oakley", "Oakley"),
        ("daniel", "Daniel"),
        ("coalville", "Coalville"),
        ("summit-county", "Summit County"),
        ("wasatch-county", "Wasatch County"),
    ]
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="assets/favicon/favicon.ico" sizes="any">
  <link rel="icon" type="image/svg+xml" href="assets/favicon/favicon.svg">
  <link rel="apple-touch-icon" href="assets/favicon/apple-touch-icon.png">
  <link rel="manifest" href="assets/favicon/site.webmanifest">
  <meta name="theme-color" content="#1f3a68">
  <title>Sun Ray Cleaning Service Areas in Summit and Wasatch County</title>
  <meta name="description" content="Sun Ray Cleaning service areas for Park City, Snyderville, Deer Valley, Canyons Village, Old Town Park City, Heber City, Midway, Kamas, Oakley, Daniel, Coalville, Summit County, and Wasatch County.">
  <meta name="robots" content="noindex, follow">
  <meta property="og:title" content="Sun Ray Cleaning Service Areas in Summit and Wasatch County">
  <meta property="og:description" content="Find Sun Ray Cleaning location pages for Park City, Snyderville, Deer Valley, Canyons Village, Old Town Park City, Heber City, Midway, Kamas, Oakley, Daniel, Coalville, Summit County, and Wasatch County.">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="styles-gpt.css">
</head>
<body>
{header("page", "")}
<main>
  <section class="page-hero">
    <div class="container page-hero-grid">
      <div>
        <div class="breadcrumb"><a href="index-gpt.html">Home</a><span>/</span><span>Service areas</span></div>
        <p class="eyebrow">Service areas</p>
        <h1>Sun Ray Cleaning service areas across Summit County and Wasatch County.</h1>
        <p class="lead">Find the right local page for residential cleaning, Airbnb and VRBO turnovers, deep cleaning, recurring cleaning, move cleaning, second-home care, and rural-home cleaning.</p>
        <div class="hero-actions"><a class="button button-yellow" href="contact-gpt.html#quote-form" data-open-quote>Get a quote</a><a class="button button-outline" href="sms:+18016042189">Text (801) 604-2189</a></div>
      </div>
      <div class="page-hero-media"><img src="assets/wasatch-county-residential-family-room-cleaning-sun-ray.jpg" alt="Sun Ray Cleaning residential service area across Summit County and Wasatch County"></div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center"><p class="eyebrow">Primary location pages</p><h2>The requested Sun Ray location set.</h2><p>These are the main city, neighborhood, and county routes for the Cloudflare preview.</p></div>
      <div class="area-list">{area_links(all_primary, "service-location/")}</div>
    </div>
  </section>

  <section class="section section-cream">
    <div class="container grid-2">
      <article class="info-card"><h2>Summit County</h2><p>Park City, Snyderville, Deer Valley, Canyons Village, Old Town Park City, Kamas, Oakley, Coalville, and nearby Summit County homes and rentals.</p><div class="pill-row">{pill_links(summit, "service-location/")}</div></article>
      <article class="info-card"><h2>Wasatch County</h2><p>Heber City, Midway, Daniel, Heber Valley, Red Ledges, Jordanelle, Old Town Heber, Center Creek, and nearby Wasatch County homes.</p><div class="pill-row">{pill_links(wasatch, "service-location/")}</div></article>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center"><p class="eyebrow">Cleaning services</p><h2>Service pages for every location.</h2></div>
      <div class="grid-2"><a class="info-card" href="services/short-term-rental-cleaning-gpt.html"><img class="card-image" src="assets/park-city-airbnb-vrbo-kitchen-island-turnover-cleaning-sun-ray.jpg" alt="Kitchen island cleaned for Airbnb and VRBO turnover service"><h3>Airbnb and VRBO cleaning</h3><p>Guest-ready turnovers for rentals, condos, cabins, and second homes.</p></a><a class="info-card" href="services/deep-cleaning-gpt.html"><img class="card-image" src="assets/summit-county-deep-cleaning-shower-detail-sun-ray.jpg" alt="Shower detail cleaned during a deep cleaning visit"><h3>Deep cleaning</h3><p>Detailed home resets for seasonal dust, kitchens, bathrooms, and buildup.</p></a><a class="info-card" href="services/recurring-cleaning-gpt.html"><img class="card-image" src="assets/midway-recurring-bedroom-cleaning-sun-ray.jpg" alt="Bedroom cleaned for recurring residential cleaning"><h3>Recurring cleaning</h3><p>Weekly, biweekly, and monthly home cleaning plans.</p></a><a class="info-card" href="services/move-in-move-out-cleaning-gpt.html"><img class="card-image" src="assets/wasatch-county-move-in-entry-kitchen-cleaning-sun-ray.jpg" alt="Entry and kitchen cleaned for move-in or move-out cleaning"><h3>Move-in/out cleaning</h3><p>Move-in and move-out cleaning before walkthroughs or unpacking.</p></a></div>
    </div>
  </section>

  <section class="section section-cream" data-gpt-faq>
    <div class="container">
      <div class="section-head center"><p class="eyebrow">Service area FAQs</p><h2>Questions before you request a local cleaning quote.</h2></div>
      <div class="faq"><details><summary>What are Sun Ray Cleaning's main service areas?</summary><div class="answer">Sun Ray Cleaning serves Park City, Snyderville, Deer Valley, Canyons Village, Old Town Park City, Heber City, Midway, Kamas, Oakley, Daniel, Coalville, Summit County, Wasatch County, and nearby mountain communities.</div></details><details><summary>Do all service areas offer the same cleaning services?</summary><div class="answer">Most service areas can request recurring cleaning, deep cleaning, move-in and move-out cleaning, and Airbnb or VRBO turnover cleaning. Final availability depends on schedule, access, scope, and location.</div></details><details><summary>How should I choose the right location page?</summary><div class="answer">Choose the closest city, neighborhood, or county page. If the home is between areas, use the county hub and include the exact address or nearest landmark when requesting a quote.</div></details></div>
    </div>
  </section>

  <section class="section section-navy cta-band">
    <div class="container">
      <p class="eyebrow">Ready for local cleaning?</p>
      <h2>Get a quote for your home.</h2>
      <p>Share your city, neighborhood, home size, service type, timing, pets, and access details so Sun Ray can recommend the right cleaning plan.</p>
      <div class="cta-actions"><a class="button button-yellow" href="contact-gpt.html#quote-form" data-open-quote>Get a quote</a><a class="button button-white" href="tel:+18016042189">Call (801) 604-2189</a></div>
    </div>
  </section>
</main>
{footer("")}
{quote_modal()}
<script src="quote-modal-gpt.js"></script>
</body>
</html>
"""


def main() -> None:
    LOCATION_DIR.mkdir(exist_ok=True)
    for page in PAGES:
        (LOCATION_DIR / f"{page['slug']}-gpt.html").write_text(page_html(page), encoding="utf-8")
    (ROOT / "service-areas-gpt.html").write_text(service_area_hub(), encoding="utf-8")
    print(f"Refreshed {len(PAGES)} location pages and service-areas-gpt.html")


if __name__ == "__main__":
    main()
