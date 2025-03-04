# box_2.py

from IPython.display import display, HTML

# Función para mostrar cajas de información
def display_magic_box(message, icon="👾", color="#ffcc00", background_color="#292929", border_l="5px", border_r="5px", font_size="14px", click_color="#1D77BD"):
    html_code = f"""
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
        transition: background-color 0.3s, transform 0.3s;
        cursor: pointer;
    "
    onmouseover="this.style.backgroundColor='#ffcc00'; this.style.transform='scale(1.05)';"
    onmouseout="this.style.backgroundColor='{background_color}'; this.style.transform='scale(1)';"
    onclick="this.style.backgroundColor='{click_color}';"
    >
        <span style="color: {color}; margin-right: 5px;">{icon}</span>
        <span style="letter-spacing: 2px;">{message}</span>
    </div>
    """
    display(HTML(html_code))  # Mostrar el HTML generado
