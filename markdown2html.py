#!/usr/bin/python3

"""
A script to convert Markdown files to HTML files.
Usage: ./markdown2html.py README.md README.html
"""

import sys
import os

def main():
    """
    Main function to handle command-line arguments and file existence checks.
    """
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
 
    markdown_file = sys.argv[1]

    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
