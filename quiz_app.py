"""
Usage:     
     quiz_app quizlist 
     quiz_app import <path_to_quiz_JSON>
     quiz_app quiz take <quiz_name>
     quiz_app upload
     quiz_app (-h|--help)
     
"""


import cmd
from docopt import docopt, DocoptExit
import time
import json
import os
import shutil
from clint.textui import colored


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
       
    prompt = '(trivia)' 
   
    @docopt_cmd
    #this function searches for all quiz files and displays them    
    def do_quizlist(self, arg):
        """Usage: quizlist """
        
 
        for file in os.listdir("."):
            if file.endswith(".json"):
                print(file)
    #this functions enables a user to import a json file from a choice path           
    def do_import(self, arg):
         """Usage:import <path_to_quiz_JSON>"""
        dest = "."
    if os.path.isfile(arg):
        shutil.copy(arg, dest)
         
    else:
        print colored.red("File doesn't exist")   
    #this function enables a user to take a test and receive scores  
    def do_quiztake(self, arg):
        """Usage: quiz take<quiz_name> """
        score = 0
        ans = ""
        self.do_quizlist(arg)
      
        with open(arg)as json_data:
                data = json.load(json_data) 
                          
                for k in data["question"]:
                    
                    print k['text']
                    print "A: " + k["A"]
                    print "B: " + k["B"]
                    print "C: " + k["C"]
                   
                    ans = raw_input("Whats your answer:")
                   
                    a = k["answer"]
                    if ans == a:
                        print colored.blue("correct!")
                        score += 1
                    else: 
                        print colored.red("Incorrect!")
                    print colored.green("Your score is %s" % (score))  
                    # outputs score
       
    def do_quit(self, arg):

        print('Goodbye')
        exit()
 
 
def main():
    QuizApp().cmdloop()

if __name__ == '__main__':
    main()
