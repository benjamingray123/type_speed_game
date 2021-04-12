import random
import time

#settings
WORD_COUNT = 5
play = True

with open('dictionary.txt') as f:
    ''' read in words from file '''
    words = [f.readline() for line in f]
    words = [word.replace('\n', '') for word in words]

def test_seq_gen(WORD_COUNT):
    ''' selects x random words [list] '''
    test_seq = [random.choice(words) for i in range(WORD_COUNT)]
    return test_seq

def input_timer_speed(WORD_COUNT):
    ''' times user to input() a submission for each word '''
    start_time = time.time()
    user_seq = [input().rstrip() for word in range(WORD_COUNT)]
    end_time = time.time()
    time_elapsed = end_time - start_time
    return user_seq, time_elapsed
    
def score(test_seq, user_seq):
    ''' compare user and test strings character-wise. returns accuracy score '''
    correct_chars, correct_words, total_chars = 0, 0, 0
    for word in test_seq:
        total_chars += len(word)
        
    for i in range(len(test_seq)):
        if test_seq[i] == user_seq[i]:
            correct_words += 1
            correct_chars += len(test_seq[i])
        else:
            for j in range(len(test_seq[i])):
                if test_seq[i][j] == user_seq[i][j]:
                    correct_chars += 1
                    
    accuracy_score = (correct_chars / total_chars)*100
    return accuracy_score, correct_words

def main(play):
    while play:
        test_seq = test_seq_gen(WORD_COUNT)
        print(*test_seq)
        print('\n')
        
        if input('hit [enter] to start the timer: \n') == '':
            user_seq, time_elapsed = input_timer_speed(WORD_COUNT)
            accuracy_score, correct_words = score(test_seq, user_seq)
            wpm = (correct_words / time_elapsed)*60
            print('\n')
            print(f'CORRECT WORDS / TOTAL WORDS: {correct_words} / {WORD_COUNT}')
            print(f'TIME ELAPSED (S): {time_elapsed:.2f}')
            print(f'(ACCURATE) WPM: {wpm:.2f}')
            print(f'ACCURACY(%): {accuracy_score:.2f}\n')
            
main(play)
        
    

    
    
    
