import random

Quizes = []

def quiz(quiz_fn):
  Quizes.append(quiz_fn)
  return quiz_fn

def run_quiz(quiz):
  """Run a quiz repeatedly until the user types C-c.
  
  Each call to quiz() should return a 2-tuple of (question string, answer int)"""
  try:
    while True:
      question, correct_answer = quiz()
      answer = None
      while True:
        answer = input(question)
        if answer and int(answer) == correct_answer:
          print('Correct!\n')
          break
  except KeyboardInterrupt:
    pass
  except EOFError:
    pass

def choose_quiz():
  index = 0
  while True:
    print('Choose a quiz to run:')
    for quiz in Quizes:
      pretty_name = quiz.__name__.replace('_', ' ')
      print('%2d: %s' % (1 + index, pretty_name))
      index += 1
    id = int(input('\nQuiz #: ')) - 1
    if id >= 0 and id < len(Quizes):
      return Quizes[id]

def choose_and_run_quiz():
  quiz = choose_quiz()
  run_quiz(quiz)

def main():
  try:
    while True: choose_and_run_quiz()
  except KeyboardInterrupt:
    pass
  except EOFError:
    pass

@quiz
def multiply_by_11():
  other = random.randrange(10, 99)
  return ('%d x 11 = ' % other, 11 * other)

@quiz
def square_ending_in_5():
  first_digit = random.randrange(1, 9)
  num = first_digit * 10 + 5
  return ('%d ** 2 = ' % num, num * num)

if __name__ == "__main__":
  main()