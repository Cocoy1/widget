# Crear widgets con Barras a los lados

# Función para mostrar cajas de información
def display_info_box(message, icon="👻", color="#ffcc00", background_color="#292929", border_l="5px", border_r="5px"):
    html_code = f"""
    <div style="
        display: inline-block;
        padding: 8px 12px;
        background-color: {background_color};
        color: white;
        font-family: Arial, sans-serif;
        font-weight: bold;
        font-size: 14px;
        text-align: center;
        border-left: {border_l} solid {color};
        border-right: {border_r} solid {color};
        margin: 3px 0;
    ">
        <span style="color: {color}; margin-right: 5px;">{icon}</span>
        <span style="letter-spacing: 2px;">{message}</span>
    </div>
    """
    display(HTML(html_code))
