"""All categories overview page."""
from components.category_card import render_category_grid
from components.ui_helpers import render_html

render_html(
    """
    <section class="section-head">
      <h2>All categories</h2>
      <p>Pick an aisle to see everything in it.</p>
    </section>
    """
)
render_category_grid(ctx="all")
