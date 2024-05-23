from django.db import models


# Model to store questions with two options and the correct answer
class Question(models.Model):
    # The text of the question
    question_text = models.CharField(max_length=255)
    # Option A for the question
    option_a = models.CharField(max_length=255)
    # Option B for the question
    option_b = models.CharField(max_length=255)

    # True option
    answer = models.CharField(max_length=1, choices=[
        ('A', 'Option A'),
        ('B', 'Option B')
    ])

    def __str__(self):
        return self.question_text
