import eightbithud
import fontframebuf
import framebuf

width = 128
height = 64
buffer = bytearray(width * (height // 8))
fbuf = fontframebuf.FontFrameBuffer(buffer, width, height, framebuf.MONO_VLSB)

fbuf.fill(0)
fbuf.text("Hello World!", 4, 16, 1, eightbithud.eight_bit_hud)