class WindowPosition:
    @staticmethod
    def get_window_position(screenWidth, screenHeight, appWidth, appHeight):
        x = (screenWidth - appWidth) / 2
        y = (screenHeight - appHeight) / 2
        return f'{appWidth}x{appHeight}+{int(x)}+{int(y)}'
