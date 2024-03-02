from flask import Flask, request, render_template_string
import pandas as pd
import io
import os
import zipfile

app = Flask(__name__)
    
# Global variable to store DataFrames
dfs = []

@app.route('/', methods=['GET', 'POST'])
def upload_files():
    global dfs  # Access the global variable

    if request.method == 'POST':
        files = request.files.getlist('fileName')
        file_contents = ""

        for file in files:
            try:
                if file.filename.endswith('.zip'):
                    # Handle zip file
                    with zipfile.ZipFile(file, 'r') as zip_ref:
                        # Extract all contents to a temporary directory
                        temp_dir = '/pandas/1'  # Change this to your desired temporary directory
                        zip_ref.extractall(temp_dir)

                        # Read the contents of each extracted file
                        for extracted_file in zip_ref.namelist():
                            with open(os.path.join(temp_dir, extracted_file), 'r') as extracted_file_content:
                                file_contents += extracted_file_content.read()
                                file_contents += "\n\n"

                else:
                    # Handle other file types
                    file_contents += file.read().decode('utf-8')
                    file_contents += "\n\n"

                print(f"Contents of {file.filename}:\n{file_contents}\n{'='*30}\n")

            except pd.errors.ParserError as e:
                print(f"Error reading {file.filename}: {str(e)}")

    return render_template_string("<pre>{{ file_contents }}</pre>", file_contents=file_contents)

if __name__ == '__main__':
    app.run(debug=True)


# Working code
# from flask import Flask, request,  render_template_string
# import pandas as pd
# import io

# app = Flask(__name__)

# # Global variable to store DataFrames
# dfs = []

# @app.route('/', methods=['GET', 'POST'])
# def upload_files():
#     global dfs  # Access the global variable

#     if request.method == 'POST':
#         files = request.files.getlist('fileName')
#         file_contents = ""
#         for file in files:
#             try:
#                 file_contents += file.read().decode('utf-8')
#                 file_contents += "\n\n"
                
#                 print(f"Contents of {file.filename}:\n{file_contents}\n{'='*30}\n")

#             except pd.errors.ParserError as e:
#                 print(f"Error reading {file.filename}: {str(e)}")
                
#     # return file_contents
#     return render_template_string("<pre>{{ file_contents }}</pre>", file_contents=file_contents)

# if __name__ == '__main__':
#     app.run(debug=True)



# Working code with finding a space and semicolon
# from flask import Flask, request, render_template_string
# import pandas as pd
# import io
# import flake8.api.legacy as flake8_legacy
# import tempfile
# import os

# app = Flask(__name__)

# # Global variable to store DataFrames
# dfs = []

# @app.route('/', methods=['GET', 'POST'])
# def upload_files():
#     global dfs  # Access the global variable

#     if request.method == 'POST':
#         files = request.files.getlist('fileName')
#         file_contents = ""

#         for file in files:
#             try:
#                 file_contents += file.read().decode('utf-8')
#                 file_contents += "\n\n"

#                 # Create a temporary file
#                 temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.py')
#                 temp_file.write(file_contents)
#                 temp_file_path = temp_file.name
#                 temp_file.close()

#                 # Perform static code analysis using Flake8
#                 style_guide = flake8_legacy.get_style_guide()
#                 report = style_guide.check_files([temp_file_path])

#                 # Get analysis results
#                 analysis_result_messages = '\n'.join(str(v) for v in report.get_statistics('E'))  # 'E' represents the error category
#                 file_contents += "Static Code Analysis Result:\n"
#                 file_contents += analysis_result_messages

#                 # Delete the temporary file
#                 os.unlink(temp_file_path)

#                 print(f"Contents of {file.filename}:\n{file_contents}\n{'='*30}\n")

#             except pd.errors.ParserError as e:
#                 print(f"Error reading {file.filename}: {str(e)}")

#     return render_template_string("<pre>{{ file_contents }}</pre>", file_contents=file_contents)

# if __name__ == '__main__':
#     app.run(debug=True)



# Not working 
# # Import necessary libraries
# from flask import Flask, request, render_template_string
# import spacy
# import pandas as pd
# import io
# from your_code_generation_module import generate_code

# app = Flask(__name__)
# nlp = spacy.load("en_core_web_sm")

# @app.route('/', methods=['GET', 'POST'])
# def upload_files():
#     if request.method == 'POST':
#         files = request.files.getlist('fileName')
#         file_contents = ""
#         for file in files:
#             try:
#                 file_contents += file.read().decode('utf-8')
#                 file_contents += "\n\n"

#             except pd.errors.ParserError as e:
#                 print(f"Error reading {file.filename}: {str(e)}")

#         # NLP analysis and code generation
#         analyzed_code = analyze_and_generate_code(file_contents)
#         print(f"Contents of {file.filename}:\n{analyzed_code}\n{'='*30}\n")
#         return render_template_string("<pre>{{ file_contents }}</pre>", file_contents=file_contents)
#         # return render_template_string("<pre>{{ analyzed_code }}</pre>", analyzed_code=analyzed_code)

# def analyze_and_generate_code(code):
#     # Use NLP techniques and code generation model
#     # You'll need to implement this part based on your specific requirements
#     generated_code = generate_code(code)
#     return generated_code

# if __name__ == '__main__':
#     app.run(debug=True)
