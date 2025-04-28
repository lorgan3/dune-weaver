# https://github.com/TheSylex/ELK-BLEDOM-bluetooth-led-strip-controller


def turn_on():
    return bytearray([0x7E, 0x00, 0x04, 0xF0, 0x00, 0x01, 0xFF, 0x00, 0xEF])


def turn_off():
    return bytearray([0x7E, 0x00, 0x04, 0x00, 0x00, 0x00, 0xFF, 0x00, 0xEF])


def set_color(red: int, green: int, blue: int):
    return bytearray([0x7E, 0x00, 0x05, 0x03, red, green, blue, 0x00, 0xEF])


def set_brightness(value: int):
    return bytearray([0x7E, 0x00, 0x01, min(value, 0x64), 0x00, 0x00, 0x00, 0x00, 0xEF])


def set_effect(value: int):
    return bytearray([0x7E, 0x00, 0x03, value, 0x03, 0x00, 0x00, 0x00, 0xEF])


def set_effect_speed(value: int):
    return bytearray([0x7E, 0x00, 0x02, min(value, 0x64), 0x00, 0x00, 0x00, 0x00, 0xEF])


COMMANDS = {
    "turn_on": turn_on,
    "turn_off": turn_off,
    "set_color <r> <g> <b>": set_color,
    "set_brightness <brightness>": set_brightness,
    "set_effect <effect>": set_effect,
    "set_effect_speed <speed>": set_effect_speed,
}

EFFECTS = {
    "jump_red_green_blue": 0x87,
    "jump_red_green_blue_yellow_cyan_magenta_white": 0x88,
    "crossfade_red": 0x8B,
    "crossfade_green": 0x8C,
    "crossfade_blue": 0x8D,
    "crossfade_yellow": 0x8E,
    "crossfade_cyan": 0x8F,
    "crossfade_magenta": 0x90,
    "crossfade_white": 0x91,
    "crossfade_red_green": 0x92,
    "crossfade_red_blue": 0x93,
    "crossfade_green_blue": 0x94,
    "crossfade_red_green_blue": 0x89,
    "crossfade_red_green_blue_yellow_cyan_magenta_white": 0x8A,
    "blink_red": 0x96,
    "blink_green": 0x97,
    "blink_blue": 0x98,
    "blink_yellow": 0x99,
    "blink_cyan": 0x9A,
    "blink_magenta": 0x9B,
    "blink_white": 0x9C,
    "blink_red_green_blue_yellow_cyan_magenta_white": 0x95,
}
