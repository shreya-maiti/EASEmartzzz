"""Temporary cart logic stored in st.session_state (nothing is saved to disk)."""
from __future__ import annotations

import random
from datetime import datetime

import streamlit as st

from data.products import get_product

MAX_QTY = 20


def format_inr(amount: float) -> str:
    if float(amount).is_integer():
        return f"₹{int(amount):,}"
    return f"₹{amount:,.2f}"


def init_state() -> None:
    """Create all session keys once. Safe to call on every rerun."""
    st.session_state.setdefault("cart", {})          # {product_id: quantity}
    st.session_state.setdefault("orders", [])        # demo orders placed this session
    st.session_state.setdefault("last_order", None)
    st.session_state.setdefault("flash", None)


# ---- cart actions (used as on_click callbacks, so the navbar count is always fresh) ----

def add_to_cart(product_id: str) -> None:
    product = get_product(product_id)
    if product is None:
        return
    cart = st.session_state["cart"]
    cart[product_id] = min(cart.get(product_id, 0) + 1, MAX_QTY)
    st.session_state["flash"] = f"Added {product['name']} to your cart."


def increase_qty(product_id: str) -> None:
    cart = st.session_state["cart"]
    if product_id in cart:
        cart[product_id] = min(cart[product_id] + 1, MAX_QTY)


def decrease_qty(product_id: str) -> None:
    cart = st.session_state["cart"]
    if product_id in cart:
        if cart[product_id] <= 1:
            del cart[product_id]
        else:
            cart[product_id] -= 1


def remove_from_cart(product_id: str) -> None:
    st.session_state["cart"].pop(product_id, None)


def clear_cart() -> None:
    st.session_state["cart"] = {}


# ---- read helpers ----

def cart_count() -> int:
    return sum(st.session_state.get("cart", {}).values())


def cart_lines() -> list[dict]:
    """Cart rows with product details and subtotals."""
    lines = []
    for product_id, qty in st.session_state.get("cart", {}).items():
        product = get_product(product_id)
        if product is None:
            continue
        lines.append({**product, "qty": qty, "subtotal": product["price"] * qty})
    return lines


def cart_total() -> float:
    return sum(line["subtotal"] for line in cart_lines())


def qty_in_cart(product_id: str) -> int:
    return st.session_state.get("cart", {}).get(product_id, 0)


# ---- demo checkout ----

def new_demo_order(name: str, address: str) -> dict:
    lines = cart_lines()
    return {
        "number": f"EM-DEMO-{random.randint(100000, 999999)}",
        "placed_at": datetime.now().strftime("%d %b %Y, %I:%M %p"),
        "name": name,
        "address": address,
        "lines": [
            {"name": l["name"], "unit": l["unit"], "qty": l["qty"],
             "price": l["price"], "subtotal": l["subtotal"], "emoji": l["emoji"]}
            for l in lines
        ],
        "total": cart_total(),
    }
