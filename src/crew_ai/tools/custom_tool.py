"""
This module defines a customizable tool for the BlogAgentBoiler framework.
It provides a simple structure for creating tools that can perform any custom action or task.
This can be modified to suit the specific needs of your project, whether it's fetching data,
processing information, or interacting with external APIs.

Simply replace the `_run` method's logic with your desired functionality.
"""

from crewai_tools import BaseTool  # Importing BaseTool class to inherit from
from typing import Any


class CustomToolSample(BaseTool):
    """
    CustomToolSample is a placeholder for any custom tool you may need to create for your project.
    It is designed to handle custom logic, making it easy to integrate specific functionalities
    into the BlogAgentBoiler framework.

    Attributes:
    - name: A descriptive name of the tool that is useful for agents to identify what the tool does.
    - description: A detailed description of the tool, which is useful for agents and developers.
    """

    # Tool's name and description, which are important for tool selection by agents
    name: str = "My Custom Tool"
    description: str = (
        "This is a customizable tool that can be modified to perform any task required by the agent. "
        "You can use this as a base for any custom logic you need."
    )

    def __init__(self):
        """
        Initializes the custom tool. This can be extended to include initialization logic,
        such as setting up API connections or loading necessary data.
        """
        super().__init__()  # Call to the parent class's initializer

    def _run(self, argument: Any) -> str:
        """
        Runs the custom tool with the provided argument. Replace the logic here with the specific task you
        want this tool to perform.

        Parameters:
        - argument: Any type of input that your tool requires to perform the task.
          This could be a string, dictionary, or any data structure that makes sense for your custom tool.

        Returns:
        A string (or any other data type) that represents the result of the tool's action.
        """

        # Example logic: Echo the provided argument (You can replace this with your own logic)
        return f"Custom tool executed with input: {argument}"
