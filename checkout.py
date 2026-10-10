
from html import escape

import streamlit as st

from components.cart_helpers import cart_lines, cart_total, format_inr, new_demo_order
from components.ui_helpers import icon, render_html


def place_demo_order() -> None:
    """on_click callback: validate, create an order, clear the cart."""
    ss = st.session_state
    name = ss.get("co_name", "").strip()
    address = ss.get("co_address", "").strip()
    if not name or not address:
        ss["co_error"] = "Enter your name and a delivery address to place the order."
        return
    order = new_demo_order(name, address)
    ss["last_order"] = order
    ss["orders"].insert(0, order)
    ss["cart"] = {}
    ss["co_error"] = None


def start_new_demo() -> None:
    st.session_state["last_order"] = None


def order_table(lines: list[dict]) -> str:
    rows = "".join(
        f"<tr><td>{l['emoji']} {escape(l['name'])} <small>({escape(l['unit'])})</small></td>"
        f"<td>{l['qty']}</td><td>{format_inr(l['price'])}</td><td>{format_inr(l['subtotal'])}</td></tr>"
        for l in lines
    )
    return (
        '<div class="table-wrap"><table class="otable"><thead><tr><th>Item</th><th>Qty</th>'
        f"<th>Unit price</th><th>Subtotal</th></tr></thead><tbody>{rows}</tbody></table></div>"
    )


render_html('<section class="section-head"><h2>Checkout and orders</h2></section>')
render_html(
    f'<div class="demo-note">{icon("tag", 16)} '
    "</div>"
)

order = st.session_state.get("last_order")
lines = cart_lines()

if order:
    render_html(
        f"""
        <div class="success">
          <h3>order placed</h3>
          <p>Order number <b>{order['number']}</b> &middot; {order['placed_at']}</p>
          <p>Deliver to: {escape(order['name'])}, {escape(order['address'])}</p>
        </div>
        """
    )
    render_html(order_table(order["lines"]))
    render_html(f'<div class="sum-total big"><span>Total</span><span>{format_inr(order["total"])}</span></div>')
    render_html(
        '<p class="fine"></p>'
    )
    c1, c2 = st.columns(2)
    with c1:
        st.page_link("pages/home.py", label="Continue Shopping", icon=":material/arrow_back:")
    with c2:
        st.button("Start anotherorder", key="new_demo", on_click=start_new_demo)
elif not lines:
    render_html(
        f"""
        <div class="empty">
          <div class="empty-art">{icon("shopping-bag", 44)}</div>
          <h3>Nothing to check out</h3>
          <p>Your cart is empty. Add some groceries to checkout.</p>
        </div>
        """
    )
    st.page_link("pages/home.py", label="Continue Shopping", icon=":material/arrow_back:")
else:
    left, right = st.columns([1.6, 1], gap="large")
    with left:
        render_html(order_table(lines))
        render_html(f'<div class="sum-total big"><span>Total</span><span>{format_inr(cart_total())}</span></div>')
    with right:
        with st.container(key="addressbox"):
            render_html("<h3>Delivery details (sample)</h3>")
            st.text_input("Full name", key="co_name", placeholder="Your name")
            st.text_area("Delivery address", key="co_address", placeholder="House no., street, area, city")
            if st.session_state.get("co_error"):
                st.error(st.session_state["co_error"])
            st.button("Place Order", key="place_order", icon=":material/check_circle:",
                      on_click=place_demo_order)
            # render_html('<p class="fine">No card or UPI details are requested.</p>')
    st.page_link("pages/cart.py", label="Back to cart", icon=":material/arrow_back:")

# Orders placed earlier in this session
if st.session_state.get("orders"):
    render_html('<section class="section-head"><h2></h2></section>')
    for past in st.session_state["orders"]:
        with st.expander(f"{past['number']}  ·  {format_inr(past['total'])}  ·  {past['placed_at']}"):
            render_html(order_table(past["lines"]))
