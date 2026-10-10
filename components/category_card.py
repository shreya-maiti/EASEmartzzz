"""Reusable category card (whole card is a link to its own page) and grid."""
from __future__ import annotations

from html import escape

import streamlit as st

from data.products import CATEGORIES, category_page_path, products_in_category
from components.ui_helpers import local_image_uri, render_html


def category_art_html(category: dict, max_items: int = 3) -> str:
    """Category picture: local image if present, else a cluster of product emoji."""
    uri = local_image_uri("categories", category["slug"])
    if uri:
        return f'<img class="cc-img" src="{uri}" alt="{escape(category["name"])}" loading="lazy">'
    emojis = []
    for product in products_in_category(category["slug"]):
        if product["emoji"] not in emojis:
            emojis.append(product["emoji"])
        if len(emojis) == max_items:
            break
    spans = "".join(f'<span class="cc-e cc-e{i}">{e}</span>' for i, e in enumerate(emojis, start=1))
    return f'<div class="cc-emojis" aria-hidden="true">{spans}</div>'


def render_category_card(category: dict, ctx: str = "home") -> None:
    count = len(products_in_category(category["slug"]))
    with st.container(key=f"cat_{ctx}_{category['slug']}"):
        render_html(f"""
        <div class="cc" style="--c1:{category['c1']};--c2:{category['c2']}">
          <div class="cc-art">{category_art_html(category)}</div>
          <div class="cc-name">{escape(category['name'])}</div>
          <div class="cc-desc">{escape(category['description'])}</div>
          <div class="cc-count">{count} items</div>
        </div>
        """)
        # Invisible link stretched over the card by CSS (.st-key-cat_* rules).
        st.page_link(category_page_path(category["slug"]), label=f"Open {category['name']}")


def render_category_grid(ctx: str = "home") -> None:
    with st.container(key=f"catgrid_{ctx}"):
        for category in CATEGORIES:
            render_category_card(category, ctx)
