import pandas as pd

siteData = {
  "brandName": "Chrisport Venture",
  "contactInfo": {
    "phone": "08102515044",
    "whatsapp": "08102515044",
    "email": "chrisportventure@gmail.com",
  },
  "navigation": [
    { "text": "HOME", "link": "#hero" },
    { "text": "SHOP", "link": "#shop" },
    { "text": "ABOUT US", "link": "#about" },
    { "text": "CONTACT", "link": "#contact" },
  ],
  "heroSection": {
    "title": "VIBERATION MACHINE",
    "subtitle": "THE BEST GYM ALTERNATIVE",
    "description1": "Treadmill is a GREAT piece of equipment.",
    "description2":
      "With so many benefits both Health & Fitness wise, Treadmills have proven to be the BEST fitness equipment anyone can have at home!",
    "tagline": "Best Option For Both Running and Walking.",
  },
  "videoSection": {
    "title": "WATCH VIDEO DEMONSTATION!",
    "videoUrl":
      "https://utfs.io/a/zxzyub6zq2/OX5ramIp6AH47gIhJV3tqloZKxjcWNCdIY0FaAgi8G1mwQkJ",
    "duration": "0:43",
    "description":
      "We have all heard it many times - regular exercise is good for you, and it can help you lose weight. Technology has changed exercise. Fitness equipment manufacturers are constantly innovating new products...",
  },
  "benefits": [
    "WEIGHT LOSS",
    "You Are In Control",
    "Reduced Impact",
    "Mental Health And Motivation",
    "Heart Health",
    "HAVE THE ABILITY TO RUN, NO MATTER THE WEATHER.",
    "Treadmills Are Convenient, Safe, And Private",
    "ALLEVIATE BOREDOM",
  ],
  "guarantee": "100% SATISFACTION GUARANTEED",
  "products": [
    {
      "id": "2HP_PLATFORM",
      "name": "2HP Platform Treadmill",
      "features": ["MP3 Player", "Handle", "Foldable"],
      "maxWeight": "100KG",
      "price": 425000,
      "oldPrice": 500000,
      "imageUrl":
        "https://utfs.io/a/zxzyub6zq2/OX5ramIp6AH4J1iSk5esDzriV8pZ04WKvHgby3wJmAQLMNfn",
      "videoUrl":
        "https://utfs.io/a/zxzyub6zq2/OX5ramIp6AH47gIhJV3tqloZKxjcWNCdIY0FaAgi8G1mwQkJ",
    },
    {
      "id": "2HP_MASSAGER",
      "name": "2HP Treadmill",
      "features": [
        "MP3 Player",
        "Sit Up Bar",
        "Dumbbells (Pair)",
        "Massager",
        "Foldable",
      ],
      "maxWeight": "110KG",
      "price": 525000,
      "oldPrice": 570000,
      "imageUrl":
        "https://utfs.io/a/zxzyub6zq2/OX5ramIp6AH4IVRPSFJaYK7so4ZDkJtpmr2qcdwAMixUOz5S",
      "videoUrl":
        "https://utfs.io/a/zxzyub6zq2/OX5ramIp6AH47gIhJV3tqloZKxjcWNCdIY0FaAgi8G1mwQkJ",
    },
    {
      "id": "2.5HP_MASSAGER",
      "name": "2.5 HP Treadmill",
      "features": [
        "Incline",
        "MP3 Player",
        "Sit Up Bar",
        "Dumbbells (Pair)",
        "Massager",
        "Foldable",
      ],
      "maxWeight": "120KG",
      "price": 750000,
      "oldPrice": 850000,
      "imageUrl":
        "https://utfs.io/a/zxzyub6zq2/OX5ramIp6AH4m9T4msjxbNuayWwsiKnYqShUCRB8VpPEvdk2",
      "videoUrl":
        "https://utfs.io/a/zxzyub6zq2/OX5ramIp6AH47gIhJV3tqloZKxjcWNCdIY0FaAgi8G1mwQkJ",
    },
    {
      "id": "HEAVY_DUTY_LUXURY",
      "name": "Heavy Duty Luxury Treadmill",
      "features": [
        "Auto-Incline",
        "MP3 Player",
        "Sit Up Bar",
        "Dumbbells (Pair)",
        "Massager",
        "Foldable",
      ],
      "maxWeight": "150KG",
      "price": 1850000,
      "oldPrice": 1980000,
      "imageUrl":
        "https://utfs.io/a/zxzyub6zq2/OX5ramIp6AH4l9MVeDbTkd4EFBSyjNXvAmV5YTPRfOcoQa7e",
      "videoUrl":
        "https://utfs.io/a/zxzyub6zq2/OX5ramIp6AH47gIhJV3tqloZKxjcWNCdIY0FaAgi8G1mwQkJ",
    },
    {
      "id": "4HP_SEMI_COMMERCIAL",
      "name": "4 HP Semi Commercial Treadmill",
      "features": [
        "Incline",
        "MP3 Player",
        "Sit Up Bar",
        "Dumbbells (Pair)",
        "Massager",
        "Foldable",
      ],
      "maxWeight": "150KG",
      "price": 1200000,
      "oldPrice": 1300000,
      "imageUrl":
        "https://utfs.io/a/zxzyub6zq2/OX5ramIp6AH4O0bTxTIp6AH4m8g2W7DMkbYQirLUe9qXvSfc",
      "videoUrl":
        "https://utfs.io/a/zxzyub6zq2/OX5ramIp6AH47gIhJV3tqloZKxjcWNCdIY0FaAgi8G1mwQkJ",
    },
    {
      "id": "BIG_HEAVY_DUTY_LUXURY",
      "name": "Big Heavy Duty Luxury Treadmill",
      "features": [
        "Auto-Incline",
        "MP3 Player",
        "Massager",
        "Foldable",
        "Extra Durable Frame",
      ],
      "maxWeight": "180KG",
      "price": 5470000,
      "oldPrice": None,
      "imageUrl":
        "https://utfs.io/a/zxzyub6zq2/OX5ramIp6AH4J1iSk5esDzriV8pZ04WKvHgby3wJmAQLMNfn",
      "videoUrl":
        "https://utfs.io/a/zxzyub6zq2/OX5ramIp6AH47gIhJV3tqloZKxjcWNCdIY0FaAgi8G1mwQkJ",
    },
  ],
  "deliveryInfo": {
    "headline": "FREE DELIVERY WHEN YOU ORDER NOW",
    "paymentInfo": "NATIONWIDE PAYMENT ON DELIVERY AVAILABLE",
    "timelines":
      "DELIVERY TO LAGOS STATE WITHIN 24HRS, OTHER STATES WITHIN 3-5 DAYS (Or Less)",
    "offerHeadline": "ORDER NOW AND ENJOY:",
    "offers": [
      "PROMO PRICE",
      "PAYMENT ON DELIVERY",
      "QUICK DELIVERY",
      "FREE DELIVERY",
      "FREE INSTALLATION",
      "1 YEAR WARRANTY",
    ],
    "importantNote": "ONLY PLACE ORDER IF YOU ARE READY FOR DELIVERY & PAYMENT",
  },
  "testimonials": [
    {
      "quote":
        "The fact that this treadmill has virtually all the exercise functions in 1 is stunning. Very wonderful machine! It's better than running on the road. Thats why i bought it, and it's serving it's purpose very well",
      "author": "Capt. Isreal",
      "location": "Warri, Delta",
    },
    {
      "quote":
        "This treadmill is more than what i expected. I bought the 2.5HP and it's amazing what it has done for me and my health status. Thank you so much for helping me improve the quality of my life.",
      "author": "Joshua Enendu",
      "location": "Abuja",
    },
    {
      "quote":
        "Very lovely customer service. The delivery and set up went fine and so far, everything is going great!",
      "author": "Mrs Bunmi",
      "location": "Ajao est. Lagos",
    },
    {
      "quote":
        "I love the TREADMILL MACHINE. I bought it last month. They delivered it right to my office, and even set it up and took time to show me how to use it. Easiest online purchase ever. Although I ordered through whatsapp.",
      "author": "Mr Dayo",
      "location": "Akure, Ondo",
    },
    {
      "quote":
        '"I love the TREADMILL MACHINE. I bought it last month. They delivered it right to my ofce, and even set it up and took time to show me how to use it. Easiest online purchase ever. Although I ordered through whatsapp."',
      "author": "Aladi U.S",
      "location": "Abuja",
    },
  ],
  "customerCount": 3731,
  "footer": {
    "usefulLinks": [
      { "text": "Home", "link": "#hero" },
      { "text": "Shop", "link": "#shop" },
      { "text": "About Us", "link": "#about" },
      { "text": "Contact Us", "link": "#contact" },
    ],
    "legalLinks": [
      { "text": "Terms Of Service", "link": "#terms" },
      { "text": "Privacy Policy", "link": "#privacy" },
      { "text": "Disclaimer", "link": "#disclaimer" },
    ],
    "facebookDisclaimer":
      "This site is not a part of the Facebook™ website or Facebook™ Inc. Additionally, this site is NOT endorsed by Facebook™ in any way. FACEBOOK™ is a trademark of FACEBOOK™, Inc.",
    "copyright": "Copyright © 2025 Chrisport Venture",
    "designer": "DESIGNED BY: Aus TI NE",
  },
}

