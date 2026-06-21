from abc import ABC, abstractmethod

class LLMGenerationError(Exception):
    """Raised when the LLM fails to generate a response."""

class BaseLLM(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass