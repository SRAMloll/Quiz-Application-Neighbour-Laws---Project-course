import flask

app = flask.Flask("quiz")

## Open, read and close a html file

def get_html(page_name) :
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content



## route 1: welcome page and rules

@app.route("/")
def homepage():
    return get_html("index")

## route 2: play the quiz page
@app.route("/quiz.html")
def play_quiz():
    html_page = get_html("quiz")
        
    ### Creating a class Question for each question of the quiz
    class Question:
        def __init__ (self, question, option_1, option_2, option_3, correct_answer):
            self.question = question
            self.option_1 = option_1
            self.option_2 = option_2
            self.option_3 = option_3
            self.correct_answer = correct_answer
      
                      
    ### Creating quiz questions
    q1 = Question("Question 1: Loud music, slamming doors: your neighbour is giving you a hard time! To constitute a night-time disturbance, noise pollution must be committed:", "A. Between 9 p.m. and 7 a.m.", "B. Between 10 p.m. and 6 a.m.", "C. From sunset to sunrise", "B")
   
    ### Showing the questions and the options
    html_page = html_page.replace("$$quiz$$", q1.question)
    options = q1.option_1 + "<br>" + q1.option_2 + "<br>" + q1.option_3
    return html_page.replace("$$choices$$", options)
    
    
    
    


    
   

        
              
 
    
    
    
     



