"""
ASCII Art Generator — no external libraries needed!
Uses a hand-drawn 5x7 pixel font for each letter.
"""

FONT = {
    'A': ['  █  ', ' █ █ ', '█████', '█   █', '█   █'],
    'B': ['████ ', '█   █', '████ ', '█   █', '████ '],
    'C': [' ████', '█    ', '█    ', '█    ', ' ████'],
    'D': ['████ ', '█   █', '█   █', '█   █', '████ '],
    'E': ['█████', '█    ', '████ ', '█    ', '█████'],
    'F': ['█████', '█    ', '████ ', '█    ', '█    '],
    'G': [' ████', '█    ', '█  ██', '█   █', ' ████'],
    'H': ['█   █', '█   █', '█████', '█   █', '█   █'],
    'I': ['█████', '  █  ', '  █  ', '  █  ', '█████'],
    'J': ['█████', '   █ ', '   █ ', '█  █ ', ' ██  '],
    'K': ['█   █', '█  █ ', '███  ', '█  █ ', '█   █'],
    'L': ['█    ', '█    ', '█    ', '█    ', '█████'],
    'M': ['█   █', '██ ██', '█ █ █', '█   █', '█   █'],
    'N': ['█   █', '██  █', '█ █ █', '█  ██', '█   █'],
    'O': [' ███ ', '█   █', '█   █', '█   █', ' ███ '],
    'P': ['████ ', '█   █', '████ ', '█    ', '█    '],
    'Q': [' ███ ', '█   █', '█ █ █', '█  ██', ' ████'],
    'R': ['████ ', '█   █', '████ ', '█  █ ', '█   █'],
    'S': [' ████', '█    ', ' ███ ', '    █', '████ '],
    'T': ['█████', '  █  ', '  █  ', '  █  ', '  █  '],
    'U': ['█   █', '█   █', '█   █', '█   █', ' ███ '],
    'V': ['█   █', '█   █', '█   █', ' █ █ ', '  █  '],
    'W': ['█   █', '█   █', '█ █ █', '██ ██', '█   █'],
    'X': ['█   █', ' █ █ ', '  █  ', ' █ █ ', '█   █'],
    'Y': ['█   █', ' █ █ ', '  █  ', '  █  ', '  █  '],
    'Z': ['█████', '   █ ', '  █  ', ' █   ', '█████'],
    '0': [' ███ ', '█  ██', '█ █ █', '██  █', ' ███ '],
    '1': ['  █  ', ' ██  ', '  █  ', '  █  ', '█████'],
    '2': [' ███ ', '█   █', '  ██ ', ' █   ', '█████'],
    '3': ['████ ', '    █', ' ███ ', '    █', '████ '],
    '4': ['█   █', '█   █', '█████', '    █', '    █'],
    '5': ['█████', '█    ', '████ ', '    █', '████ '],
    '6': [' ███ ', '█    ', '████ ', '█   █', ' ███ '],
    '7': ['█████', '    █', '   █ ', '  █  ', ' █   '],
    '8': [' ███ ', '█   █', ' ███ ', '█   █', ' ███ '],
    '9': [' ███ ', '█   █', ' ████', '    █', ' ███ '],
    '!': ['  █  ', '  █  ', '  █  ', '     ', '  █  '],
    '?': [' ███ ', '    █', '  ██ ', '     ', '  █  '],
    '.': ['     ', '     ', '     ', '     ', '  █  '],
    ' ': ['     ', '     ', '     ', '     ', '     '],
}

STYLES = {
    '1': ('Default (blocks)',   '█', '░'),
    '2': ('Bold (filled)',      '#', '.'),
    '3': ('Light (dots)',       '•', ' '),
    '4': ('Stars',              '★', '·'),
}

def render(text, on_char='█', off_char=' '):
    text = text.upper()
    rows = [''] * 5
    for i, ch in enumerate(text):
        glyph = FONT.get(ch, FONT[' '])
        for row_idx, row in enumerate(glyph):
            rows[row_idx] += row.replace('█', on_char).replace(' ', off_char)
        if i < len(text) - 1:
            for row_idx in range(5):
                rows[row_idx] += off_char  # letter spacing
    return rows

def main():
    print('\n  ✨  ASCII Art Generator\n')
    print('  Available styles:')
    for key, (name, on, off) in STYLES.items():
        print(f'    [{key}] {name}')

    style = input('\n  Pick a style (1-4, default 1): ').strip() or '1'
    _, on_char, off_char = STYLES.get(style, STYLES['1'])

    while True:
        text = input('\n  Enter text to render (or "quit" to exit): ').strip()
        if text.lower() in ('quit', 'exit', 'q'):
            print('\n  Bye! ✨\n')
            break
        if not text:
            continue
        if len(text) > 15:
            print('  (Tip: long text may wrap — try 15 chars or fewer)')
        print()
        for row in render(text, on_char, off_char):
            print('  ' + row)
        print()

if __name__ == '__main__':
    main()
