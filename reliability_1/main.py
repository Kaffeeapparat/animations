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
#a: arrow


#Frist number O
#1: enumerator

#string y...y
#identifyer for understanding


class Intro(Scene):
    def construct(self):

        #!What is relaiability exactly

        s01x1_hdd=SVGMobject("graphics/harddrive.svg",fill_opacity=1.0).to_corner(LEFT)



        t01x1=Tex(r"What is reliability?",font_size=80).move_to(ORIGIN)
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

        g02x4_bematrix=VGroup(
            *[SVGMobject("graphics/device.svg",
                         stroke_color=Color("green"),
                         fill_color=WHITE,
                         fill_opacity=1.0
                         ).to_corner(LEFT).scale(0.06) for s in range(0,100)])

        #self.play(AnimationGroup(*[Create(s) for s in g02x4_bematrix  ],lag_ratio=0.1))
        self.wait(1)

        #!Calculating lambda

        t02x4_ratep=MathTex(r"\text{rate of failure}",r"\approx\frac{ \text{failed devices} }{ \text{number of devices}\cdot\text{time difference} }")
        t02x5_ratec=MathTex(r"\lambda\phantom{texttexttext}",r"\approx",r"\frac{\Delta n }{\phantom{\text{text}}n\phantom{te}\cdot \phantom{te}\Delta  t\phantom{texttext}}",r"=\frac{1}{\text{MTBF}}=\frac{1}{\text{MTTF}}")

        #g02x5_rate=VGroup(t02x4_ratep,t02x5_ratec)

        self.wait(1)



        v02x01_dn=ValueTracker(0)
        v02x02_dt=ValueTracker(1)
        g02x4_bematrix.add_updater(lambda x: setMatrixColor(x,v02x01_dn.get_value()))

        g02x4_bematrix.arrange_in_grid(cols=20).move_to(UP*2.5+LEFT*0)
        self.play(ReplacementTransform(s02x1_be,g02x4_bematrix))

        self.add(v02x01_dn)
        self.add(v02x02_dt)
        self.play(Create(t02x4_ratep))
        self.wait(1)
        self.play(ReplacementTransform(
            t02x4_ratep,
            t02x5_ratec)
        )
        self.play(FadeOut(t02x5_ratec[3]))

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
            o02x01_n.get_value()/o02x02_dn.get_value()*o02x03_dt.get_value(),
            show_ellipsis=False,
            num_decimal_places=9,
            include_sign=False,
            )


        o02x02_dn.add_updater(lambda x: x.set_value(getMatrixGreenN(g02x4_bematrix)))
        o02x03_dt.add_updater(lambda x: x.set_value(v02x02_dt.get_value()))
        o02x04_lambda.add_updater(lambda x: x.set_value(o02x01_n.get_value()/(o02x02_dn.get_value()*o02x03_dt.get_value())))

        #self.add(index_labels(t02x5_ratec[0]))
        self.play(ShrinkToCenter(t02x5_ratec[0]),FadeIn(o02x04_lambda.move_to(t02x5_ratec[0].get_center())))

        self.play(ShrinkToCenter(t02x5_ratec[2][0:2]),FadeIn(o02x02_dn.move_to(t02x5_ratec[2][0:2].get_center())))

        o02x01_n.move_to(t02x5_ratec[2][3:4].get_center()+UP*0.05)
        self.play(ShrinkToCenter(t02x5_ratec[2][3:4]),FadeIn(o02x01_n.move_to(t02x5_ratec[2][3:4].get_center()+UP*0.05)))

        self.play(ShrinkToCenter(t02x5_ratec[2][5:7]),FadeIn(o02x03_dt.move_to(t02x5_ratec[2][5:7].get_center())))

        #self.add(VGroup(o02x01_n,o02x02_dn,o02x03_dt).arrange(DOWN).to_corner(DOWN,LEFT))

        self.play(v02x01_dn.animate.set_value(99))
        self.wait(10)
        self.play(v02x02_dt.animate.set_value(10000000))
        self.wait(10)
        self.play(v02x01_dn.animate.set_value(50))

        self.wait(1)
        self.clear()

        t02x9=MathTex(r"\text{Electronics are extremly reliable}",r"[\lambda]= 1 FIT = 1\cdot10^{-9}h^{-1}").arrange(DOWN)

        self.add(t02x9)
        self.wait(1)

        #showing rate of 1 and others
        g02x5_bematback=g02x4_bematrix
        self.clear()

        #!Of course  it is only a statistical figure

        t02x6=Tex(r"MTBF/MTTF").move_to(UP*3)
        t02x8=Tex(r"MTBF:",r"Mean Time between failure",r"$\implies$repairable")
        t02x7=Tex(r"MTTF:",r"Mean Time to failure",r"$\implies$unrepairable")

        s02x5_wrench=SVGMobject("graphics/wrench.svg",stroke_color=GREEN,fill_color=GREEN,fill_opacity=1.0).scale(0.5)
        s02x6_rec=SVGMobject("graphics/recycle.svg",stroke_color=RED,fill_color=RED,fill_opacity=1.0).scale(0.5)

        self.add(t02x6)

        g02x6=VGroup(t02x7[0],t02x7[1])
        g02x7=VGroup(t02x8[0],t02x8[1])
        self.add(g02x6.arrange(DOWN))
        self.play(Create(s02x5_wrench.next_to(g02x6,RIGHT)))
        self.add(g02x7.arrange(DOWN).next_to(g02x6,DOWN,buff=2.0))
        self.play(Create(s02x6_rec.next_to(g02x7,RIGHT)))
        self.wait(1)
        self.clear()

