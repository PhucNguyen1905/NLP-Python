# NLP Assignment - Plane Question Answering System
### Introduction:
This repository contains the code for my assignment in NLP course. The project focuses on implementing a question-answering system for a simple intercity plane database.


### Folder Hierarchy:
- **main.py**: Program entry point.
- **input/**: Folder to place questions as txt files (Sample format: questions.txt).
- **output/**: Contains 6 output files corresponding to requirements a to f.
- **models/**: Holds helper functions and models for the project.
- **data/**: Includes *atime, dtime*, runtime, and *plane* data.

### Implementation:
The system follows a sequential process where *the output of each step serves as the input* for the next one:

1. **Tokenization:** Tokenize sentences and determine the type of each phrase.

2. **Dependency Parsing:** Perform dependency parsing.

3. **Grammatical Relation Transformation:** Transform the parsed output into grammatical relations.

4. **Logical Form Transformation:** Transform the grammatical relations into logical forms.

5. **Procedure Semantics Transformation:** Transform the logical forms into procedure semantics.

6. **Execution of Procedure Semantics:** Execute the procedure semantics to derive the answer to the given question.



## Installation:
1. **Clone the repository**:
    ```bash
    git clone https://github.com/PhucNguyen1905/NLP-Python.git
    cd NLP=Python
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```


## Run:
- Run the application using the default questions file:
    ```bash
    python main.py
    ```
- Alternatively, specify a custom questions file:
    ```bash
    python main.py file.txt # Default is questions.txt
    ```
    or
    ```bash
    python3 main.py file.txt
    ```
