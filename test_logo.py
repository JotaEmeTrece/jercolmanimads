from manim import *
from branding import get_jercol_logo # Importamos lo que acabas de crear

class TestLogo(Scene):
    def construct(self):
        logo = get_jercol_logo()
        self.play(DrawBorderThenFill(logo[0]), run_time=1.5) # Dibuja las barras
        self.play(Write(logo[1:])) # Escribe el texto
        self.wait(2)