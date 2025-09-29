import random

activities = [
    "Go for a run",
    "Read a book",
    "Learn a new Python trick",
    "Cook something new",
    "Play a video game",
    "Do 20 push-ups",
    "Listen to music",
    "Take a short nap",
    "Write in a journal",
    "Watch a movie"
]

motivations = [
    "You got this! 💪",
    "Keep pushing forward! 🌟",
    "Make today amazing! ✨",
    "Small steps lead to big wins! 🏆",
    "Believe in yourself! 🙌"
]

choice = random.choice(activities)
motivation = random.choice(motivations)

print("Today's random activity is:", choice)
print("Motivation for you:", motivation)