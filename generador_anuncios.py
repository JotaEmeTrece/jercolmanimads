from manim import *
from branding import get_jercol_logo, COL_VERDE, COL_AZUL

# ==============================================================
# PARÁMETROS DEL ANUNCIO (Edita esto para cambiar el video)
# ==============================================================
# OPCIÓN 1: VENTAS PERDIDAS
GANCHO_1 = "¿Pierdes ventas por no atender"
GANCHO_2 = "15 chats al mismo tiempo?"

# OPCIÓN 2: ATENCIÓN 24/7 (Sustituir arriba si deseas probar este)
# GANCHO_1 = "¿Tu negocio deja de vender"
# GANCHO_2 = "cuando tú te vas a dormir?"

# OPCIÓN 3: OLVIDOS/FUGAS (Sustituir arriba si deseas probar este)
# GANCHO_1 = "¿Cuántos clientes has olvidado"
# GANCHO_2 = "seguir por falta de tiempo?"

SOLUCION = "Atención masiva y automática con IA."
CTA = "Jercol Technologies: Escalamos tu respuesta."

# ==============================================================

class AnuncioMaestro(Scene):
    def construct(self):
        # --- 1. ELEMENTOS ---
        logo = get_jercol_logo().scale(0.6).to_edge(UP, buff=0.3)
        
        # Textos paramétricos
        txt_gancho = VGroup(
            Text(GANCHO_1, font_size=36, color=WHITE),
            Text(GANCHO_2, font_size=38, color=COL_AZUL, weight=BOLD)
        ).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        txt_solucion = Text(SOLUCION, font_size=34, color=COL_VERDE).move_to(ORIGIN)
        txt_cta = Text(CTA, font_size=26, color=WHITE).to_edge(DOWN, buff=0.7)

        # Representación de "Atención Simultánea" (Nodos de chat)
        puntos_chat = VGroup(*[Dot(color=COL_AZUL) for _ in range(15)]).arrange_in_grid(3, 5, buff=0.5)
        lineas_conexion = VGroup(*[Line(logo.get_bottom(), p.get_center(), stroke_width=1, color=GRAY, stroke_opacity=0.3) for p in puntos_chat])

        # --- 2. ANIMACIÓN ---
        
        # Fase 1: El Dolor (Hook)
        self.play(Write(txt_gancho), run_time=2)
        self.wait(2)
        self.play(txt_gancho.animate.scale(0.7).to_edge(UP))
        
        # Fase 2: Visualización de la solución (Multitasking)
        self.play(FadeIn(puntos_chat, shift=DOWN), run_time=1)
        self.play(Create(lineas_conexion), run_time=1.5)
        self.wait(1)

        # Fase 3: Transformación a Jercol
        self.play(
            FadeOut(txt_gancho),
            FadeOut(lineas_conexion),
            ReplacementTransform(puntos_chat, logo),
            ReplacementTransform(VGroup(), txt_solucion) # Aparece la solución
        )
        self.wait(2)

        # Fase 4: Cierre
        self.play(Write(txt_cta))
        self.play(Indicate(txt_solucion))
        self.wait(3)