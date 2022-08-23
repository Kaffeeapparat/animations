from manim import *
from numpy import *
from colour import Color

config.background_color= BLACK
config.quality='high_quality'

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
#a: arrow


#Frist number O
#1: enumerator

#string y...y
#identifyer for understanding

class complete(Scene):
    def construct(self):
        Intro.construct(self)
        Definition.construct(self)
        Bathtub.construct(self)
        RandomFail.construct(self)
        Serialparallel.construct(self)
        Economics.construct(self)
        Enviroment.construct(self)
        Availability.construct(self)

class Intro(Scene):
    def construct(self):

        #!What is relaiability exactly

        s01x1_hdd=SVGMobject("graphics/harddrive.svg",fill_opacity=1.0).to_corner(LEFT)

        t01x1=Tex(r"Understanding reliability",font_size=80).move_to(ORIGIN)
        t01x2_hdd=Tex(r"HDD MTTF\\1 million hours!!!",font_size=30).rotate(PI*-0.1)
        g01x2_hdd=VGroup(s01x1_hdd,t01x2_hdd).arrange(UP, buff=0.1).move_to(DOWN*2+RIGHT*5)

        t01x4=Tex(r"MTTF?\\MTTR???\\ A????",font_size=50).rotate(PI*0.15).move_to(DOWN*2.5+LEFT*2)
        t01x5=Tex(r"Higer V through\\backup Powersupply",font_size=40).rotate(-PI*0.2).move_to(UP*2+RIGHT*5)
        t01x6=Tex(r"Electronics\\seem to never break!",font_size=40).rotate(PI*0.3).move_to(LEFT*5)
        t01x7=Tex(r"High redundancy and high availability!!!",font_size=33).rotate(-PI*0.1).move_to(UP*2+LEFT*1)

        g01x1_title=VGroup(t01x4,g01x2_hdd,t01x5,t01x6,t01x7)


        self.play(Create(t01x1))
        self.play(AnimationGroup(*[FadeIn(s) for s in g01x1_title],lag_ratio=0.5))
        self.wait(1)
        self.clear()

        #!On different elctronic devices like Harddrives are printed some numbers

        #!Will it really run 4 million hours, and why does it seem that modern car break down more regularly

