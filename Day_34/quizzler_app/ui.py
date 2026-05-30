from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg= THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width=280,
            text="Some Question Text", 
            font=("Arial", 20, "italic"), 
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.knwon_image = PhotoImage(file="images/true.png")
        self.known_btn = Button(image=self.knwon_image, highlightthickness=0, command=self.true_pressed)
        self.known_btn.grid(row=2, column=0)

        self.unknwon_image = PhotoImage(file="images/false.png")
        self.unknown_btn = Button(image=self.unknwon_image, highlightthickness=0, command=self.false_pressed)
        self.unknown_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.known_btn.config(state="disabled")
            self.unknown_btn.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            bg_color = "green"
        else:
            bg_color = "red"
        
        self.canvas.config(bg=bg_color)

        self.window.after(1000, self.get_next_question)

