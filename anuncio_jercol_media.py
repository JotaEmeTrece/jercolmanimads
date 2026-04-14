from manim import *
import random
from branding import get_jercol_logo, COL_VERDE, COL_AZUL

# Configuración de alta fidelidad vertical
config.pixel_width = 1080
config.pixel_height = 1920

class AnuncioJercolMedia(Scene):
    def construct(self):
        self.camera.frame_height = 16
        self.camera.frame_width = 9
        random.seed(42) 

        # ==============================================================
        # ESCENA 1: EL DOLOR (Ajuste de altura basado en el Logo)
        # ==============================================================
        
        txt_gancho = VGroup(
            Text("¿PIERDES VENTAS", font_size=42, color=RED, weight=BOLD),
            Text("POR NO PODER ATENDER", font_size=28, color=WHITE),
            Text("15 CONVERSACIONES DE", font_size=28, color=COL_AZUL),
            Text("WHATSAPP AL MISMO TIEMPO?", font_size=28, color=COL_VERDE, weight=BOLD)
        ).arrange(DOWN, buff=0.2).shift(UP * 2.5)

        self.play(Write(txt_gancho), run_time=1.5)
        self.wait(0.3)
        
        # AJUSTE DE PRECISIÓN: Subimos a la altura visual del Logo (UP * 4.5)
        self.play(txt_gancho.animate.move_to(UP * 4.5), run_time=0.8)

        txt_negocio = Text("TU NEGOCIO", font_size=35, color=WHITE, weight=BOLD)
        rect_negocio = SurroundingRectangle(txt_negocio, color=RED, buff=0.3, stroke_width=4)
        
        # El negocio y los iconos bajan un poco respecto al texto para no amontonarse
        nodo_negocio = VGroup(rect_negocio, txt_negocio).next_to(txt_gancho, DOWN, buff=1.2)

        self.play(FadeIn(nodo_negocio, shift=DOWN), run_time=0.5)

        def get_whatsapp_icon():
            circulo = Circle(radius=0.25, color="#25D366", fill_opacity=1, stroke_width=0)
            burbuja = Polygon(
                [-0.12, -0.18, 0], [-0.3, -0.35, 0], [-0.22, -0.12, 0],
                color="#25D366", fill_opacity=1, stroke_width=0
            )
            telefono = Dot(radius=0.1, color=WHITE).move_to(circulo.get_center())
            return VGroup(circulo, burbuja, telefono)

        # Rango de iconos ajustado a la nueva altura
        iconos_wa = VGroup()
        for _ in range(15):
            ico = get_whatsapp_icon()
            rand_x = random.uniform(-3.5, 3.5)
            # Mantenemos la zona de exclusión para no tapar "TU NEGOCIO"
            rand_y = random.uniform(-5.0, -1.0) 
            ico.move_to(RIGHT * rand_x + UP * rand_y)
            iconos_wa.add(ico)

        lineas_rojas = VGroup(
            Line(nodo_negocio.get_bottom(), iconos_wa[0].get_center(), color=RED, stroke_width=2),
            Line(nodo_negocio.get_bottom(), iconos_wa[1].get_center(), color=RED, stroke_width=2)
        )
        
        self.play(
            LaggedStart(*[FadeIn(ico, scale=0) for ico in iconos_wa], lag_ratio=0.05),
            Create(lineas_rojas),
            run_time=1.2
        )
        
        self.play(
            *[Wiggle(ico, scale_value=1.2, rotation_angle=0.1) for ico in iconos_wa],
            Wiggle(nodo_negocio, scale_value=1.1),
            run_time=1.5
        )

        # ==============================================================
        # ESCENA 2: TRANSFORMACIÓN
        # ==============================================================
        
        txt_garantia = VGroup(
            Text("TE GARANTIZAMOS EL 100%", font_size=36, color=WHITE, weight=BOLD),
            Text("DE CLIENTES ATENDIDOS", font_size=36, color=COL_VERDE, weight=BOLD)
        ).arrange(DOWN, buff=0.2).move_to(txt_gancho.get_center())

        self.play(
            FadeOut(lineas_rojas),
            rect_negocio.animate.set_color(COL_VERDE),
            ReplacementTransform(txt_gancho, txt_garantia),
            run_time=1
        )

        # La cuadrícula ahora tiene espacio de sobra abajo
        grid_ordenada = VGroup(*[get_whatsapp_icon() for _ in range(15)]).arrange_in_grid(
            5, 3, buff=0.7 # Un pelín más compacto para asegurar seguridad
        ).next_to(nodo_negocio, DOWN, buff=0.8)

        self.play(
            *[ico.animate.move_to(grid_ordenada[i].get_center()) for i, ico in enumerate(iconos_wa)],
            run_time=1.2
        )

        lineas_verdes = VGroup(*[
            Line(nodo_negocio.get_bottom(), ico.get_top(), color=COL_VERDE, stroke_width=2, stroke_opacity=0.6)
            for ico in iconos_wa
        ])
        
        self.play(Create(lineas_verdes), run_time=1)
        self.wait(1.5)

        # FUSIÓN AL LOGO
        logo_jercol = get_jercol_logo().scale(1.2).move_to(ORIGIN)
        self.play(
            ReplacementTransform(VGroup(iconos_wa, lineas_verdes, nodo_negocio, txt_garantia), logo_jercol),
            run_time=1.5
        )

        # ==============================================================
        # ESCENA 3: CIERRE (Branding Final)
        # ==============================================================
        
        self.play(logo_jercol.animate.shift(UP * 4.5).scale(0.8), run_time=0.8)

        txt_promesa = VGroup(
            Text("AUMENTARÁS ENTRE UN", font_size=32, color=WHITE),
            Text("50% - 70% TUS VENTAS", font_size=45, color=COL_VERDE, weight=BOLD)
        ).arrange(DOWN, buff=0.2).shift(UP * 1.5)

        txt_dolor = Text("NO SIGAS PERDIENDO DINERO", font_size=28, color=COL_AZUL, weight=BOLD).next_to(txt_promesa, DOWN, buff=1.2)
        txt_cta = Text("ESCALAMOS TUS RESPUESTAS", font_size=35, color=COL_VERDE, weight=BOLD).next_to(txt_dolor, DOWN, buff=0.8)

        firma = Text("Creado por Jercol Media Studio", font_size=18, color=GRAY_B).to_edge(DOWN, buff=1.2)

        self.play(Write(txt_promesa), run_time=1.2)
        self.play(FadeIn(txt_dolor, shift=UP))
        self.play(FadeIn(txt_cta, scale=0.5))
        self.play(FadeIn(firma))
        self.wait(4)