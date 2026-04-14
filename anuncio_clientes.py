from manim import *
from branding import get_jercol_logo, COL_VERDE, COL_AZUL

class AnuncioClientes(Scene):
    def construct(self):
        # 1. Preparar el Logo (Escalado para que quepa todo)
        logo = get_jercol_logo().scale(0.7).to_edge(UP, buff=0.5)

        # 2. El Mensaje de Impacto
        mensaje_1 = Text("¿Tu negocio ignora clientes?", font_size=32, color=WHITE)
        mensaje_2 = Text("Dales una respuesta inmediata con IA.", font_size=32, color=COL_VERDE)
        
        grupo_mensajes = VGroup(mensaje_1, mensaje_2).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        # 3. La Animación de "Flujo" (Simbolizando atención 24/7)
        flujo = StreamLines(
            lambda p: np.array([np.sin(p[1]), np.cos(p[0]), 0]),
            colors=[COL_AZUL, COL_VERDE],
            padding=3,
            stroke_width=2
        )

        # 4. SECUENCIA DE ANIMACIÓN
        # Fase 1: El problema
        self.play(Write(mensaje_1))
        self.wait(1.5)
        
        # Fase 2: La solución aparece
        self.play(
            mensaje_1.animate.scale(0.8).to_edge(UP),
            FadeIn(mensaje_2, shift=UP)
        )
        self.wait(1.5)
        
        # Fase 3: El sistema Jercol en acción
        self.play(FadeOut(mensaje_1), FadeOut(mensaje_2))
        self.play(DrawBorderThenFill(logo))
        self.play(flujo.create()) # Líneas de energía que representan el bot trabajando
        self.wait(2)
        
        # Fase 4: Cierre con autoridad
        cta = Text("Jercol Technologies: Tu negocio nunca duerme.", font_size=24).to_edge(DOWN, buff=0.5)
        self.play(Write(cta))
        self.wait(3)