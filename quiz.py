import flask 
import math

app = flask.Flask("quiz")

## Open, read and close a html file

def get_html(page_name) :
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

def save_score(user_score):
    text_file =  open("scores.txt", "a")
    text_file.write(str(user_score) + " point(s): " )
    text_file.close()

def save_name(user_name):
    text_file =  open("scores.txt", "a")
    text_file.write(str(user_name) + "\n")
    text_file.close()

def get_scores():
    scoresdb = open("scores.txt")
    content = scoresdb.read()
    scoresdb.close()
    scores = content.split("\n")
    scores_sorted = sorted(scores,reverse=True)
    return scores_sorted


## Creating a class Question:
class QuizGame:
    def __init__ (self, correct_answer, user_answer):
        self.correct_answer = correct_answer
        self.user_answer = user_answer
        self.score = 0
            
    def check_answer (self):
        return self.user_answer.upper() == self.correct_answer
              
    def update_score (self):
        if self.check_answer():
            self.score =+ 1 
        return self.score
    
  
    
## route 1: welcome page 

@app.route("/")
def homepage():
    return get_html("index")
   

## route 2: let the user play the quiz page
@app.route("/quiz.html")
def play_quiz():
    return get_html("quiz")

# route 3: checking answers and displaying results
@app.route("/result.html")
def check_results():
    html_page = get_html("result")
    
    
    
                      
    ### Creating quiz questions (objects)
    q1 = QuizGame("B", flask.request.args.get("query1"))
    q2 = QuizGame("A", flask.request.args.get("query2"))
    q3 = QuizGame("C", flask.request.args.get("query3"))
    q4 = QuizGame("A", flask.request.args.get("query4"))
    q5 = QuizGame("C", flask.request.args.get("query5"))
    
    questions_list = [q1, q2, q3, q4, q5]
    
    ### Calling the methods to check answers and score:
        
    for q in questions_list:
        if (q.user_answer == "A") or (q.user_answer == "B") or (q.user_answer == "C") or (q.user_answer == "a") or (q.user_answer == "b") or (q.user_answer == "c"): 
            q.check_answer()
            q.update_score()

            scores = [q1.score, q2.score, q3.score, q4.score, q5.score]
            total_score = round(math.fsum(scores))
            message = "Your score is " + str(total_score) + " out of 5!"

        else:
            message = "Please retry again and check that you have entered a valid choice: A,B or C."
    
    ### saving the user's score
    try:
        user_score = total_score 
        save_score(user_score)
    except:
        message = "Please retry again and check that you have entered a valid choice: A,B or C."

    return html_page.replace("$$results$$", message )
    
## route 4: display the correct answers page
@app.route("/answers.html")
def answers():
    return get_html("answers")
    
## route 5: display all time scores
@app.route("/scores.html")
def display_scores():
    html_page = get_html("scores")

    ##save user name
    user_name = flask.request.args.get("name")
    if user_name != "":
        save_name(user_name)
    else:
        user_name= "Unknown"
        save_name(user_name)
    
    ##display the saved scores and names
    scores = get_scores()
    actual_scores = ""
    for score in scores:
        actual_scores += "<p>" + score + " </p>"
    return html_page.replace("$$scores$$", actual_scores)
    
    

    


    


    
   

        
              
 
    
    
    
     



