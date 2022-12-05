from manimlib import *



#if __name__ == "__main__":
    #main()


class Test(Scene):
    def construct(self):
        title = Tex(r"VI. \ Quellen", font_size=86).set_y(1)
        # upperCorner = Tex(r"II.").move_to([-6.5, 3.5, 0])
        self.play(Write(title))

        quellen = Tex(r"Quellen \ befinden \ sich \ in \ der \ zugehörigen \ quellen.txt \ datei \\ 'https://github.com/lukas0x1/manim-prod/'").set_y(-1)
        self.play(Write(quellen))

        self.wait(self.on_key_press(0, 0))
        exit()


