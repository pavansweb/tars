import json
import os

# Load existing JSON data from a file or create a new structure
def load_json(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        # Create a new structure if file doesn't exist
        print(f"File '{file_path}' not found. Creating a new file.")
        data = {"questions_answers": []}
        save_json(file_path, data)
        return data
    else:
        # If the file exists, load its contents
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Error: The JSON file contains invalid syntax. Resetting the data structure.")
            data = {"questions_answers": []}  # Reset the structure in case of error
        return data

# Save the updated JSON data back to the file
def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Function to add a new question-answer pair to the JSON data
def add_question_answer(data, question, answer):
    new_entry = {
        "question": question,
        "answer": answer
    }
    data['questions_answers'].append(new_entry)

# Main function to interact with the user
def main():
    file_path = "tars_dataset.json"

    # Load existing data or create a new JSON file if it doesn't exist
    data = load_json(file_path)

    while True:
        # Get user input for a new question
        question = input("Enter the question (or type 'upload' to finish): ")
        if question.strip().lower() == 'upload':
            break

        # Get user input for the corresponding answer
        answer = input("Enter the answer: ")

        # Add the new question-answer pair to the JSON structure
        add_question_answer(data, question, answer)

    # Save the updated data when 'upload' is entered
    save_json(file_path, data)
    print("Data has been successfully added and saved to the file.")

if __name__ == "__main__":
    main()
