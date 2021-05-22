def convert_html_to_dash(html_code, dash_modules=None):
    """Convert standard html (as string) to Dash components.

    Looks into the list of dash_modules to find the right component (default to [html, dcc, dbc])."""
    from xml.etree import ElementTree

    if dash_modules is None:
        import dash_html_components as html
        import dash_core_components as dcc

        dash_modules = [html, dcc]
        try:
            import dash_bootstrap_components as dbc

            dash_modules.append(dbc)
        except ImportError:
            pass

    def find_component(name):
        for module in dash_modules:
            try:
                return getattr(module, name)
            except AttributeError:
                pass
        raise AttributeError(f"Could not find a dash widget for '{name}'")

    def parse_css(css):
        """Convert a style in ccs format to dictionary accepted by Dash"""

my_value = 3
my_marks = {0: "min", 3:"3", 5:"max"}
html = f'<slider  min="0" max="5" step="1" value="{my_value}" marks="{my_marks}" class="col-span-4"></slider>'
slider = convert_html_to_dash(html)

print(slider)