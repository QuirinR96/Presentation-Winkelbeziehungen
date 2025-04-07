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

class IntroAngles(Slide):
    def construct(self):
        title = Title("Basics von Winkeln")
        self.play(Write(title))

        # ==========
        
        self.next_slide()

        tracker = ValueTracker(0.1)

        line1 = Line(ORIGIN, RIGHT*2)
        line2 = Line(ORIGIN, RIGHT*2).rotate_about_origin(tracker.get_value()*DEGREES)
        referenceline = line2.copy()

        angle1 = Angle(line1, line2, radius=0.4)

        text1 = Text(f"{round(tracker.get_value())}°").shift(UP*2.5)

        self.play(Create(line1))
        self.play(Write(text1))
        self.add(line2, angle1)

        line2.add_updater(
            lambda line2: line2.become(referenceline.copy().rotate_about_origin(
                tracker.get_value()*DEGREES
            ))
        )

        angle1.add_updater(
            lambda angle1: angle1.become(Angle(line1, line2, radius=0.4))
        )

        text1.add_updater(
            lambda text1: text1.become(Text(f"{round(tracker.get_value())}°").shift(UP*2.5))
        )

        self.next_slide()

        self.play(tracker.animate.increment_value(359.5), run_time=10)

        # ==========

        self.next_slide()

        self.play(
            FadeOut(line1), 
            FadeOut(line2), 
            FadeOut(angle1), 
            FadeOut(text1), 
            run_time=3
        )

        dotA = LabeledDot("A", radius=0.25).shift(UP*0.5)

        line1 = Line(dotA, RIGHT*2 + UP*0.5)
        line2 = Line(dotA, RIGHT*2 + UP*0.5).rotate(45*DEGREES, about_point=UP*0.5)

        angle1 = Angle(line1, line2, radius=0.75)

        label1 = MathTex(r"\alpha", color=RED).move_to(Angle(line1, line2, radius=0.75/1.5).point_from_proportion(0.5))

        self.play(Create(dotA))
        self.play(
            Create(line1),
            Create(line2)
        )
        self.play(Create(angle1))
        self.play(Write(label1))

        self.next_slide()

        incompletetable = MathTable(
            [
                [ "A",       "B",      "C",       "D",       "E",        "F"],
                [r"\alpha", r"\beta", r"\gamma", r"\delta", r"\epsilon", "?"]
            ], 
            include_outer_lines=True
        ).scale(1).to_edge(DOWN, buff=SMALL_BUFF)

        self.play(Create(incompletetable, run_time=3))

        self.next_slide()

        completetable = MathTable(
            [
                [ "A",       "B",      "C",       "D",       "E",        "F"],
                [r"\alpha", r"\beta", r"\gamma", r"\delta", r"\epsilon", r"\zeta"]
            ], 
            include_outer_lines=True
        ).scale(1).to_edge(DOWN, buff=SMALL_BUFF)

        self.play(
            FadeOut(incompletetable),
            FadeIn(completetable)
        )

        # ==========

        self.next_slide()

        self.play(
            FadeOut(dotA), 
            FadeOut(line1), 
            FadeOut(line2), 
            FadeOut(angle1), 
            FadeOut(label1), 
            FadeOut(completetable), 
            run_time=3
        )


class Test(Slide):
    def construct(self):
        ""