# Create a Pandas Excel writer using XlsxWriter as the engine.
excel_file_path = "/tmp/chrisport_venture_data.xlsx"
writer = pd.ExcelWriter(excel_file_path, engine='xlsxwriter')

# Sheet 1: General Info
general_info_data = {
    "Brand Name": [siteData["brandName"]],
    "Phone": [siteData["contactInfo"]["phone"]],
    "WhatsApp": [siteData["contactInfo"]["whatsapp"]],
    "Email": [siteData["contactInfo"]["email"]],
    "Guarantee": [siteData["guarantee"]],
    "Customer Count": [siteData["customerCount"]]
}
df_general_info = pd.DataFrame(general_info_data)
df_general_info.to_excel(writer, sheet_name='General_Info', index=False)

# Sheet 2: Navigation
df_navigation = pd.DataFrame(siteData["navigation"])
df_navigation.to_excel(writer, sheet_name='Navigation', index=False)

# Sheet 3: Hero Section
df_hero_section = pd.DataFrame([siteData["heroSection"]])
df_hero_section.to_excel(writer, sheet_name='Hero_Section', index=False)

# Sheet 4: Video Section
df_video_section = pd.DataFrame([siteData["videoSection"]])
df_video_section.to_excel(writer, sheet_name='Video_Section', index=False)

