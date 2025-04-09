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

        table1 = MathTable(
            [
                [ "A",       "B",      "C",       "D",       "E"       ],
                [r"\alpha", r"\beta", r"\gamma", r"\delta", r"\epsilon"]
            ], 
            include_outer_lines=True
        ).scale(1).to_edge(DOWN, buff=SMALL_BUFF)

        self.play(Create(table1, run_time=3))

        # ==========

        self.next_slide()

        self.play(
            FadeOut(dotA), 
            FadeOut(line1), 
            FadeOut(line2), 
            FadeOut(angle1), 
            FadeOut(label1), 
            FadeOut(table1), 
            run_time=3
        )

        radius = 2
        dotRadius = 0.25
        angleRadius = 0.75
        labels = [r"\alpha", r"\beta", r"\gamma", r"\delta", r"\epsilon"]
        quadrant = (-1, 1)

        dots = VGroup(
            LabeledDot(chr(65 + index), radius=dotRadius)
            .shift(RIGHT * radius)
            .rotate_about_origin(TAU / 6 * index)
            for index in range(6)
        )

        lines = VGroup(
            Line(dots[index], dots[(index + 1) % 6])
            for index in range(6)
        )

        angles = VGroup(
            Angle(lines[index - 1], lines[index], radius=angleRadius, quadrant=quadrant, other_angle=True)
            for index in range(6)
        )

        self.play(LaggedStart(Create(dots), lag_ratio=3 / 7, run_time=3))
        self.play(LaggedStart(Create(lines), lag_ratio=3 / 7, run_time=3))
        self.play(LaggedStart(Create(angles), lag_ratio=3 / 7, run_time=3))

        self.next_slide()

        angleLabels = [
            MathTex(label).scale(0.75).move_to(
                Angle(
                    lines[index - 1], lines[index],
                    radius=angleRadius / 1.5, quadrant=quadrant, other_angle=True
                ).point_from_proportion(0.5)
            )
            for index, label in enumerate(labels)
        ]

        self.play(Write(angleLabels[0], run_time=0.5))
        self.play(Write(angleLabels[1], run_time=0.5))
        self.play(Write(angleLabels[2], run_time=0.5))
        self.play(Write(angleLabels[3], run_time=0.5))
        self.play(Write(angleLabels[4], run_time=0.5))

        self.next_slide()

        zetaCenter = Angle(
                    lines[4], lines[5],
                    radius=angleRadius / 1.5, quadrant=quadrant, other_angle=True
                ).point_from_proportion(0.5)

        arrow1 = Arrow(zetaCenter + RIGHT * 2 + DOWN, zetaCenter, buff=0)

        text1 = Text("der hier").shift(zetaCenter + RIGHT * 2 + DOWN * 1.5)

        cross1 = VGroup(
            Line(LEFT, RIGHT, color=RED).rotate(30 * DEGREES),
            Line(LEFT, RIGHT, color=RED).rotate(-30 * DEGREES)
        )

        cross2 = VGroup(
            Line(LEFT, RIGHT, color=RED).rotate(30 * DEGREES),
            Line(LEFT, RIGHT, color=RED).rotate(-30 * DEGREES)
        )

        self.play(GrowArrow(arrow1))
        self.play(Write(text1))

        self.next_slide()

        text2 = Tex(r"sin(dem dort)").to_corner(DR, buff=0.25)

        self.play(Write(text2))

        self.next_slide()

        self.play(
            Create(cross1.move_to(text1)),
            Create(cross2.move_to(text2))
        )

        # ==========

        self.next_slide()

        self.play(
            FadeOut(dots),
            FadeOut(lines), 
            FadeOut(angles),
            FadeOut(VGroup(*angleLabels)),
            FadeOut(arrow1), 
            FadeOut(text1), 
            FadeOut(cross1), 
            FadeOut(cross2),
            FadeOut(text2)
        )

        dotA = LabeledDot("A").shift(DOWN + 2 * RIGHT)
        dotB = LabeledDot("B").shift(UP + 2 * RIGHT)
        dotS = LabeledDot("S")

        line1 = Line(ORIGIN, DOWN + 2 * RIGHT)
        line2 = Line(ORIGIN, UP + 2 * RIGHT)
        movingLine = Line(ORIGIN, RIGHT * (5 ** 0.5), color=RED)
        
        angle1 = Angle(line1, line2, radius=0.75)

        text1 = Text("Winkel: ∢???").to_edge(UP, buff=1.5)
        text2 = Text("Winkel: ∢?S?").to_edge(UP, buff=1.5)
        text3 = Text("Winkel: ∢AS?").to_edge(UP, buff=1.5)
        text4 = Text("Winkel: ∢ASB").to_edge(UP, buff=1.5)

        arrow1 = Arrow(dotS, text2.get_center() + DOWN * 0.25 + RIGHT * 1.5)
        arrow2 = Arrow(dotA, text3.get_center() + DOWN * 0.25 + RIGHT * 1.5)
        arrow3 = Arrow(dotB, text4.get_center() + DOWN * 0.25 + RIGHT * 1.5)

        self.play(LaggedStart(
            Create(dotS),
            Create(dotA),
            Create(dotB),
            lag_ratio=1 / 4
        ))

        self.play(LaggedStart(
            Create(line1),
            Create(line2),
            lag_ratio=1 / 3
        ))
        self.add(dotS, dotA, dotB)

        self.play(Create(angle1))
        self.play(Write(text1))

        self.next_slide()

        self.play(Circumscribe(dotS, Circle))
        self.play(GrowArrow(arrow1))
        self.play(FadeOut(text1), FadeIn(text2))

        self.next_slide()

        self.play(FadeOut(arrow1))
        self.play(Create(movingLine))

        self.next_slide()

        self.play(Rotate(movingLine, (-26.57 * DEGREES), about_point = ORIGIN))
        self.play(Circumscribe(dotA, Circle))
        self.play(GrowArrow(arrow2))
        self.play(FadeOut(text2), FadeIn(text3))

        self.next_slide()

        self.play(FadeOut(arrow2))
        self.play(Rotate(movingLine, (2 * 26.57 * DEGREES), about_point = ORIGIN))
        self.play(Circumscribe(dotB, Circle))
        self.play(GrowArrow(arrow3))
        self.play(FadeOut(text3), FadeIn(text4))

        self.next_slide()

        self.play(
            FadeOut(dotA),
            FadeOut(dotB),
            FadeOut(dotS),
            FadeOut(line1),
            FadeOut(line2),
            FadeOut(movingLine),
            FadeOut(angle1),
            FadeOut(text4),
            FadeOut(arrow3)
        )
        self.play(Unwrite(title))