class Bathtub(Scene):
    def construct(self):

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
        self.play(o03x2.animate.set_color(BLUE_A))
        self.play(FadeIn(g03x1_ef))
        self.wait(1)
        self.play(o03x4.animate.set_color(BLUE_A))
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
        t04x3_poi=MathTex(r"\frac{1}{\text{MTBF}}",font_size=25)
        t04x4_ylb=Tex(r"R(t)",r"F(t)")
        t04x4_ylb.arrange(DOWN)
        t04x4_ylb[0].set_color(YELLOW_C)
        t04x4_ylb[1].set_color(ORANGE)

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
                                color=ORANGE
                            )

        g04x1_initstart=VGroup(o04x1,o04x5_rt,o04x4_xlb)

        self.play(ReplacementTransform(g03x2_finallineup,g04x1_initstart))
        self.wait(1)
        self.wait(1)
        #self.play()

        o04x6 = o04x1.get_graph_label(
            graph=o04x5_rt,
            label=MathTex(r"0.37"),
            x_val=1,
            dot=True,
            direction=UR,).move_to(UP*1.5)

        o04x7=Line(o04x1.c2p(1,0),o04x1.c2p(1,0.37)).set_color(YELLOW_B)
        o04x8=Line(o04x1.c2p(1,0.37),o04x1.c2p(1,0.63)).set_color(RED_B)

        self.add(o04x7,t04x3_poi.next_to(o04x1.c2p(1,0),DOWN))
        self.play(Create(g04x1_f[0]))
        self.wait(1)
        self.add(o04x5_ft)
        self.add(o04x8)
        self.play(Create(g04x1_f[1]))
        self.add(t04x4_ylb.next_to(o04x4_ylb,RIGHT))

        self.wait(1)
        self.clear()

class Headlightexample(Scene):
    def construct(self):
        #!Modeling some examples, headlights for example

        t05x1=Tex(r"For example headlights")

        #!Dive into availability with repair time figures

        t06x1=Tex(r"MTTR")

