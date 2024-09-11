import requests
from crewai_tools import BaseTool
from typing import Any


class APIFetchTool(BaseTool):
    """
    APIFetchTool is a tool that fetches data from a specified API endpoint.
    This can be used to integrate external data sources into your agent's workflow.
    """

    name: str = "API Fetch Tool"
    description: str = (
        "Fetches data from a given API endpoint and returns the response. "
        "Useful for integrating external data sources into the agent's workflow."
    )

    def __init__(self, api_url: str):
        """
        Initializes the API Fetch Tool with the base API URL.
        """
        super().__init__()
        self.api_url = api_url  # The base URL for the API

    def _run(self, endpoint: str) -> Any:
        """
        Makes a GET request to the specified API endpoint and returns the response.

        Parameters:
        - endpoint: The API endpoint to fetch data from (appended to the base URL).``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

        Returns:
        The JSON response from the API.
        """
        full_url = f"{self.api_url}/{endpoint}"
        response = requests.get(full_url)

        if response.status_code == 200:
            return response.json()  # Return JSON data if the request was successful
        else:
            return f"Failed to fetch data from {full_url}: {response.status_code}"
