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
#v: variable


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
        self.clear()

        #!On different elctronic devices like Harddrives are printed some numbers

        #!Will it really run 4 million hours, and why does it seem that modern car break down more regularly




        #!Of course  it is only a statistical figure


        #!Bathtub curve

        #Basic Axes, length can't be changed
        #o05x1=Axes(x_range=[0,3,1],
                        #y_range=[0, 1, 1],
                        #x_length=5,
                        #y_length=3,
                        #tips=True,
        #)

        #Axes with ValueTracker, to change parameters and enable animations
        v05x1=ValueTracker(2)
        o05x1=always_redraw(lambda:Axes
                                (x_range=[0,3,1],
                                y_range=[0, 1, 1],
                                x_length=v05x1.get_value(),
                                y_length=3,
                                tips=True,
                                )
                            )


        #Functions to indicate the early stage, random stage, and wearout failures
        o05x2=always_redraw(lambda: o05x1.plot
                                (lambda x:np.exp(-x)-0.3,
                                    x_range=[0,1],
                                    use_smoothing=False
                                )
                            )

        o05x3=always_redraw(lambda: o05x1.plot
                                (lambda x:np.exp(-1)-0.3,
                                x_range=[1,2],
                                use_smoothing=False
                                )
                            )

        o05x4=always_redraw(lambda: o05x1.plot
                                (lambda x:
                                np.exp(x-3)-0.3,
                                x_range=[2,3],
                                use_smoothing=False
                                )
                            )

        o05x5=Brace(o05x3)
        o05x6=Brace(o05x2)
        o05x7=Brace(o05x4)
        t05x1=Tex(r"early\\failures")
        t05x2=Tex(r"random\\failures")
        t05x3=Tex(r"wearout\\failures")

        g05x1_ef=VGroup(o05x5,t05x1).arrange(DOWN,buff=0.5).next_to(o05x2,DOWN)
        g05x2_rf=VGroup(o05x6,t05x2).arrange(DOWN,buff=0.5).next_to(o05x3,DOWN)
        g05x3_wf=VGroup(o05x7,t05x3).arrange(DOWN,buff=0.5).next_to(o05x4,DOWN*1.09)

        self.wait(1)
        self.clear
        v05x1.set_value(10)
        self.play(FadeIn(o05x1))
        self.wait(1)
        self.play(v05x1.animate.set_value(12))

        o05x2.update()
        o05x3.update()
        o05x4.update()

        self.play(o05x2.animate.set_color(PINK))
        o05x2.update()
        self.wait(1)
        self.play(o05x4.animate.set_color(PINK))
        self.wait(1)
        self.play(o05x3.animate.set_color(YELLOW))
        self.play(FadeIn(g05x1_ef))
        self.play(FadeIn(g05x2_rf))
        self.play(FadeIn(g05x3_wf))

        self.wait(1)
        self.clear()


        #!"Electronic devices fail with following distribution", early, random and wearout failures



        #!Distingushing the important part of the Bathtub and the nonimportant part of the bathtub

        #!Brilliantly modeling the exp(-tλ) curve in relationship to bathtub curve

        #!Calculating lambda

        #!Modeling some examples, headlights for example

        #!The task with the drinking water system is funny

        #!Dive into availability with repair time figures

        #!Decreaseing  Reliability is easy

        #!Ambient system influences, look in script about silicon lifetime vs tempature

        #!Increase reliability with parallel systems

        #Big Axes that shows the effect on adding multiple devices in parallel on MTBF

        o08x1=Axes(tips=False,
                 x_range=[0,1,1],
                 y_range=[0,1,1],
                 x_length=12,
                 y_length=6,
                 )


        o08x1.to_corner(LEFT+DOWN)

        h08x1=[]
        for i in range(0,10,1):
            h08x1.append(always_redraw(lambda: o08x1.plot
                                        (lambda x: 1-(1-exp(-10*x))**i,
                                        x_range=[0,1],
                                        )
                                    )
                                )

        self.clear()
        self.add(o08x1)
        for i in range(len(h08x1)):
            #self.play(FadeIn(h08x1[i]))
            self.add(h08x1[i])
            self.wait(0.5)
        self.wait(1)








