"""Announcement bar + navigation bar rendered once by app.py on every page."""
from __future__ import annotations

import streamlit as st

from components.cart_helpers import cart_count
from components.ui_helpers import icon, render_html

HOME = "pages/home.py"
CATEGORIES = "pages/categories.py"
CART = "pages/cart.py"
CHECKOUT = "pages/checkout.py"
SEARCH = "pages/search.py"


def logo_html(light: bool = False) -> str:
    tone = " logo-light" if light else ""
    return f"""
    <div class="logo{tone}">
      <span class="logo-mark">{icon("basket", 22)}</span>
      <span class="logo-text">EASE<span>martzzz</span></span>
    </div>
    """


def _request_search() -> None:
    # st.switch_page cannot run inside a callback, so app.py acts on this flag.
    st.session_state["go_search"] = True


def render_navbar() -> None:
    render_html(
        f'<div class="announce">{icon("tag", 15)}'
        "Fresh picks, happy prices: make every grocery run easier!</div>"
    )
    count = cart_count()
    with st.container(key="navbar"):
        c_logo, c_search, c_home, c_cats, c_orders, c_cart, c_user = st.columns(
            [2.2, 3.4, 1.3, 1.8, 1.4, 1.7, 0.5], vertical_alignment="center"
        )
        with c_logo:
            with st.container(key="logo"):
                render_html(logo_html())
                st.page_link(HOME, label="EASEmartzzz home")
        with c_search:
            st.text_input(
                "Search products",
                key="nav_search",
                placeholder="Search milk, mangoes, atta...",
                label_visibility="collapsed",
                on_change=_request_search,
            )
        with c_home:
            st.page_link(HOME, label="Home", icon=":material/home:")
        with c_cats:
            st.page_link(CATEGORIES, label="Categories", icon=":material/grid_view:")
        with c_orders:
            st.page_link(CHECKOUT, label="Orders", icon=":material/receipt_long:")
        with c_cart:
            with st.container(key="cartlink"):
                st.page_link(CART, label=f"Cart ({count})", icon=":material/shopping_cart:")
        with c_user:
            # Visual only: this demo has no login.
            render_html(f'<div class="avatar" title="Profile (demo only)">{icon("user", 20)}</div>')
