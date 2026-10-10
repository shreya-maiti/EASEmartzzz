"""Shopping cart page (temporary, session-only)."""
from html import escape

import streamlit as st

from components.cart_helpers import (
    cart_count, cart_lines, cart_total, clear_cart, decrease_qty, format_inr,
    increase_qty, remove_from_cart,
)
from components.ui_helpers import icon, render_html

lines = cart_lines()
render_html('<section class="section-head"><h2>My cart</h2></section>')

if not lines:
    render_html(
        f"""
        <div class="empty">
          <div class="empty-art">{icon("shopping-bag", 44)}</div>
          <h3>Your cart is empty</h3>
          <p>Add a few groceries and they will show up here.</p>
        </div>
        """
    )
    st.page_link("pages/home.py", label="Continue Shopping", icon=":material/arrow_back:")
else:
    main, side = st.columns([2.3, 1], gap="large")
    with main:
        for line in lines:
            pid = line["id"]
            with st.container(key=f"line_{pid}"):
                c_name, c_price, c_qty, c_sub, c_del = st.columns(
                    [3, 1.2, 1.9, 1.2, 0.6], vertical_alignment="center"
                )
                with c_name:
                    render_html(
                        f"""
                        <div class="line-name"><span class="line-emoji">{line['emoji']}</span>
                        <span><b>{escape(line['name'])}</b><br><small>{escape(line['unit'])}</small></span></div>
                        """
                    )
                with c_price:
                    render_html(f'<div class="line-price">{format_inr(line["price"])} each</div>')
                with c_qty:
                    q1, q2, q3 = st.columns([1, 1, 1], vertical_alignment="center")
                    with q1:
                        st.button(":material/remove:", key=f"dec_{pid}", on_click=decrease_qty,
                                  args=(pid,), help="Decrease quantity")
                    with q2:
                        render_html(f'<div class="qty">{line["qty"]}</div>')
                    with q3:
                        st.button(":material/add:", key=f"inc_{pid}", on_click=increase_qty,
                                  args=(pid,), help="Increase quantity")
                with c_sub:
                    render_html(f'<div class="line-sub">{format_inr(line["subtotal"])}</div>')
                with c_del:
                    st.button(":material/delete:", key=f"del_{pid}", on_click=remove_from_cart,
                              args=(pid,), help="Remove item")
        b1, b2 = st.columns(2)
        with b1:
            st.page_link("pages/home.py", label="Continue Shopping", icon=":material/arrow_back:")
        with b2:
            st.button("Clear Cart", key="clear_cart", icon=":material/delete_sweep:", on_click=clear_cart)
    with side:
        with st.container(key="summary"):
            render_html(
                f"""
                <h3>Order summary</h3>
                <div class="sum-row"><span>Items</span><span>{cart_count()}</span></div>
                <div class="sum-row"><span>Delivery</span><span>Demo only</span></div>
                <div class="sum-total"><span>Total</span><span>{format_inr(cart_total())}</span></div>
                <p class="fine">Prices are sample values for demonstration.</p>
                """
            )
            st.page_link("pages/checkout.py", label="Proceed to Checkout", icon=":material/arrow_forward:")
