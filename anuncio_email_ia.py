# anuncio_email_ia.py

from manim import *
import random
from branding import get_jercol_logo, COL_VERDE, COL_AZUL

config.pixel_width  = 1080
config.pixel_height = 1920

FONT_T = "Orbitron"
FONT_B = "Rajdhani"

def get_email_icon(color=COL_AZUL, scale=1.0):
    body = Rectangle(width=0.55, height=0.38, color=color,
                     stroke_width=2.5, fill_opacity=0)
    left  = Line(body.get_corner(UL), body.get_center() + UP * 0.08,
                 color=color, stroke_width=2.5)
    right = Line(body.get_corner(UR), body.get_center() + UP * 0.08,
                 color=color, stroke_width=2.5)
    icon = VGroup(body, left, right)
    icon.scale(scale)
    return icon

def make_label(texto, font_size=40, color=WHITE, font=None):
    fnt = font or "Rajdhani"
    txt = Text(texto, font=fnt, font_size=font_size,
               color=color, weight=BOLD)
    bg  = Rectangle(
        width=txt.width + 0.5,
        height=txt.height + 0.25,
        fill_color="#000000",
        fill_opacity=0.72,
        stroke_width=0,
    ).move_to(txt.get_center())
    return VGroup(bg, txt)

def get_ia_core():
    centro  = Circle(radius=0.5, color=COL_VERDE,
                     fill_opacity=1, stroke_width=0)
    simbolo = Text("IA", font="Orbitron", font_size=28,
                   color=BLACK, weight=BOLD).move_to(centro.get_center())
    anillo1 = Circle(radius=0.85, color=COL_VERDE,
                     stroke_width=2.5, fill_opacity=0)
    anillo2 = Circle(radius=1.25, color=COL_AZUL,
                     stroke_width=1.8, fill_opacity=0)
    anillo3 = Circle(radius=1.7,  color=COL_AZUL,
                     stroke_width=1.0, fill_opacity=0, stroke_opacity=0.5)
    return VGroup(anillo3, anillo2, anillo1, centro, simbolo)

def get_chat_bubble(texto, color_burbuja=COL_AZUL, font_size=28, ancho=4.5):
    txt = Text(texto, font="Rajdhani", font_size=font_size,
               color=WHITE, weight=BOLD)
    txt.set_max_width(ancho - 0.6)
    burbuja = RoundedRectangle(
        width=max(txt.width + 0.6, 2.0),
        height=txt.height + 0.55,
        corner_radius=0.28,
        fill_color=color_burbuja,
        fill_opacity=1,
        stroke_width=0,
    )
    txt.move_to(burbuja.get_center())
    return burbuja, txt

def make_badge(texto, color_borde, color_fondo):
    txt = Text(texto, font=FONT_B, font_size=20, color=color_borde, weight=BOLD)
    bg = RoundedRectangle(
        width=txt.width + 0.6, height=txt.height + 0.25, corner_radius=0.15,
        fill_color=color_fondo, fill_opacity=0.8,
        stroke_color=color_borde, stroke_width=1.5
    )
    txt.move_to(bg.get_center())
    return VGroup(bg, txt)

def get_cursor(scale=0.7):
    cursor = Polygon(
        ORIGIN,
        DOWN * 0.7 + RIGHT * 0.25,
        DOWN * 0.5 + RIGHT * 0.35,
        DOWN * 0.8 + RIGHT * 0.6,
        DOWN * 0.7 + RIGHT * 0.7,
        DOWN * 0.4 + RIGHT * 0.45,
        DOWN * 0.3 + RIGHT * 0.75,
        fill_color=WHITE, fill_opacity=1, stroke_color=BLACK, stroke_width=2
    )
    cursor.scale(scale)
    return cursor

