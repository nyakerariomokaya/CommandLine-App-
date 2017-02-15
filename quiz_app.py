"""
Usage: 
quiz_app quizlist 
quiz_app import <path_to_quiz_JSON>
quiz_app quiz take <quiz_name>
quiz_app (-h|--help)
"""

import cmd
from docopt import docopt, DocoptExit
import time
import json
from collections import Counter


def docopt_cmd(func):
    """
    This decorator describes the annotation @docopt_cmd
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:     
            print('Invalid Command!')
            print(e)
            return
        return func(self, opt)
    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class QuizApp(cmd.Cmd, dict):
    intro = 'Welcome to Quiz_app\n'       
    prompt = '(quiz_app)' 
    
    @docopt_cmd    
    def do_quizlist(self, arg):
        """Usage: quizlist """           
        with open('quizlist.json') as json_data:
            data = json.load(json_data)             
            for k in data: 
                print str(k)

    def do_import(self, arg):
        """Usage:import <path_to_quiz_JSON>"""
        if arg == "history":
            with open('history.json') as json_data:
                data = json.load(json_data)
                for k in data: 
                    print str(k) 
        elif arg == "english":
            with open('english.json') as json_data:
                data = json.load(json_data)                 
                for k in data: 
                    print str(k)
        else:
            with open('math.json') as json_data:
                data = json.load(json_data)
                for k in data: 
                    print str(k) 
                    
    def do_quiztake(self, arg):
        """Usage: quiz take<quiz_name> """
        score = 0
        ans = 0
        choices = "A", "B", "C"
        if arg == "history ":
            with open('history.json') as json_data:
                data = json.load(json_data)
                print str(data)                   
        elif arg == "english":
            with open('english.json') as json_data:
                data = json.load(json_data)
                for k in data: 
                    print str(k)
        elif arg == "math":
            with open('math.json') as json_data:
                data = json.load(json_data) 
                for k in data: 
                    print str(k)
                    
    def do_quit(self, arg):

        print('Goodbye')
        exit()


def main():
    QuizApp().cmdloop()
if __name__ == '__main__':
        main()
