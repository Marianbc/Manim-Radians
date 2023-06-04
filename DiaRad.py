from manim import *

class rollOut2(Scene):
    def construct(self):
        # Explaining Diameter
        title = Title("Diameter of a unit circle", match_underline_width_to_text= True, font_size= 35, underline_buff= 0.1)
        title[0][15:len(title[0])].set_color("#6df207")
        self.add(title)
        ang = ValueTracker(0)
        rad = 1
        arc1 = Circle(radius=rad).move_to([-4,0,0], aligned_edge=DOWN)
        def arcUpdater1(mobj): 
            arc = Arc(
                    radius = rad,
                    start_angle=ang.get_value(),
                    angle=2*PI-ang.get_value()
            ).rotate(1.5*PI-ang.get_value())
            arc.shift((rad*ang.get_value() - arc.get_start()[0] - 4)*RIGHT - arc.get_start()[1]*UP)
            mobj.become(arc)
        arc1.add_updater(arcUpdater1)
        line1 = always_redraw(lambda:
                Line(
                    start=[-4,0,0],
                    end=[rad*ang.get_value() - 4,0,0]
                )
        )

        diameter = Line(start= arc1.get_left(), end= arc1.get_right())
        dia_tex = always_redraw(lambda: Tex("d", font_size= 35).next_to(diameter, DOWN, buff= 0.3))
        numberline = NumberLine(x_range= [0,2*PI, 1], numbers_to_include= [0,1,2,3,4,5,6]).shift(DOWN * 0.4 + LEFT * 0.85)

        self.add(arc1, line1, numberline, diameter, dia_tex)
        self.play(diameter.animate.shift(DOWN * 2 + RIGHT * 1))

        dia_s = list()
        dia_tex_s = list()
        dia_s.append(diameter)
        dia_tex_s.append(dia_tex)
        pre = diameter
        #colors = ["#072bf2", "#f2076d"]
        for i in range(0,2):
            d = pre.copy()
            #d.set_color(colors[i])

            self.play(ang.animate.increment_value(2),
                      rate_func= rate_functions.linear)
            self.play(Rotate(
                d,
                about_point= d.get_right(),
                angle= PI
            ))
            
            t = dia_tex.copy().next_to(d, DOWN, buff= 0.3)
            self.add(d, t)

            dia_s.append(d)
            dia_tex_s.append(t)
            pre = d
        self.play(ang.animate.increment_value(2),
                rate_func= rate_functions.linear)
        
        self.wait(1)
        self.play(ang.animate.increment_value(0.14),
                rate_func= rate_functions.linear)
        line = Line(start= dia_s[2].get_right(), end= dia_s[2].get_right() - [0.14*2,0,0], color= RED)
        self.add(line)
        self.play(Rotate(
            line,
            about_point= line.get_right(),
            angle= PI   
        ))
        brace = Brace(line, DOWN, buff= 0.2, color= RED)
        rem = Tex("0.14 d", font_size= 35).next_to(brace, DOWN)
        dia_tex_s.append(rem)
        self.play(Create(brace), Write(rem), run_time= 1)
        self.wait(2)
        self.play(FadeOut(brace))

        pre = dia_tex_s[0]
        pluses = list()
        for i in range(1,len(dia_tex_s)):
            plus = Tex("+", font_size= 30).next_to(pre, RIGHT, buff= 0.2)
            pluses.append(plus)
            self.play(Create(plus))
            self.play(dia_tex_s[i].animate.next_to(plus, RIGHT))
            pre = dia_tex_s[i]
        all = MathTex("= ( 1 + 1 + 1 + 0.14)d = 3.14 d = \pi d", font_size= 30).next_to(pre, DOWN)
        self.play(Create(all))
        self.wait(3)

        self.play(FadeOut(VGroup(VGroup(*dia_tex_s), all, VGroup(*pluses), VGroup(*dia_s), line)))

        self.play(ang.animate.increment_value(-2*PI), run_time= 2)

        # Explaining Radius
        title_rad = Tex("Radius", font_size= 35).move_to(title[0][0:8].get_center())
        self.play(ReplacementTransform(title[0][0:8], title_rad))

        rad_line = Line(start= arc1.get_center(), end= arc1.get_right())
        rad_tex = always_redraw(lambda: Tex("r", font_size= 35).next_to(rad_line, DOWN, buff= 0.3))
        
        
        self.play(Create(rad_line), Write(rad_tex)) 
        self.play(rad_line.animate.shift(DOWN * 2.2 + RIGHT * 0.15))
        rad_tex.clear_updaters()

        self.play(ang.animate.increment_value(1))

        rad_lines = list()
        rad_texs = list()
        rad_lines.append(rad_line)
        rad_texs.append(rad_tex)
        for i in range(5):
            rad_copy = rad_line.copy()
            self.add(rad_copy)
            self.play(
                ang.animate.increment_value(1),
                Rotate(
                    rad_copy,
                    about_point= rad_copy.get_right(),
                    angle = PI
                )
            )
            rad_tex_copy = rad_tex.copy().next_to(rad_copy, DOWN)
            self.play(Write(rad_tex_copy))
            rad_line = rad_copy
            rad_lines.append(rad_line)
            rad_texs.append(rad_tex_copy)
        

        liner = Line(start= rad_lines[len(rad_lines)-1].get_right(), end= rad_lines[len(rad_lines)-1].get_right() - [0.14*2,0,0], color= RED)
        self.add(liner)
        self.play(
            ang.animate.increment_value(0.14*(1+1)),
            Rotate(
            liner,
            about_point= liner.get_right(),
            angle= PI   
        ))
        brace = Brace(liner, DOWN, buff= 0.2, color= RED)
        rem = Tex("0.14 (r+r)", font_size= 30).next_to(brace, DOWN)
        rad_texs.append(rem)
        self.play(Create(brace), Write(rem), run_time= 1)
        self.wait(2)
        self.play(FadeOut(brace))


        pre = rad_texs[0]
        pluses = list()
        for i in range(1,len(rad_texs)):
            plus = Tex("+", font_size= 30).next_to(pre, RIGHT, buff= 0.2)
            pluses.append(plus)
            self.play(Create(plus), run_time= 0.3)
            self.play(rad_texs[i].animate.next_to(plus, RIGHT), run_time= 0.3)
            pre = rad_texs[i]
        allrad1 = MathTex(r"=(1 + 1 +  1 +  1 + 1 + 1 + 1 +  0.14  + 0.14 ) r = 6.28 r = 2 \times 3.14 r = 2 \pi r", font_size= 30).next_to(pre, DOWN)
        # allrad2 = MathTex()
        self.play(Write(allrad1), run_time= 3)
        self.wait(2)

        self.clear()


        title = Title("Arc Length", font_size= 35, match_underline_width_to_text= True, underline_buff= 0.1)
        self.play(Create(title))
        ang = ValueTracker(0)
        angle = always_redraw(lambda : Arc(
            start_angle= 0,
            angle = ang.get_value(),
            radius= 0.3
        ))
        angle_tex = always_redraw(lambda : MathTex(rf"{round(np.rad2deg(ang.get_value()),2)} ^\circ", font_size= 15).move_to(np.array([0.5,0.2,0])))
        arc1 = always_redraw(lambda : Arc(
            start_angle= 0,
            angle = ang.get_value(),
            radius= 1,
            color= RED
        ))
        radius = Line(start= ORIGIN, end= arc1.get_start())
        moving_radius = always_redraw(lambda : Line(start= ORIGIN, end= arc1.get_end()))

        self.add(arc1, radius, moving_radius, angle, angle_tex)
        self.play(ang.animate.increment_value(PI/4), run_time= 3)
        arc1.clear_updaters()
        angle.clear_updaters()
        moving_radius.clear_updaters()
        angle_tex.clear_updaters()
        arc1_copy = arc1.copy()
        arc2 = Arc(
            start_angle= PI/4,
            angle= 7*(PI/4),
            radius= 1,
            color= YELLOW
        )
        self.play(Create(arc2))

        self.wait(1)
        l1 = Line(start= np.array([1,0,0]), end= np.array([1,(PI/4),0]), color= RED)
        l1.rotate(PI/2 - l1.get_angle())
        
        self.add(arc1)
        self.play(arc1.animate.become(l1).shift(RIGHT * 2), run_time= 2)
        numline = NumberLine(length= l1.get_length(), x_range= [0,PI/4,PI/4]).rotate(PI/2).next_to(l1, RIGHT, buff= 2.1)
        length = MathTex(r"{\frac{\pi}{4}}", font_size= 30).next_to(numline, RIGHT)
        self.play(Create(numline))
        self.play(Write(length))
        self.wait(1)
        self.play(Rotate(radius, angle= -PI/2, about_point= radius.get_right()))
        self.play(radius.animate.next_to(numline, LEFT, buff= 0.2))
        times_angle = MathTex(r"\times", font_size= 25).next_to(radius, LEFT)
        self.play(
            Create(times_angle),
            angle_tex.animate.next_to(times_angle, LEFT, buff= 0.1).scale(1.3)
        )
        self.wait(2)
        radius_copy = radius.copy().stretch_to_fit_height(PI/4)
        self.play(
            radius.animate.stretch_to_fit_height(PI/4),
            VGroup(angle_tex, times_angle).animate.become(radius_copy)
        )
        self.wait(3)
        self.play(FadeOut(VGroup(numline, length, radius, angle_tex, times_angle)))
        self.play(arc1.animate.become(arc1_copy), run_time= 2)
        self.wait(2)

        self.clear()

        ang = ValueTracker(2*PI)
        background_circle = Arc(
            start_angle= 0,
            angle= 2*PI,
            radius= 1,
            color= "#112ff2"
        )
        foreground_circle = always_redraw(lambda : Arc(
            start_angle = 0,
            angle = ang.get_value(),
            radius =1,
            color= "#43e81a"
        ))

        # Building up a NumberLine and labeling the points
        angle = 0
        numline = NumberLine(length= 2*PI, x_range= [0,2*PI, PI/6], unit_size= PI/6).rotate(PI/2).to_edge(LEFT).shift(RIGHT * 0.7)
        rad_scl = Tex("Radian Scale", font_size= 25).next_to(numline, UP, buff= 0.2)
        MathTex.set_default(font_size= 20)
        angles_rad = list(map(MathTex, [
            r"0",
            r"\frac{\pi}{6}",
            r"\frac{\pi}{3}",
            r"\frac{\pi}{2}",
            r"\frac{2\pi}{3}",
            r"\frac{5\pi}{6}",
            r"\pi",
            r"\frac{7\pi}{6}",
            r"\frac{4\pi}{3}",
            r"\frac{3\pi}{2}",
            r"\frac{5\pi}{3}",
            r"\frac{11\pi}{6}",
            r"2\pi",
        ]))
        for i in range(0, len(angles_rad)):
            angles_rad[i].move_to(numline.n2p(PI/6 * i)).shift(LEFT * 0.5)
        numline.add(VGroup(*angles_rad))

        line = always_redraw(lambda : Line(start= numline.n2p(0), end= numline.n2p(ang.get_value()), color= BLUE))
        dot = always_redraw(lambda : Dot(point= line.get_end()))
        ang_times_rad = always_redraw(lambda : MathTex(rf"1\times {round(np.rad2deg(ang.get_value()),2)} ^\circ").next_to(dot, RIGHT, buff= 0.2))

        self.play(Create(VGroup(background_circle, foreground_circle, numline, line, ang_times_rad, dot)), run_time= 2)
        self.wait(2)

        self.play(ang.animate.increment_value(-PI), run_time= 8)
        self.wait(2)
        self.play(ang.animate.increment_value(-PI/2), run_time= 5)
        self.wait(2)
        self.play(ang.animate.increment_value(-PI/4), run_time= 3)
        self.wait(2)
