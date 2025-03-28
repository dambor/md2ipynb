import argparse
import pypandoc

def convert_to_ipynb(input_file, output_file):
    """
    Converts a Markdown file to a Jupyter Notebook file using pypandoc.
    """
    # Convert the Markdown file to a Jupyter Notebook
    result = pypandoc.convert_file(input_file, "ipynb", outputfile=output_file)
    
    # Print the result (usually just a success message)
    print(f"Conversion completed: {result}")

if __name__ == "__main__":
    # Create the command-line interface
    parser = argparse.ArgumentParser(description="Convert a Markdown file to a Jupyter Notebook file.")
    parser.add_argument("input_file", help="the input Markdown file path")
    parser.add_argument("output_file", help="the output Jupyter Notebook file path")
    args = parser.parse_args()
    
    # Convert the input file to a Jupyter Notebook file
    convert_to_ipynb(args.input_file, args.output_file)
