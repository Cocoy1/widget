# Cajas con gradiente

# Función para mostrar cajas con gradiente animado en los bordes
def display_outside_box(message, color1="#3498db", color2="#9b59b6", left="7px", right="7px", size="12px", text="white", fund="#292929", Wide="auto"):
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
        width: {Wide};
    ">
        <span style="letter-spacing: 2px;">{message}</span>
    </div>
    """
    display(HTML(html_code))

# Función para mostrar cajas con gradiente animado en el interior
def display_inside_box(message, color1="#3498db", color2="#9b59b6", left="7px", right="7px", size="12px", text="white", fund="#292929", Wide="auto"):
    animation_id = hash(message)
    
    html_code = f"""
    <style>
    @keyframes gradientAnimation_{animation_id} {{
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
        color: {text};
        font-family: Arial, sans-serif;
        font-weight: bold;
        font-size: {size};
        text-align: center;
        border-left: {left} solid {fund};
        border-right: {right} solid {fund};
        margin: 3px 0;
        background: linear-gradient(90deg, {color1}, {color2});
        background-size: 200% 100%;
        animation: gradientAnimation_{animation_id} 3s ease infinite;
        width: {Wide};
    ">
        <span style="letter-spacing: 2px;">{message}</span>
    </div>
    """
    display(HTML(html_code))

# Función para mostrar cajas con gradiente animado en los bordes y fondo al pasar el ratón
def display_interactive_box(message, color1="#3498db", color2="#9b59b6", left="7px", right="7px", size="12px", text="white", fund="#292929", Wide="auto"):
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
    @keyframes gradientAnimation_{animation_id} {{
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
    <div id="box_{animation_id}" style="
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
        width: {Wide};
        cursor: pointer;
    " onmouseover="activateGradient('box_{animation_id}', '{color1}', '{color2}', '{fund}')"
      onmouseout="deactivateGradient('box_{animation_id}', '{color1}', '{color2}', '{fund}')">
        <span style="letter-spacing: 2px;">{message}</span>
    </div>
    <script>
    function activateGradient(boxId, color1, color2, fund) {{
        var box = document.getElementById(boxId);
        // Quitar el gradiente de los bordes y ponerlos de color sólido
        box.style.borderImage = "none";
        box.style.borderLeft = "7px solid {fund}";
        box.style.borderRight = "7px solid {fund}";
        box.style.animation = "none";
        // Aplicar el gradiente al fondo
        box.style.background = `linear-gradient(90deg, ${{color1}}, ${{color2}})`;
        box.style.backgroundSize = '200% 100%';
        box.style.animation = `gradientAnimation_${{boxId.split('_')[1]}} 3s ease infinite`;
    }}

    function deactivateGradient(boxId, color1, color2, fund) {{
        var box = document.getElementById(boxId);
        // Restaurar el gradiente en los bordes
        box.style.borderImage = `linear-gradient(90deg, ${{color1}}, ${{color2}}) 1`;
        box.style.borderLeft = "{left} solid transparent";
        box.style.borderRight = "{right} solid transparent";
        box.style.animation = `borderGradientAnimation_${{boxId.split('_')[1]}} 3s ease infinite`;
        // Restaurar el fondo sólido
        box.style.background = "{fund}";
        box.style.animation = "none";
    }}
    </script>
    """
    display(HTML(html_code))

    #Fin

