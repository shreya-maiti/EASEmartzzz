"""Site footer with brand blurb, quick links, category links and contact placeholder."""
from __future__ import annotations

from datetime import datetime

import streamlit as st

from components.navbar import CART, CATEGORIES, CHECKOUT, HOME, SEARCH, logo_html
from components.ui_helpers import icon, render_html
from data.products import CATEGORIES as CATEGORY_LIST
from data.products import category_page_path


def render_footer() -> None:
    with st.container(key="footer"):
        c_brand, c_quick, c_cats, c_contact = st.columns([2.2, 1.3, 2.4, 1.8])
        with c_brand:
            render_html(logo_html(light=True))
            render_html(
                '<p class="ft-text">Fresh groceries, easy shopping'
                "</p>"
            )
        with c_quick:
            render_html('<div class="ft-title">Quick links</div>')
            st.page_link(HOME, label="Home")
            st.page_link(CATEGORIES, label="All categories")
            st.page_link(SEARCH, label="Shop all groceries")
            st.page_link(CART, label="My cart")
            st.page_link(CHECKOUT, label="Checkout and orders")
        with c_cats:
            render_html('<div class="ft-title">Shop by category</div>')
            left, right = st.columns(2)
            half = (len(CATEGORY_LIST) + 1) // 2
            for column, group in ((left, CATEGORY_LIST[:half]), (right, CATEGORY_LIST[half:])):
                with column:
                    for category in group:
                        st.page_link(category_page_path(category["slug"]), label=category["name"])
        with c_contact:
            render_html(
                f"""
                <div class="ft-title">Contact (placeholder)</div>
                <p class="ft-text">{icon("mail", 16)} help@easemartzzz.com</p>
                <p class="ft-text">{icon("phone", 16)} +91 808189xxxx</p>
                <p class="ft-text">{icon("pin", 16)} SRM University, Chennai</p>
                """
            )
        render_html(
            f'<div class="ft-legal">&copy; {datetime.now().year} EASEmartzzz. '
            "</div>"
        )
