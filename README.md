# EASEmartzzz

A modern grocery shopping website demo built with **Python + Streamlit + HTML + CSS**.
Fresh groceries, easy shopping.

> **This is a frontend demonstration.** There is no database, no payment gateway, no real login,
> no API key and no backend. Products are sample data and prices are not live market prices.

## Features

- Homepage: announcement bar, navbar with live cart count, hero banner, 12 category cards, "Popular Picks", special offer banner, footer
- **12 separate category pages** (one file each) with breadcrumb, banner, search box, sorting and a responsive product grid
- Local product search (by product name) with sorting and "no results" help
- Temporary cart (add, increase, decrease, remove, clear, per-item subtotal, total)
- Demo checkout with a sample address form and a fake order number
- Responsive layout for desktop, tablet and mobile

## Project structure

```
EASEmartzzz/
├── app.py                      # Entry point: page config, navigation, navbar, footer
├── requirements.txt
├── README.md
├── .streamlit/config.toml      # Light theme and hidden sidebar navigation
├── data/
│   └── products.py             # All categories and products (plain Python)
├── components/
│   ├── navbar.py               # Announcement bar, logo, search, links, cart count
│   ├── footer.py
│   ├── product_card.py         # Product card + responsive grid
│   ├── category_card.py        # Category card + grid
│   ├── category_layout.py      # Shared layout used by every category page
│   ├── cart_helpers.py         # Cart logic in st.session_state
│   └── ui_helpers.py           # CSS loading, inline icons, image fallbacks
├── pages/
│   ├── home.py  categories.py  search.py  cart.py  checkout.py
│   └── fruits.py vegetables.py meat_seafood.py bakery.py dairy_eggs.py snacks.py
│       beverages.py frozen_foods.py rice_pulses_grains.py personal_care.py
│       household_essentials.py spices_condiments.py
└── assets/
    ├── css/style.css           # All styling
    └── images/{logo,categories,products}/   # Optional images (see below)
```

All pages are registered in one place, `app.py`, with `st.Page` and `st.navigation`.

## Installation

You need Python 3.9 or newer.

```bash
python -m pip install -r requirements.txt
```

## Launch

```bash
streamlit run app.py
```

Then open the address Streamlit prints (normally http://localhost:8501).

## How to edit product names and prices

Open `data/products.py` and find `RAW_PRODUCTS`. Each row is:

```python
("Royal Gala Apples", 160, 190, "1 kg", 4.5, "🍎")
#  name              price mrp  unit    rating emoji
```

- `price` is the selling price in rupees.
- `mrp` is the original price. Use `None` for no discount (the discount badge is calculated automatically).
- Save the file; Streamlit reloads the page.

To change the "Popular Picks" on the homepage, edit `POPULAR_IDS`.
A product id is `<category slug>-<row number starting at 1>`, for example `fruits-1`.

### Using real product pictures (optional)

If a file named after the product id exists, it is used instead of the emoji tile:
`assets/images/products/fruits-1.png` (also `.jpg`, `.jpeg`, `.webp`, `.svg`).
Category pictures work the same way: `assets/images/categories/fruits.png`.
Missing images are fine; the emoji tile is the fallback.

## How to add a new grocery category

1. In `data/products.py`, add an entry to `CATEGORIES`, for example:
   ```python
   {"slug": "pet_care", "name": "Pet Care", "description": "Food and treats.",
    "banner": "Everyday essentials for pets.", "c1": "#E8F5D0", "c2": "#CFE8A0"},
   ```
2. Add its products to `RAW_PRODUCTS` under the same slug:
   ```python
   "pet_care": [("Dog Biscuits", 140, 160, "500 g", 4.3, "🦴"), ...],
   ```
3. Create `pages/pet_care.py` (the file name must equal the slug):
   ```python
   from components.category_layout import render_category_page

   render_category_page("pet_care")
   ```
4. Register the page in `app.py`. Categories are added automatically because `app.py`
   loops over `CATEGORIES`, so no change is needed there.

The homepage card and footer link appear automatically.

## Demonstration-only features

| Feature | What it really does |
| --- | --- |
| Cart | Lives in `st.session_state`; refreshing the browser tab empties it |
| Checkout | Shows a fake order number and summary; no payment, no order, no delivery |
| Orders | Lists demo orders from the current browser session only |
| Profile icon | Visual only; there is no login |
| Prices and products | Sample values; not real stock or market prices |
| Footer contact details | Placeholders |

## Notes for students

- Navigation uses `st.navigation(..., position="hidden")` plus our own navbar, built from
  `st.page_link`. Using Streamlit's own links (instead of plain HTML links) keeps the cart
  alive while moving between pages.
- Cart buttons use `on_click` callbacks so the cart count in the navbar updates immediately.
- Icons: inline Lucide-style SVGs in the HTML, and Material icons on Streamlit buttons and links.
  Both are outline icon sets and nothing is loaded from a CDN. Only the Google Fonts stylesheet
  is fetched online; if it is blocked, the CSS falls back to system fonts.
