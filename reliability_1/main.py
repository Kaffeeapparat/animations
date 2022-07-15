from manim import *
from numpy import *


config.background_color= DARK_GREY
config.quality='medium_quality'

#Naming convention for text and objects
# xOOxO_y...y

#First number OO
#11:slide number

#First letter x
#t: text
#g: textgroup
#h: array
#s: svg
#o: object


#Frist number O
#1: enumerator

#string y...y
#identifyer for understanding


class Reliability(Scene):
    def construct(self):

        #!What is relaiability exactly

        s01x1_hdd=SVGMobject("graphics/harddrive.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).rotate(120)

        t01x1=Tex(r"What is reliability?",font_size=60)

        t01x2_hdd=Tex(r"MTBF\\4 million hours",font_size=23).rotate(120)
        t01x4=Tex(r"MTTF").rotate(-23)
        t01x5=Tex(r"MTTR").rotate(56)
        t01x6=Tex(r"Seems to never break")
        t01x7=Tex(r"Just needs new Caps")

        g01x1_title= VGroup(t01x1,t01x2_hdd).arrange(DOWN, buff=1)
        g01x1_title.move_to(UP*1.5)

        g01x2_hdd=VGroup(t01x2_hdd,s01x1_hdd).arrange(DOWN).move_to(DOWN*2+RIGHT*5)

        g01x3_fadeout=(FadeOut(g01x1_title,shift=UP))


        self.add(g01x1_title,g01x2_hdd)
        self.wait(1)
        self.play(g01x3_fadeout)
        self.wait(1)
        self.clear

        #!On different elctronic devices like Harddrives are printed some numbers





        #!Will it really run 4 million hours, and why does it seem that modern car break down more regularly




        #!Of course  it is only a statistical figure


        #!Bathtub curve

        o05x1=Axes(x_range=[0, 3, 1],
            y_range=[0, 1, 1],
            x_length=4,
            y_length=2,
            tips=True,s
        )
        o05x2=o05x1.plot(lambda x:
                             np.exp(-x)-0.3,
                             x_range=[0,0.75], use_smoothing=False)
        o05x3=o05x1.plot(lambda x:
                             np.exp(-0.75)-0.3,
                             x_range=[0.75,2.25],use_smoothing=False)
        o05x4=o05x1.plot(lambda x:
                             np.exp(x-3)-0.3,
                             x_range=[2.25,3],
                             use_smoothing=False)

        self.add(o05x1,o05x2,o05x3,o05x4)
        self.wait(1)
        self.play(o05x2.animate.set_color(PINK))
        self.wait(1)
        self.play(o05x4.animate.set_color(PINK))
        self.wait(1)
        self.play(o05x3.animate.set_color(YELLOW))
        self.wait(1)
        self.clear()

        #!"Electronic devices fail with following distribution", early, random and wearout failures

        #!Distingushing the important part of the Bathtub and the nonimportant part of the bathtub

        #!Brilliantly modeling the exp(-tλ) curve in relationship to bathtub curve

        #!Calculating lambda

        #!Modeling some examples, headlights for example

        #!The task with the drinking water system is funny

        #!Dive into availability with repair time figures

        #!Decreaseing  Reliability

        #!Ambient system influences, look in script about silicon lifetime vs tempature

        #!Increase reliability

        #!Parallel systems




