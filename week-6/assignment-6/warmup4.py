score = int(input('Enter your score: '))
def is_valid_score(score):
     if 0 <= score <= 100:
          return True
         
     else:
        return False
               
if is_valid_score(score):
    print('Valid score.')
else:
    print('Invalid score — must be between 0 and 100.')
