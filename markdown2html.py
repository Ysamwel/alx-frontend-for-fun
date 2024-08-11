#!/usr/bin/env python3
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
import os

def main():
    if len(sys.argv) != 3:
        # Print usage message to STDERR and exit with status code 1
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        # Print missing file message to STDERR and exit with status code 1
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)
    
    # No errors, exit with status code 0
    sys.exit(0)

if __name__ == "__main__":
    main()
