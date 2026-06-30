import requests
from backend.app.llm.base import BaseLLM, LLMGenerationError

class OllmaClient(BaseLLM):
    def __init__(
            self,
            model: str = "llama3",
            base_url: str = "http://localhost:11434",
            timeout: int = 60,
    ):
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def generate(self, prompt: str) -> str:
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty")
        
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "format": "json",
                },
                timeout=self.timeout,
            )
            response.raise_for_status()

        except requests.RequestException as error:
            raise LLMGenerationError(
                "Failed to generate response from Ollama."
            ) from error
        
        data = response.json()
        answer = data.get("response", "").strip()

        if not answer:
            raise LLMGenerationError("Ollama returned an empty response.")
        
        return answer