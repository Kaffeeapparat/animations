from manim import *
from numpy import *
from colour import Color

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

        #!First define the device that gets observed

        t02x1=Tex(r"Definition: A device that runs and fails")

        t02x2=Tex(r"State of the Device:")
        t02x3=Tex(r"functioning",r"defect",font_size=50).arrange(DOWN)
        g02x3_bestate=VGroup(t02x2,t02x3).arrange(DOWN)

        #tex.animate.set_color(RED),
        #be stands for Bauelement, the basic bulding block of devices
        s02x1_be=SVGMobject("graphics/device.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.5)

        s02x2_be=SVGMobject("graphics/device_connected.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.5)

        s02x3_d1=SVGMobject("graphics/diode.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.5)

        s02x4_d2=SVGMobject("graphics/diode2.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.5)

        s02x2_cap=SVGMobject("graphics/cap.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.5)

        g02x1=VGroup()
        for i in range(1,10,1):
            g02x1.add(SVGMobject("graphics/device_connected.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.3))
        g02x1.arrange(DOWN,buff=0)

        g02x2=VGroup(s02x3_d1,s02x4_d2,s02x2_cap)

        self.add(s02x1_be)
        o01x1=s02x1_be
        for i in range(0,3,1):
            self.play(ReplacementTransform(o01x1,g02x2[i]))
            o01x1=g02x2[i]
        self.wait(1)
        g02x3_bestate.move_to(ORIGIN+RIGHT*3)
        self.play(Create(g02x3_bestate))
        self.wait(1)

        self.play(g02x3_bestate[1][1].animate.set_color(RED),o01x1.animate.set_color(RED))
        self.wait(1)
        self.play(g02x3_bestate[1][0].animate.set_color(GREEN),o01x1.animate.set_color(GREEN))
        self.wait(1)
        self.clear()

        self.play(ReplacementTransform(o01x1,s02x1_be.move_to(ORIGIN).set_color(GREEN)))

        #Showing the Din Symbol of a resistor and merging iot into different Symbols

        g02x4_bematrix=VGroup(*[SVGMobject("graphics/device.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.06) for s in range(0,100)])
        g02x4_bematrix.arrange_in_grid(cols=20).move_to(UP*2.5+LEFT*0)
        self.play(ReplacementTransform(s02x1_be,g02x4_bematrix))

        #self.play(AnimationGroup(*[Create(s) for s in g02x4_bematrix  ],lag_ratio=0.1))
        self.wait(1)

        #!Calculating lambda

        t02x4_ratep=MathTex(r"\text{rate of failure}\approx\frac{ \text{failed devices} }{ \text{number of devices}\times\text{time difference} }")
        t02x5_ratec=MathTex(r"\lambda\approx\frac{\Delta n}{n\Delta t}",r"=\frac{1}{\text{MTBF}}=\frac{1}{\text{MTTF}}")

        #g02x5_rate=VGroup(t02x4_ratep,t02x5_ratec)
        self.play(Create(t02x4_ratep))
        self.wait(1)
        self.play(ReplacementTransform(t02x4_ratep,t02x5_ratec))
        self.wait(1)

        o02x01_n=DecimalNumber(
            100,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )

        o02x02_dn=DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )

        o02x03_dt=DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )

        o02x04_rate=DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )

        #showing rate of 1 and others
        g02x5_bematback=g02x4_bematrix
        self.clear()

        #!Of course  it is only a statistical figure


        #!Bathtub curve
        t03x1=Tex(r"Typical failure distribution of electronic systems")



        #Basic Axes, length can't be changed
        #o03x1=Axes(x_range=[0,3,1],
                        #y_range=[0, 1, 1],
                        #x_length=5,
                        #y_length=3,
                        #tips=True,
        #)

        #Axes with ValueTracker, to change parameters and enable animations
        v03x1=ValueTracker(10)
        o03x1=Axes(x_range=[0,3,1],
                                y_range=[0, 1, 1],
                                x_length=v03x1.get_value(),
                                y_length=3,
                                tips=True,
                                y_axis_config={
                                    #"numbers_to_include":[1,1],

                                    }
                                )
        o03x1_ylb=o03x1.get_y_axis_label("Probability of failure")
        o03x1_xlb=o03x1.get_x_axis_label("t")
        g03x4_labels=VGroup(o03x1_xlb,o03x1_ylb)

        #Functions to indicate the early stage, random stage, and wearout failures
        o03x2=o03x1.plot(lambda x:np.exp(-x)-0.3,
                                x_range=[0,1],
                                use_smoothing=False
                            )


        o03x3=o03x1.plot(lambda x:np.exp(-1)-0.3,
                                x_range=[1,2],
                                use_smoothing=False
                            )


        o03x4=o03x1.plot(lambda x:np.exp(x-3)-0.3,
                                x_range=[2,3],
                                use_smoothing=False
                                )

        g03x5_bathtub=VGroup(o03x2,o03x3,o03x4)

        o03x5=Brace(o03x3)
        o03x6=Brace(o03x2)
        o03x7=Brace(o03x4)
        t05x4=Tex(r"early\\failures")
        t05x5=Tex(r"random\\failures")
        t05x6=Tex(r"wearout\\failures")

        g03x1_ef=VGroup(o03x5,t05x4).arrange(DOWN,buff=0.5).next_to(o03x2,DOWN)
        g03x2_rf=VGroup(o03x6,t05x5).arrange(DOWN,buff=0.5).next_to(o03x3,DOWN)
        g03x3_wf=VGroup(o03x7,t05x6).arrange(DOWN,buff=0.5).next_to(o03x4,DOWN*1.09)


        #!"Electronic devices fail with following distribution", early, random and wearout failures


        self.wait(1)
        self.clear
        v03x1.set_value(10)
        self.play(Create(o03x1))
        self.play(AnimationGroup(*[FadeIn(s) for s in g03x4_labels],lag_ratio=0.5))
        self.wait(1)
        self.play(AnimationGroup(*[Create(s) for s in g03x5_bathtub],lag_ratio=1))

        #Animate the brace fade in after the color shift
        self.play(o03x2.animate.set_color(BLUE_A))
        self.play(FadeIn(g03x1_ef))
        self.wait(1)
        self.play(o03x4.animate.set_color(BLUE_A))
        self.play(FadeIn(g03x3_wf))
        self.wait(1)
        self.play(o03x3.animate.set_color(YELLOW_C))
        self.play(FadeIn(g03x2_rf))

        g03x2_finallineup=VGroup(o03x1,g03x1_ef,g03x2_rf,g03x3_wf,g03x4_labels,g03x5_bathtub,)


        self.wait(1)
        self.clear()


        #!Distingushing the important part of the Bathtub and the nonimportant part of the bathtub

        t04x1_Rt=MathTex(r"R\left(t\right)=",r"e",r"^{-t",r"\lambda}")
        t04x2_Ft=MathTex(r"F\left(t\right)=1-R\left(t\right)")
        g04x1_f=VGroup(t04x1_Rt,t04x2_Ft).arrange(DOWN).move_to(UP*2+RIGHT*2)

        o04x1=Axes(x_range=[0,3,1],
                    y_range=[0, 1.5, 1],
                    x_length=10,
                    y_length=5,
                    tips=True,
                    y_axis_config={
                    "numbers_to_include":[1,1],
                                }
                    ).to_corner(LEFT+DOWN)

        o04x3_ylb=o04x1.get_y_axis_label("Probability of failure")
        o04x4_xlb=o04x1.get_x_axis_label("t")


        o04x5_rt=o04x1.plot(lambda x:np.exp(-x),
                                x_range=[0,3],
                                use_smoothing=False,
                                color=YELLOW_C
                            )
        o04x5_ft=o04x1.plot(lambda x:1-np.exp(-x),
                                x_range=[0,3],
                                use_smoothing=False,
                                color=ORANGE
                            )

        g04x1_initstart=VGroup(o04x1,o04x5_rt,o04x3_ylb,o04x4_xlb)

        self.play(ReplacementTransform(g03x2_finallineup,g04x1_initstart))
        self.wait(1)
        self.wait(1)
        #self.play()

        o04x6 = o04x1.get_graph_label(
            graph=o04x5_rt,
            label=MathTex(r"0.37"),
            x_val=1,
            dot=True,
            direction=UR,)

        o04x7=Line(o04x1.c2p(1,0),o04x1.c2p(1,0.37)).set_color(YELLOW_B)
        o04x8=Line(o04x1.c2p(1,0.37),o04x1.c2p(1,0.63)).set_color(RED_B)

        self.add(o04x7)
        self.play(Create(g04x1_f[0]))
        self.wait(1)
        self.add(o04x5_ft)
        self.add(o04x8)
        self.play(Create(g04x1_f[1]))
        self.wait(1)
        self.clear()


        #!Modeling some examples, headlights for example

        t05x1=(r"For example headlights")

        #!Dive into availability with repair time figures

        t06x1=(r"Availability is dircetly connected to the reliability")

        #!Decreaseing  Reliability is easy

        t07x1=(r"Adding components together increasees variables")

        #!Ambient system influences, look in script about silicon lifetime vs tempature

        t08x1=(r"Decreaseing the reliability even more")

        #!Increase reliability with parallel systems

        t09x1=(r"Increasing the reliability of our system")


        #Big Axes that shows the effect on adding multiple devices in parallel on MTBF

        t10x1=(r"Reliability of parallel systems visualised")


        t10x1=Axes(tips=False,
                 x_range=[0,1,1],
                 y_range=[0,1,1],
                 x_length=12,
                 y_length=5,
                 )


        t10x1.to_corner(LEFT+DOWN)

        t10x2=[]
        g10x1=VGroup()
        for i in range(1,10,1):
            g10x1.add(t10x1.plot
                      (lambda x: 1-(1-exp(-5*x))**i,
                            x_range=[0,1],
                            color=Color(hue=i/10,saturation=1,luminance=0.5)
                        )
                    )

        self.add(t10x1)
        self.play(AnimationGroup(*[FadeIn(s) for s in g10x1],lag_ratio=1))
        self.wait(5)








