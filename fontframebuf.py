import framebuf

class FontFrameBuffer(framebuf.FrameBuffer):
    def __init__(self, buffer, width, height, format) -> None:
        super().__init__(buffer, width, height, format)
        self._width = width
        self._height = height

    def text(self, str, x, y, c = None, font = None):
        if font is None:
            if c is None:
                super().text(str, x, y)
            else:
                super().text(str, x, y, c)
            return

        pos_x = x
        for i in range(len(str)):
            pos_x += self.char(str[i], pos_x, y, c, font)
    
    def char(self, char, x, y, c, font):
        bitmap = font[char]
        if bitmap is not None:
            for i in range(len(bitmap)):
                line = bitmap[i]
                for j in range(8):
                    if line & (1 << j):
                        if x+i <= self._width and y+(8-j) <= self._height:
                            self.pixel(x+i, y+(8-j), c)
            return len(bitmap)
        return 0
    