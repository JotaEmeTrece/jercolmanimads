from manim import *
from branding import get_jercol_logo, COL_VERDE, COL_AZUL

# ==============================================================
# TEXTOS ORIGINALES (Restaurados)
# ==============================================================
GANCHO_1 = "¿Pierdes ventas por no atender"
GANCHO_2 = "15 chats al mismo tiempo?"
SOLUCION = "Atención masiva y automática con IA."
CTA = "Jercol Technologies: Escalamos tu respuesta."
# ==============================================================

class AnuncioVerticalFinal(Scene):
    def construct(self):
        # 1. CONFIGURACIÓN DE CÁMARA VERTICAL NATIVA (9:16)
        self.camera.frame_height = 16
        self.camera.frame_width = 9
        
        # 2. CABECERA: TU NEGOCIO
        tu_negocio = Text("TU NEGOCIO", font_size=40, color=WHITE, weight=BOLD).to_edge(UP, buff=1.0)
        rect_negocio = SurroundingRectangle(tu_negocio, color=COL_AZUL, buff=0.25, stroke_width=3)
        cabecera = VGroup(tu_negocio, rect_negocio)

        # 3. CREACIÓN DEL ICONO DE WHATSAPP (Geometría pura)
        def get_whatsapp_icon():
            circulo = Circle(radius=0.2, color="#25D366", fill_opacity=1, stroke_width=0)
            # Dibujamos la "burbuja" de diálogo abajo a la izquierda
            burbuja = Polygon(
                [-0.1, -0.15, 0], [-0.25, -0.3, 0], [-0.18, -0.1, 0],
                color="#25D366", fill_opacity=1, stroke_width=0
            )
            # El icono del teléfono blanco (simplificado como un punto)
            telefono = Dot(radius=0.08, color=WHITE).move_to(circulo.get_center())
            return VGroup(circulo, burbuja, telefono)

        # 4. GENERACIÓN DE LOS 15 ICONOS
        iconos_wa = VGroup(*[
            get_whatsapp_icon() for _ in range(15)
        ]).arrange_in_grid(5, 3, buff=0.7).shift(DOWN * 1)

        # 5. TEXTOS PARAMÉTRICOS (Ajustados para vertical)
        txt_gancho = VGroup(
            Text(GANCHO_1, font_size=32, color=WHITE),
            Text(GANCHO_2, font_size=34, color=COL_AZUL, weight=BOLD)
        ).arrange(DOWN, buff=0.3).next_to(cabecera, DOWN, buff=1.0)

        # 6. LOGO Y TEXTOS DE CIERRE (Ocultos al inicio)
        logo = get_jercol_logo().scale(0.9).move_to(ORIGIN)
        txt_solucion = Text(SOLUCION, font_size=30, color=COL_VERDE).next_to(logo, DOWN, buff=0.5)
        txt_cta = Text(CTA, font_size=24, color=WHITE).to_edge(DOWN, buff=1.0)

        # === SECUENCIA DE ANIMACIÓN (CORREGIDA) ===
        
        # Fase 1: El Dolor (Hook Vertical)
        self.play(Write(txt_gancho), run_time=2)
        self.wait(1)
        
        # === AQUÍ ESTÁ LA CORRECCIÓN CLAVE ===
        # Limpiamos la pantalla del gancho ANTES de mostrar el negocio
        self.play(FadeOut(txt_gancho, shift=UP)) 
        self.wait(0.5)
        
        # Fase 2: Aparece "Tu Negocio" y los clientes (WhatsApp)
        self.play(FadeIn(cabecera, shift=DOWN))
        self.wait(0.5)
        # Aparecen los 15 iconos con un pequeño retraso entre ellos
        self.play(LaggedStart(*[FadeIn(ico, scale=0.5) for ico in iconos_wa], lag_ratio=0.05), run_time=1.5)
        
        # Las "rayas" de conexión caóticas (Simbolizando estrés)
        conexiones = VGroup(*[
            Line(tu_negocio.get_bottom(), ico.get_center(), stroke_width=1.5, color=RED, stroke_opacity=0.6)
            for ico in iconos_wa
        ])
        self.play(Create(conexiones), run_time=1)
        self.wait(2)

        # Fase 3: La Transformación a Jercol (Limpia)
        # Limpiamos TODA la fase 2 antes de la solución
        self.play(
            FadeOut(cabecera),
            FadeOut(conexiones),
            # Los iconos se fusionan en tu logo
            ReplacementTransform(iconos_wa, logo) 
        )
        self.wait(0.5)
        self.play(Write(txt_solucion))
        self.wait(2)

        # Fase 4: Cierre con CTA original
        self.play(Write(txt_cta))
        self.play(Indicate(txt_solucion)) # Pequeño pulso de énfasis
        self.wait(3)