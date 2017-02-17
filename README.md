<hi>CommandLine-App-</h1>

<h3>SYNOPSIS</h3>
<p>This application contains quizzes that a user could take ,a user could also import a JSON file containing quizzes and get a score after completion.</p>

<h3>INSTALLATION</h3>

<br>pip install docopt==0.6.2</br>
<br>virtual environment</br>


<h3>COMMANDS</h3>
 <b>quizlist</b> <p>- displays a list of available quizzes</p>
 <b>import 'path_to_quiz_JSON'></b> <p>-enables user to import</p>
 <b>quiztake 'quiz_name'</b> -<p>enables a user to take a quiz and gives score</p>
    
 <b>(-h|--help)</b> -displays lists of viable commands
IMPORTS
import cmd
from docopt import docopt, DocoptExit
import time
import json
import os
from firebase import firebase
