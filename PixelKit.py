import board
import analogio, digitalio
import neopixel
from adafruit_pixel_framebuf import PixelFramebuffer

# Hardware info
# In CircuitPython, ESP32 pins are labeled with a D,
# unlike other languages that reference the GPIO number.
pixel_pin = board.D4
WIDTH = 16
HEIGHT = 8
dial_pin = board.VP # In CircuitPython, GPIO 36 is board.VP
microphone_pin = board.VN # In CircuitPython, GPIO 39 is board.VN
joystick_up_pin = board.D35
joystick_down_pin = board.D34
joystick_left_pin = board.D26
joystick_right_pin = board.D25
joystick_click_pin = board.D27
button_b_pin = board.D18
button_a_pin = board.D23
button_reset_pin = board.D5

# Hardware Instances
# Objects representing the available hardware on the Pixel Kit
# Keep in mind that the Pixel Kit's matrix is NOT serpentine, meaning alternating CANNOT be true
np = neopixel.NeoPixel(pixel_pin, WIDTH * HEIGHT, brightness=0.05, auto_write=False)
matrix = PixelFramebuffer(np, WIDTH, HEIGHT, alternating=False) # The PixelFramebuffer makes graphics much easier!
# Directions of digital pins must be set with var.direction = digitalio.Direction.INPUT or OUTPUT
joystick_up = digitalio.DigitalInOut(joystick_up_pin)
joystick_up.direction = digitalio.Direction.INPUT
joystick_down = digitalio.DigitalInOut(joystick_down_pin)
joystick_down.direction = digitalio.Direction.INPUT
joystick_left = digitalio.DigitalInOut(joystick_left_pin)
joystick_left.direction = digitalio.Direction.INPUT
joystick_right = digitalio.DigitalInOut(joystick_right_pin)
joystick_right.direction = digitalio.Direction.INPUT
button_a = digitalio.DigitalInOut(button_a_pin)
button_a.direction = digitalio.Direction.INPUT
button_b = digitalio.DigitalInOut(button_b_pin)
button_b.direction = digitalio.Direction.INPUT
button_reset = digitalio.DigitalInOut(button_reset_pin)
button_reset.direction = digitalio.Direction.INPUT

dial = analogio.AnalogIn(dial_pin)

microphone = analogio.AnalogIn(microphone_pin)

# Hardware Values
# Values based on available hardware
dial_value = dial.value
microphone_value = microphone.value
is_pressing_up = False
is_pressing_down = False
is_pressing_left = False
is_pressing_right = False
is_pressing_click = False
is_pressing_a = False
is_pressing_b = False
is_pressing_reset = False

# Group all other function together to check hardware
def check_controls():
    check_joystick()
    check_buttons()
    check_dial()
    check_microphone()

def check_joystick():
    global is_pressing_up
    global is_pressing_down
    global is_pressing_left
    global is_pressing_right
    global is_pressing_click
    if joystick_up.value == 0 and not is_pressing_up:
        is_pressing_up = True
        on_joystick_up()
    if joystick_up.value != 0 and is_pressing_up:
        is_pressing_up = False

    if joystick_down.value == 0 and not is_pressing_down:
        is_pressing_down = True
        on_joystick_down()
    if joystick_down.value != 0 and is_pressing_down:
        is_pressing_down = False

    if joystick_left.value == 0 and not is_pressing_left:
        is_pressing_left = True
        on_joystick_left()
    if joystick_left.value != 0 and is_pressing_left:
        is_pressing_left = False

    if joystick_right.value == 0 and not is_pressing_right:
        is_pressing_right = True
        on_joystick_right()
    if joystick_right.value != 0 and is_pressing_right:
        is_pressing_right = False

    if joystick_click.value == 0 and not is_pressing_click:
        is_pressing_click = True
        on_joystick_click()
    if joystick_click.value != 0 and is_pressing_click:
        is_pressing_click = False

# Checks the buttons, "debounce" the presses and calls the
# function related to which button was pressed
def check_buttons():
    global is_pressing_a
    global is_pressing_b
    global is_pressing_reset
    if button_a.value == 0 and not is_pressing_a:
        is_pressing_a = True
        on_button_a()
    if button_a.value != 0 and is_pressing_a:
        is_pressing_a = False
    if button_b.value == 0 and not is_pressing_b:
        is_pressing_b = True
        on_button_b()
    if button_b.value != 0 and is_pressing_b:
        is_pressing_b = False
    if button_reset.value == 0 and not is_pressing_reset:
        is_pressing_reset = True
        on_button_reset()
    if button_reset.value != 0 and is_pressing_reset:
        is_pressing_reset = False

# Checks the dial value and only set the hardware value and call the
# function related with the dial if the new value is different from the previous
def check_dial():
    global dial_value
    newValue = dial.value
    if newValue != dial_value:
        dial_value = dial.value
        on_dial(dial_value)

# Checks the microphone value and only set the hardware value and call the
# function related with the microphone if the new value is different from the previous
def check_microphone():
    global microphone_value
    newValue = microphone.value
    if newValue != microphone_value:
        dial_value = mic.value
        on_microphone(microphone_value)

# Called when those hardware change values
def on_joystick_up():
    return False
def on_joystick_down():
    return False
def on_joystick_left():
    return False
def on_joystick_right():
    return False
def on_joystick_click():
    return False
def on_button_a():
    return False
def on_button_b():
    return False
def on_button_reset():
    return False
def on_dial(dial_value):
    return False
def on_microphone(microphone_value):
    return False

def set_brightness(brightness=0.05): # Any number from 0 to 1
    np.brightness = brightness

def set_pixel(x, y, color=0x00FF00):
        matrix.pixel(x, y, color)

def get_pixel(x, y):
    matrix.pixel(x, y)

def set_background(color=0xFFFF00):
    matrix.fill(color)

def clear():
    set_background(0x000000)

def draw_line(x, y, sx, sy, color=0x00FF00):
    matrix.line(x, y, sx, sy, color)

def draw_hline(x, y, length, color=0x00FF00):
    matrix.hline(x, y, length, color)

def draw_vline(x, y, length, color=0x00FF00):
    matrix.vline(x, y, length, color)

def draw_rect(x, y, width, height, color=0x00FF00):
    matrix.rect(x, y, width, height, color)

def draw_fill_rect(x, y, width, height, color=0x00FF00):
    matrix.fill_rect(x, y, width, height, color)

def draw_text(x, y, text="RPK", color=0xFF0000):
    matrix.text(text, x, y, color)

def render():
    matrix.display()