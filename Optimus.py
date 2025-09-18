import os
import json
from datetime import datetime

class Optimus:
    def __init__(self, data_file='optimus_qna.json'):
        self.data_file = data_file
        self.qna = self._load_qna()
        self.short_term_memory = []

    def _load_qna(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return []

    def _save_qna(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.qna, f, indent=2)

    def reset_memory(self):
        self.short_term_memory = []
        print("Optimus: Memory reset.")

    def find_answer(self, user_input):
        user_input = user_input.strip().lower()
        for pair in self.qna:
            if pair['question'].strip().lower() == user_input:
                return pair['answer']
        return None

    def chat(self):
        print("Optimus v1.0")
        print("Type 'reset' to clear memory or 'quit' to exit.\n")

        while True:
            try:
                user_input = input("You: ").strip()
                if not user_input:
                    continue

                if user_input.lower() == 'quit':
                    break
                elif user_input.lower() == 'reset':
                    self.reset_memory()
                    continue

                answer = self.find_answer(user_input)

                if answer:
                    print(f"Optimus: {answer}")
                else:
                    print("Optimus: I don't know that yet. Want to teach me? (Type the answer or 'skip')")
                    new_answer = input("Your answer: ").strip()
                    if new_answer.lower() != 'skip':
                        self.qna.append({
                            "question": user_input,
                            "answer": new_answer,
                            "timestamp": datetime.now().isoformat()
                        })
                        self._save_qna()
                        print("Optimus: Got it. I'll remember that.")
                    else:
                        print("Optimus: No problem. Ask me something else.")
            except KeyboardInterrupt:
                print("\nOptimus: Bye!")
                break
            except Exception as e:
                print(f"Optimus: Error - {e}")

if __name__ == "__main__":
    Optimus().chat()
