quiz = {}
quiz['History'] = {
       'question': 'Question one',
       'text':'Who is the president of USA ?\n',
       'options 1':'Barack Obama ',
       'options 2':'Donald Trump'
}
      
quiz['Math'] = {
       'question': 'Question one',
       'text':'What is the formula of finding the area of rectangle ?',
       'option 1':'length * width * height'
       
}
quiz['English'] = {
       'question': 'Question one',
       'text':'What is the plural of octupus ?',
       'options 1':'octopuses',
       'options 2':'octupi'
}

import json
s = json.dumps(quiz)
with open("/home/janet/Desktop/ quiz .txt", "w") as f:
     f.write(s)
