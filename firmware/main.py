import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.matrix import DiodeOrientation
from kmk.keys import KC
from kmk.modules.macros import Macros, Tap, Press, Release
from kmk.extensions.display import Display, SSD1306, TextEntry
from kmk.modules.encoder import RotaryEncoder

# --- Create the main keyboard instance first ---
keyboard = KMKKeyboard()

# --- Matrix setup ---
keyboard.row_pins = (board.GP3, board.GP4)
keyboard.col_pins = (board.GP2, board.GP1, board.GP29)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

macros = Macros()
keyboard.modules.append(macros)
HELLO = [Tap(KC.H), Tap(KC.E), Tap(KC.L), Tap(KC.L), Tap(KC.O)]
keyboard.keymap = [
    [KC.X, KC.Y, KC.Z],        # row1
    [HELLO, KC.B, KC.C],       # row2
]

# --- Display setup ---
i2c_bus = busio.I2C(board.GP21, board.GP20)
display_driver = SSD1306(i2c=i2c_bus, device_address=0x3C)

display = Display(
    display=display_driver,
    width=128,
    height=32,
    brightness=1,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    entries=[
        TextEntry(text='Layer:', x=0, y=0),
        TextEntry(text='BASE', x=40, y=0, layer=0),
        TextEntry(text='NUM', x=40, y=0, layer=1),
        TextEntry(text='NAV', x=40, y=0, layer=2),
    ],
)
keyboard.extensions.append(display)

# --- Encoder setup ---
encoder = RotaryEncoder()
keyboard.modules.append(encoder)

# Encoder rotation (volume control)
encoder.pairs = [
    (board.GP7, board.GP8, KC.VOLU, KC.VOLD)
]

# Encoder push button (mute)
encoder.buttons = [(board.GP9, KC.MUTE)]

# --- Start the keyboard ---
if __name__ == '__main__':
    keyboard.go()
