import random
word_list = ['knee', 'knife', 'knock', 'adapt', 'know', 'affect', 'land', 'afford', 'lap', 'large', 'last', 'borrow', 'map', 'margin', 'budget', 'mark', 'market', 'campus', 'nerve', 'civil', 'oppose', 'deal', 'porch', 'port', 'pose', 'quit', 'elite', 'quote', 'recipe', 'email', 'emerge', 'refuse', 'regard', 'scope', 'score', 'fiber', 'scream', 'screen', 'field', 'script', 'tactic', 'forest', 'tail', 'forget', 'form', 'talent', 'formal', 'uncle', 'gear', 'gender', 'gene', 'video', 'view', 'viewer', 'holy', 'weapon', 'home', 'wear', 'image', 'week', 'impact', 'year', 'income', 'yell', 'yellow', 'joy', 'judge', 'equal', 'lord', 'king', 'france', 'cousin', 'will', 'move', 'speedy', 'friend', 'seem', 'make', 'denial', 'love', 'wisdom', 'answer', 'mean', 'freely', 'leave', 'stand', 'part', 'well', 'serve', 'gentry', 'sick', 'enter', 'count', 'good', 'young', 'youth', 'bear', 'father', 'face', 'frank', 'nature', 'haste', 'moral', 'paris', 'duty', 'look', 'time', 'long', 'steal', 'talk', 'return', 'hide', 'honour', 'like', 'pride', 'clock', 'true', 'minute', 'speak', 'tongue', 'obey', 'hand', 'place', 'proud', 'poor', 'praise', 'copy', 'follow', 'rich', 'royal', 'speech', 'always', 'say', 'hear', 'word', 'ear', 'grow', 'live', 'begin', 'heel', 'flame', 'lack', 'snuff', 'sense', 'expire', 'wish', 'honey', 'bring', 'home', 'hive', 'give', 'room', 'lend', 'fill', 'know', 'month', 'rest', 'debate', 'stock', 'exchange', 'note', 'sell', 'equity', 'large', 'liquid', 'attractive', 'guarantor', 'settlement', 'counter', 'dealer', 'different', 'attract', 'cover', 'interest', 'frequently', 'likely', 'trade', 'transfer', 'money', 'security', 'seller', 'buyer', 'agree', 'price', 'ownership', 'particular', 'company', 'market', 'range', 'small', 'individual', 'larger', 'world', 'include', 'insurance', 'pension', 'hedge', 'trader', 'physical', 'floor', 'method', 'known', 'open', 'offer', 'type', 'network', 'example', 'potential', 'specific', 'accept', 'match', 'sale', 'place', 'multiple', 'purpose', 'facilitate', 'provide', 'real', 'discovery', 'hybrid', 'location', 'flow', 'broker', 'order', 'post', 'maintain', 'spread', 'case', 'close', 'difference', 'tape', 'brokerage', 'firm', 'investor', 'play', 'important', 'role', 'program', 'electronic', 'computer', 'similar', 'purchase', 'drive', 'late', 'system']

def get_word():
    choice = random.choice(word_list).upper()
    return choice

def display_hangman(mistakes):
    stages = [      # 0 mistakes
                    '''
                       --------
                       |      |
                       |      
                       |    
                       |      
                       |     
                       -
                    ''',
                    # 1 mistake
                    '''
                       --------
                       |      |
                       |      O
                       |    
                       |      
                       |     
                       -
                    ''',
                    # 2 mistakes
                    '''
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    ''',
                    # 3 mistakes
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |     
                       -
                    ''',
                    # 4 mistakes
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |      
                       -
                    ''',
                    # 5 mistakes
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / 
                       -
                    ''',
                    # The End: 6 mistakes
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    ''']
    return stages[mistakes]

name = input('What is your name? - ')
next_game = '+'

def play():
    word = get_word()
    l = len(word)
    mistakes = 0    
    inputs = []
    
    print(f'''Hello, {name}! Welcome to Guess the Word Play!
    The Bot has chosen a word for you, and now your task is to guess it.
    It can be either a noun, a verb, or an adjective.
    Remember: 6 mistakes - and you\'ll find yourself hanging on the gallows.
    Good luck, chicken shit!''')
    answer = ['_' for _ in range(l)]
    print(f'The chosen word has {l} letters. Let\'s begin!')
    
    while mistakes < 6:
        while '_' in answer:
            print('Enter the letter, you think, is in the hidden word: ')
            letter = input().upper()
            if letter in inputs:
                print('You\'ve already named this letter, try another one.')
                break            
            if letter in word:
                for i in range(l):
                    if word[i] == letter:
                        answer[i] = letter
                print('Wow! Are you a fucking magician or something?! You guessed it!')
            else:
                mistakes += 1 
                print(f'You guessed wrong, stupid asshole! Let\'s see you hanging :*')
        
            print(f'Your progress: {"".join(answer)}. You', 'still ' * (mistakes < 6) + 'have', 'only ' * (mistakes == 5) + f'{6 - mistakes} attempt' + 's' * (mistakes != 5), 'left to survive.')
            print(display_hangman(mistakes))     
            inputs.append(letter)            
            break
        else:
            print('Congratulations! You saved your ass this time - you guessed the word! Mr. Hangman will generously spare your life.')
            global next_game            
            next_game = input('''Although, if you\'re still willing to press your luck and eventually die on the gallows, of course -
            you're welcome to start the Game once again. Just tap '+', little shit, let's see what you've got!
            Or press '-' and get out of here for good, man: ''')
            break
        
    else:
        print('''Sorry to inform, but you\'ve run out of chances to save your miserable life, dumbass, ha-ha!
        Go see your ancestors! And good luck next time.''')
        print('The answer was just around the corner... (not really, blockhead):', word) 
        next_game = input(f'''Although, in case you wanna die multiple times, the Game is always at your service, dear little {name}.
        Just press '+' to start over, or go cry to your mommy with '-': ''')

while next_game == '+':
    play()
else:
    print('\n' + 'Well, it was pleasure to spend time with you. Bye-bye, honey! Take care.')