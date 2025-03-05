from IPython.display import display, HTML

def borde_circular_box(message, icon="🔵", color="#ffcc00", background_color="#292929", font_size="14px", border_color1="#3498db", border_color2="#9b59b6"):
    html_code = f"""
    <style>
    @keyframes circularBorderAnimation {{
        0% {{
            border-color: {border_color1};
        }}
        50% {{
            border-color: {border_color2};
        }}
        100% {{
            border-color: {border_color1};
        }}
    }}
    </style>
    <div style="
        display: inline-block;
        padding: 8px 12px;
        background-color: {background_color};
        color: white;
        font-family: Arial, sans-serif;
        font-weight: bold;
        font-size: {font_size};
        text-align: center;
        border-radius: 50px;
        border: 3px solid {border_color1};
        margin: 3px 0;
        animation: circularBorderAnimation 3s ease infinite;
    ">
        <span style="color: {color}; margin-right: 5px;">{icon}</span>
        <span style="letter-spacing: 2px;">{message}</span>
    </div>
    """
    display(HTML(html_code))
