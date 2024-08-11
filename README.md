# Markdown to HTML Converter

This project is a Python script that converts Markdown files into HTML. The goal is to understand how Markdown is rendered into HTML and to implement a tool that can perform this conversion with various Markdown features.

## Project Overview

### Requirements
- **Python Version:** Python 3.7 or higher.
- **Platform:** Ubuntu 18.04 LTS.
- **PEP 8 Compliance:** The code follows the PEP 8 style guide.
- **Execution:** All files are executable and should start with #!/usr/bin/python3.
- **Documentation:** Modules should be documented and not execute code when imported.

### Features
- **Headings:** Converts Markdown headings (#, ##, ###, etc.) into corresponding HTML <h1> to <h6> tags.
- **Unordered Lists:** Converts Markdown unordered lists (-, *) into HTML <ul> and <li> tags.
- **Ordered Lists:** Converts Markdown ordered lists (1., 2., 3.) into HTML <ol> and <li> tags.
- **Paragraphs:** Converts text separated by newlines into HTML paragraphs (<p> tags).
- **Bold and Emphasis:** Converts **bold** to <b> and __emphasis__ to <em> tags.
- **Special Syntax:** Converts special Markdown syntax like [[text]] to its MD5 hash and removes characters from text using ((text)).

## Usage

### Script Execution

To convert a Markdown file to HTML, use the following command:

`ash
./markdown2html.py input.md output.html

## Error Handling
If the number of arguments is less than 2, the script prints an error message:
Usage: ./markdown2html.py README.md README.html

If the Markdown file doesn’t exist, the script prints
Missing <filename>

## Example
Here’s an example of how the script converts a Markdown file:

Input (README.md)
# My title
- Hello
- Bye

Hello

I'm **a** text
with __2 lines__

((I will live in Caracas))

But it's [[private]]

So cool!
Output (README.html)

<h1>My title</h1>
<ul>
  <li>Hello</li>
  <li>Bye</li>
</ul>
<p>Hello</p>
<p>I'm <b>a</b> text<br/>with <em>2 lines</em></p>
<p>I will live in araas</p>
<p>But it's 2c17c6393771ee3048ae34d6b380c5ec</p>
<p>So cool!</p>


Repository
The project is hosted on GitHub:

Repository: alx-frontend-for-fun
File: markdown2html.py
License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
Yvonne Atieno _ Ysamwel
