from manim import *
from numpy import *


config.background_color= DARK_GREY
config.quality='medium_quality'

#Naming convention for text and objects
# xO_y...y

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

        s1_hdd=SVGMobject("graphics/harddrive.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).rotate(120)

        t1=Tex(r"What is reliability?",font_size=60)

        t2_hdd=Tex(r"MTBF\\4 million hours",font_size=23).rotate(120)
        t4=Tex(r"MTTF").rotate(-23)
        t5=Tex(r"MTTR").rotate(56)
        t6=Tex(r"Seems to never break")
        t7=Tex(r"Just needs new Caps")

        g1_title= VGroup(t1,t4).arrange(DOWN, buff=1)
        g1_title.move_to(UP*1.5)

        g2_hdd=VGroup(t2_hdd,s1_hdd).arrange(DOWN).move_to(DOWN*2+RIGHT*5)

        g1_fadeout=(FadeOut(g1_title,shift=UP))


        self.add(g1_title,g2_hdd)
        self.wait(1)
        self.play(g1_fadeout)
        self.wait(1)

        #!On different elctronic devices like Harddrives are printed some numbers

        #!Will it really run 4 million hours, and why does it seem that modern car break down more regularly

        #!Of course  it is only a statistical figure

        #!Bathtub curve

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




