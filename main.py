from models.Process import *
from models.helper import *

import sys
def main():
    input_file_name = 'questions.txt'
    if len(sys.argv) >=2:
        input_file_name = sys.argv[1]
    input_file_path = './input/'
    
    process = Process.get_instance()


    with open(input_file_path+input_file_name, 'r', encoding='utf-8') as input_file:
        questions = input_file.read().splitlines()
    process.process_base_output()
        
    for question in questions:
        try:
            print("Processing question:", question)
            tokens = tokenize(question)
            types = getWordTypes(tokens)

            process.process_question(question, tokens, types)
        except:
            question

if __name__ == "__main__":
    main()