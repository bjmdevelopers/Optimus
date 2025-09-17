import os
import json
from datetime import datetime
import time
import sys

class Optimus:
    def __init__(self, data_file='optimus_qna.json'):
        self.data_file = data_file
        self.qna = self._load_qna()
        self.short_term_memory = []
        self.user_name = "User"
        
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
        print("\n" + "="*50)
        print("Optimus: Memory cleared successfully.")
        print("="*50 + "\n")
    
    def find_answer(self, user_input):
        for pair in self.qna:
            if pair['question'].strip().lower() == user_input.strip().lower():
                return pair['answer']
        return None
    
    def display_welcome(self):
        welcome = [
            "╔══════════════════════════════════════════╗",
            "║               OPTIMUS                    ║",
            "║    Advanced AI Assistant System          ║",
            "║            Version 1.0.1                 ║",
            "╚══════════════════════════════════════════╝",
            "",
            f"Initialization complete. {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "Type 'help' for available commands.",
            ""
        ]
        for line in welcome:
            print(line)
            time.sleep(0.1)
    
    def display_help(self):
        help_text = [
            "\n" + "═" * 60,
            "OPTIMUS COMMANDS:",
            "═" * 60,
            "help         - Show this help menu",
            "reset        - Clear conversation memory",
            "quit/exit    - End the conversation",
            "time         - Display current date and time",
            "learn        - Teach Optimus a new Q&A pair",
            "═" * 60,
            ""
        ]
        for line in help_text:
            print(line)
    
    def learn_mode(self):
        print("\n" + "═" * 50)
        print("OPTIMUS LEARNING MODE")
        print("═" * 50)
        question = input("Enter the question: ").strip()
        if not question:
            print("Learning cancelled.")
            return
        
        # Check if question already exists
        for pair in self.qna:
            if pair['question'].lower() == question.lower():
                print(f"I already know about: '{question}'")
                print(f"Current answer: {pair['answer']}")
                change = input("Would you like to change the answer? (y/n): ").lower()
                if change == 'y':
                    new_answer = input("Enter the new answer: ").strip()
                    if new_answer:
                        pair['answer'] = new_answer
                        self._save_qna()
                        print("Answer updated successfully!")
                    return
                else:
                    print("Learning mode cancelled.")
                    return
        
        answer = input("Enter the answer: ").strip()
        if not answer:
            print("Learning cancelled.")
            return
            
        self.qna.append({
            "question": question,
            "answer": answer,
            "learned": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self._save_qna()
        print("New knowledge added successfully!")
        print("═" * 50)
    
    def type_effect(self, text, delay=0.03):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def chat(self):
        self.display_welcome()
        
        print("Optimus: Hello, I am Optimus. What is your name?")
        name_input = input("You: ").strip()
        if name_input:
            self.user_name = name_input
        
        self.type_effect(f"Optimus: Nice to meet you, {self.user_name}. How can I assist you today?")
        
        while True:
            try:
                user_input = input(f"{self.user_name}: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit']:
                    self.type_effect("Optimus: Thank you for chatting with me. Have a great day!")
                    break
                
                elif user_input.lower() == 'reset':
                    self.reset_memory()
                
                elif user_input.lower() == 'help':
                    self.display_help()
                
                elif user_input.lower() == 'time':
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.type_effect(f"Optimus: Current date and time is {current_time}")
                
                elif user_input.lower() == 'learn':
                    self.learn_mode()
                
                else:
                    answer = self.find_answer(user_input)
                    if answer:
                        self.type_effect(f"Optimus: {answer}")
                    else:
                        self.type_effect("Optimus: I don't have an answer for that yet.")
                        learn = input("Would you like to teach me? (y/n): ").lower()
                        if learn == 'y':
                            self.learn_mode()
            
            except KeyboardInterrupt:
                print("\n\nOptimus: Session interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"\nOptimus: An error occurred: {str(e)}")

if __name__ == "__main__":
    optimus = Optimus()
    optimus.chat()
