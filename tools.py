from langchain_core.tools import tool
import datetime

@tool
def calculator(expression: str) -> str:
    """A simple calculator tool that evaluates mathematical expressions."""
    try:
        builtins_dict = __builtins__ if isinstance(__builtins__, dict) else __builtins__.__dict__
        allowed_names = {k: builtins_dict[k] for k in ["abs", "round", "min", "max", "pow", "sum", "divmod"]}
        
        result = eval(expression, {"__builtins__": allowed_names})
        return str(result)
    except:
        return f"Error: Invalid expression: {expression}"

@tool
def get_current_time() -> str:
    """A tool that returns the current date and time."""

    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')
