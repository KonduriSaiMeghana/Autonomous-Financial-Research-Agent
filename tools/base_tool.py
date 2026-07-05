# tools/base_tool.py

from abc import ABC, abstractmethod


class BaseTool(ABC):
    """
    Base class for every tool in the Financial Research Agent.
    All tools must inherit from this class.
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def execute(self, **kwargs):
        """
        Every tool must implement this method.
        """
        pass