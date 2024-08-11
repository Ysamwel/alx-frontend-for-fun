#!/usr/bin/python3
"""
This script converts a Markdown file to HTML.

Usage:
    ./markdown2html.py [input_file] [output_file]

Arguments:
    input_file: the name of the Markdown file to be converted
    output_file: the name of the output HTML file

Example:
    ./markdown2html.py README.md README.html
"""

import argparse
import pathlib
import re
import hashlib

def convert_md_to_html(input_file, output_file):
    '''
    Converts a Markdown file to an HTML file
    '''
    with open(input_file, encoding='utf-8') as f:
        md_content = f.readlines()

    html_content = []
    inside_ul = False
    inside_ol = False
    inside_paragraph = False

    for line in md_content:
        line = line.rstrip()

        if line.startswith('#'):
            if inside_ul:
                html_content.append("</ul>\n")
                inside_ul = False
            if inside_ol:
                html_content.append("</ol>\n")
                inside_ol = False
            if inside_paragraph:
                html_content.append("</p>\n")
                inside_paragraph = False
            heading_level = len(line.split(' ')[0])
            heading_text = line[heading_level:].strip()
            html_content.append(f"<h{heading_level}>{heading_text}</h{heading_level}>\n")

        elif line.startswith('-'):
            if inside_ol:
                html_content.append("</ol>\n")
                inside_ol = False
            if not inside_ul:
                if inside_paragraph:
                    html_content.append("</p>\n")
                    inside_paragraph = False
                html_content.append("<ul>\n")
                inside_ul = True
            item_text = line[1:].strip()
            html_content.append(f"  <li>{item_text}</li>\n")

        elif line.startswith('*'):
            if inside_ul:
                html_content.append("</ul>\n")
                inside_ul = False
            if not inside_ol:
                if inside_paragraph:
                    html_content.append("</p>\n")
                    inside_paragraph = False
                html_content.append("<ol>\n")
                inside_ol = True
            item_text = line[1:].strip()
            html_content.append(f"  <li>{item_text}</li>\n")

        else:
            if not inside_paragraph:
                if inside_ul:
                    html_content.append("</ul>\n")
                    inside_ul = False
                if inside_ol:
                    html_content.append("</ol>\n")
                    inside_ol = False
                html_content.append("<p>")
                inside_paragraph = True

            line = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", line)  # Bold
            line = re.sub(r"__(.*?)__", r"<em>\1</em>", line)  # Emphasis
            line = re.sub(r"\[\[(.*?)\]\]", lambda m: hashlib.md5(m.group(1).encode()).hexdigest(), line)  # MD5 hash
            line = re.sub(r"\(\((.*?)\)\)", lambda m: m.group(1).replace('c', ''), line)  # Remove 'c'
            html_content.append(line)

        if not line and inside_paragraph:
            html_content.append("</p>\n")
            inside_paragraph = False

    if inside_ul:
        html_content.append("</ul>\n")
    if inside_ol:
        html_content.append("</ol>\n")
    if inside_paragraph:
        html_content.append("</p>\n")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(html_content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Markdown to HTML')
    parser.add_argument('input_file', help='Path to input Markdown file')
    parser.add_argument('output_file', help='Path to output HTML file')
    args = parser.parse_args()

    input_path = pathlib.Path(args.input_file)
    if not input_path.is_file():
        print(f'Missing {input_path}', file=sys.stderr)
        sys.exit(1)

    convert_md_to_html(args.input_file, args.output_file)
