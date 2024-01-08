from langchain.tools import tool
from langchain_experimental.utilities import PythonREPL

class PythonTools():

  @tool("Python REPL to execute commands in")
  def python_repl(command):
    """A Python shell. Use this to execute python
    commands. Input should be a valid python command. 
    If you want to see the output of a value, you should print
    it out with `print(...)`."""
    python_repl = PythonREPL()
    resutl = python_repl.run(command)
    return resutl
