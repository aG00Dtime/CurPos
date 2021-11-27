# simple script to add the x,y of the mouse pointer next to it

from tkinter import *

import pyautogui as pa


class CurPos(Tk):
    def __init__(self):
        super().__init__()

        # positions var
        self.pos_x = StringVar()
        self.pos_y = StringVar()

        # background color
        self.background = "black"
        self.configure(bg=self.background)
        # label
        self.label_x = Label(self, textvariable=self.pos_x, font='Arial 12 bold', foreground='cyan', bg=self.background)
        self.label_x.pack()

        self.label_y = Label(self, textvariable=self.pos_y, font='Arial 12 bold', foreground='yellow',
                             bg=self.background)
        self.label_y.pack()

        # hide title bar
        self.overrideredirect(1)

        # top layer
        self.attributes('-topmost', True)

        # run func
        self.after(1, self.get_pos)

    # update pos
    def get_pos(self):

        # get mouse x y
        x, y = pa.position()

        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()

        # relocate the xy box if mouse is at the end of the screen or bottom
        if x > (screen_w - 100):
            x = x - 150

        if y > (screen_h - 100):
            y = y - 150

        # set self pos to follow cursor
        self.geometry(f"100x60+{x + 20}+{y + 30}")

        # change label values
        self.pos_x.set(f"X : {x}")
        self.pos_y.set(f"Y : {y}")

        # call again
        self.after(20, self.get_pos)


if __name__ == '__main__':
    cur = CurPos()
    cur.mainloop()