class Nebenwinkel(Slide):
    def construct(self):
        title = Title("Nebenwinkel")

        self.play(Write(title))

        self.next_slide()

        mainLine = Line(LEFT, RIGHT)
        movingLine = Line(ORIGIN, RIGHT)
        referenceLine = movingLine.copy()

        movingLine.rotate_about_origin(90 * DEGREES)

        angle1 = Angle(mainLine, movingLine, quadrant=(1, 1), color=RED)
        angle2 = Angle(mainLine, movingLine, quadrant=(-1, 1), color=BLUE, other_angle=True)

        valueAngle1 = Text("90°", color=RED)
        plus = Text(" + ")
        valueAngle2 = Text("90°", color=BLUE)
        equals = Text(" = 180°")

        text1 = VGroup(valueAngle1, plus, valueAngle2, equals).arrange().shift(UP * 2.5)

        self.play(Create(mainLine))
        self.play(Create(movingLine))
        self.play(LaggedStart(Create(angle1), Create(angle2), lag_ratio=1 / 3))
        self.play(Write(text1))

        self.next_slide()

        tracker = ValueTracker(90)

        movingLine.add_updater(
            lambda movingLine: movingLine.become(
                referenceLine.copy().rotate_about_origin(tracker.get_value() * DEGREES)
            )
        )

        angle1.add_updater(
            lambda angle1: angle1.become(
                Angle(mainLine, movingLine, quadrant=(1, 1), color=RED)
            )
        )

        angle2.add_updater(
            lambda angle2: angle2.become(
                Angle(mainLine, movingLine, quadrant=(-1, 1), color=BLUE, other_angle=True)
            )
        )

        valueAngle1.add_updater(
            lambda valueAngle1: valueAngle1.become(
                Text(f"{180 - round(tracker.get_value())}°", color=RED)
                .move_to(valueAngle1)
            )
        )

        valueAngle2.add_updater(
            lambda valueAngle2: valueAngle2.become(
                Text(f"{round(tracker.get_value())}°", color=BLUE)
                .move_to(valueAngle2)
            )
        )

        text1.add_updater(
            lambda text1: text1.become(
                VGroup(valueAngle1, plus, valueAngle2, equals)
                .arrange()
                .shift(UP * 2.5)
            )
        )

        self.next_slide(loop=True)

        self.play(tracker.animate.set_value(30))
        self.play(tracker.animate.set_value(175))
        self.play(tracker.animate.set_value(60))
        self.play(tracker.animate.set_value(120))
        self.play(tracker.animate.set_value(45))
        self.play(tracker.animate.set_value(135))
        self.play(tracker.animate.set_value(80))
        self.play(tracker.animate.set_value(160))
        self.play(tracker.animate.set_value(90))

        self.next_slide()

        self.play(
            FadeOut(mainLine),
            FadeOut(movingLine),
            FadeOut(angle1),
            FadeOut(angle2),
            FadeOut(text1)
        )

        self.play(Unwrite(title))

