import argparse

from frontend import App

parser = argparse.ArgumentParser(description = '')

parser.add_argument('--open', help = 'Open a window', default = False)

def __main__():
    args = parser.parse_args()

    if args.open:
        app = App()
        app.execute()

if __name__ == '__main__':
    __main__()