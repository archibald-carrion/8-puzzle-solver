import os
import IA   # TODO: change name of the file to something more significant

class App():
    def __init__(self):
        print('App is initialized')

    def run(self):
        IA.tryMove()
        print('App is running')