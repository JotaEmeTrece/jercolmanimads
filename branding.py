from manim import *

# === PALETA DE COLORES OFICIAL ===
COL_AZUL = "#2B76FF"
COL_VERDE = "#27C99F"
COL_GRIS_OSCURO = "#101010"
COL_TITULO = "#FFFFFF"
COL_SUBTITULO = "#606060"

# === FUNCIÓN PARA GENERAR TU LOGO ===
def get_jercol_logo():
    # Barra azul (Larga)
    barra_azul = Rectangle(width=0.35, height=1.1, color=COL_AZUL, fill_opacity=1)
    barra_azul.rotate(-18 * DEGREES) # Inclinación según tu imagen
    barra_azul.shift(LEFT * 0.25)
    
    # Barra verde (Corta)
    barra_verde = Rectangle(width=0.35, height=0.9, color=COL_VERDE, fill_opacity=1)
    barra_verde.rotate(-18 * DEGREES)
    barra_verde.shift(RIGHT * 0.25 + DOWN * 0.1)
    
    logo_simbolo = VGroup(barra_azul, barra_verde)
    
    # Texto
    texto_jercol = Text("Jercol", font_size=50, color=COL_TITULO, weight=BOLD)
    texto_tech = Text("Technologies", font_size=22, color=COL_SUBTITULO)
    
    texto_jercol.next_to(logo_simbolo, DOWN, buff=0.4)
    texto_tech.next_to(texto_jercol, DOWN, buff=0.1)
    
    return VGroup(logo_simbolo, texto_jercol, texto_tech)