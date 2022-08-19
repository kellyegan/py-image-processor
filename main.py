from kivy.app import App
from kivy.uix.widget import Widget


class ImageProcessor(Widget):
    pass


class ImageProcessorApp(App):
    def build(self):
        return ImageProcessor()


if __name__ == '__main__':
    ImageProcessorApp().run()