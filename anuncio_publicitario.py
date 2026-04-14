from manim import *
from branding import get_jercol_logo, COL_VERDE, COL_AZUL

class AnuncioPublicitario(Scene):
    def construct(self):
        self.camera.frame_height = 16
        self.camera.frame_width = 9
        
        # --- ELEMENTOS ---
        gancho = VGroup(
            Text("¿PIERDES VENTAS?", font_size=42, color=RED, weight=BOLD),
            Text("por falta de tiempo?", font_size=32)
        ).arrange(DOWN).shift(UP * 3)

        logo = get_jercol_logo().scale(1.2)
        cta = Text("CONTÁCTANOS HOY", font_size=35, color=COL_VERDE).to_edge(DOWN, buff=1.5)
        
        # Iconos de WhatsApp (Versión mejorada)
        def get_wa():
            return VGroup(
                Circle(radius=0.2, color="#25D366", fill_opacity=1), 
                Dot(radius=0.08, color=WHITE)
            )

        iconos = VGroup(*[get_wa() for _ in range(15)]).arrange_in_grid(5, 3, buff=0.8)

        # --- ANIMACIÓN ---
        # 1. El Gancho con impacto
        self.play(Write(gancho), run_time=1.5)
        self.play(Indicate(gancho[0], scale_factor=1.2, color=RED))
        self.wait(1)

        # 2. El Caos (Aparecen iconos y vibran)
        self.play(FadeIn(iconos, lag_ratio=0.1))
        
        # Efecto de estrés: los iconos vibran usando wiggle
        self.play(
            *[ico.animate(rate_func=wiggle).scale(1.1) for ico in iconos],
            run_time=2
        )
        
        # 3. La Solución (Jercol al rescate)
        # Fix aplicado: Flash se lanza directamente en el play
        flash = Flash(ORIGIN, color=COL_VERDE, line_length=2, num_lines=20)
        
        self.play(
            FadeOut(gancho),
            ReplacementTransform(iconos, logo),
            flash # Manim ejecuta la animación de Flash automáticamente aquí
        )
        
        self.play(Write(cta))
        
        # 4. LA FIRMA (Jercol Studio)
        firma = Text("Diseñado por Jercol Studio", font_size=18, color=GRAY).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(firma))
        
        self.wait(3)