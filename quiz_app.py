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
from firebase import firebase



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

      path_to_json = "/home/janet/Desktop/docopt"
      all_json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        #checks for every file with extension .json available for import by user
      print all_json_files 
      for r in all_json_files :
       with open(os.path.join(path_to_json, r)) as all_json_files :
        # do something with your json; I'll just print
             data = json.load(all_json_files  )
             
             for k,v in data.items(): 
                    print (str(k))
                    print (str(v))
                
           
           
           
     
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
                print (data['question one'])
                time.sleep(5)
                raw_input(arg)
                if arg == "B":
                    score = score + 1
                    print "Correct"
                else:
                    print "Incorrect"
                print (data[str('question two')])
                time.sleep(5)
                if arg == "B":
                    score = score + 1
                    print "Correct"
                else:
                    print "Incorrect"
                time.sleep(5)
                print score
    
                
    def do_quit(self, arg):

        print('Goodbye')
        exit()


def main():
    QuizApp().cmdloop()


if __name__ == '__main__':
    main()
