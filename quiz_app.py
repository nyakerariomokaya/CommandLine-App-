"""

Usage:
     
     quiz_app quiz list <view>
     quiz_app import <path_to_quiz_JSON>
     quiz_app quiz take <quiz_name>
     quiz_app (-h|--help)
"""


import cmd
from docopt import docopt, DocoptExit

def load_json_config():
    import json
    
    source = '''
        {"--force": true,
         "--timeout": "10",
         "--baud": "9600"}
    '''
    return json.loads(source)

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
    
   

    def __init__(self):
        super(QuizApp, self).__init__()
        
     

    @docopt_cmd
    
    def do_quizlist(self, arg):
        """Usage: quiz list <view> """
        
        print(arg)
    

   


    def do_quit(self, arg):

        print('Goodbye')
        exit()


def main():
    QuizApp().cmdloop()


if __name__ == '__main__':
   main()
