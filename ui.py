from tkinter import *
from quiz_brain import QuizBrain
from data import AMOUNT

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_text = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, "bold"))
        self.score_text.grid(column=1, row=0)
        
        self.canvas = Canvas(width=400, height=300)
        self.question_text = self.canvas.create_text(200, 150, width=350, text="Question goes here", fill=THEME_COLOR, font=("Arial", 17, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, bg=THEME_COLOR, command=self.true_clicked)
        self.true_button.grid(column=0, row=2)
        
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, bg=THEME_COLOR, command=self.false_clicked)
        self.false_button.grid(column=1, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.score_text.config(text="")
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz!\nScore: {self.quiz.score}/{AMOUNT}" )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def true_clicked(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)
        
    def false_clicked(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)
        
    def give_feedback(self, is_correct):
        self.score_text.config(text=f"Score: {self.quiz.score}")
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)        
        