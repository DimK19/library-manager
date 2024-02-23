from LibraryApp import app
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-host', '--host', default = '127.0.0.1')

if __name__ == '__main__':
    app.run(host = vars(parser.parse_args()).get('host'), debug = True, port = 8009)
