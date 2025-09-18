
# Optimus Q&A Chatbot

Optimus is a simple, file-based question-and-answer chatbot written in Python. It stores Q&A pairs in a JSON file and allows users to interact with it via a command-line interface. Optimus can learn new answers from users, save them persistently, and retrieve them when the same question is asked again. It also maintains a short-term memory (in-memory) that can be reset.

## Features
- **Persistent Storage**: Q&A pairs are saved in a JSON file (`optimus_qna.json` by default).
- **Learning Capability**: If Optimus doesn't know an answer, users can teach it by providing a new answer.
- **Memory Reset**: Users can reset the short-term memory using the `reset` command.
- **Simple Commands**: Type `quit` to exit or `reset` to clear the short-term memory.
- **Error Handling**: Basic error handling for file operations and user input.

## Requirements
- Python 3.x
- Standard libraries: `os`, `json`, `datetime`

No external dependencies are required.

## Installation
1. Clone or download this repository.
2. Ensure you have Python 3.x installed.
3. Place the `Optimus.py` script in your desired directory.

## Usage
1. Run the script using Python:
   ```bash
   python Optimus.py
   ```
2. Interact with Optimus via the command-line interface:
   - Type a question to get an answer.
   - If Optimus doesn't know the answer, provide one or type `skip`.
   - Use `reset` to clear short-term memory.
   - Use `quit` to exit the program.

Example interaction:
```
Optimus v1.0
Type 'reset' to clear memory or 'quit' to exit.

You: What is the capital of France?
Optimus: I don't know that yet. Want to teach me? (Type the answer or 'skip')
Your answer: Paris
Optimus: Got it. I'll remember that.
You: What is the capital of France?
Optimus: Paris
You: reset
Optimus: Memory reset.
You: quit
Optimus: Bye!
```

## File Structure
- `Optimus.py`: The main Python script containing the Optimus chatbot logic.
- `optimus_qna.json`: The JSON file where Q&A pairs are stored (created automatically when new answers are provided).

## Notes
- The JSON file (`optimus_qna.json`) is created in the same directory as the script when you teach Optimus a new answer.
- The short-term memory (`short_term_memory`) is currently unused in this version but is included for potential future enhancements.
- The chatbot is case-insensitive when matching questions.
- If the JSON file is corrupted or inaccessible, Optimus will start with an empty Q&A list.

## Limitations
- No advanced natural language processing; exact question matches are required.
- Short-term memory is not utilized in this version.
- No support for partial question matching or synonyms.

## Future Improvements
- Add fuzzy matching or NLP for better question recognition.
- Implement short-term memory for contextual conversations.
- Add support for editing or deleting Q&A pairs.
- Include a graphical or web-based interface.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to submit issues or pull requests to improve Optimus. Suggestions for new features or bug fixes are welcome!

## Contact
- For questions or feedback, please open an   issue on the repository.
- Contact Us On Reddit or Twitter.
