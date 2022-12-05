from manimlib import *

#mein kopf brennt

class Test(Scene):
    def construct(self):

        greeting = Tex(r'''Die \ Produktregel''', font_size=86)
        greetingUp = Tex(r'''Die \ Produktregel''', font_size=86).move_to([0, 1, 0])
        name = Tex(r'''von \ Lukas \ Beyer''', font_size=86).move_to([0, -1, 0])

        self.play(Write(greeting))
        self.play(Transform(greeting, greetingUp))
        self.play(Write(name))
        self.wait(self.on_key_press(0, 0))
        self.play(FadeOut(greeting, shift=DOWN), FadeOut(name, shift=DOWN))
#        self.play(Unwrite(greeting), Unwrite(name))
        title = Tex(r"I. \ Widerholung", font_size=86)
        upperCorner = Tex(r"I.").move_to([-6.5, 3.5, 0])
        self.play(Write(title))
        #self.wait(1)
        self.wait(self.on_key_press(0, 0))
        self.play(Transform(title, upperCorner))

        text = Tex(r"1. \ Ableiten", font_size=64).set_x(-1, ORIGIN).set_y(1, ORIGIN)
        self.play(Write(text))
        self.wait(self.on_key_press(0, 0))
        formel = Tex(r"f(x)=2x^3 + 5", color=RED).next_to(text, DOWN).align_to(text, LEFT)
        self.play(Write(formel))
        self.wait(self.on_key_press(0, 0))
        formelres = Tex(r"f'(x)=6x^2", color=BLUE).next_to(formel, DOWN).align_to(formel, LEFT)
        self.play(Write(formelres))
        self.wait(self.on_key_press(0, 0))
        self.play(FadeOut(formel, shift=DOWN), FadeOut(formelres, shift=DOWN))
        textMov = Tex(r"1. \ Ableiten").next_to(title, DOWN).move_to([-5.5, 2.5, 0])
        self.play(Transform(text, textMov))


        text2 = Tex(r"2. \ Ableiten \ von \ trig. \ fkt.", font_size=64).set_y(1, ORIGIN)
        self.play(Write(text2))
        self.wait(self.on_key_press(0, 0))
        formel = Tex(r"f(x)=sin(x)", color=RED).next_to(text2, DOWN).align_to(text2, LEFT)
        self.play(Write(formel))
        self.wait(self.on_key_press(0, 0))
        formelres = Tex(r"f'(x)=cos(x)", color=BLUE).next_to(formel, DOWN).align_to(formel, LEFT)
        self.play(Write(formelres))
        self.wait(self.on_key_press(0, 0))
        self.play(FadeOut(formel, shift=DOWN), FadeOut(formelres, shift=DOWN))
        textMov2 = Tex(r"2. \ Ableitung \ trig.").next_to(text, DOWN).align_to(text, LEFT)

        self.play(Transform(text2, textMov2))

        text3 = Tex(r"3. \ Kettenregel", font_size=64).set_y(1, ORIGIN)
        self.play(Write(text3))
        self.wait(self.on_key_press(0, 0))
        formel = Tex(r"f(x)=u(x)+v(x)", color=RED).next_to(text3, DOWN).align_to(text3, LEFT)
        self.play(Write(formel))
        self.wait(self.on_key_press(0, 0))
        formelres = Tex(r"f'(x)=u'(v(x)) * v'(x)", color=BLUE).next_to(formel, DOWN).align_to(formel, LEFT)
        self.play(Write(formelres))
        self.wait(self.on_key_press(0, 0))
        self.play(FadeOut(formel, shift=DOWN), FadeOut(formelres, shift=DOWN))
        textMov2 = Tex(r"3. \ Kettenregel").next_to(text2, DOWN).align_to(text2, LEFT)
        self.play(Transform(text3, textMov2))

        text4 = Tex(r"4. Ableitung \ e \ fkt.", font_size=64).set_y(1, ORIGIN)
        self.play(Write(text4))
        self.wait(self.on_key_press(0, 0))
        formel = Tex(r"f(x)=e^x", color=RED).next_to(text4, DOWN).align_to(text4, LEFT)
        self.play(Write(formel))
        self.wait(self.on_key_press(0, 0))
        formelres = Tex(r"f'(x)=e^x", color=BLUE).next_to(formel, DOWN).align_to(formel, LEFT)
        self.play(Write(formelres))
        self.wait(self.on_key_press(0, 0))
        self.play(FadeOut(formel, shift=DOWN), FadeOut(formelres, shift=DOWN))
        textMov2 = Tex(r"4. \ Ableitung \ e \ fkt.").next_to(text3, DOWN).align_to(text3, LEFT)
        self.play(Transform(text4, textMov2))

        self.wait(self.on_key_press(0, 0))
        self.play(FadeOut(text, DOWN), FadeOut(text2, DOWN), FadeOut(text3, DOWN), FadeOut(text4, DOWN), FadeOut(title, UP))

        title = Tex(r"II. \ Produktregel", font_size=86)
        upperCorner = Tex(r"II.").move_to([-6.5, 3.5, 0])
        self.play(Write(title))
        # self.wait(1)
        self.wait(self.on_key_press(0, 0))
        self.play(Transform(title, upperCorner))

        head = Tex(r"Die \ Produktregel \ oder \ Leibnizregel \ ist \ eine \\ grundlegende \ Regel \ der \ Differentialrechnung. \\ Mit \ ihr \ wird \ die \ Ableitung \ eines \ Produktes \\ von \ Funktionen \ aus \ den \ Ableitungen \ der \\ einzelnen \ Funktionen \ berechnet. ").arrange(DOWN, center=True, aligned_edge=LEFT)
        self.play(Write(head))
        self.wait(self.on_key_press(0, 0))
        self.play(FadeOut(head, shift=DOWN))


        text = Tex(r"f(x) = ", "u(x)", "*", "v(x)")
        textUp = Tex(r"f(x) = ", "u(x)", "*", "v(x)").move_to([0, 1, 0])
        text[1].set_color(BLUE)
        text[3].set_color(RED)
        textUp[1].set_color(BLUE)
        textUp[3].set_color(RED)
        self.play(Write(text))

        self.wait(self.on_key_press(0, 0))
        text2 = Tex(r"f'(x)=", "u'(x)", "*", "v(x)", "+" ,"u(x)", "*", "v'(x)")
        text2[1].set_color(YELLOW)
        text2[5].set_color(BLUE)
        text2[3].set_color(RED)
        text2[7].set_color(GREEN)

        self.play(Transform(text, textUp))
        self.play(Write(text2))
        self.wait(self.on_key_press(0, 0))
        self.play(FadeOut(text, shift=DOWN), FadeOut(text2, shift=DOWN), FadeOut(title, UP))


        title = Tex(r"III. \ Beispiel", font_size=86)
        upperCorner = Tex(r"III.").move_to([-6.5, 3.5, 0])
        self.play(Write(title))
        # self.wait(1)
        self.wait(self.on_key_press(0, 0))
        self.play(Transform(title, upperCorner))

        text2 = Tex(r"f'(x)=", "u'(x)", "*", "v(x)", "+", "u(x)", "*", "v'(x)").set_y(2.5, ORIGIN)
        text2[1].set_color(YELLOW)
        text2[5].set_color(BLUE)
        text2[3].set_color(RED)
        text2[7].set_color(GREEN)
        self.play(Write(text2))

        formel = Tex(r"f(x) = ", "sin(x)", "*", "e^x").set_y(1, ORIGIN)
        formel[1].set_color(BLUE)
        formel[3].set_color(RED)
        self.play(Write(formel))

        self.wait(self.on_key_press(0, 0))
        u1 = Tex(r"u(x) = sin(x)", color = BLUE).set_x(-4)
        self.play(Write(u1))
        self.wait(self.on_key_press(0, 0))
        u2 = Tex(r"u'(x) = cos(x)", color=YELLOW).next_to(u1, DOWN).align_to(u1, LEFT)
        self.play(Write(u2))

        self.wait(self.on_key_press(0, 0))
        v1 = Tex(r"v(x) = e^x", color=RED).set_x(3.2)
        self.play(Write(v1))

        self.wait(self.on_key_press(0, 0))
        v2 = Tex(r"v'(x) = e^x", color=GREEN).next_to(v1, DOWN).align_to(v1, LEFT)
        self.play(Write(v2))

        self.wait(self.on_key_press(0, 0))
        res = Tex(r"f'(x) = ", "cos(x)", "*", "e^x", "+", "sin(x)", "*", "e^x").set_y(-2)
        res[1].set_color(YELLOW)
        res[5].set_color(BLUE)
        res[3].set_color(RED)
        res[7].set_color(GREEN)
        self.play(Write(res))

        self.wait(self.on_key_press(0, 0))

        self.play(FadeOut(text2, UP), FadeOut(u1, DOWN), FadeOut(u2, DOWN), FadeOut(v1, DOWN), FadeOut(v2, DOWN), FadeOut(res, DOWN), FadeOut(formel, DOWN) ,FadeOut(title, UP))

        title = Tex(r"IV. \ Aufgaben", font_size=86)
        upperCorner = Tex(r"IV.").move_to([-6.5, 3.5, 0])
        self.play(Write(title))
        # self.wait(1)
        self.wait(self.on_key_press(0, 0))
        self.play(Transform(title, upperCorner))



        a = Tex(r"a) \ f(x)=x^2*(x-1)").set_x(-3.5, ORIGIN).set_y(3.5, ORIGIN)
        b = Tex(r"b) \ f(x)=(x^2+\frac{1}{4}x)*(x^3+3)").next_to(a, DOWN).align_to(a, LEFT)
        c = Tex(r"c) \ f(x)= x^2 * x").next_to(b, DOWN).align_to(b, LEFT)
        d = Tex(r"d) \ f(x)= (x-1) * (x^2 + x + 7)").next_to(c, DOWN).align_to(c, LEFT)
        e = Tex(r"e) \ f(x)= x * cos(x)").next_to(d, DOWN).align_to(d, LEFT)
        f = Tex(r"f) \ f(x)= 4x * (x^3 + 2)").next_to(e, DOWN).align_to(e, LEFT)
        g = Tex(r"g) \ f(x)= (\frac{1}{2}x^2 + 2x) * (x - 1)").next_to(f, DOWN).align_to(f, LEFT)
        h = Tex(r"h) \ f(x)= \frac{sin(x)}{x}").next_to(g, DOWN).align_to(g, LEFT)






        #should probably use loops :]

        aa = Tex(r"f'(x) = ").set_x(2, ORIGIN).set_y(3.5, ORIGIN) #\frac{3}{2}x^2 + 3x-2
        ab = Tex(r"f'(x) = ").next_to(b, RIGHT).align_to(aa, LEFT)
        ac = Tex(r"f'(x) = ").next_to(c, RIGHT).align_to(ab, LEFT)
        ad = Tex(r"f'(x) = ").next_to(d, RIGHT).align_to(ac, LEFT)
        ae = Tex(r"f'(x) = ").next_to(e, RIGHT).align_to(ad, LEFT)
        af = Tex(r"f'(x) = ").next_to(f, RIGHT).align_to(ae, LEFT)
        ag = Tex(r"f'(x) = ").next_to(g, RIGHT).align_to(af, LEFT)
        ah = Tex(r"f'(x) = ").next_to(h, RIGHT).align_to(ag, LEFT)
        self.play(Write(a))
        self.play(Write(aa))
        self.play(Write(b))
        self.play(Write(ab))
        self.play(Write(c))
        self.play(Write(ac))
        self.play(Write(d))
        self.play(Write(ad))
        self.play(Write(e))
        self.play(Write(ae))
        self.play(Write(f))
        self.play(Write(af))
        self.play(Write(g))
        self.play(Write(ag))
        self.play(Write(h))
        self.play(Write(ah))


        ra = Tex(r"3x^2 - 2x").next_to(aa, RIGHT)
        rb = Tex(r"5x^4 + x^3 + 6x + \frac{3}{4}").next_to(ab, RIGHT)
        rc = Tex(r"3x^2").next_to(ac, RIGHT)
        rd = Tex(r"3x^2 + 6").next_to(ad, RIGHT)
        re = Tex(r"cos(x) - x * sin(x)").next_to(ae, RIGHT)
        rf = Tex(r"16x^3 + 8").next_to(af, RIGHT)
        rg = Tex(r"\frac{3}{2}x^2 + 3x-2").next_to(ag, RIGHT)
        rh = Tex(r"\frac{x * cos(x) - sin(x)}{x^2}").next_to(ah, RIGHT)

        self.wait(self.on_key_press(0, 0))
        self.play(Write(ra))
        self.wait(self.on_key_press(0, 0))
        self.play(Write(rb))
        self.wait(self.on_key_press(0, 0))
        self.play(Write(rc))
        self.wait(self.on_key_press(0, 0))
        self.play(Write(rd))
        self.wait(self.on_key_press(0, 0))
        self.play(Write(re))
        self.wait(self.on_key_press(0, 0))
        self.play(Write(rf))
        self.wait(self.on_key_press(0, 0))
        self.play(Write(rg))
        self.wait(self.on_key_press(0, 0))
        self.play(Write(rh))
        self.wait(self.on_key_press(0, 0))

        #wtf
        self.play(FadeOut(a, DOWN), FadeOut(b, DOWN), FadeOut(c, DOWN), FadeOut(d, DOWN), FadeOut(e, DOWN), FadeOut(f, DOWN), FadeOut(g, DOWN), FadeOut(h, DOWN), FadeOut(aa, DOWN), FadeOut(ab, DOWN), FadeOut(ac, DOWN), FadeOut(ad, DOWN), FadeOut(ae, DOWN), FadeOut(af, DOWN), FadeOut(ag, DOWN), FadeOut(ah, DOWN), FadeOut(ra, DOWN), FadeOut(rb, DOWN), FadeOut(rc, DOWN), FadeOut(rd, DOWN), FadeOut(re, DOWN), FadeOut(rf, DOWN), FadeOut(rg, DOWN), FadeOut(rh, DOWN), FadeOut(title, UP))

        title = Tex(r"V. \ Herleitung", font_size=86)
        upperCorner = Tex(r"V.").move_to([-6.5, 3.5, 0])
        self.play(Write(title))
        # self.wait(1)
        self.wait(self.on_key_press(0, 0))
        self.play(Transform(title, upperCorner))

        text = Tex(r"f(x) = ", "u(x)", "*", "v(x)")
        text[1].set_color(BLUE)
        text[3].set_color(RED)
        self.play(Write(text))
        self.wait(self.on_key_press(0, 0))
        self.play(FadeOut(text, DOWN))

        text2 = Tex(r"m = \frac{y2-y1}{x2-x1}").set_y(3.2, ORIGIN).set_x(-4, ORIGIN)
        text3 = Tex(r"\displaystyle \lim_{x \to 0} \frac{u(x + h) * v(x + h) - u(x) * v(x)}{h}").set_y(3.2,
                                                                                                       ORIGIN).set_x(2,
                                                                                                                     ORIGIN)
        text4 = Tex(
            r"\displaystyle \lim_{h \to 0} \frac{u(x + h) * v(x + h) - u(x) * v(x + h) + u(x) * v(x + h)  - u(x) * v(x)}{h}",
            font_size=42).set_y(2, ORIGIN)
        text4[0][19:43].set_color(RED)
        text5 = Tex(
            r"\displaystyle \lim_{h \to 0} \frac{[u(x + h) - u(x)] * v(x + h) + u(x) * [v(x + h) - v(x)]}{h}").set_y(
            0.5, ORIGIN)
        text6 = Tex(
            r"\displaystyle \lim_{h \to 0} \frac{u(x + h) - u(x)}{h} * \displaystyle \lim_{h \to 0} \frac{v(x + h)}{h} + \displaystyle \lim_{h \to 0} \frac{u(x)}{h} * \displaystyle \lim_{h \to 0} \frac{v(x + h) - v(x)}{h}",
            font_size=42).set_y(-1, ORIGIN)
        text7 = Tex(r"u'(x)", color=YELLOW).set_y(-2.5, ORIGIN).set_x(-4)
        text8 = Tex(r"u(x)", color=BLUE).set_y(-2.5, ORIGIN).set_x(1.7)
        text9 = Tex(r"v'(x)", color=GREEN).set_y(-2.5, ORIGIN).set_x(5)
        text10 = Tex(r"v(x)", color=RED).set_y(-2.5, ORIGIN).set_x(-0.8)

        self.play(Write(text2))
        self.wait(self.on_key_press(0, 0))
        self.play(Write(text3))
        self.wait(self.on_key_press(0, 0))
        self.play(Write(text4))
        self.wait(self.on_key_press(0, 0))
        self.play(Write(text5))
        self.wait(self.on_key_press(0, 0))
        self.play(Write(text6))
        self.wait(self.on_key_press(0, 0))
        self.play(Write(text7))
        self.play(Write(text10))
        self.play(Write(text8))
        self.play(Write(text9))

        self.wait(self.on_key_press(0, 0))
        self.play(FadeOut(text2, DOWN), FadeOut(text3, DOWN), FadeOut(text4, DOWN), FadeOut(text5, DOWN),
                  FadeOut(text6, DOWN), FadeOut(text7, DOWN), FadeOut(text8, DOWN), FadeOut(text9, DOWN),
                  FadeOut(text10, DOWN), FadeOut(title, UP))

