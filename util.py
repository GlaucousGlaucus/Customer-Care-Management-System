import colorama

code = lambda x: f"\033[{x}m"

class text_formatting:
    BOLD = code(1)
    CLEAR = code(2)
    ITALIC = code(3)
    UNDERLINE = code(4)
    BLINKING = code(5)
    STRIKETHROUGH = code(9)

