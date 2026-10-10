"""Search results (and the 'shop all groceries' view when the search box is empty)."""
from html import escape

import streamlit as st

from components.product_card import render_product_grid
from components.ui_helpers import icon, render_html
from data.products import (
    CATEGORIES, PRODUCTS, SORT_OPTIONS, category_page_path, get_category, search_products,
)

query = st.session_state.get("nav_search", "").strip()
heading = f"Results for “{escape(query)}”" if query else "Shop all groceries"
render_html(f'<section class="section-head"><h2>{heading}</h2></section>')

names = ["All categories"] + [c["name"] for c in CATEGORIES]
slugs = [None] + [c["slug"] for c in CATEGORIES]
f1, f2 = st.columns(2)
with f1:
    chosen = st.selectbox("Category", names, key="search_category")
with f2:
    sort = st.selectbox("Sort by", SORT_OPTIONS, key="search_sort")

category = slugs[names.index(chosen)]
results = search_products(query, category=category, sort=sort)

if results:
    render_html(f'<p class="result-note">{len(results)} of {len(PRODUCTS)} products</p>')
    # Links to the category pages that contain matches
    found = {}
    for product in results:
        found[product["category"]] = found.get(product["category"], 0) + 1
    render_html('<p class="result-note">Open a category page:</p>')
    with st.container(key="search_cats"):
        cols = st.columns(min(len(found), 4))
        for i, (slug, n) in enumerate(found.items()):
            with cols[i % len(cols)]:
                st.page_link(category_page_path(slug), label=f"{get_category(slug)['name']} ({n})")
    render_product_grid(results, ctx="search")
else:
    render_html(
        f"""
        <div class="empty">
          <div class="empty-art">{icon("search", 40)}</div>
          <h3>No products found</h3>
          <p>We couldn&rsquo;t find &ldquo;{escape(query)}&rdquo;. Check the spelling, try a shorter word like
          &ldquo;milk&rdquo; or &ldquo;rice&rdquo;, or browse a category instead.</p>
        </div>
        """
    )
    st.page_link("pages/categories.py", label="Browse categories", icon=":material/grid_view:")