class Scheitelwinkel(Slide):
    def construct(self):
        title = Title("Scheitelwinkel")

        self.play(Write(title))

        self.next_slide()

        mainLine = Line(LEFT, RIGHT)
        movingLine = Line(LEFT, RIGHT)
        referenceLine = movingLine.copy()

        movingLine.rotate_about_origin(60 * DEGREES)

        angle1 = Angle(mainLine, movingLine, quadrant=(1, 1), color=RED)
        angle2 = Angle(mainLine, movingLine, quadrant=(-1, 1), color=BLUE, other_angle=True)
        angle3 = Angle(mainLine, movingLine, quadrant=(-1, -1), color=RED)
        angle4 = Angle(mainLine, movingLine, quadrant=(1, -1), color=BLUE, other_angle=True)

        self.play(Create(mainLine))
        self.play(Create(movingLine))
        self.play(LaggedStart(
            Create(angle1), 
            Create(angle2),
            Create(angle3),
            Create(angle4),
            lag_ratio=1 / 5
            )
        )

        self.next_slide()

        tracker = ValueTracker(60)

        movingLine.add_updater(
            lambda movingLine: movingLine.become(
                referenceLine.copy().rotate_about_origin(tracker.get_value() * DEGREES)
            )
        )

        angle1.add_updater(
            lambda angle1: angle1.become(
                Angle(mainLine, movingLine, quadrant=(1, 1), color=RED)
            )
        )

        angle2.add_updater(
            lambda angle2: angle2.become(
                Angle(mainLine, movingLine, quadrant=(-1, 1), color=BLUE, other_angle=True)
            )
        )

        angle3.add_updater(
            lambda angle3: angle3.become(
                Angle(mainLine, movingLine, quadrant=(-1, -1), color=RED)
            )
        )

        angle4.add_updater(
            lambda angle4: angle4.become(
                Angle(mainLine, movingLine, quadrant=(1, -1), color=BLUE, other_angle=True)
            )
        )

        self.next_slide(loop=True)

        self.play(tracker.animate.set_value(175))
        self.play(tracker.animate.set_value(60))
        self.play(tracker.animate.set_value(120))
        self.play(tracker.animate.set_value(30))
        self.play(tracker.animate.set_value(135))
        self.play(tracker.animate.set_value(80))
        self.play(tracker.animate.set_value(160))
        self.play(tracker.animate.set_value(45))
        self.play(tracker.animate.set_value(90))

        self.next_slide()

        self.play(
            FadeOut(mainLine),
            FadeOut(movingLine),
            FadeOut(angle1),
            FadeOut(angle2),
            FadeOut(angle3),
            FadeOut(angle4)
        )

        self.play(Unwrite(title))


class Stufenwinkel(Slide):
    def construct(self):
        ""
        title = Title("Stufenwinkel")

        self.play(Write(title))

        self.next_slide()

        tracker = ValueTracker(60)

        line1 = Line(LEFT * 2, RIGHT * 2)
        line2 = line1.copy()
        movingLine = Line(LEFT * 2.5, RIGHT * 2.5)
        referenceLine = movingLine.copy()

        movingLine.rotate(60 * DEGREES)

        angle1 = Angle(line1, movingLine, quadrant=(1, 1), color=RED).add_updater(
            lambda angle1: angle1.become(Angle(line1, movingLine, quadrant=(1, 1), color=RED))
        )

        angle2 = Angle(line2, movingLine, quadrant=(1, 1), color=RED).add_updater(
            lambda angle2: angle2.become(Angle(line2, movingLine, quadrant=(1, 1), color=RED))
        )

        movingLine.add_updater(
            lambda movingLine: movingLine.become(referenceLine.copy().rotate_about_origin(tracker.get_value() * DEGREES))
        )

        self.play(
            Create(line1),
            Create(line2),
            Create(movingLine)
        )

        self.play(
            Create(angle1),
            Create(angle2)
        )

        self.next_slide()

        self.play(
            line1.animate().shift(UP),
            line2.animate().shift(DOWN)
        )

        self.next_slide()

        self.next_slide(loop=True)

        self.play(tracker.animate(run_time=2).set_value(120))
        self.play(tracker.animate(run_time=2).set_value(40))
        self.play(tracker.animate(run_time=2).set_value(90))
        self.play(tracker.animate(run_time=2).set_value(70))
        self.play(tracker.animate(run_time=2).set_value(110))
        self.play(tracker.animate(run_time=2).set_value(80))
        self.play(tracker.animate(run_time=2).set_value(140))
        self.play(tracker.animate(run_time=2).set_value(60))
        
        self.next_slide()

        self.play(
            FadeOut(line1),
            FadeOut(line2),
            FadeOut(movingLine),
            FadeOut(angle1),
            FadeOut(angle2)
        )

        self.play(Unwrite(title))

class Test(Slide):
    def construct(self):
        ""
