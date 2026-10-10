"""Static sample data for EASEmartzzz.

Everything here is demonstration data (not live market prices).
To edit a product, change its row in RAW_PRODUCTS. To add a category, see README.md.
"""
from __future__ import annotations

# --------------------------------------------------------------------------
# Categories. `slug` must match the page file name in pages/ (pages/<slug>.py)
# --------------------------------------------------------------------------
CATEGORIES = [
    {"slug": "fruits", "name": "Fruits",
     "description": "Seasonal, juicy and ready to eat.",
     "banner": "Orchard-fresh fruit for breakfast bowls, lunchboxes and snacking.",
     "c1": "#FFE3D3", "c2": "#FFC9A8"},
    {"slug": "vegetables", "name": "Vegetables",
     "description": "Crisp greens and kitchen staples.",
     "banner": "Everyday vegetables, from curry bases to salad crunch.",
     "c1": "#DDF3C4", "c2": "#B9E48A"},
    {"slug": "meat_seafood", "name": "Meat & Seafood",
     "description": "Cleaned, cut and ready to cook.",
     "banner": "Fresh cuts of chicken, mutton, fish and shellfish.",
     "c1": "#FFD9D4", "c2": "#FFB5AA"},
    {"slug": "bakery", "name": "Bakery",
     "description": "Breads, buns and sweet treats.",
     "banner": "Soft loaves, flaky pastries and cookies for tea time.",
     "c1": "#FBE7C0", "c2": "#F5CE86"},
    {"slug": "dairy_eggs", "name": "Dairy & Eggs",
     "description": "Milk, curd, paneer, butter and eggs.",
     "banner": "Daily dairy and farm eggs for every kitchen.",
     "c1": "#DCEBFA", "c2": "#B7D3F2"},
    {"slug": "snacks", "name": "Snacks",
     "description": "Crunchy, salty and sweet bites.",
     "banner": "Munchies for movie nights, commutes and cravings.",
     "c1": "#FFF0B8", "c2": "#FFDF6E"},
    {"slug": "beverages", "name": "Beverages",
     "description": "Juices, coffee, tea and cold drinks.",
     "banner": "Something to sip, hot or chilled.",
     "c1": "#D5F0EC", "c2": "#A6E0D8"},
    {"slug": "frozen_foods", "name": "Frozen Foods",
     "description": "Quick meals and frozen favourites.",
     "banner": "Freezer-aisle shortcuts for busy evenings.",
     "c1": "#E0E7FF", "c2": "#BFCBFA"},
    {"slug": "rice_pulses_grains", "name": "Rice, Pulses & Grains",
     "description": "Pantry staples in family packs.",
     "banner": "Rice, atta, dals and oats to stock the pantry.",
     "c1": "#F2E8CF", "c2": "#E3D0A0"},
    {"slug": "personal_care", "name": "Personal Care",
     "description": "Skin, hair and daily hygiene.",
     "banner": "Everyday care products for the whole family.",
     "c1": "#F3DDF5", "c2": "#E2B9E8"},
    {"slug": "household_essentials", "name": "Household Essentials",
     "description": "Cleaning and home basics.",
     "banner": "Cleaners, detergents and home basics.",
     "c1": "#D9EEF7", "c2": "#AFDAEC"},
    {"slug": "spices_condiments", "name": "Spices & Condiments",
     "description": "Masalas, salt, sauces and more.",
     "banner": "Ground spices and sauces that make the meal.",
     "c1": "#FFD8C2", "c2": "#FFB48C"},
]

