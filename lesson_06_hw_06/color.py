""" 2. Створити context manager який буде фарбувати колір виведеного тексту"""


class Colorizer:
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'orange': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'cyan': '\033[36m',
        'lightgrey': '\033[37m',
        'darkgrey': '\033[90m',
        'lightred': '\033[91m',
        'lightgreen': '\033[92m',
        'yellow': '\033[93m',
        'lightblue': '\033[94m',
        'pink': '\033[95m',
        'lightcyan': '\033[96m',
    }

    def __init__(self, color):
        self.color = Colorizer.colors[color]

    def __enter__(self):
        def color(text):
            print(self.color + str(text))
        return color

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(Colorizer.colors['lightgrey'])


with Colorizer('red') as print_color:
    print_color('Hello')