# Sheet 5: Benefits
df_benefits = pd.DataFrame(siteData["benefits"], columns=["Benefit"])
df_benefits.to_excel(writer, sheet_name='Benefits', index=False)

# Sheet 6: Products
# Flattening product features for better representation in Excel
products_data = []
for product in siteData["products"]:
    product_copy = product.copy()
    product_copy["features"] = ", ".join(product_copy["features"]) # Join features into a single string
    products_data.append(product_copy)
df_products = pd.DataFrame(products_data)
df_products.to_excel(writer, sheet_name='Products', index=False)


# Sheet 7: Delivery Info
delivery_info_data = {
    "Headline": [siteData["deliveryInfo"]["headline"]],
    "Payment Info": [siteData["deliveryInfo"]["paymentInfo"]],
    "Timelines": [siteData["deliveryInfo"]["timelines"]],
    "Offer Headline": [siteData["deliveryInfo"]["offerHeadline"]],
    "Offers": [", ".join(siteData["deliveryInfo"]["offers"])], # Join offers into a single string
    "Important Note": [siteData["deliveryInfo"]["importantNote"]]
}
df_delivery_info = pd.DataFrame(delivery_info_data)
df_delivery_info.to_excel(writer, sheet_name='Delivery_Info', index=False)


# Sheet 8: Testimonials
df_testimonials = pd.DataFrame(siteData["testimonials"])
df_testimonials.to_excel(writer, sheet_name='Testimonials', index=False)

# Sheet 9: Footer
footer_data = {
    "Facebook Disclaimer": [siteData["footer"]["facebookDisclaimer"]],
    "Copyright": [siteData["footer"]["copyright"]],
    "Designer": [siteData["footer"]["designer"]]
}
df_footer_info = pd.DataFrame(footer_data)
df_footer_info.to_excel(writer, sheet_name='Footer_Info', index=False)

df_footer_useful_links = pd.DataFrame(siteData["footer"]["usefulLinks"])
df_footer_useful_links.to_excel(writer, sheet_name='Footer_Useful_Links', index=False)

df_footer_legal_links = pd.DataFrame(siteData["footer"]["legalLinks"])
df_footer_legal_links.to_excel(writer, sheet_name='Footer_Legal_Links', index=False)


# Close the Pandas Excel writer and output the Excel file.
writer.close()

print(f"Excel file created at: {excel_file_path}")