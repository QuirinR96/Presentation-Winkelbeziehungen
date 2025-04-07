from manim import *
from manim_slides import Slide

class Start(Slide):
    def construct(self):
        self.wait()

        self.next_slide()

        title = Text("Winkelbeziehungen", font_size=100)

        self.play(Write(title))

        self.next_slide()

        self.play(FadeOut(title))
