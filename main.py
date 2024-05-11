import pathlib
import textwrap
import os
from dotenv import load_dotenv
from debug import maquinaEscrever

load_dotenv()

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def main():
  genai.configure(api_key=GOOGLE_API_KEY)

  model = genai.GenerativeModel('gemini-pro')

  def print_center(message):
    terminal_width = os.get_terminal_size().columns
    print(message.center(terminal_width))
    
  os.system("cls" if os.name == "nt" else "clear")
  print_center("Sophie Chat Bot")
  
  while True:
    
    choice = input("\nDigite algo: ")
    response = model.generate_content(choice)
    maquinaEscrever(response.text,0.015)
    
    if choice == "Sair":
      break
    
main()