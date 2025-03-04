# gradiente_s.py

from IPython.display import display, HTML

# Función para mostrar cajas de información con gradiente animado en los bordes
def gradiente_s_box(message, icon="☂️", color="#ffcc00", background_color="#292929", border_l="5px", border_r="5px", font_size="14px", gradient_color1="#3498db", gradient_color2="#9b59b6"):
    html_code = f"""
    <style>
    @keyframes borderGradientAnimation {{
        0% {{
            border-image-source: linear-gradient(90deg, {gradient_color1}, {gradient_color2});
        }}
        50% {{
            border-image-source: linear-gradient(90deg, {gradient_color2}, {gradient_color1});
        }}
        100% {{
            border-image-source: linear-gradient(90deg, {gradient_color1}, {gradient_color2});
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
        border-left: {border_l} solid transparent;
        border-right: {border_r} solid transparent;
        margin: 3px 0;
        border-image: linear-gradient(90deg, {gradient_color1}, {gradient_color2}) 1;
        animation: borderGradientAnimation 3s ease infinite;
    ">
        <span style="color: {color}; margin-right: 5px;">{icon}</span>
        <span style="letter-spacing: 2px;">{message}</span>
    </div>
    """
    display(HTML(html_code))  # Mostrar el HTML generado
