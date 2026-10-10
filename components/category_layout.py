"""Shared layout for the category pages. Each category still has its own file in pages/."""
from __future__ import annotations

from html import escape

import streamlit as st

from components.cart_helpers import cart_count
from components.category_card import category_art_html
from components.navbar import CART, HOME
from components.product_card import render_product_grid
from components.ui_helpers import icon, render_html
from data.products import SORT_OPTIONS, get_category, products_in_category, search_products


def render_category_page(slug: str) -> None:
    category = get_category(slug)
    total = len(products_in_category(slug))

    # 1. Breadcrumb: Home > Category
    with st.container(key="crumb"):
        c_home, c_sep, c_here = st.columns([1, 1, 1], vertical_alignment="center")
        with c_home:
            st.page_link(HOME, label="Home", icon=":material/home:")
        with c_sep:
            render_html(f'<span class="crumb-sep">{icon("chevron", 16)}</span>')
        with c_here:
            render_html(f'<span class="crumb-here">{escape(category["name"])}</span>')

    # 2-4. Title, description, banner visual and product count
    render_html(
        f"""
        <section class="cat-banner" style="--c1:{category['c1']};--c2:{category['c2']}">
          <div class="cat-banner-text">
            <h1>{escape(category['name'])}</h1>
            <p>{escape(category['banner'])}</p>
            <span class="pill">{total} products</span>
          </div>
          <div class="cat-banner-art">{category_art_html(category, max_items=3)}</div>
        </section>
        """
    )

    # 5. Search + sort controls
    c_q, c_sort, c_cart = st.columns([3, 2, 1.4], vertical_alignment="bottom")
    with c_q:
        query = st.text_input(
            f"Search in {category['name']}",
            key=f"q_{slug}",
            placeholder=f"Search in {category['name']}",
        )
    with c_sort:
        sort = st.selectbox("Sort by", SORT_OPTIONS, key=f"sort_{slug}")
    with c_cart:
        # 9. Visible cart count
        st.page_link(CART, label=f"Cart ({cart_count()})", icon=":material/shopping_cart:")

    products = search_products(query, category=slug, sort=sort)

    # 6-8. Product grid
    if products:
        shown = f"{len(products)} of {total}" if len(products) != total else f"{total}"
        render_html(f'<p class="result-note">Showing {shown} products</p>')
        render_product_grid(products, ctx=slug)
    else:
        render_html(
            f"""
            <div class="empty">
              <div class="empty-art">{icon("search", 40)}</div>
              <h3>No matches in {escape(category['name'])}</h3>
              <p>Nothing here matches &ldquo;{escape(query)}&rdquo;. Clear the search box to see all {total} products.</p>
            </div>
            """
        )

    # 10. Back to home
    st.page_link(HOME, label="Back to Home", icon=":material/arrow_back:")
