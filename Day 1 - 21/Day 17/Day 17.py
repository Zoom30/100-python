# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User(1, "Daniel")
#
# user_2 = User(2, "Dan")
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

# ============================================

# Quiz Game
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
# My method
for index in range(0, len(question_data)):
    question_text = question_data[index]["text"]
    question_answer = question_data[index]["answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
quiz.next_question()
while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# Angela's method
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)
