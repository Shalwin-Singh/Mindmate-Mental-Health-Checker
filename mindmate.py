def ask_questions():
    print("Welcome to MindMate - Your Mental Health Checker")
    print("Please answer the following questions with 'yes' or 'no'.\n")

    questions = [
        "Do you often feel anxious or worried?",
        "Have you been feeling unusually sad or down lately?",
        "Do you struggle to fall asleep or stay asleep?",
        "Do you find it hard to concentrate on tasks?",
        "Have you lost interest in activities you once enjoyed?",
        "Do you feel tired or have little energy most days?",
        "Do you feel bad about yourself or that you are a failure?",
        "Have you been isolating yourself from friends or family?",
        "Do you feel overwhelmed with daily responsibilities?",
        "Have you had thoughts of self-harm or hurting yourself?"
    ]

    score = 0

    for q in questions:
        while True:
            answer = input(q + " (yes/no): ").strip().lower()
            if answer in ['yes', 'no']:
                break
            print("Please answer with 'yes' or 'no'.")

        if answer == 'yes':
            score += 1

    return score

def evaluate_health(score):
    if score <= 2:
        return "Great"
    elif 3 <= score <= 6:
        return "Moderate"
    else:
        return "Poor"

def main():
    score = ask_questions()
    status = evaluate_health(score)

    print("\nYour Mental Health Status: ", status)
    if status == "Great":
        print("You're doing well! Keep maintaining a healthy routine.")
    elif status == "Moderate":
        print("You're experiencing some challenges. Consider talking to someone or taking small steps to self-care.")
    else:
        print("You might be going through a tough time. It's highly recommended to speak with a mental health professional.")

if __name__ == "__main__":
    main()
