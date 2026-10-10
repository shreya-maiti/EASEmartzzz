"""Homepage: hero, categories, popular picks and the special offer."""
import streamlit as st

from components.category_card import render_category_grid
from components.navbar import CATEGORIES, SEARCH
from components.product_card import render_product_grid
from components.ui_helpers import icon, render_html
from data.products import category_page_path, popular_products

# ---- Hero -------------------------------------------------------------------
with st.container(key="hero"):
    left, right = st.columns([1.15, 1], vertical_alignment="center")
    with left:
        render_html(
            f"""
            <span class="hero-badge">{icon("tag", 15)}Fresh deals this week</span>
            <h1 class="hero-title">Your everyday essentials, delivered to your screen.</h1>
            <p class="hero-sub">Discover fresh produce, pantry favourites, dairy essentials,
            and everyday groceries, all in one easy place.</p>
            """
        )
        b1, b2 = st.columns(2)
        with b1:
            with st.container(key="hero_cta1"):
                st.page_link(SEARCH, label="Explore Groceries", icon=":material/storefront:")
        with b2:
            with st.container(key="hero_cta2"):
                st.page_link(CATEGORIES, label="Browse Categories", icon=":material/grid_view:")
    with right:
        render_html(
            """
            <div class="hero-art" aria-hidden="true">
              <div class="hero-blob"></div>
              <span class="hb hb1">🍅</span><span class="hb hb2">🥛</span>
              <span class="hb hb3">🍞</span><span class="hb hb4">🥭</span>
              <span class="hb hb5">🥕</span><span class="hb hb6">🍚</span>
              <div class="hero-tag"><small>Mangoes from</small><b>₹140</b><small>per kg</small></div>
            </div>
            """
        )

# ---- Shop by category -----------------------------------------------------------
render_html(
    """
    <section class="section-head">
      <h2>Shop by category</h2>
      <p>Twelve aisles, each with its own page.</p>
    </section>
    """
)
render_category_grid(ctx="home")

# ---- Popular picks ---------------------------------------------------------------
render_html(
    """
    <section class="section-head">
      <h2>Popular Picks</h2>
      <p>What other shoppers are adding to their carts. Sample prices for demonstration.</p>
    </section>
    """
)
render_product_grid(popular_products(), ctx="popular")

# ---- Special offer -----------------------------------------------------------------
with st.container(key="offer"):
    o_text, o_art = st.columns([1.6, 1], vertical_alignment="center")
    with o_text:
        render_html(
            """
            <h2 class="offer-title">Stock up on goodness. Save on your favourites.</h2>
            <p class="offer-sub">Rice, atta, dals and oats at pantry-friendly prices.</p>
            """
        )
        with st.container(key="offer_cta"):
            st.page_link(
                category_page_path("rice_pulses_grains"),
                label="Shop pantry staples",
                icon=":material/arrow_forward:",
            )
    with o_art:
        render_html('<div class="offer-art" aria-hidden="true">🍚 🌾 🍛 🥣</div>')
