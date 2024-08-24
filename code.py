import board
import pwmio

from adafruit_debouncer import Button
from digitalio import DigitalInOut, Direction, Pull

from defaults import *
try:
  from settings import *
except ImportError as e:
  print(f'Error loading settings: {type(e).__name__}: {e}')


def getpin(name):
  return getattr(board, name)

def init_pullup(pin):
  io = DigitalInOut(pin)
  io.direction = Direction.INPUT
  io.pull = Pull.UP
  return io

def init_button(pin):
  return Button(init_pullup(pin), short_duration_ms=50, long_duration_ms=5000)

num_outputs = min(num_outputs, len(pwm_pins))
num_outputs = max(num_outputs, 0)
pwm_pins = pwm_pins[:num_outputs]
print(f'{num_outputs=} {pwm_pins=}')
pwm = tuple(map(pwmio.PWMOut, map(getpin, pwm_pins)))

buttons = tuple(map(init_button, map(getpin, button_pins)))
if invert_buttons:
  print(f'{invert_buttons=}')
  buttons = tuple(reversed(buttons))
button_less, button_select, button_more = buttons

if min_level is None: 
  min_level = 1
else:
  min_level = max(1, min_level)
  min_level = min(len(duty_cycles) - 1, min_level)
print(f'{min_level=}')

if max_level is None or max_level < 0:
  max_level = len(duty_cycles) - 1
else:
  max_level = max(1, max_level)
  max_level = min(len(duty_cycles) - 1, max_level)
print(f'{max_level=}')

levels = [min_level] * len(pwm)
values = [None] * len(pwm)
selected = len(pwm)
change = True

while True:
  for button in buttons:
    button.update()
    if button.short_count:
      change = True
  if not change:
    continue
  for _ in range(button_select.short_count):
    if selected == len(pwm):
      selected = 0
    else:
      selected += 1
  for i in range(len(pwm)):
    down = button_less.short_count
    up = button_more.short_count
    if selected == i or selected == len(pwm):
      if down:
        levels[i] -= down
        if levels[i] < min_level:
          levels[i] = 0
      if up:
        if levels[i] == 0:
          levels[i] = min_level
          up -= 1
        levels[i] += up
        levels[i] = min(levels[i], max_level)
      pwm[i].duty_cycle = values[i] = duty_cycles[levels[i]]
  print(f'{levels=} {values=} {selected=}')
  change = False
