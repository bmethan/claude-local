import random
import time

WORDS = {
    'easy': [
        'cat', 'dog', 'sun', 'map', 'cup', 'run', 'hat', 'big',
        'red', 'fly', 'zoo', 'arm', 'key', 'box', 'jam',
    ],
    'medium': [
        'brave', 'cloud', 'flame', 'glide', 'hinge', 'joust', 'knack',
        'lemon', 'mango', 'noble', 'olive', 'plumb', 'quirk', 'rivet',
        'sugar', 'tiger', 'umbra', 'vapor', 'waltz', 'yacht',
    ],
    'hard': [
        'blizzard', 'clamber', 'dazzle', 'eclipse', 'frenzy',
        'grapple', 'harmony', 'igloo', 'jigsaw', 'kaleidoscope',
        'labyrinth', 'monarch', 'nucleus', 'odyssey', 'phantom',
        'quantum', 'radiant', 'serenity', 'triumph', 'universe',
    ],
}

def scramble(word):
    letters = list(word)
    for _ in range(20):  # shuffle until it's actually different
        random.shuffle(letters)
        if ''.join(letters) != word:
            break
    return ''.join(letters)

def print_header(score, streak, round_num):
    print(f'\n  🔀  Word Scramble  |  Score: {score}  |  Streak: {streak}🔥  |  Round: {round_num}\n')

def main():
    print('\n  🔀  Word Scramble!')
    print('  ──────────────────────────────')
    print('  Unscramble the word as fast as you can.')
    print('  Type "hint" for a hint (-1 point), "skip" to skip, "quit" to exit.\n')

    print('  Choose difficulty:')
    print('    [1] Easy    (3-letter words)')
    print('    [2] Medium  (5-letter words)')
    print('    [3] Hard    (7-12 letter words)')
    choice = input('\n  Your choice (1/2/3): ').strip()
    difficulty = {'1': 'easy', '2': 'medium', '3': 'hard'}.get(choice, 'medium')
    print(f'\n  Great! Starting {difficulty} mode...\n')

    score = 0
    streak = 0
    round_num = 0
    used_words = set()

    try:
        while True:
            pool = [w for w in WORDS[difficulty] if w not in used_words]
            if not pool:
                used_words.clear()
                pool = WORDS[difficulty][:]

            word = random.choice(pool)
            used_words.add(word)
            jumbled = scramble(word)
            round_num += 1

            print_header(score, streak, round_num)
            print(f'  Scrambled:  {jumbled.upper()}\n')

            hint_used = False
            start = time.time()

            while True:
                guess = input('  Your answer: ').strip().lower()

                if guess == 'quit':
                    raise KeyboardInterrupt

                if guess == 'skip':
                    print(f'\n  Skipped! The word was: {word.upper()}\n')
                    streak = 0
                    break

                if guess == 'hint':
                    if not hint_used:
                        hint_used = True
                        score = max(0, score - 1)
                        print(f'  Hint: The word starts with "{word[0].upper()}" and has {len(word)} letters. (-1 pt)\n')
                    else:
                        print('  You already used your hint for this word!\n')
                    continue

                if guess == word:
                    elapsed = time.time() - start
                    streak += 1
                    bonus = 2 if elapsed < 5 else 1
                    pts = bonus - (1 if hint_used else 0)
                    score += max(1, pts)
                    tag = '⚡ Speed bonus!' if elapsed < 5 else ''
                    print(f'\n  ✅  Correct! +{max(1, pts)} pts  {tag}  (solved in {elapsed:.1f}s)\n')
                    break
                else:
                    print('  ❌  Not quite, try again!\n')

    except KeyboardInterrupt:
        print(f'\n\n  Game over! Final score: {score} points across {round_num} round(s).')
        if streak >= 3:
            print(f'  🔥 You had a {streak}-word streak at the end!')
        print('  Thanks for playing!\n')

if __name__ == '__main__':
    main()
