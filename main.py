import flask

app = flask.Flask("quiz")

# Functions/ class definition

## Open, read and close a html file

def get_html(page_name) :
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

## Creating a class Question for each question of the quiz
class Question:
    def __init__(self, question, choices, correct_answer):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer
    ### method to check the correct answer
    def check_answer (self, user_answer):
        return user_answer == self.correct_answer        

## Creating quiz questions
question_1 = Question("Loud music, slamming doors: your neighbour is giving you a hard time! To constitute a night-time disturbance, noise pollution must be committed:", ["A. Between 9 p.m. and 7 a.m.", "B. Between 10 p.m. and 6 a.m.", "C. From sunset to sunrise"], "B")
question_2 = Question("You live in Lausanne and the branches of your neighbour's cherry tree encroach on your property:", ["A. You have the right to pick the cherries from the branches overhanging your property.",
"B. You can pick the cherries, only if they have fallen from the tree.", "C. You do not have the right to pick the cherries, whether on the tree or on the ground."], "A")
question_3 = Question("Your neighbour has installed a camera outside his house. Do they have to ask your permission?", ["A. Yes, you cannot be sure what he is recording.", "B. No, he or she has the right to protect his/her private property.", "C. It depends where the camera is oriented."], "C")
question_4 = Question("Is your neighbour allowed to burn branches, twigs and dead leaves in his garden?", ["A. Yes", "B. No", "C. Only in the countryside."], "A")
question_5 = Question("You are helping your neighbour to dig a hole in his garden for his swimming pool. While he's away, your pick hits a historical chest containing gold coins. Who does this treasure belong to?", ["A. The one who found the treasure.", "B. The neighbour who is the owner of the land.", "C. None of them."], "C")

## Creating a class Quiz to ask the questions and keep the score.

class Quiz:
    def __init__ (self, questions):
        self.questions = questions
        self.score = 0
    

# routes definition

## route 1: welcome page and rules
@app.route("/")
def homepage():
    return get_html("index")

## route 2: play the quiz page
@app.route("/quiz.html")
def play_quiz():
    html_page = get_html("quiz")
    ### insert method to play the quiz here:
    
## route 3: score page

