# gradiente_i.py

from IPython.display import display, HTML

# Función para mostrar cajas de información con gradiente animado en los bordes
def gradiente_i_box(message, icon="🌂", color="#292929", background_color="#ffcc00", border_l="5px", border_r="5px", font_size="14px", gradient_color1="#3498db", gradient_color2="#9b59b6"):
    html_code = f"""
    <style>
    @keyframes gradientAnimation {{
        0% {{
            background-position: 0% 50%;
        }}
        50% {{
            background-position: 100% 50%;
        }}
        100% {{
            background-position: 0% 50%;
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
        border-left: {border_l} solid {color};
        border-right: {border_r} solid {color};
        margin: 3px 0;
        background: linear-gradient(90deg, {gradient_color1}, {gradient_color2});
        background-size: 200% 100%;
        animation: gradientAnimation 3s ease infinite;
    ">
        <span style="color: {color}; margin-right: 5px;">{icon}</span>
        <span style="letter-spacing: 2px;">{message}</span>
    </div>
    """
    display(HTML(html_code))  # Mostrar el HTML generado
