"""

Run with:  streamlit run app.py

This file configures navigation centrally. Every page in pages/ is registered
here, and the navbar and footer are drawn around whichever page is active.
"""
import streamlit as st

# set_page_config must be the first Streamlit command.
st.set_page_config(
    page_title="EASEmartzzz | Fresh groceries, easy shopping",
    page_icon=":material/shopping_basket:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from components.cart_helpers import init_state  # noqa: E402
from components.footer import render_footer  # noqa: E402
from components.navbar import render_navbar  # noqa: E402
from components.ui_helpers import load_css  # noqa: E402
from data.products import CATEGORIES  # noqa: E402

load_css()
init_state()

pages = [
    st.Page("pages/home.py", title="Home", icon=":material/home:", default=True),
    st.Page("pages/categories.py", title="All Categories", icon=":material/grid_view:"),
]
pages += [
    st.Page(f"pages/{c['slug']}.py", title=c["name"], icon=":material/category:")
    for c in CATEGORIES
]
pages += [
    st.Page("pages/search.py", title="Search", icon=":material/search:"),
    st.Page("pages/cart.py", title="My Cart", icon=":material/shopping_cart:"),
    st.Page("pages/checkout.py", title="Checkout and Orders", icon=":material/receipt_long:"),
]

# position="hidden": we draw our own navbar instead of Streamlit's default menu.
current_page = st.navigation(pages, position="hidden")

render_navbar()

# Show a one-time confirmation after "Add to Cart" (set by the button callback).
if st.session_state.get("flash"):
    st.toast(st.session_state["flash"], icon=":material/check_circle:")
    st.session_state["flash"] = None

# The navbar search box asks for a switch; do it here (not inside a callback).
if st.session_state.pop("go_search", False):
    st.switch_page("pages/search.py")

current_page.run()
render_footer()
