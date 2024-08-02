import flask

app = flask.Flask("quiz")

## Open, read and close a html file

def get_html(page_name) :
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

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

    ### Creating a class Question:
    class Quiz_game:
        def __init__ (self, correct_answer, user_answer):
            self.correct_answer = correct_answer
            self.user_answer = user_answer
            
            
        def check_answer (self):
            return self.user_answer == self.correct_answer
              
                                
        def update_score (self):
            score_question = 0
            if self.check_answer():
                score_question =+ 1 
            return score_question
                        
    ### Creating quiz questions (objects)
    q1 = Quiz_game("B", flask.request.args.get("query1"))
    q2 = Quiz_game("A", flask.request.args.get("query2"))
    q3 = Quiz_game("C", flask.request.args.get("query3"))
    q4 = Quiz_game("A", flask.request.args.get("query4"))
    q5 = Quiz_game("C", flask.request.args.get("query5"))
    
    questions_list = [q1, q2, q3, q4, q5]
    
    ### Calling the methods to check answers and score:
    
    q1.check_answer()
    question_score = q1.update_score()
    if q1.check_answer():
        return html_page.replace("$$results$$", "Your result is correct and your score is " + str(question_score) + " !")
    

    
    
    


    
   

        
              
 
    
    
    
     