# --------------------------------------------------------------------------
# Products: (name, price in INR, original price or None, unit, rating, emoji)
# --------------------------------------------------------------------------
RAW_PRODUCTS = {
    "fruits": [
        ("Royal Gala Apples", 160, 190, "1 kg", 4.5, "🍎"),
        ("Robusta Bananas", 56, 64, "1 dozen", 4.4, "🍌"),
        ("Seedless Green Grapes", 99, 120, "500 g", 4.3, "🍇"),
        ("Nagpur Oranges", 89, None, "1 kg", 4.2, "🍊"),
        ("Banganapalli Mangoes", 140, 169, "1 kg", 4.6, "🥭"),
        ("Strawberries", 120, 150, "250 g", 4.1, "🍓"),
        ("Watermelon", 60, None, "1 piece (about 2 kg)", 4.0, "🍉"),
    ],
    "vegetables": [
        ("Fresh Tomatoes", 38, 45, "1 kg", 4.3, "🍅"),
        ("Carrots", 52, 60, "500 g", 4.4, "🥕"),
        ("Potatoes", 34, None, "1 kg", 4.2, "🥔"),
        ("Onions", 42, 48, "1 kg", 4.3, "🧅"),
        ("Spinach Bunch", 25, None, "250 g", 4.5, "🥬"),
        ("Sweet Corn", 30, 36, "2 pieces", 4.1, "🌽"),
        ("Cucumber", 28, None, "500 g", 4.0, "🥒"),
        ("Brinjal", 40, 46, "500 g", 4.0, "🍆"),
    ],
    "meat_seafood": [
        ("Chicken Curry Cut", 220, 249, "500 g", 4.5, "🍗"),
        ("Mutton Curry Cut", 520, 580, "500 g", 4.4, "🥩"),
        ("Rohu Fish Cuts", 260, 290, "500 g", 4.2, "🐟"),
        ("Tiger Prawns, Cleaned", 399, 449, "250 g", 4.6, "🦐"),
        ("Boneless Chicken Breast", 290, 330, "500 g", 4.5, "🍗"),
        ("Seer Fish Steaks", 450, None, "500 g", 4.3, "🐟"),
        ("Fresh Crab", 380, 420, "500 g", 4.1, "🦀"),
    ],
    "bakery": [
        ("Whole Wheat Bread", 45, 50, "400 g", 4.4, "🍞"),
        ("Butter Croissants", 90, 110, "2 pieces", 4.5, "🥐"),
        ("Multigrain Baguette", 70, None, "1 piece", 4.2, "🥖"),
        ("Chocolate Muffins", 120, 140, "Pack of 2", 4.6, "🧁"),
        ("Oatmeal Cookies", 85, 99, "200 g", 4.3, "🍪"),
        ("Plain Bagels", 95, None, "Pack of 4", 4.1, "🥯"),
        ("Glazed Doughnuts", 150, 180, "4 pieces", 4.4, "🍩"),
    ],
    "dairy_eggs": [
        ("Toned Milk", 58, 62, "1 litre", 4.5, "🥛"),
        ("Farm Fresh Eggs", 84, 96, "12 pieces", 4.6, "🥚"),
        ("Cheddar Cheese Block", 195, 220, "200 g", 4.4, "🧀"),
        ("Salted Butter", 58, 64, "100 g", 4.7, "🧈"),
        ("Fresh Curd", 52, None, "400 g", 4.3, "🥣"),
        ("Paneer", 98, 110, "200 g", 4.5, "🧀"),
        ("Greek Yogurt", 65, 75, "400 g", 4.2, "🥣"),
    ],
    "snacks": [
        ("Salted Popcorn", 40, 50, "100 g", 4.2, "🍿"),
        ("Baked Pretzels", 75, None, "150 g", 4.0, "🥨"),
        ("Dark Chocolate Bar", 120, 140, "100 g", 4.6, "🍫"),
        ("Rice Crackers", 60, 70, "100 g", 4.1, "🍘"),
        ("Roasted Peanuts", 70, 80, "200 g", 4.3, "🥜"),
        ("Potato Chips, Classic", 20, None, "52 g", 4.4, "🍟"),
        ("Namkeen Mixture", 95, 110, "400 g", 4.5, "🍘"),
    ],
    "beverages": [
        ("Orange Juice", 110, 125, "1 litre", 4.2, "🧃"),
        ("Filter Coffee Powder", 240, 270, "500 g", 4.7, "☕"),
        ("Cola", 40, None, "750 ml", 4.0, "🥤"),
        ("Green Tea Bags", 150, 175, "25 bags", 4.3, "🍵"),
        ("Packaged Drinking Water", 20, None, "1 litre", 4.1, "💧"),
        ("Tender Coconut Water", 40, 45, "200 ml", 4.4, "🥥"),
        ("Peach Iced Tea", 45, 50, "500 ml", 4.0, "🥤"),
    ],
    "frozen_foods": [
        ("French Fries", 130, 150, "420 g", 4.3, "🍟"),
        ("Margherita Pizza", 249, 299, "1 piece", 4.2, "🍕"),
        ("Vanilla Ice Cream", 210, 240, "700 ml", 4.6, "🍦"),
        ("Veg Momos", 140, 160, "10 pieces", 4.4, "🥟"),
        ("Frozen Sweet Corn", 90, 105, "500 g", 4.1, "🌽"),
        ("Frozen Broccoli Florets", 110, None, "400 g", 4.0, "🥦"),
        ("Chicken Nuggets", 260, 299, "400 g", 4.3, "🍗"),
    ],
    "rice_pulses_grains": [
        ("Basmati Rice", 120, 140, "1 kg", 4.6, "🍚"),
        ("Whole Wheat Atta", 265, 290, "5 kg", 4.5, "🌾"),
        ("Toor Dal", 165, 180, "1 kg", 4.4, "🍛"),
        ("Moong Dal", 130, 145, "1 kg", 4.3, "🍛"),
        ("Rolled Oats", 175, 199, "1 kg", 4.4, "🥣"),
        ("Thick Poha", 55, None, "500 g", 4.2, "🍚"),
        ("Kabuli Chana", 110, 125, "1 kg", 4.3, "🍛"),
    ],
    "personal_care": [
        ("Herbal Shampoo", 180, 210, "340 ml", 4.3, "🧴"),
        ("Bathing Soap", 140, 160, "Pack of 5", 4.4, "🧼"),
        ("Fluoride Toothpaste", 95, 105, "200 g", 4.5, "🪥"),
        ("Razor Pack", 150, None, "Pack of 3", 4.1, "🪒"),
        ("Gentle Face Wash", 160, 190, "100 ml", 4.2, "🧴"),
        ("Body Lotion", 250, 290, "400 ml", 4.3, "🧴"),
        ("Facial Tissues", 80, 90, "100 pulls", 4.0, "🧻"),
    ],
    "household_essentials": [
        ("Dishwash Liquid", 110, 125, "750 ml", 4.4, "🧽"),
        ("Floor Cleaner", 180, 200, "1 litre", 4.3, "🧹"),
        ("Laundry Detergent", 420, 480, "2 kg", 4.5, "🧺"),
        ("Garbage Bags", 99, 120, "30 pieces", 4.1, "🗑️"),
        ("Kitchen Towel Rolls", 140, None, "Pack of 2", 4.2, "🧻"),
        ("Scrub Sponges", 60, 70, "Pack of 3", 4.0, "🧽"),
        ("Toilet Cleaner", 95, 110, "500 ml", 4.2, "🧴"),
    ],
    "spices_condiments": [
        ("Red Chilli Powder", 78, 90, "200 g", 4.4, "🌶️"),
        ("Turmeric Powder", 62, 70, "200 g", 4.5, "🌿"),
        ("Garam Masala", 85, None, "100 g", 4.6, "🥘"),
        ("Iodised Salt", 28, None, "1 kg", 4.3, "🧂"),
        ("Black Pepper", 120, 140, "100 g", 4.4, "🌶️"),
        ("Cumin Seeds", 95, 110, "200 g", 4.3, "🌿"),
        ("Tomato Ketchup", 130, 150, "950 g", 4.2, "🍅"),
    ],
}

