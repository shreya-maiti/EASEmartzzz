"""Small shared helpers: CSS loading, HTML rendering, inline icons, image fallbacks."""
from __future__ import annotations

import base64
import mimetypes
from functools import lru_cache
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = ROOT_DIR / "assets"
IMAGE_EXTENSIONS = (".webp", ".png", ".jpg", ".jpeg", ".svg")

# Lucide-style outline icons (24x24, 2px stroke), inlined so nothing needs a CDN.
_ICON_PATHS = {
    "basket": '<path d="m15 11-1 9"/><path d="m19 11-4-7"/><path d="M2 11h20"/>'
              '<path d="m3.5 11 1.6 7.4a2 2 0 0 0 2 1.6h9.8a2 2 0 0 0 2-1.6l1.7-7.4"/>'
              '<path d="m5 11 4-7"/><path d="m9 11 1 9"/>',
    "user": '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/>'
            '<path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>',
    "tag": '<path d="M12.586 2.586A2 2 0 0 0 11.172 2H4a2 2 0 0 0-2 2v7.172a2 2 0 0 0 .586 1.414l8.704 8.704'
           'a2.426 2.426 0 0 0 3.42 0l6.58-6.58a2.426 2.426 0 0 0 0-3.42z"/>'
           '<circle cx="7.5" cy="7.5" r=".5" fill="currentColor"/>',
    "star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "chevron": '<path d="m9 18 6-6-6-6"/>',
    "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 '
             '19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81'
             'a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7'
             'A2 2 0 0 1 22 16.92z"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "shopping-bag": '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/>'
                    '<path d="M16 10a4 4 0 0 1-8 0"/>',
}


def icon(name: str, size: int = 18) -> str:
    """Return an inline SVG string for a named icon."""
    paths = _ICON_PATHS[name]
    return (
        f'<svg class="ic" xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
        f'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>'
    )


def clean_html(markup: str) -> str:
    """Strip indentation/blank lines so Markdown never turns HTML into a code block."""
    return " ".join(line.strip() for line in markup.strip().splitlines() if line.strip())


def render_html(markup: str) -> None:
    st.markdown(clean_html(markup), unsafe_allow_html=True)


def load_css() -> None:
    css_path = ASSETS_DIR / "css" / "style.css"
    try:
        css = css_path.read_text(encoding="utf-8")
    except OSError:
        css = ""
    # Per-category card gradients (the card container carries the background).
    from data.products import CATEGORIES

    for c in CATEGORIES:
        css += (
            f'\n[class*="st-key-cat_"][class*="_{c["slug"]}"]'
            f'{{background:linear-gradient(160deg,{c["c1"]},{c["c2"]});}}'
        )
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


@lru_cache(maxsize=256)
def local_image_uri(folder: str, stem: str) -> str | None:
    """Return a data URI for assets/images/<folder>/<stem>.<ext> if the file exists."""
    for ext in IMAGE_EXTENSIONS:
        path = ASSETS_DIR / "images" / folder / f"{stem}{ext}"
        if path.is_file():
            mime = mimetypes.guess_type(path.name)[0] or "image/png"
            data = base64.b64encode(path.read_bytes()).decode("ascii")
            return f"data:{mime};base64,{data}"
    return None