class Definition(Scene):
    def construct(self):

        #!First define the device that gets observed

        t02x1=Tex(r"Definition: A device that runs and fails")

        t02x2=Tex(r"State of the Device:")
        t02x3=Tex(r"defect",r"functioning",font_size=50).arrange(DOWN)
        g02x3_bestate=VGroup(t02x2,t02x3).arrange(DOWN)
        t02x11=Tex(r"Definition",font_size=80)
        t02x12=Tex(r"Device",font_size=60)

        #tex.animate.set_color(RED),
        #be stands for Bauelement, the basic bulding block of devices
        s02x1_be=SVGMobject("graphics/device.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.5)
        s02x2_be=SVGMobject("graphics/device_connected.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.5)
        s02x3_d1=SVGMobject("graphics/diode.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.5)
        s02x4_d2=SVGMobject("graphics/diode2.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.5)
        s02x5_cap=SVGMobject("graphics/cap.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.5)
        s02x8_complexbe=SVGMobject("graphics/complex_device.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).move_to(LEFT*3).scale(0.5)

        self.play(FadeIn(t02x11))
        self.wait(1)
        self.play(FadeOut(t02x11))
        self.clear
        self.wait(1)

        g02x1=VGroup()
        for i in range(1,10,1):
            g02x1.add(SVGMobject("graphics/device_connected.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.3))
        g02x1.arrange(DOWN,buff=0)

        g02x2=VGroup(s02x3_d1,s02x4_d2,s02x5_cap,s02x8_complexbe,s02x1_be)
        s02x1_be=SVGMobject("graphics/device.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.5)


        self.add(s02x1_be)
        o01x1=s02x1_be
        t02x12.move_to(s02x1_be.get_center()+UP)
        self.play(FadeIn(t02x12))

        for i in range(0,5,1):
            self.play(ReplacementTransform(o01x1,g02x2[i]))
            o01x1=g02x2[i]
            self.wait(3)



        self.wait(1)
        g02x3_bestate.move_to(ORIGIN+RIGHT*3)
        self.play(Create(g02x3_bestate))
        self.wait(1)

        self.play(g02x3_bestate[1][1].animate.set_color(GREEN),o01x1.animate.set_color(GREEN))
        self.wait(1)
        self.play(g02x3_bestate[1][0].animate.set_color(RED),o01x1.animate.set_color(RED))
        self.wait(1)
        self.play(FadeOut(g02x3_bestate))

        self.play(ReplacementTransform(o01x1,s02x1_be.move_to(ORIGIN).set_color(GREEN)))

        #Showing the Din Symbol of a resistor and merging iot into different Symbols

        g02x4_bematrix=VGroup(
            *[SVGMobject("graphics/device.svg",
                         stroke_color=Color("green"),
                         fill_opacity=1.0
                         ).to_corner(LEFT).scale(0.06) for s in range(0,100)])
        for i in range(0,100):
            if i < 51:
                g02x4_bematrix[i].set(stroke_color=Color("red"))

        #self.play(AnimationGroup(*[Create(s) for s in g02x4_bematrix  ],lag_ratio=0.1))
        self.wait(1)

        #!Calculating lambda

        t02x4_ratep=MathTex(r"\text{rate of failure}",r"\approx\frac{ \text{failed devices} }{ \text{number of devices}\cdot\text{time difference} }")
        t02x10_ratec=MathTex(r"\lambda\phantom{ }",r"\approx",r"\frac{\Delta n }{\phantom{\text{txt}}n\phantom{te}\cdot \phantom{tetext}\Delta t \phantom{text}}",r"=\frac{1}{\text{MTBF}}=\frac{1}{\text{MTTF}}")
        t02x5_ratec=MathTex(r"\lambda\phantom{ }",r"\approx",r"\frac{\Delta n }{\phantom{\text{txt}}n\phantom{te}\cdot \phantom{tetext}\Delta t \phantom{text}\phantom{te}h}",r"=\frac{1}{\text{MTBF}}=\frac{1}{\text{MTTF}}")

        #g02x5_rate=VGroup(t02x4_ratep,t02x5_ratec)

        self.wait(1)



        v02x01_dn=ValueTracker(50)
        v02x02_dt=ValueTracker(1000000000)
        g02x4_bematrix.add_updater(lambda x: setMatrixColor(x,v02x01_dn.get_value()))

        g02x4_bematrix.arrange_in_grid(cols=20).move_to(UP*2.5+LEFT*0)
        self.play(ReplacementTransform(s02x1_be,g02x4_bematrix),FadeOut(t02x12))

        self.add(v02x01_dn)
        self.add(v02x02_dt)
        self.wait(1)
        self.play(Create(t02x4_ratep))
        self.wait(1)
        self.play(ReplacementTransform(
            t02x4_ratep,
            t02x10_ratec)
        )
        self.wait(1)
        o02x05_origindot=Dot()
        self.play(ReplacementTransform(t02x10_ratec,t02x5_ratec),FadeOut(t02x5_ratec[3]))
        self.wait(1)
        g02x8=VGroup(t02x5_ratec[0],t02x5_ratec[1],t02x5_ratec[2])
        g02x8.generate_target()
        g02x8.target.shift(RIGHT*3.5)
        self.play(MoveToTarget(g02x8))
        self.wait(1)
        o02x01_n=DecimalNumber(
            100,
            show_ellipsis=False,
            num_decimal_places=0,
            include_sign=False,
        )

        o02x02_dn=(DecimalNumber(
            v02x01_dn.get_value(),
            show_ellipsis=False,
            num_decimal_places=0,
            include_sign=False,
        ))

        o02x03_dt=DecimalNumber(
            v02x02_dt.get_value(),
            show_ellipsis=False,
            num_decimal_places=0,
            include_sign=False,
        )



        o02x04_lambda=DecimalNumber(
            100/o02x02_dn.get_value()*o02x03_dt.get_value(),
            show_ellipsis=False,
            num_decimal_places=9,
            include_sign=False,
            )


        o02x02_dn.add_updater(lambda x: x.set_value(getMatrixGreenN(g02x4_bematrix)))
        o02x03_dt.add_updater(lambda x: x.set_value(v02x02_dt.get_value()))
        o02x04_lambda.add_updater(lambda x: x.set_value(100/(o02x02_dn.get_value()*o02x03_dt.get_value())))

        #self.add(index_labels(t02x5_ratec[0]))
        self.play(ShrinkToCenter(t02x5_ratec[0]),FadeIn(o02x04_lambda.move_to(t02x5_ratec[0].get_center())))
        self.wait(1)
        self.play(ShrinkToCenter(t02x5_ratec[2][0:2]),FadeIn(o02x02_dn.move_to(t02x5_ratec[2][0:2].get_center())))

        self.wait(1)
        o02x01_n.move_to(t02x5_ratec[2][3:4].get_center()+UP*0.05)
        self.play(ShrinkToCenter(t02x5_ratec[2][3:4]),FadeIn(o02x01_n.move_to(t02x5_ratec[2][3:4].get_center()+UP*0.11)))


        self.wait(1)
        self.play(ShrinkToCenter(t02x5_ratec[2][5:7]),FadeIn(o02x03_dt.move_to(t02x5_ratec[2][5:7].get_center())))

        #self.add(VGroup(o02x01_n,o02x02_dn,o02x03_dt).arrange(DOWN).to_corner(DOWN,LEFT))

        self.play(v02x01_dn.animate.set_value(99))
        self.wait(2)
        self.play(v02x01_dn.animate.set_value(2))
        self.wait(2)
        self.play(v02x01_dn.animate.set_value(50))
        self.wait(2)
        self.play(v02x02_dt.animate.set_value(50000000))
        self.wait(2)
        self.play(v02x01_dn.animate.set_value(99))
        self.wait(2)
        self.play(v02x01_dn.animate.set_value(70))
        self.wait(2)

        g02x9=VGroup(g02x4_bematrix)

        t02x9=MathTex(r"\text{Electronics are extremly reliable}",r"[\lambda]= 1 FIT = 1\cdot10^{-9}h^{-1}").arrange(DOWN)


        self.play(ReplacementTransform(g02x9,t02x9),FadeOut(o02x01_n,o02x02_dn,o02x03_dt,o02x04_lambda,t02x5_ratec[0],t02x5_ratec[1],t02x5_ratec[2]))
        self.wait(1)

        #showing rate of 1 and others
        g02x5_bematback=g02x4_bematrix
        self.play(FadeOut(t02x9))
        self.wait(1)

        #!Of course  it is only a statistical figure

        t02x6=MathTex(r"\text{MTBF,MTTF}=\frac{1}{\lambda}").move_to(UP*2)
        t02x8=Tex(r"MTBF:",r"Mean Time Between Failure",r"$\implies$repairable")
        t02x7=Tex(r"MTTF:",r"Mean Time To Failure",r"$\implies$unrepairable").move_to(DOWN*2)
        s02x5_wrench=SVGMobject("graphics/wrench.svg",stroke_color=GREEN,fill_color=GREEN,fill_opacity=1.0).scale(0.5)
        s02x6_rec=SVGMobject("graphics/recycle.svg",stroke_color=RED,fill_color=RED,fill_opacity=1.0).scale(0.5)

        self.play(Create(t02x6))
        self.wait(1)

        g02x6=VGroup(t02x7[0],t02x7[1])
        g02x7=VGroup(t02x8[0],t02x8[1])
        self.play(Create(g02x6.arrange(DOWN)))
        self.wait(1)
        self.play(Create(s02x5_wrench.next_to(g02x6,RIGHT)))
        self.wait(1)
        self.play(Create(g02x7.arrange(DOWN).move_to(DOWN*2)))
        self.wait(1)
        self.play(Create(s02x6_rec.next_to(g02x7,RIGHT)))
        self.wait(1)
        self.clear()

class Bathtub(Scene):
    def construct(self):

        #!Bathtub curve
        t03x1=Tex(r"Typical failure distribution of electronic systems")
        t03x8=Tex(r"Failure distributions",font_size=50)

        self.play(FadeIn(t03x8))
        self.wait(1)
        self.play(FadeOut(t03x8))
        self.wait(1)

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
        o03x1_ylb=o03x1.get_y_axis_label(r"\lambda")
        o03x1_xlb=o03x1.get_x_axis_label(r"t")
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

        o03x8=o03x1.plot(lambda x:np.exp(-x),
                                x_range=[0,1],
                                use_smoothing=False,
                                color=RED
                            )

        o03x9=o03x1.plot(lambda x:np.exp(x-2),
                                x_range=[1,2],
                                use_smoothing=False,
                                color=RED
                            )



        g03x5_bathtub=VGroup(o03x2,o03x3,o03x4)
        g03x6_mechtub=VGroup(o03x8,o03x9)

        o03x5=Brace(o03x3)
        o03x6=Brace(o03x2)
        o03x7=Brace(o03x4)
        t03x4=Tex(r"early\\failures")
        t03x5=Tex(r"random\\failures")
        t03x6=Tex(r"wearout\\failures")
        t03x7=Tex(r"mechanical\\systems")

        g03x1_ef=VGroup(o03x5,t03x4).arrange(DOWN,buff=0.5).next_to(o03x2,DOWN)
        g03x2_rf=VGroup(o03x6,t03x5).arrange(DOWN,buff=0.5).next_to(o03x3,DOWN)
        g03x3_wf=VGroup(o03x7,t03x6).arrange(DOWN,buff=0.5).next_to(o03x4,DOWN*1.09)
        t03x7.next_to(o03x8,buff=-1.1)


        #!"Electronic devices fail with following distribution", early, random and wearout failures


        self.wait(1)
        self.clear
        v03x1.set_value(10)
        self.play(Create(o03x1))
        self.play(AnimationGroup(*[FadeIn(s) for s in g03x4_labels],lag_ratio=0.5))
        self.wait(1)
        self.play(AnimationGroup(*[Create(s) for s in g03x5_bathtub],lag_ratio=1))

        #Animate the brace fade in after the color shift
        self.play(o03x2.animate.set_color(BLUE_D))
        self.play(FadeIn(g03x1_ef))
        self.wait(1)
        self.play(o03x4.animate.set_color(BLUE_D))
        self.play(FadeIn(g03x3_wf))
        self.wait(1)
        self.play(o03x3.animate.set_color(YELLOW_C))
        self.play(FadeIn(g03x2_rf))

        self.wait(1)
        self.play(Create(g03x6_mechtub))
        self.play(FadeIn(t03x7))
        self.wait(1)
        self.clear()

        g03x2_finallineup=VGroup(o03x1,g03x1_ef,g03x2_rf,g03x3_wf,g03x4_labels,g03x5_bathtub,)


        self.wait(1)
        self.clear()


        #!Distingushing the important part of the Bathtub and the nonimportant part of the bathtub

class RandomFail(Scene):
    def construct(self):

        t04x1_Rt=MathTex(r"R\left(t\right)=",r"e",r"^{-t",r"\lambda}")
        t04x2_Ft=MathTex(r"F\left(t\right)=1-R\left(t\right)")
        g04x1_f=VGroup(t04x1_Rt,t04x2_Ft).arrange(DOWN).move_to(UP*2+RIGHT*2)
        t04x3_poi=MathTex(r"\text{MTBF,MTTF}",font_size=40)
        t04x4_ylb=Tex(r"R(t)",r"F(t)")
        t04x4_ylb.arrange(DOWN)
        t04x4_ylb[0].set_color(YELLOW_C)
        t04x4_ylb[1].set_color(BLUE_D)

        t04x5_val=MathTex(r"0.63",r"0.37")
        t04x5_val.arrange(DOWN)
        t04x5_val[0].set_color(BLUE_D)
        t04x5_val[1].set_color(YELLOW_C)

        o04x1=Axes(x_range=[0,3,1],
                    y_range=[0, 1.5, 1],
                    x_length=10,
                    y_length=5,
                    tips=True,
                    y_axis_config={
                    "numbers_to_include":[1,1],
                                }
                    ).to_corner(LEFT+DOWN).move_to(DOWN*0.5)

        o04x4_xlb=o04x1.get_x_axis_label("t")
        o04x4_ylb=o04x1.get_y_axis_label("t")


        o04x5_rt=o04x1.plot(lambda x:np.exp(-x),
                                x_range=[0,3],
                                use_smoothing=False,
                                color=YELLOW_C
                            )
        o04x5_ft=o04x1.plot(lambda x:1-np.exp(-x),
                                x_range=[0,3],
                                use_smoothing=False,
                                color=BLUE
                            )

        t04x4_ylb.next_to(o04x4_ylb,RIGHT)
        g04x1_initstart=VGroup(o04x1,o04x4_xlb,t04x4_ylb[0])

        self.play(Create(g04x1_initstart))
        self.play(Create(o04x5_rt,run_time=2))
        self.wait(1)
        self.wait(1)
        #self.play()

        o04x6 = o04x1.get_graph_label(
            graph=o04x5_rt,
            label=MathTex(r"0.37"),
            x_val=1,
            dot=True,
            direction=UR,).move_to(UP*1.5)

        o04x7=Line(o04x1.c2p(1,0),o04x1.c2p(1,0.37)).set_color(WHITE)
        o04x8=Line(o04x1.c2p(1,0.37),o04x1.c2p(1,0.63)).set_color(WHITE)

        t04x5_val.next_to(o04x8,RIGHT)

        self.play(Create(o04x7))
        self.play(FadeIn(t04x3_poi.next_to(o04x1.c2p(1,0),DOWN)))
        self.play(Create(g04x1_f[0]))
        self.wait(1)
        self.play(Create(o04x5_ft,run_time=2),FadeIn(t04x4_ylb[1]))
        self.play(Create(o04x8))
        self.play(Create(g04x1_f[1]))
        self.wait(1)
        self.play(FadeIn(t04x5_val))


        self.wait(1)
        self.clear()

class Headlightexample(Scene):
    def construct(self):
        #!Modeling some examples, headlights for example

        t05x1=Tex(r"For example headlights")

        #!Dive into availability with repair time figures

        t06x1=Tex(r"MTTR")

        self.clear()

class Serialparallel(Scene):
    def construct(self):
        #!In Real world systems are build out of many parts. They influence the reliability, too.

        t07x8=Tex(r"Evaluating serial and parallel systems",font_size=50)

        self.play(FadeIn(t07x8))
        self.wait(1)
        self.play(FadeOut(t07x8))
        self.wait(1)

        t07x1=Tex(r"Parallel systems").move_to(UP*3+LEFT*4)

        t07x2=Tex(r"Serial systems").move_to(UP*3+RIGHT*4)

        s07x1_beh=SVGMobject("graphics/device.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).scale(0.2)

        s07x2_bev=SVGMobject("graphics/device_connected.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).rotate(PI*0.5).scale(0.3)

        t07x3_cont=MathTex(r".     ...     .")
        t07x4_cont=MathTex(r"      ...      ")

        g07x1_ser=VGroup()

        #!Decrease reliability with serial systems

        for i in range(0,2):
            g07x1_ser.add(SVGMobject("graphics/device.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.2))

        g07x1_ser.add(t07x3_cont,s07x1_beh)
        g07x1_ser.arrange(RIGHT,buff=-0.04).move_to(UP*1.5+RIGHT*4)

        #!Increase reliability with parallel systems

        g07x2_par=VGroup()

        for i in range(0,4):
            g07x2_par.add(SVGMobject("graphics/device_connected.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).rotate(PI*0.5).scale(0.3))

        g07x2_par.add(t07x4_cont,s07x2_bev).arrange(RIGHT,buff=-0.05).move_to(UP*1.5+LEFT*4)

        self.play(FadeIn(t07x1[0]))
        self.play(Create(g07x2_par))
        self.wait(1)

        t07x5_sRt=MathTex(r"R_{serial}\left( t \right)=\prod_{i=1}^{i}R_{i}\left( t \right)=R_{1}\left( t \right)\cdot R_{2}\left( t \right)\cdot ...",font_size=35)
        t07x6_pRt=MathTex(r"R_{parallel}\left( t \right)=\prod_{i=1}^{i}F_{i}\left( t \right)=F_{1}\left( t \right)\cdot F_{2}\left( t \right)\cdot ...",font_size=35)

        t07x5_sRt.move_to(RIGHT*3.5)
        t07x6_pRt.move_to(LEFT*3.5)

        self.play(Create(t07x6_pRt))


        o07x1_axp=Axes(tips=False,
                 x_range=[0,1,1],
                 y_range=[0,1,1],
                 x_length=5,
                 y_length=2,
                 )


        o07x1_axp.move_to(DOWN*2+LEFT*4)

        h07x1=[]
        g07x3_axp=VGroup()
        for i in range(1,10,1):
            g07x3_axp.add(o07x1_axp.plot
                      (lambda x: 1-(1-exp(-5*x))**i,
                            x_range=[0,1],
                            color=Color("red",hue=(i-0.9999)/(13),)
                        )
                    )

        self.play(FadeIn(o07x1_axp))
        self.play(AnimationGroup(*[FadeIn(s) for s in g07x3_axp],lag_ratio=1))
        self.wait(5)



        o07x2_axs=Axes(tips=False,
                 x_range=[0,1,1],
                 y_range=[0,1,1],
                 x_length=5,
                 y_length=2,
                 )


        o07x2_axs.move_to(DOWN*2+RIGHT*4)

        h07x1=[]
        g07x4_axs=VGroup()
        for i in range(1,10,1):
            g07x4_axs.add(o07x2_axs.plot
                      (lambda x: ((exp(-5*x))**i),
                            x_range=[0,1,0.001],
                            color=Color("red",hue=(i-0.9999)/(13),),
                            use_smoothing=False,
                        )
                    )
        self.play(FadeIn(t07x2))
        self.wait(1)
        self.play(Create(g07x1_ser))
        self.wait(1)
        self.play(Create(t07x5_sRt))
        self.wait(1)
        self.play(FadeIn(o07x2_axs))
        self.play(AnimationGroup(*[FadeIn(s) for s in g07x4_axs],lag_ratio=1))
        self.wait(5)



        self.clear()

        t09x1=Tex(r"Increasing the reliability of our system")

        t09x2=Tex(r"Redundancy")

        t09x3=MathTex(r"r=n_{devices}-1")

        g09x1=VGroup(t09x2,t09x3).arrange(DOWN)

        self.add(t09x1)
        self.add()
        self.wait(1)
        self.clear()



        #Big Axes that shows the effect on adding multiple devices in parallel on MTBF

class Economics(Scene):
    def construct(self):
        t10x1=Tex(r"Economics for parallel systems")


        o10x1=Axes(tips=False,
                 x_range=[0,1,1],
                 y_range=[0,1,1],
                 x_length=12,
                 y_length=5,
                 )


        o10x1.to_corner(DOWN+LEFT)

        o10x5_fp=lambda x: ((x+1)**3)+x**2+x-3
        def o10x4_fb(i):
            return lambda x: 1-(1-exp(-5*x))**i


        o10x2=[]
        g10x1=VGroup()
        for i in range(1,10,1):
            g10x1.add(o10x1.plot(o10x4_fb(i),
                        x_range=[0,1,0.001],
                        color=Color("red",hue=(i-0.9999)/(13)),
                        use_smoothing=False
                        )
                    )

        o10x3=o10x1.plot(o10x5_fp,
                   color=WHITE)
        #self.add(o10x3)
        #self.play(FadeIn(t10x1.move_to(UP*3)))
        self.add(o10x1)
        self.play(AnimationGroup(*[FadeIn(s) for s in g10x1],lag_ratio=1))
        self.wait(2)

        t10x2=MathTex(r"r=0",r"r=1",r"r=2",r"r=3",r"r=4",r"r=5",r"r=6",r"r=7",r"r=8",r"r=9",font_size=20)
        g10x3=VGroup()
        h10x1=[0.00,0.05,0.08 ,0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.9]
        for i in range(1,10,1):
            g10x3.add(Rectangle(height=0.5,width=1,fill_color=LIGHT_BROWN,color=Color("red",hue=(i-0.9999)/(13),),fill_opacity=1).move_to(o10x1.c2p(h10x1[i],
                                (o10x4_fb(i)(h10x1[i]))
                                ))
                        )
            g10x3.add(t10x2[i].move_to(o10x1.c2p(h10x1[i],
                                (o10x4_fb(i)(h10x1[i]))
                                )))

        self.play(AnimationGroup(*[Create(s) for s in g10x3],lag_ratio=1,run_time=3))
        self.wait(1)



        t10x3=MathTex(r"MTBF,MTTF ",font_size=30)
        o10x6=Line(o10x1.c2p(0.2,0),o10x1.c2p(0.2,1)).set_color(YELLOW_B)
        g10x4=VGroup(o10x6,t10x3)
        t10x3.next_to(o10x6,DOWN)
        self.add(g10x4)
        self.wait(1)


        self.wait(1)
        h10x2=o10x1.c2p(0.1,0.5)
        h10x3=o10x1.c2p(0.2,1)

        o10x7=Rectangle(height=1*o10x1.get_y_unit_size(),width=0.2*o10x1.get_x_unit_size(),fill_opacity=0.5,fill_color=GREEN,stroke_opacity=1,stroke_width=0).move_to(h10x2)
        self.wait(1)

        h10x2=[2,4,5,6,7]

        for i in h10x2:
            self.play(FadeOut(g10x3[i*2],g10x3[(i*2+1)]))
            self.play(FadeOut(g10x1[i]))
        self.wait(2)

        self.play(FadeIn(o10x7))
        self.wait(2)
        self.clear()

class Enviroment(Scene):
    def construct(self):
        #!Ambient system influences, look in script about silicon lifetime vs tempature

        t11x1=Tex(r"Enviromental Factors",font_size=50)
        self.play(FadeIn(t11x1))
        self.wait(1)
        self.play(FadeOut(t11x1))
        self.wait(1)

        t11x7=Tex(r"Enviromental Factors",font_size=50)
        t11x7.move_to(UP*3)

        s11x1_be=SVGMobject("graphics/device.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.5)
        s11x1_be.move_to(DOWN)
        s11x2_heat=SVGMobject("graphics/heat.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).scale(0.5).next_to(s11x1_be,UP*3+RIGHT*3)
        s11x3_voltage=SVGMobject("graphics/voltage.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).scale(0.5).next_to(s11x1_be,UP*3+LEFT*3)

        a11x1_heat=Arrow().put_start_and_end_on(s11x2_heat.get_center(),s11x1_be.get_center()).scale(0.3)
        a11x2_temp=Arrow().put_start_and_end_on(s11x3_voltage.get_center(),s11x1_be.get_center()).scale(0.3)

        t11x1_hum=MathTex(r"rel.Humidity%")
        t11x2_uv=MathTex(r"UV")
        t11x3_temp=MathTex(r"Temp")
        t11x4_U=MathTex(r"U(t)")
        t11x5_oth=MathTex(r"...").next_to(s11x1_be,UP*9)

        a11x3_oth=Arrow().put_start_and_end_on(t11x5_oth.get_center(),s11x1_be.get_center()).scale(0.3)

        t11x6_form=MathTex(r"\lambda=\lambda_{ref}\cdot\pi_{temp}\cdot\pi_{humidity}\cdot\pi_{...}")
        t11x6_form.move_to(DOWN*3)

        g11x1=(s11x2_heat,a11x1_heat,s11x3_voltage,a11x2_temp,t11x5_oth,a11x3_oth)

        self.add(s11x1_be)
        self.wait(0.5)
        s=range(0,1)
        self.play(Create(s11x2_heat),Create(a11x1_heat))
        self.wait(1)
        self.play(s11x2_heat.animate.set(color=RED))
        self.wait(2)
        self.play(Create(s11x3_voltage),Create(a11x2_temp))
        self.wait(1)
        self.play(s11x3_voltage.animate.set(color=RED))
        self.wait(2)
        self.play(Create(t11x5_oth),Create(a11x3_oth))
        self.wait(1)
        self.play(t11x5_oth.animate.set(color=RED))
        self.wait(2)
        self.play(Create(t11x6_form))
        self.wait(2)
        self.clear()

class Availability(Scene):
    def construct(self):
        #! Explaining availability

        t12x10=Tex(r"Availability",font_size=50)

        self.play(FadeIn(t12x10))
        self.wait(1)
        self.play(FadeOut(t12x10))
        self.wait(1)


        t12x1=Tex(r"How high is the availability of a system",font_size=50).move_to(UP*3)
        t12x2=MathTex(r"\text{A}=\frac{\text{MTBR}}{\text{MTBR}\cdot\text{MTTR}}")
        t12x4=MathTex(r"MTTR_{changelightbulb}=2h",r"MTTR_{system}=HIGH",r"MTTR_{system}=LOW")
        t12x3=MathTex(r"MTBF_{lightbulb}=1000h^{-1}",r"MTBF_{repair}=LOW")
        t12x5=MathTex(r"MTBF_{}=1000h^{-1}")
        t12x6=MathTex(r"0.998",r"=\frac{1000}{1000\cdot{2}")
        t12x7=MathTex(r"0.002",r"=1- \frac{1000}{1000\cdot{2}")

        t12x8=MathTex(r"A=",r"\text{LOW}=\frac{\text{LOW}}{\text{LOW}\cdot\text{HIGH}}")
        t12x9=MathTex(r"A=",r"\text{HIGH}=\frac{\text{LOW}}{\text{LOW}\cdot\text{LOW}}")

        s12x1_lampwork=SVGMobject("graphics/lamp_on.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0)
        s12x2_lampnowork=SVGMobject("graphics/lamp_off.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0)
        s12x3_bulbwork=SVGMobject("graphics/lightbulb_on.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0)
        s12x4_bulbnwork=SVGMobject("graphics/lightbulb_off.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0)
        s12x5_complexdevice=SVGMobject("graphics/complex_device.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0)


        s12x1_lampwork.move_to(LEFT*2)
        s12x2_lampnowork.move_to(s12x1_lampwork.get_center()+LEFT*0.2).set
        g12x2=VGroup(s12x1_lampwork,s12x2_lampnowork)

        #self.play(Create(t12x1))
        self.wait(1)

        self.play(Create(s12x2_lampnowork))
        self.wait(1)
        self.play(FadeIn(s12x1_lampwork))
        self.wait(0.5)
        self.play(s12x1_lampwork.animate.set(stroke_color=GREEN))
        self.wait(1)
        self.play(FadeOut(s12x1_lampwork))
        self.wait(1)
        self.play(s12x2_lampnowork.animate.set(stroke_color=RED))
        self.wait(1)
        self.play(FadeIn(s12x1_lampwork),FadeOut(s12x2_lampnowork))
        self.wait(1)

        s12x2_lampnowork.set(color=WHITE)
        s12x1_lampwork.set(color=WHITE)
        self.play(g12x2.animate.to_corner(LEFT))
        self.wait(1)


        g12x1_f=VGroup(t12x2,t12x3[0],t12x4[0],t12x5).arrange(DOWN).move_to(RIGHT*2)
        self.play(FadeIn(g12x1_f[0]))
        self.wait(1)
        #self.add(index_labels(t12x2[0]))
        self.wait(2)
        self.play(g12x1_f[0][0][2:6].animate.set(color=YELLOW),g12x1_f[0][0][7:11].animate.set(color=YELLOW))
        self.wait(1)
        self.play(FadeIn(g12x1_f[1]))
        self.wait(1)

        self.play(g12x1_f[0][0][1:6].animate.set(color=WHITE),g12x1_f[0][0][6:11].animate.set(color=WHITE))
        self.play(g12x1_f[0][0][12:16].animate.set(color=YELLOW))
        self.wait(1)
        self.play(FadeIn(g12x1_f[2]))
        self.wait(1)
        self.play(g12x1_f[0][0][12:16].animate.set(color=WHITE))

        #self.play(FadeIn(g12x1_f[1:3]))
        self.wait(1)

        t12x6.move_to((g12x1_f [0].get_center()))
        t12x7.move_to(t12x6.get_center())
        self.play(ReplacementTransform(g12x1_f[0],t12x6))
        self.wait(1)
        self.play(s12x1_lampwork.animate.set(stroke_color=GREEN),s12x2_lampnowork.animate.set(stroke_color=GREEN),t12x6[0].animate.set(color=GREEN))
        self.wait(1)
        self.play(ReplacementTransform(t12x6,t12x7))
        self.wait(1)
        self.play(t12x7[0].animate.set(color=RED),s12x2_lampnowork.animate.set(stroke_color=RED),FadeOut(s12x1_lampwork))
        self.wait(2)

        t12x2=MathTex(r"\text{A}=\frac{\text{MTBR}}{\text{MTBR}\cdot\text{MTTR}}").move_to(g12x1_f[0].get_center())
        self.play(ReplacementTransform(g12x2,s12x5_complexdevice.move_to(g12x2.get_center())),ReplacementTransform(t12x7,t12x2),FadeOut(t12x4[0]),FadeOut(t12x3[0]))

        self.play(FadeIn(t12x3[1].move_to(t12x3[0].get_center())))
        self.play(FadeIn(t12x4[1].move_to(t12x4[0].get_center())))

        self.play(ReplacementTransform(t12x2,t12x8.move_to(t12x2.get_center())))
        self.wait(1)

        self.play(s12x5_complexdevice.animate.set(stroke_color=RED),t12x4[1][11:15].animate.set(color=RED))
        #self.add(index_labels(t12x4[1]))
        self.wait(3)


        #self.play(ReplacementTransform(t12x9))

        self.play(FadeIn(t12x4[2].move_to(t12x4[0].get_center())),FadeOut(t12x4[1]))
        #self.play(FadeIn(t12x3[1].move_to(t12x3[0].get_center())))
        self.play(ReplacementTransform(t12x8,t12x9.move_to(t12x2.get_center())))
        self.wait(1)

        self.play(s12x5_complexdevice.animate.set(stroke_color=GREEN),t12x4[2][11:14].animate.set(color=GREEN))
        #self.add(index_labels(t12x4[1]))
        self.wait(1)
        #self.play(FadeIn())

        self.wait(1)

class endcard(Scene):
    def construct(self):
        t13x1=Tex(r"Thanks for watching",font_size=50).move_to(UP*3)
        t13x2=Tex(r"Further resources in the video describtion:",font_size=40).move_to(UP*0.5,)
        t13x3=Tex(r"-Sourcecode for the animation",r"-Book with more detailed animation",font_size=40).arrange(DOWN).next_to(t13x2,DOWN)
        t13x3=BulletedList(r"Sourcecode for the animation",r"Book with more detailed animation",r"Credits", height=4, width=4).arrange(DOWN,center=False, aligned_edge=LEFT).next_to(t13x2,DOWN)
        t13x4=Tex(r"Enjoy!",font_size=50)

        self.play(FadeIn(t13x1))
        self.wait(1)
        self.play(Create(t13x2))
        self.wait
        self.play(Create(t13x3))
        self.wait(1)

        self.wait(0.5)
        self.play(FadeOut(t13x1,t13x2,t13x3))
        self.wait(1)
        self.play(FadeIn(t13x4))
        self.wait(1)
        self.play(FadeOut(t13x4))
        self.wait(1)




#At the end I was not sure whether to keep in the title cards or not. Since I done most editing up to that point
#the Titlecards are created here seperatly
class afterthoughts(Scene):
    def construct(self):
        t14x1=Tex(r"Definition",font_size=80)
        t14x2=Tex(r"Failure distributions",font_size=80)
        t14x3=Tex(r"Evaluating serial and parallel systems",font_size=80)
        t14x4=Tex(r"Economics for parallel systems",font_size=80)
        t14x5=Tex(r"Enviromental Factors",font_size=80)
        t14x6=Tex(r"Availability",font_size=80)
        t14x7=Tex(r"*63\%",font_size=120)

        self.clear()
        self.wait(1)
        self.play(FadeIn(t14x1))
        self.wait(1)
        self.play(FadeOut(t14x1))

        self.clear()
        self.wait(1)
        self.play(FadeIn(t14x2))
        self.wait(1)
        self.play(FadeOut(t14x2))

        self.clear()
        self.wait(1)
        self.play(FadeIn(t14x3))
        self.wait(1)
        self.play(FadeOut(t14x3))

        self.clear()
        self.wait(1)
        self.play(FadeIn(t14x4))
        self.wait(1)
        self.play(FadeOut(t14x4))

        self.clear()
        self.wait(1)
        self.play(FadeIn(t14x5))
        self.wait(1)
        self.play(FadeOut(t14x5))

        self.clear()
        self.wait(1)
        self.play(FadeIn(t14x6))
        self.wait(1)
        self.play(FadeOut(t14x6))

        self.clear()
        self.add(t14x7)
        self.wait()


def getMatrixGreenN(resgroup):
    x=0
    gr=Color("green")
    for i in range(0,100):
        if(resgroup[i].get_stroke_color()==gr):
            x=x+1
    if x==0:
        return 0.001
    return x

def setMatrixColor(bematrix,trackervalue):
    for i in range(0,100):
        if (i < trackervalue):
                bematrix[i].set(stroke_color=Color("green"))
        if (i >= trackervalue):
                bematrix[i].set(stroke_color=Color("red"))





