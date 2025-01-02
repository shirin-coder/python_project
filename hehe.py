import time

def sing_lyrics():
    lyrics = [
        "If", "the", "world", "was", "ending,", "I", "wanna", "be", "next", "to", "you..."
    ]
    
    for word in lyrics:
        print(word, end=' ', flush=True)
        time.sleep(0.5)  # Adjust this delay to change the speed

# Sing the lyrics (loop runs only once)
sing_lyrics()
