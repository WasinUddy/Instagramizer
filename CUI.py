import curses
from curses import wrapper

from settings import *
from functions import *
from modes import Mode_0, Mode_1, Mode_2


class CUI:
    def __init__(self, stdscr):
        self.stdscr = stdscr

        # Get Dimensions of Terminal
        self.h, self.w = self.stdscr.getmaxyx()

        # Initialize Colors
        for i in range(1, 8):
            curses.init_pair(i, i, curses.COLOR_BLACK)        
        self.colors={
            'blue': curses.color_pair(1),
            'green': curses.color_pair(2),
            'cyan': curses.color_pair(3),
            'red': curses.color_pair(4),
            'purple': curses.color_pair(5),
            'yellow': curses.color_pair(6),
            'white': curses.color_pair(7)
        }

        # Selection & Activation state
        self.select = 0
        self.active = 0

        self.Mode_0_data = [[]]     # [Images]
        self.Mode_1_data = [0]      # [Active Color]
        self.Mode_2_data = [False]  # [Done, photos, color]

        self.modes = [
            Mode_0(self.Mode_0_data),
            Mode_1(self.Mode_1_data),
            Mode_2(self.Mode_2_data)
        ]

    def draw_static(self):
        """
        draw_static draws the static elements of the CUI

        1. Border
        2. Title
        3. Toolbar
        4. 3 Boxes for Import Custom Export

        """
        self.stdscr.clear()

        # 1. Draw Border
        self.stdscr.border()

        # 2. Draw Title
        title = f"Instagramizer v{VERSION_TAGS}"
        self.stdscr.addstr(0, self.w // 2 - len(title) // 2, title)

        # 3. Draw Tool Commands
        toolbar_text = "[Q]uit [A]ctivate [I]nteract ↑ ↓ ← →"
        self.stdscr.addstr(1, 2, toolbar_text)

        # 4 Boxes for 3 Modes
        # 4.1. Import : Import Images
        # 4.2. Custom : Choose Color of Image
        # 4.3. Export : Export Images
        self.stdscr.addstr(3, 2, f"Imported Images: {0}", curses.color_pair(7))
        self.stdscr.hline(4, 2, curses.ACS_HLINE, self.w//3 - 2, curses.color_pair(7))
        self.stdscr.addstr(3, self.w//3+2, f"SelectedColor: blue", curses.color_pair(7))
        self.stdscr.hline(4, self.w//3+2, curses.ACS_HLINE, self.w//3 -3, curses.color_pair(7))
        self.stdscr.addstr(3, self.w*2//3+1, "Export [I] to start", curses.color_pair(7))
        self.stdscr.hline(4, self.w*2//3, curses.ACS_HLINE, self.w//3 -3, curses.color_pair(7))

        self.stdscr.subwin(self.h-4, self.w//3, 2, 1).box()
        self.stdscr.subwin(self.h-4, self.w//3-1, 2, self.w//3 + 1).box()
        self.stdscr.subwin(self.h-4, self.w//3-1, 2, self.w//3 * 2).box()

        # Color Palette in Custom Mode
        for i, c in enumerate(self.colors):
            self.stdscr.addstr(5 + list(self.colors.keys()).index(c), self.w//3 + self.w//6 -7, f"{c.ljust(6)}    -     {i}", curses.color_pair(list(self.colors.keys()).index(c) + 1))
        
        # Draw Checkboxes
        for i, c in enumerate(self.colors):
            self.stdscr.addstr(5 + list(self.colors.keys()).index(c), self.w//3 + self.w//6 -10, "[ ]", curses.color_pair(7))


    def mainloop(self):
        """
        mainloop is the main loop of the CUI handle interactive features of the CUI
        """
        self.draw_static()

        while True:
            key = self.stdscr.getch()

            '''
            Handle Key Presses
            '''
            # Quit            
            if key == ord('q'):
                break
            
            # Activation of Mode
            if key == ord('a'):
                self.active = self.select

            # Interact with Mode
            if key == ord('i'):
                if self.active == 2:
                    self.modes[self.active].interact(self.modes[0].data[0], self.modes[1].data[0])
                else:
                    self.modes[self.active].interact()

            if key == curses.KEY_LEFT:
                self.select = bound(self.select - 1, 0, 2) # Switch between 0, 1, 2
            
            if key == curses.KEY_RIGHT:
                self.select = bound(self.select + 1, 0, 2) # Switch between 0, 1, 2

            if key == curses.KEY_UP:
                self.modes[self.active].up()
            
            if key == curses.KEY_DOWN:
                self.modes[self.active].down()


            self.draw_static()
            # ---All interactive Features---
            
            # Selection and Activation of Mode
            mode_boxes = ((self.h-4, self.w//3, 2, 1), (self.h-4, self.w//3-1, 2, self.w//3 + 1), (self.h-4, self.w//3-1, 2, self.w//3 * 2))
            select_box = self.stdscr.subwin(*mode_boxes[self.select])
            select_box.bkgd(' ', curses.color_pair(6))
            select_box.box()
            active_box = self.stdscr.subwin(*mode_boxes[self.active])
            active_box.bkgd(' ', curses.color_pair(4))
            active_box.box()

            # Dynamic Text Labels 
            # How many images are imported?
            self.stdscr.addstr(3, 2, f"Imported Images: {len(self.modes[0].data[0])}", curses.color_pair(7))
            for img in self.modes[0].data[0]:
                self.stdscr.addstr(5 + self.modes[0].data[0].index(img), 2, name_limit(self.w//3-5, img), curses.color_pair(7))

            # What color is selected?
            self.stdscr.addstr(3, self.w//3+2, f"SelectedColor: {list(self.colors.keys())[self.Mode_1_data[0]]} ", curses.color_pair(7))

            # Checkboxes on the Color Palette
            self.stdscr.addstr(5 + self.Mode_1_data[0], self.w//3 + self.w//6 -10, "[*]", curses.color_pair(7))

            # Export Done Message
            if self.Mode_2_data[0]:
                self.stdscr.addstr(self.h//2, (self.w*2//3) + self.w//6 - 6, "Export Done!", curses.color_pair(7))
            # ------------------------------
            # SetCursor
            self.stdscr.move(self.h-2, 1)
            self.stdscr.refresh()
        
        curses.endwin()


def main(stdscr):
    cui = CUI(stdscr)
    cui.mainloop()


if __name__ == "__main__":
    wrapper(main)
