from StudyBuddy import StudyBuddyAssistant

if __name__ == "__main__":
    assistant = StudyBuddyAssistant(
        model_name="llama3.2",
        embedding_model="nomic-embed-text:latest",
        documents_dir="./pdfs_notes"
    )
    
    print('\n> StudyBuddy: Hola! Soy tu asistente para estudiar. ¿Cómo te gustaría que te ayude el día de hoy?')
    while True:
        user_input = input('User:')
        if user_input == 'x':
            break
        print('\n> StudyBuddy:')
        assistant.ask(user_input)
        print('\nPara finalizar con el chat, inserta x')