class AnuncioEmailIA(Scene):
    def create_caos_panel(self):
        panel = VGroup()
        frame = Rectangle(width=4.0, height=5.5, color=DARK_GRAY, stroke_width=2).move_to(LEFT * 2.25 + UP * 2.5)
        title = Text("ANTES", font=FONT_T, font_size=24, color=RED).next_to(frame, UP, buff=0.2)
        
        correos_caos = VGroup()
        for _ in range(25):
            ico = get_email_icon(color=random.choice([RED, WHITE, BLUE]), scale=random.uniform(0.8, 1.2))
            ico.move_to(
                frame.get_center() + 
                RIGHT * random.uniform(-1.8, 1.8) + 
                UP * random.uniform(-2.5, 2.5)
            )
            correos_caos.add(ico)
            
        panel.add(frame, title, correos_caos)
        return panel

    def create_orden_panel(self):
        panel = VGroup()
        frame = Rectangle(width=4.0, height=5.5, color=DARK_GRAY, stroke_width=2).move_to(RIGHT * 2.25 + UP * 2.5)
        title = Text("DESPUÉS", font=FONT_T, font_size=24, color=COL_VERDE).next_to(frame, UP, buff=0.2)
        
        correos_orden = VGroup()
        col_x = [-1.2, 0, 1.2]
        col_colors = [RED, COL_VERDE, COL_AZUL]
        for cx, cc in zip(col_x, col_colors):
            for i in range(4):
                ico = get_email_icon(color=cc, scale=0.8)
                ico.move_to(frame.get_center() + RIGHT * cx + UP * (1.8 - i * 1.2))
                correos_orden.add(ico)

        panel.add(frame, title, correos_orden)
        return panel

    def construct(self):
        self.camera.frame_height = 16
        self.camera.frame_width  = 9
        random.seed(42)

        # ══════════════════════════════════════
        # ESCENA 1 — HOOK
        # ══════════════════════════════════════

        txt_hook = VGroup(
            Text("¿100+ CORREOS", font=FONT_T, font_size=46,
                 color=WHITE, weight=BOLD),
            Text("AL DÍA?", font=FONT_T, font_size=46,
                 color=COL_VERDE, weight=BOLD),
        ).arrange(DOWN, buff=0.15).move_to(UP * 5.2)

        self.play(
            LaggedStart(
                FadeIn(txt_hook[0], shift=DOWN * 0.3),
                FadeIn(txt_hook[1], shift=DOWN * 0.3),
                lag_ratio=0.35,
            ),
            run_time=0.8,
        )

        zonas_y    = [(-6.5,-4.5),(-4.5,-2.5),(-2.5,-0.5),(2.0,3.8)]
        columnas_x = [-3.5,-1.8,0.0,1.8,3.5]
        colores    = [COL_AZUL, WHITE, COL_VERDE]
        correos    = VGroup()
        idx = 0
        for zona in zonas_y:
            for col_x in columnas_x:
                ico = get_email_icon(
                    color=colores[idx % 3],
                    scale=random.uniform(1.4, 2.0),
                )
                ico.move_to(RIGHT * (col_x + random.uniform(-0.6,0.6))
                            + UP   * random.uniform(zona[0], zona[1]))
                correos.add(ico)
                idx += 1

        self.play(
            LaggedStart(*[FadeIn(c, shift=DOWN*random.uniform(0.5,1.5), scale=0.3)
                          for c in correos], lag_ratio=0.06),
            run_time=1.4,
        )
        self.play(*[Wiggle(c, scale_value=1.15, rotation_angle=0.08)
                    for c in correos], run_time=0.9)

        def make_counter(n, color=WHITE):
            return Text(str(n), font=FONT_T, font_size=90,
                        color=color, weight=BOLD)

        cnt  = make_counter(12,  COL_AZUL).move_to(UP * 1.2)
        self.play(FadeIn(cnt, scale=0.5), run_time=0.3)
        self.wait(0.15)
        cnt2 = make_counter(47,  COL_AZUL).move_to(UP * 1.2)
        self.play(ReplacementTransform(cnt, cnt2), run_time=0.25)
        self.wait(0.1)
        cnt3 = make_counter(103, RED).move_to(UP * 1.2)
        self.play(ReplacementTransform(cnt2, cnt3), run_time=0.25)
        self.play(cnt3.animate.scale(1.25), rate_func=there_and_back, run_time=0.4)
        self.wait(1.0)

        # ══════════════════════════════════════
        # ESCENA 2 — CAOS
        # ══════════════════════════════════════

        self.play(FadeOut(cnt3), run_time=0.4)

        correos_extra = VGroup()
        for px, py in [(-3.2,1.5),(3.0,2.8),(-1.0,0.3),(2.5,-1.2),(-2.8,-3.0),
                       (1.2,3.2),(-3.8,-5.5),(3.5,-4.0),(0.5,-2.0),(-1.5,2.5)]:
            ico = get_email_icon(color=random.choice([RED,COL_AZUL,WHITE]),
                                 scale=random.uniform(1.2,1.9))
            ico.move_to(RIGHT*px + UP*py)
            correos_extra.add(ico)

        self.play(
            LaggedStart(*[FadeIn(c, shift=DOWN*random.uniform(1.0,2.5), scale=0.2)
                          for c in correos_extra], lag_ratio=0.08),
            run_time=1.2,
        )

        lbl1 = make_label("Clientes esperando…",    color=WHITE,    font_size=42).move_to(UP * 0.6)
        lbl2 = make_label("Respuestas tardías…",    color=COL_AZUL, font_size=42).move_to(DOWN * 0.9)
        lbl3 = make_label("Oportunidades perdidas", color=RED,      font_size=42).move_to(DOWN * 2.4)

        self.play(FadeIn(lbl1, shift=LEFT*0.3), run_time=0.5)
        self.wait(0.8)
        self.play(FadeIn(lbl2, shift=LEFT*0.3), run_time=0.5)
        self.wait(0.8)
        self.play(FadeIn(lbl3, shift=LEFT*0.3), run_time=0.5)
        self.wait(0.6)

        indices_alarma = random.sample(range(len(correos)), 6)
        self.play(
            LaggedStart(*[Flash(correos[i], color=RED, line_length=0.3,
                                num_lines=8, flash_radius=0.5)
                          for i in indices_alarma], lag_ratio=0.1),
            run_time=1.0,
        )
        todos = VGroup(correos, correos_extra)
        self.play(*[Wiggle(c, scale_value=1.2, rotation_angle=0.1)
                    for c in todos], run_time=1.0)
        self.wait(0.8)

        # ══════════════════════════════════════
        # ESCENA 3 — APARICIÓN IA
        # ══════════════════════════════════════

        self.play(
            FadeOut(todos), FadeOut(lbl1), FadeOut(lbl2),
            FadeOut(lbl3),  FadeOut(txt_hook),
            run_time=0.6,
        )

        nucleo = get_ia_core().move_to(UP * 1.5)
        self.play(GrowFromCenter(nucleo[3]), run_time=0.5)
        self.play(FadeIn(nucleo[4]),         run_time=0.3)
        self.play(Create(nucleo[2]),         run_time=0.4)
        self.play(Create(nucleo[1]),         run_time=0.4)
        self.play(Create(nucleo[0]),         run_time=0.4)
        self.play(nucleo.animate.scale(1.15), rate_func=there_and_back, run_time=0.5)

        angulos = [30, 90, 150, 210, 270, 330]
        lineas  = VGroup()
        for ang in angulos:
            rad       = ang * DEGREES
            direccion = RIGHT * np.cos(rad) + UP * np.sin(rad)
            lineas.add(Line(
                nucleo.get_center() + direccion * 1.8,
                nucleo.get_center() + direccion * 4.2,
                color=COL_VERDE, stroke_width=1.5, stroke_opacity=0.7,
            ))

        self.play(LaggedStart(*[Create(l) for l in lineas], lag_ratio=0.08),
                  run_time=0.8)
        self.play(nucleo.animate.scale(1.1), rate_func=there_and_back, run_time=0.4)

        txt_ia = VGroup(
            Text("Automatiza", font=FONT_T, font_size=48,
                 color=WHITE, weight=BOLD),
            Text("con IA",     font=FONT_T, font_size=48,
                 color=COL_VERDE, weight=BOLD),
        ).arrange(DOWN, buff=0.1).next_to(nucleo, DOWN, buff=1.2)

        self.play(Write(txt_ia[0]), run_time=0.6)
        self.play(Write(txt_ia[1]), run_time=0.6)
        self.wait(1.2)

        # ══════════════════════════════════════
        # ESCENA 4 — CLASIFICACIÓN
        # ══════════════════════════════════════

        self.play(
            FadeOut(txt_ia), FadeOut(lineas),
            nucleo.animate.scale(0.55).move_to(UP * 6.0),
            run_time=0.7,
        )

        col_x_vals  = [-3.0, 0.0, 3.0]
        col_colores = [RED, COL_VERDE, COL_AZUL]
        col_labels  = ["🔴 Urgente", "🟢 Ventas", "🔵 Soporte"]

        titulos_col = VGroup()
        for cx, cc, cl in zip(col_x_vals, col_colores, col_labels):
            t = Text(cl, font=FONT_B, font_size=32, color=cc, weight=BOLD)
            t.move_to(RIGHT * cx + UP * 4.8)
            titulos_col.add(t)

        self.play(
            LaggedStart(*[FadeIn(t, shift=DOWN*0.2) for t in titulos_col],
                        lag_ratio=0.2),
            run_time=0.7,
        )

        correos_clasificados = VGroup()
        for cx, cc in zip(col_x_vals, col_colores):
            for row in range(5):
                ico = get_email_icon(color=cc, scale=1.5)
                ico.move_to(RIGHT * cx + UP * (3.6 - row * 1.5))
                correos_clasificados.add(ico)

        correos_caos_temp = VGroup()
        for i in range(15):
            ico = get_email_icon(
                color=random.choice([RED, COL_AZUL, COL_VERDE]),
                scale=random.uniform(1.2, 1.8),
            )
            ico.move_to(RIGHT * random.uniform(-4.0, 4.0)
                        + UP   * random.uniform(-6.0, 3.5))
            correos_caos_temp.add(ico)

        self.play(
            LaggedStart(*[FadeIn(c, scale=0.3) for c in correos_caos_temp],
                        lag_ratio=0.04),
            run_time=0.6,
        )
        self.play(
            *[Transform(correos_caos_temp[i], correos_clasificados[i])
              for i in range(15)],
            run_time=1.4,
        )

        txt_clasificacion = make_label("Clasificación automática",
                                       color=COL_VERDE, font_size=38)\
                            .move_to(DOWN * 4.2)
        self.play(FadeIn(txt_clasificacion, shift=UP*0.3), run_time=0.5)
        self.wait(1.5)

        # ══════════════════════════════════════
        # ESCENA 5 — RESPUESTA IA
        # ══════════════════════════════════════

        self.play(
            FadeOut(correos_caos_temp),
            FadeOut(titulos_col),
            FadeOut(txt_clasificacion),
            run_time=0.5,
        )

        nucleo_mini = get_ia_core().scale(0.6).move_to(UP * 4.5)
        self.play(ReplacementTransform(nucleo, nucleo_mini), run_time=0.5)

        mensajes = [
            ("¡Hola! ¿En qué te ayudo?",  COL_AZUL,  UP * 2.2,   "izq"),
            ("Tu pedido está en camino",   COL_VERDE, UP * 0.4,   "der"),
            ("Resuelto en segundos ✓",     COL_AZUL,  DOWN * 1.4, "izq"),
        ]

        txt_respuestas = Text("Respuestas inteligentes",
                              font=FONT_T, font_size=36,
                              color=WHITE, weight=BOLD).move_to(DOWN * 3.2)

        burbujas_group = VGroup()
        for texto, color, pos, lado in mensajes:
            shell, txt_mob = get_chat_bubble(
                texto, color_burbuja=color, font_size=30, ancho=4.5)

            grupo = VGroup(shell, txt_mob)
            if lado == "izq":
                grupo.move_to(pos).align_to(LEFT * 4.2, LEFT)
            else:
                grupo.move_to(pos).align_to(RIGHT * 4.2, RIGHT)

            txt_mob.move_to(shell.get_center())

            self.play(FadeIn(shell, scale=0.85), run_time=0.35)
            self.play(Write(txt_mob, run_time=0.6))
            self.wait(0.35)
            burbujas_group.add(grupo)

        self.play(Write(txt_respuestas), run_time=0.7)
        self.wait(1.2)

        # ══════════════════════════════════════
        # ESCENA 6 — MINI CRM
        # ══════════════════════════════════════

        self.play(
            FadeOut(burbujas_group),
            FadeOut(txt_respuestas),
            run_time=0.5
        )

        crm_bg = RoundedRectangle(
            width=8.2, height=6.5, corner_radius=0.3,
            fill_color="#0D0D0D", fill_opacity=0.95,
            stroke_color="#333333", stroke_width=2
        ).move_to(DOWN * 0.5)

        dots_macos = VGroup(
            Dot(color="#FF5F56", radius=0.08),
            Dot(color="#FFBD2E", radius=0.08),
            Dot(color="#27C93F", radius=0.08)
        ).arrange(RIGHT, buff=0.15).move_to(crm_bg.get_corner(UL) + RIGHT * 0.4 + DOWN * 0.3)

        top_line = Line(
            crm_bg.get_corner(UL) + DOWN * 0.6,
            crm_bg.get_corner(UR) + DOWN * 0.6,
            color="#333333", stroke_width=2
        )
        
        sidebar_x = crm_bg.get_corner(UL)[0] + 1.8
        sidebar_line = Line(
            [sidebar_x, top_line.get_y(), 0],
            [sidebar_x, crm_bg.get_corner(DL)[1], 0],
            color="#333333", stroke_width=2
        )

        sidebar_icons = VGroup(*[
            RoundedRectangle(width=0.8, height=0.35, corner_radius=0.1, 
                             fill_color="#222222", fill_opacity=1, stroke_width=0)
            for _ in range(4)
        ]).arrange(DOWN, buff=0.4)
        
        centro_sidebar_x = crm_bg.get_corner(UL)[0] + 0.9
        sidebar_icons.move_to([centro_sidebar_x, crm_bg.get_center()[1] + 0.5, 0])
        sidebar_icons[0].set_fill(COL_AZUL, opacity=0.3)

        crm_title = Text("Jercol CRM", font=FONT_T, font_size=26, color=WHITE, weight=BOLD)
        crm_title.next_to(sidebar_line.get_start(), RIGHT, buff=0.4).shift(DOWN * 0.4)

        headers = VGroup(
            Text("Cliente", font=FONT_B, font_size=18, color="#CCCCCC"),
            Text("Asunto", font=FONT_B, font_size=18, color="#CCCCCC"),
            Text("Estado", font=FONT_B, font_size=18, color="#CCCCCC")
        )
        headers[0].next_to(crm_title, DOWN, buff=0.6).align_to(crm_title, LEFT)
        headers[1].move_to(headers[0].get_center() + RIGHT * 1.8)
        headers[2].move_to(headers[1].get_center() + RIGHT * 2.0)

        header_y = headers[0].get_y() - 0.3
        header_line = Line(
            [sidebar_x, header_y, 0],
            [crm_bg.get_corner(UR)[0], header_y, 0],
            color="#222222", stroke_width=1.5
        )

        crm_ui_base = VGroup(crm_bg, dots_macos, top_line, sidebar_line, sidebar_icons, crm_title, headers, header_line)

        self.play(GrowFromCenter(crm_bg), run_time=0.5)
        self.play(FadeIn(VGroup(dots_macos, top_line, sidebar_line, sidebar_icons, crm_title, headers, header_line)), run_time=0.5)

        estados = [
            (RED, "Pendiente", "#330000"),
            (YELLOW, "En proceso", "#333300"),
            (COL_VERDE, "Enviado", "#003300")
        ]

        filas_crm_content = VGroup()
        badge_pendiente = None 

        for i, (color_borde, texto_estado, color_fondo) in enumerate(estados):
            fila = VGroup()
            y_pos = headers[0].get_y() - 0.8 - i * 1.1
            ico = get_email_icon(color=WHITE, scale=0.5).move_to([headers[0].get_x() - 0.2, y_pos, 0])
            linea_nombre = Line(ORIGIN, RIGHT * 1.0, color=WHITE, stroke_width=3).next_to(ico, RIGHT, buff=0.2)
            linea_asunto = Line(ORIGIN, RIGHT * 1.5, color=LIGHT_GREY, stroke_width=2).move_to([headers[1].get_x(), y_pos, 0]).align_to(headers[1], LEFT)
            badge = make_badge(texto_estado, color_borde, color_fondo).move_to([headers[2].get_x(), y_pos, 0]).align_to(headers[2], LEFT)
            
            if i == 0:
                badge_pendiente = badge
            
            if i < 2:
                sep_y = y_pos - 0.55
                separador = Line([sidebar_x, sep_y, 0], [crm_bg.get_corner(UR)[0], sep_y, 0], color="#222222", stroke_width=1)
                fila.add(separador)
                
            fila.add(ico, linea_nombre, linea_asunto, badge)
            filas_crm_content.add(fila)

        self.play(
            LaggedStart(*[FadeIn(fila, shift=RIGHT * 0.2) for fila in filas_crm_content], lag_ratio=0.15),
            run_time=1.0
        )

        crm_completo = VGroup(crm_ui_base, filas_crm_content)
        txt_crm = make_label("Todo en un solo lugar", color=WHITE, font_size=38).move_to(DOWN * 4.5)
        self.play(FadeIn(txt_crm, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)

        # ══════════════════════════════════════════════════
        # ESCENA 7 — CONTROL HUMANO (HOVER-REVEAL)
        # ══════════════════════════════════════════════════

        cursor = get_cursor(scale=0.6).move_to(RIGHT * 4.0 + DOWN * 3.0)
        target_pos = badge_pendiente.get_center() + RIGHT * 0.1 + DOWN * 0.1
        
        self.play(cursor.animate.move_to(target_pos), run_time=0.8, rate_func=smooth)

        btn_aprobar = make_badge("Aprobar", COL_AZUL, "#001133").move_to(badge_pendiente.get_center())

        self.play(FadeOut(badge_pendiente, scale=0.8), FadeIn(btn_aprobar, scale=1.2), run_time=0.2)
        self.wait(0.2)

        self.play(VGroup(cursor, btn_aprobar).animate.scale(0.85), run_time=0.15)
        self.play(VGroup(cursor, btn_aprobar).animate.scale(1 / 0.85), run_time=0.15)

        badge_aprobado = make_badge("Aprobado ✔", COL_VERDE, "#003300").move_to(btn_aprobar.get_center())
        txt_control = make_label("Control total", color=COL_VERDE, font_size=42).move_to(txt_crm.get_center())

        self.play(ReplacementTransform(btn_aprobar, badge_aprobado), ReplacementTransform(txt_crm, txt_control), run_time=0.6)
        
        self.play(cursor.animate.shift(RIGHT * 1.5 + DOWN * 1.5), run_time=0.6, rate_func=smooth)
        self.wait(1.0)

        # ══════════════════════════════════════════════════
        # ESCENA 8 — RESULTADO + CTA (FIX FONT SIZE)
        # ══════════════════════════════════════════════════

        elementos_escena7 = VGroup(crm_completo, badge_aprobado, txt_control, cursor, nucleo_mini)
        self.play(FadeOut(elementos_escena7), run_time=0.5)
        
        caos_panel = self.create_caos_panel()
        orden_panel = self.create_orden_panel()
        divisor_line = Line(UP * 5.25, DOWN * -0.25, color=WHITE, stroke_width=2.5).move_to(UP * 2.5)
        
        self.play(FadeIn(caos_panel, shift=RIGHT * 0.5), run_time=0.6)
        self.play(FadeIn(orden_panel, shift=LEFT * 0.5), Create(divisor_line), run_time=0.6)
        self.wait(1.0)
        
        split_screen = VGroup(caos_panel, orden_panel, divisor_line)
        self.play(split_screen.animate.scale(0.6).to_edge(UP, buff=0.8), run_time=0.8)
        
        logo = get_jercol_logo().scale(0.8).next_to(split_screen, DOWN, buff=1.2)
        
        # AJUSTE DE FONT_SIZE AQUÍ
        cta_principal = Text("Automatiza tu negocio con IA", font=FONT_T, font_size=38, weight=BOLD).next_to(logo, DOWN, buff=0.8) 
        marca = Text("Jercol Technologies", font=FONT_B, font_size=36, color=COL_AZUL, weight=BOLD).next_to(cta_principal, DOWN, buff=0.3)
        
        self.play(GrowFromCenter(logo), run_time=0.6)
        self.play(
            LaggedStart(FadeIn(cta_principal, shift=UP * 0.3), FadeIn(marca, shift=UP * 0.3), lag_ratio=0.3),
            run_time=0.8
        )
        self.wait(0.5)

        credito = Text("Diseñado por Jercol Media Studio", font=FONT_B, font_size=24, color=GRAY).move_to(DOWN * 6.5)
        
        self.play(Flash(credito, color=WHITE, line_length=0.2, num_lines=12, flash_radius=1.5), run_time=0.7)
        self.play(credito.animate.set_opacity(0.4), run_time=0.5)
        
        self.wait(2.5)