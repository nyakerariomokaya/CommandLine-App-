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
       
    prompt = '(trivia)' 
    score =0
   
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
      
      #print arg 
      with open(arg)as json_data:
                data = json.load(json_data)  
                self.do_quiztake(arg)
      
      
    def do_quiztake(self, arg):
        """Usage: quiz take<quiz_name> """
        score = 0
        ans = ""
        
        path_to_json = "/home/janet/Desktop/docopt"
        all_json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        #checks for every file with extension .json available for import by user
      
        #print arg 
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
                       print ("correct")
                       score +=1
                    else: 
                        print("Incorrect")
                    print("Your score is %s" % (score)) #outputs score
                    
          
                     
    def do_quit(self, arg):

        print('Goodbye')
        exit()
     


def main():
    QuizApp().cmdloop()


if __name__ == '__main__':
    main()
