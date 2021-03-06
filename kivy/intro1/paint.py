from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line, Rectangle, Triangle
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty


class PaintWidget(Widget):

    def __init__(self, **kwargs):
        Widget.__init__(self, **kwargs)
        self.shaped_Rectangle = 1

    # shuffle between: circle, triangle, rectangle
    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            if self.shaped_Rectangle == 1:
                Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
                self.shaped_Rectangle = 2
            elif self.shaped_Rectangle == 2:
                coords = [touch.x - d / 2, touch.y - d / 2, touch.x,
                          touch.y + d / 2, touch.x + d / 2, touch.y - d / 2]
                Triangle(points=coords)
                self.shaped_Rectangle = 3
            else:
                Rectangle(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
                self.shaped_Rectangle = 1

            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class Menu(FloatLayout):

    paint_canvas = ObjectProperty(None)

    def clear_canvas(self):
        self.paint_canvas.canvas.clear()


class PaintApp(App):

    def build(self):
        return Menu()


if __name__ == '__main__':
    PaintApp().run()
