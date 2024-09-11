#!/usr/bin/env python
"""
main.py
-------
This file serves as the entry point for running the BlogAgentBoiler framework.
It provides several commands to manage agents, execute tasks, and control workflows.

Ensure that your environment variables (API keys, model names, etc.) are set in the .env file.

This file is designed to be executed using:
    poetry run ScribeStarter
"""

import sys
import os
from dotenv import load_dotenv
from crew_ai.crew import BlogagentCrew

# Load environment variables from the .env file
load_dotenv()

# Set necessary environment variables (this can be extended as needed)
os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME", "gpt-4o")


def run():
    print("Running crew")
    """
    Run the crew.
    """
    inputs = {
        "url": "https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/l"
    }
    BlogagentCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "url": "https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/"
    }
    try:
        BlogagentCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An esrror occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        BlogagentCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "url": "https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/"
    }
    try:
        BlogagentCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
