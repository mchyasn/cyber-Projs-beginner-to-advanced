import time
import string

# Simulated secret password
SECRET = "cyber"

def insecure_compare(user_input):
    for i in range(len(user_input)):
        if i >= len(SECRET) or user_input[i] != SECRET[i]:
            return False
        time.sleep(0.1)  # Leak: delay for correct characters
    return len(user_input) == len(SECRET)

def guess_password():
    guessed = ""
    chars = string.ascii_lowercase
    while len(guessed) < len(SECRET):
        max_time = 0
        next_char = ''
        for ch in chars:
            attempt = guessed + ch
            start = time.time()
            insecure_compare(attempt)
            elapsed = time.time() - start
            if elapsed > max_time:
                max_time = elapsed
                next_char = ch
        guessed += next_char
        print(f"[+] Guessed so far: {guessed}")
    print(f"[✔] Final password guess: {guessed}")

if __name__ == "__main__":
    guess_password()
