from turtle import delay
from manim import *

class CreateCircle(Scene):
    def construct(self):
        square = Square()
        square.set_color(RED)
        square.set_fill(RED, opacity = 0.5)
        self.play(Create(square))
        self.wait(1)

class DrawText(Scene):
    def construct(self):
        text = Tex(r"\LaTeX", font_size = 144)
        self.play(Write(text))
        self.wait(1)

class WriteEquation(Scene):
    def construct(self):
        text = MathTex(r"f(x) = x^2", font_size = 160)
        boundary = AnimatedBoundary(text, colors=[WHITE], cycle_rate = 5)
        #self.add(text)
        self.play(Write(text), run_time = 3)
        #self.play(FadeIn(text, function = exponential_decay))
        self.wait(1)

class GenerateArray(Scene):
    def construct(self):
        #create title, shift to top, create underline, draw both title and underline
        title = Text("Linear Search", font_size = 75)
        title.shift(UP * 3.2)
        line = Underline(mobject = title, buff=0.2)
        self.play(AnimationGroup(Write(title, run_time = 2), Write(line, run_time = 2)))


        #create each cell of the array, arrange them next to one another
        squares = [Square() for _ in range(5)]
        arr = [11, 22, 33, 44, 55]
        nums = []
        for i in range(5):
            squares[i].set_color(BLUE)
            squares[i].height = 1
            squares[i].width = 1
            squares[i].set_fill(BLUE, opacity = 0.2)
        VGroup(*squares).set_x(0).arrange(buff=0)
        
        #create each latex object per cell based on the numbers in arr
        for i in range(len(arr)):
            textMobject = SingleStringMathTex(str(arr[i]), font_size = 40)
            nums.append(textMobject)
            textMobject.move_to(squares[i].get_center())
            # add an updater to ensure each text stays in the center of its square cell
            textMobject.add_updater(lambda x, i=i: x.move_to(squares[i].get_center()))

        #Draw borders of each square and then fill them up
        self.play(AnimationGroup(DrawBorderThenFill(VGroup(*squares))))#,
        #VGroup(*squares).animate.set_fill(BLUE, opacity = 0.2)))

        #do the wave animations for the whole array and write the numbers at the same time
        self.play(AnimationGroup(ApplyWave(VGroup(*squares)), Write(VGroup(*nums), run_time = 0.9), lag_ratio = 0.3))
