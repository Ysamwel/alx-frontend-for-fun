#!/usr/bin/python3
"""
This is a script to convert a Markdown file to HTML.

Usage:
    ./markdown2html.py [input_file] [output_file]

Arguments:
    input_file: the name of the Markdown file to be converted
    output_file: the name of the output HTML file

Example:
    ./markdown2html.py README.md README.html
"""

import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Get the Markdown file name and HTML file name from the arguments
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    try:
        # Try to open the Markdown file to see if it exists
        with open(markdown_file, 'r') as f:
            pass
    except FileNotFoundError:
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # If everything is fine, exit with code 0
    sys.exit(0)
