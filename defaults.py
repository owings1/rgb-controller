##########################################

# Runtime Preferences

# Number of LEDs connected. Max is number of pwm_pins.
num_outputs = 3

# Disable onboard LED to save power
disable_led = False

# Invert up/down buttons
invert_buttons = False

# Minimum brightness level (1-30)
min_level = 1

# Maximum brightness level
max_level = None

##########################################

# Circuit Configuration

pwm_pins = ('D2', 'D5', 'D3')

button_pins = ('D8', 'D7', 'D6')

##########################################

# Brightness level duty cycles, 0-65535

# Adapted from https://forum.arduino.cc/t/logarithmic-scaling-for-led-dimming/144333/11
duty_cycles = (
  0,
  257,
  514,
  771,
  1028,
  1285,
  1799,
  2313,
  3084,
  3855,
  4626,
  5654,
  6939,
  8224,
  9766,
  11308,
  13107,
  14906,
  17219,
  19532,
  22102,
  24672,
  27756,
  30840,
  34438,
  38036,
  41891,
  46260,
  50629,
  55512,
  60395,
  65535,
)
