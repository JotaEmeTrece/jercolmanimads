from manim import *

class Test(Scene):
    def construct(self):
        circulo = Circle(color=BLUE)
        self.play(Create(circulo))
        self.wait(1)