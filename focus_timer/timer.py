import time
import sys
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_bar(elapsed, total, width=40):
    filled = int(width * elapsed / total)
    bar = '█' * filled + '░' * (width - filled)
    pct = int(100 * elapsed / total)
    return f'[{bar}] {pct}%'

def beep():
    # Simple terminal bell
    print('\a', end='', flush=True)

def format_time(seconds):
    m, s = divmod(int(seconds), 60)
    return f'{m:02d}:{s:02d}'

def run_timer(label, duration_sec):
    start = time.time()
    while True:
        elapsed = time.time() - start
        remaining = duration_sec - elapsed
        if remaining <= 0:
            clear()
            print(f'\n  ✅  {label} complete!\n')
            beep()
            time.sleep(2)
            return
        clear()
        print(f'\n  🍅  Pomodoro Focus Timer\n')
        print(f'  {label}')
        print(f'\n  Time left: {format_time(remaining)}')
        print(f'\n  {draw_bar(elapsed, duration_sec)}\n')
        print('  Press Ctrl+C to cancel\n')
        time.sleep(0.5)

def main():
    sessions = 0
    WORK_MIN = 25
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 15

    print('\n  🍅  Pomodoro Focus Timer')
    print('  ─────────────────────────')
    print(f'  Work:        {WORK_MIN} min')
    print(f'  Short break: {SHORT_BREAK_MIN} min')
    print(f'  Long break:  {LONG_BREAK_MIN} min (every 4 sessions)')
    print('\n  Press Enter to start, Ctrl+C to quit\n')

    try:
        while True:
            input('  > Hit Enter to begin a focus session...')
            sessions += 1
            run_timer(f'Focus session #{sessions}', WORK_MIN * 60)

            if sessions % 4 == 0:
                input(f'  > Session {sessions} done! Long break time. Hit Enter...')
                run_timer('Long break ☕', LONG_BREAK_MIN * 60)
            else:
                input('  > Short break time! Hit Enter...')
                run_timer('Short break 🌿', SHORT_BREAK_MIN * 60)

    except KeyboardInterrupt:
        print(f'\n\n  Goodbye! You completed {sessions} session(s) today. 💪\n')

if __name__ == '__main__':
    main()
