from manim import *
class square(Scene):
    def construct(self):
        #9:16 vertical layout setup
        self.camera.frame_width = 9
        self.camera.frame_height = 16
        self.next_section(skip_animations=False)
        title = MathTex(r"(a+b)^2 = a^2 + 2ab + b^2")
        title.to_edge(UP)

        self.play(Write(title))
        self.wait(1)
        # Create 4 label for the Square
        up_a = MathTex("a")
        up_a_copy = up_a.copy()
        left_a = up_a.copy()
        left_a_copy = up_a.copy()
        multiplayFirst = MathTex(r"\times")
        

        # Create a2 for the Square

        square_a = MathTex(r'a^2')

        # Make the square 

        square = Square(side_length=4)
        

        # Place the all labels outside of the Square
        multiplayFirst.move_to(square.get_center())
        up_a.move_to(square.get_top()).shift(UP*0.3)
        left_a.move_to(square.get_left()).shift(LEFT*0.3)
        left_a_copy.next_to(multiplayFirst,LEFT,buff=0.1)
        up_a_copy.next_to(multiplayFirst,RIGHT,buff=0.1)

        # Make Group
        a_times_a_group = VGroup(left_a_copy,up_a_copy,multiplayFirst)


        # Add then on the Scene

        self.play(Write(square), run_time = 2)
        self.play(FadeIn(up_a))
        self.play(FadeIn(left_a))
        self.play(TransformFromCopy(left_a,left_a_copy))
        self.play(FadeIn(multiplayFirst))
        self.play(TransformFromCopy(up_a,up_a_copy))
        self.play(Transform(a_times_a_group,square_a))
        
        self.play(FadeOut(up_a,left_a),FadeOut(square_a),FadeOut(square), FadeOut(a_times_a_group))
        # Next Section of the video
        self.next_section(skip_animations=False)
        
        #split value
        a = 2.5
        b = 1.5

        #create pertitions
        v_line = Line(
            square.get_top()+RIGHT*(a-2),
            square.get_bottom()+RIGHT*(a-2),
            color=WHITE
        )
        
        h_line = Line(
            square.get_left()+DOWN*(2-b),
            square.get_right()+DOWN*(2-b),
            color=WHITE
        )
        #Regions
        a2_rect = Rectangle(
            width=a,
            height=a,
            stroke_color =GREEN
        ).align_to(square, UL)

        ab_rect1 = Rectangle(
            width=b,
            height=a,
             stroke_color =YELLOW
        ).next_to(a2_rect, RIGHT, buff=0)
        ab_rect2 = Rectangle(
            width=a,
            height=b,
           stroke_color = ORANGE
        ).next_to(a2_rect, DOWN, buff=0)
        b2_rect = Rectangle(
            width=b,
            height=b,
            stroke_color = RED
        ).next_to(ab_rect2, RIGHT, buff=0)

        label_a1 = MathTex("a")
        label_a1.next_to(a2_rect,UP,buff=0.1)
        label_b1 = MathTex("b")
        label_b1.next_to(ab_rect1,UP,buff=0.1)

        label_a2 = label_a1.copy().next_to(a2_rect,LEFT,buff=0.1)
        label_b2 = label_b1.copy().next_to(ab_rect2,LEFT,buff=0.1)


        self.play(FadeIn(square))
        self.play(Create(v_line), Create(h_line))
        self.play(FadeIn(label_a1),FadeIn(label_b1))
        self.play(FadeIn(label_a2),FadeIn(label_b2))

        # a2_rect animation a*a

        anim_label_a1 = label_a1.copy()
        anim_label_a2 = label_a2.copy()

        multiplay1 = MathTex(r"\times")
        multiplay1.move_to(a2_rect.get_center())
        a2_group = VGroup(anim_label_a1,anim_label_a2,multiplay1)
        self.play(
            anim_label_a2.animate.next_to(multiplay1,LEFT,buff=0.1),
            FadeIn(multiplay1),
            anim_label_a1.animate.next_to(multiplay1,RIGHT,buff=0.1)
            )

        # a*b animation 
        anim_label_b1 = label_b1.copy()
        anim_label_ab = label_a2.copy()
        multiplay2 = multiplay1.copy()
        multiplay2.move_to(ab_rect1.get_center())
        ab_group1 = VGroup(anim_label_b1,anim_label_ab,multiplay2)
        self.play(
            anim_label_b1.animate.next_to(multiplay2,UP,buff=0.1),
            FadeIn(multiplay2),
            anim_label_ab.animate.next_to(multiplay2,DOWN,buff=0.1)
            )

        # ab2 a*b animation
        anim_label_a_ab2 = label_a1.copy()
        anim_label_b_ab2 = label_b2.copy()
        multiplay3 = multiplay1.copy()
        multiplay3.move_to(ab_rect2.get_center())
        ab_group2 = VGroup(anim_label_a_ab2,anim_label_b_ab2,multiplay3)
        self.play(
                  anim_label_b_ab2.animate.next_to(multiplay3,LEFT,buff=0.1),
                  FadeIn(multiplay3),
                  anim_label_a_ab2.animate.next_to(multiplay3,RIGHT,buff=0.1)
                  
                  )

        # b2 b*b animation
        anim_label_b_b1 = label_b1.copy()
        anim_label_b_b2 = label_b2.copy()
        multiplay4 = multiplay1.copy()
        multiplay4.move_to(b2_rect.get_center())

        b2_group = VGroup(anim_label_b_b1,anim_label_b_b2,multiplay4)

        self.play(
            anim_label_b_b1.animate.next_to(multiplay4,UP,buff=0.1),
            FadeIn(multiplay4),
            anim_label_b_b2.animate.next_to(multiplay4,DOWN,buff=0.1)
        )


        # FadeOut and FadeIn Animationt
        # self.play(FadeOut(a2_group),FadeOut(ab_group1), FadeOut(ab_group2), FadeOut(b2_group))

        # Area Calculations Text
        a2 = MathTex(r"a^2")
        a2.move_to(a2_rect)
        ab1 = MathTex("ab")
        ab1.move_to(ab_rect1)
        ab2 = ab1.copy()
        ab2.move_to(ab_rect2)
        b2 = MathTex(r"b^2")
        b2.move_to(b2_rect)
        self.play(Transform(a2_group,a2),
                  Transform(ab_group1,ab1),
                  Transform(ab_group2,ab2),
                  Transform(b2_group,b2)
                  )
        # Final law animation a2+2ab+b2
        a2_copy = a2.copy()
        a2_copy.next_to(square,DOWN, buff=0.5).shift(LEFT*1.5)
        plus_sign1 = MathTex("+")
        plus_sign1.next_to(a2_copy,RIGHT, buff=0.1)
        ab1_copy = ab1.copy()
        ab1_copy.next_to(plus_sign1,RIGHT,buff=0.1)
        plus_sign2 = plus_sign1.copy()
        plus_sign2.next_to(ab1_copy,RIGHT,buff=0.1)
        ab2_copy = ab2.copy()
        ab2_copy.next_to(plus_sign2,RIGHT,buff=0.1)
        plus_sign3 = plus_sign1.copy()
        plus_sign3.next_to(ab2_copy,RIGHT,buff=0.1)
        b2_copy = b2.copy()
        b2_copy.next_to(plus_sign3,RIGHT,buff=0.1)

        # Animation part
        self.play(TransformFromCopy(a2,a2_copy))
        self.play(FadeIn(plus_sign1))
        self.play(TransformFromCopy(ab1,ab1_copy))
        self.play(FadeIn(plus_sign2))
        self.play(TransformFromCopy(ab2,ab2_copy))
        self.play(FadeIn(plus_sign3))
        self.play(TransformFromCopy(b2,b2_copy))

        # Next Animation
        eq_line1 = VGroup(ab1_copy,ab2_copy,a2_copy,b2_copy,plus_sign1,plus_sign2,plus_sign3)
        eq_line2 = MathTex(r"a^2 + 2ab + b^2")
        eq_line2.next_to(square,DOWN, buff=0.5)
        self.play(Transform(eq_line1,eq_line2))
        self.wait()

        eq_line3 = MathTex(r"\therefore (a+b)^2 = a^2 + 2ab + b^2")
        eq_line3.next_to(square,DOWN, buff=0.5)
        self.play(FadeOut(eq_line1),Transform(eq_line2,eq_line3))

        self.wait(2)



    
        

