# gradient_box.py

# mostrar cajas de información con gradiente animado en los bordes
def display_outside_box(message, color1="#3498db", color2="#9b59b6", left="5px", right="5px", size="14px", text="white", fund="#292929"):
    # Crear un identificador único para la animación usando el hash del mensaje
    animation_id = hash(message)
    
    html_code = f"""
    <style>
    @keyframes borderGradientAnimation_{animation_id} {{
        0% {{
            border-image-source: linear-gradient(90deg, {color1}, {color2});
        }}
        50% {{
            border-image-source: linear-gradient(90deg, {color2}, {color1});
        }}
        100% {{
            border-image-source: linear-gradient(90deg, {color1}, {color2});
        }}
    }}
    </style>
    <div style="
        display: inline-block;
        padding: 8px 12px;
        background-color: {fund};
        color: {text};
        font-family: Arial, sans-serif;
        font-weight: bold;
        font-size: {size};
        text-align: center;
        border-left: {left} solid transparent;
        border-right: {right} solid transparent;
        margin: 3px 0;
        border-image: linear-gradient(90deg, {color1}, {color2}) 1;
        animation: borderGradientAnimation_{animation_id} 3s ease infinite;
    ">
        <span style="letter-spacing: 2px;">{message}</span>
    </div>
    """
    display(HTML(html_code))