# Product ids are "<category slug>-<position starting at 1>".
POPULAR_IDS = [
    "fruits-1", "vegetables-1", "dairy_eggs-2", "bakery-2",
    "beverages-2", "snacks-3", "rice_pulses_grains-1", "meat_seafood-1",
]

SORT_OPTIONS = ["Relevance", "Price: low to high", "Price: high to low", "Top rated"]


def _build_products():
    products = []
    for slug, rows in RAW_PRODUCTS.items():
        for i, (name, price, mrp, unit, rating, emoji) in enumerate(rows, start=1):
            discount = round((mrp - price) * 100 / mrp) if mrp and mrp > price else 0
            products.append({
                "id": f"{slug}-{i}", "category": slug, "name": name,
                "price": price, "mrp": mrp if discount else None,
                "discount": discount, "unit": unit, "rating": rating, "emoji": emoji,
            })
    return products


PRODUCTS = _build_products()
_PRODUCT_INDEX = {p["id"]: p for p in PRODUCTS}
_CATEGORY_INDEX = {c["slug"]: c for c in CATEGORIES}


def get_product(product_id):
    return _PRODUCT_INDEX.get(product_id)


def get_category(slug):
    return _CATEGORY_INDEX[slug]


def category_page_path(slug):
    return f"pages/{slug}.py"


def products_in_category(slug):
    return [p for p in PRODUCTS if p["category"] == slug]


def popular_products():
    return [_PRODUCT_INDEX[i] for i in POPULAR_IDS if i in _PRODUCT_INDEX]


def search_products(query="", category=None, sort="Relevance"):
    """Local, case-insensitive search by product name (and category name)."""
    items = PRODUCTS if category in (None, "", "all") else products_in_category(category)
    tokens = query.lower().split()
    results = []
    for p in items:
        haystack = f"{p['name']} {_CATEGORY_INDEX[p['category']]['name']}".lower()
        if all(t in haystack for t in tokens):
            position = p["name"].lower().find(tokens[0]) if tokens else 0
            results.append((position if position >= 0 else 999, p))
    if sort == "Price: low to high":
        results.sort(key=lambda r: r[1]["price"])
    elif sort == "Price: high to low":
        results.sort(key=lambda r: -r[1]["price"])
    elif sort == "Top rated":
        results.sort(key=lambda r: -r[1]["rating"])
    else:
        results.sort(key=lambda r: r[0])
    return [p for _, p in results]
