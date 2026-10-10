"""Reusable product card + responsive product grid."""
from __future__ import annotations

from html import escape

import streamlit as st

from components.cart_helpers import add_to_cart, format_inr, qty_in_cart
from components.ui_helpers import icon, local_image_uri, render_html
from data.products import get_category


def product_media_html(product: dict) -> str:
    """Product picture: a local image if one exists, otherwise a tinted emoji tile."""
    category = get_category(product["category"])
    uri = local_image_uri("products", product["id"])
    if uri:
        inner = f'<img src="{uri}" alt="{escape(product["name"])}" loading="lazy">'
    else:
        inner = f'<span class="pc-emoji" role="img" aria-label="{escape(product["name"])}">{product["emoji"]}</span>'
    badge = f'<span class="tag-badge">{product["discount"]}% off</span>' if product["discount"] else ""
    return (
        f'<div class="pc-media" style="--c1:{category["c1"]};--c2:{category["c2"]}">'
        f'{badge}{inner}</div>'
    )


def _card_html(product: dict) -> str:
    mrp = f'<s>{format_inr(product["mrp"])}</s>' if product["mrp"] else ""
    in_cart = qty_in_cart(product["id"])
    in_cart_html = f'<span class="pc-incart">{in_cart} in cart</span>' if in_cart else ""
    return f"""
    {product_media_html(product)}
    <div class="pc-body">
      <div class="pc-name">{escape(product["name"])}</div>
      <div class="pc-unit">{escape(product["unit"])}</div>
      <div class="pc-meta"><span class="pc-rating">{icon("star", 14)}{product["rating"]:.1f}</span>{in_cart_html}</div>
      <div class="pc-price"><strong>{format_inr(product["price"])}</strong>{mrp}</div>
    </div>
    """


def render_product_card(product: dict, ctx: str) -> None:
    with st.container(key=f"card_{ctx}_{product['id']}"):
        render_html(_card_html(product))
        st.button(
            "Add to Cart",
            key=f"add_{ctx}_{product['id']}",
            icon=":material/add_shopping_cart:",
            on_click=add_to_cart,
            args=(product["id"],),
        )


def render_product_grid(products: list[dict], ctx: str) -> None:
    """Render products in a CSS grid whose column count adapts to the screen width."""
    with st.container(key=f"grid_{ctx}"):
        for product in products:
            render_product_card(product, ctx)