class Serialparallel(Scene):
    def construct(self):
        #!In Real world systems are build out of many parts. They influence the reliability, too.


        t07x1=Tex(r"Parallel systems",r"\\ rendundancy").move_to(UP*3+LEFT*4)

        t07x2=Tex(r"Serial systems").move_to(UP*3+RIGHT*4)

        s07x1_beh=SVGMobject("graphics/device.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).scale(0.1).rotate(90)

        s07x2_bev=SVGMobject("graphics/device_connected.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).scale(0.5)

        t07x3_cont=MathTex(r"    ...    ")
        t07x4_cont=MathTex(r"    ...    ")

        g07x1_ser=VGroup()

        #!Decrease reliability with serial systems

        for i in range(0,2):
            g07x1_ser.add(SVGMobject("graphics/device.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.1))

        g07x1_ser.add(t07x3_cont,s07x1_beh)
        g07x1_ser.arrange(RIGHT,buff=0.01).move_to(UP*1.5+RIGHT*4)

        #!Increase reliability with parallel systems

        g07x2_par=VGroup()

        for i in range(0,2):
            g07x2_par.add(SVGMobject("graphics/device_connected.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.1).rotate(90))

        g07x2_par.add(t07x4_cont,s07x2_bev).arrange(RIGHT,buff=0.01).move_to(UP*1.5+LEFT*4)

        self.add(t07x1,t07x2,g07x1_ser,g07x2_par)
        self.wait(1)

        t07x5_sRt=MathTex(r"R_{serial}\left( t \right)=\prod_{i=1}^{i}R_{i}\left( t \right)=R_{1}\left( t \right)\cdot R_{2}\left( t \right)\cdot ...",font_size=35)
        t07x6_pRt=MathTex(r"R_{parallel}\left( t \right)=\prod_{i=1}^{i}F_{i}\left( t \right)=F_{1}\left( t \right)\cdot F_{2}\left( t \right)\cdot ...",font_size=35)

        t07x5_sRt.move_to(RIGHT*3.5)
        t07x6_pRt.move_to(LEFT*3.5)

        self.play(Create(t07x5_sRt),Create(t07x6_pRt))


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
                            color=Color(hue=i/10,saturation=1,luminance=0.5)
                        )
                    )

        self.add(o07x1_axp)
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
                            color=Color(hue=i/10,saturation=1,luminance=0.5),
                            use_smoothing=False,
                        )
                    )

        self.add(o07x2_axs)
        self.play(AnimationGroup(*[FadeIn(s) for s in g07x4_axs],lag_ratio=1))
        self.wait(5)



        self.clear()

        t09x1=Tex(r"Increasing the reliability of our system")

        t09x2=Tex(r"Redundancy")

        t09x3=MathTex(r"r=r-1")

        self.add(t09x3)
        self.wait(1)
        self.clear()



        #Big Axes that shows the effect on adding multiple devices in parallel on MTBF

        t10x1=(r"Reliability of parallel systems visualised")
class Economics(Scene):
    def construct(self):


        t10x1=Axes(tips=False,
                 x_range=[0,1,1],
                 y_range=[0,1,1],
                 x_length=12,
                 y_length=5,
                 )


        o07x2_axs.move_to(DOWN*2+LEFT*4)

        o10x5_fp=lambda x: ((x+1)**3)+x**2+x-3
        def o10x4_fb(i):
            return lambda x: 1-(1-exp(-5*x))**i


        o10x2=[]
        g10x1=VGroup()
        for i in range(1,10,1):
            g10x1.add(o10x1.plot(o10x4_fb(i),
                        x_range=[0,1],
                        color=Color(hue=i/10,saturation=1,luminance=0.5)
                        )
                    )

        o10x3=o10x1.plot(o10x5_fp,
                   color=WHITE)
        #self.add(o10x3)

        self.add(o10x1)
        self.play(AnimationGroup(*[FadeIn(s) for s in g10x1],lag_ratio=1))
        self.wait(2)


        t10x2=MathTex(r"r=0",r"r=1",r"r=2",r"r=3",r"r=4",r"r=5",r"r=6",r"r=7",r"r=8",font_size=20)
        g10x3=VGroup()
        h10x1=[0.05,0.075,0.15,0.25,0.35,0.45,0.55,0.65,0.75]
        for i in range(0,9,1):
            g10x3.add(Rectangle(height=0.5,width=1,fill_color=LIGHT_BROWN,color=YELLOW,fill_opacity=1).move_to(o10x1.c2p(h10x1[i],
                                (o10x4_fb(i+1)(h10x1[i]))
                                ))
                        )
            g10x3.add(t10x2[i].move_to(o10x1.c2p(h10x1[i],
                                (o10x4_fb(i+1)(h10x1[i]))
                                )))

        self.add(g10x3)
        self.wait(1)

        o10x6=Line(o10x1.c2p(0.2,0),o10x1.c2p(0.2,2)).set_color(YELLOW_B)
        self.add(o10x6)
        self.wait(1)

        self.clear()


        #!Ambient system influences, look in script about silicon lifetime vs tempature

class enviroment(Scene):
    def construct(self):
        t11x1=(r"Considering the enviroment")

        s11x1_be=SVGMobject("graphics/device.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).to_corner(LEFT).scale(0.5)
        s11x1_be.move_to(ORIGIN)

        s11x2_heat=SVGMobject("graphics/heat.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).scale(0.5).next_to(s11x1_be,UP*2+RIGHT*2)
        s11x3_voltage=SVGMobject("graphics/voltage.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0).scale(0.5).next_to(s11x1_be,UP*2+LEFT*2)

        a11x1_heat=Arrow().put_start_and_end_on(s11x2_heat.get_center(),s11x1_be.get_center()).scale(0.2)
        a11x2_temp=Arrow().put_start_and_end_on(s11x3_voltage.get_center(),s11x1_be.get_center()).scale(0.2)

        t11x1_hum=MathTex(r"rel.Humidity%")
        t11x2_uv=MathTex(r"UV")
        t11x3_temp=MathTex(r"Temp")
        t11x4_U=MathTex(r"U(t)")
        t11x5_oth=MathTex(r"...")

        t11x6_form=MathTex(r"\lambda=\lambda_{ref}\cdot\pi_{temp}\cdot\pi_{humidity}\cdot\pi_{...}")
        t11x6_form.move_to(DOWN*3)

        self.add(s11x1_be)
        self.wait(0.5)
        self.add(s11x2_heat,s11x3_voltage)
        self.wait(0.5)
        self.add(a11x1_heat,a11x2_temp)

        self.add(t11x6_form)
        self.wait(2)

class availability(Scene):
    def construct(self):
        #! Explaining availability

        s12x1_lampwork=SVGMobject("graphics/lamp_on.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0)
        s12x2_lampnowork=SVGMobject("graphics/lamp_off.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0)
        s12x3_bulbwork=SVGMobject("graphics/lightbulb_on.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0)
        s12x4_bulbnwork=SVGMobject("graphics/lightbulb_off.svg",stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.0)

        s12x1_lampwork.move_to(LEFT*2)
        s12x2_lampnowork.move_to(s12x1_lampwork.get_center()+LEFT*0.2)
        g12x2=VGroup(s12x1_lampwork,s12x2_lampnowork).to_corner(LEFT+UP)

        self.play(Create(s12x2_lampnowork))
        self.wait(1)
        self.play(FadeIn(s12x1_lampwork))
        self.wait(1)
        self.play(FadeOut(s12x1_lampwork))
        self.wait(1)

        t12x1=MathTex(r"How high is the availability\\of the system lamp?")

        t12x2=MathTex(r"\text{V}=text{MTBR}/text{MTTR}\cdot\text{MTTB}")

        t12x3=MathTex(r"MTTR_{change lightbulb}=2h")
        t12x4=MathTex(r"MTBF_{lightbulb}=1000h^{-1}")
        t12x4=MathTex(r"MTBF_{lightbulb}=1000h^{-1}")
        t12x5=MathTex(r"n_{repairs}=5")
        self.wait(1)

        g12x1_f=VGroup(t12x3,t12x4,t12x5).arrange(DOWN).move_to(RIGHT*2)
        self.play(FadeIn(g12x1_f))
        self.wait(1)


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
                bematrix[i].set(stroke_color=Color("white"))





