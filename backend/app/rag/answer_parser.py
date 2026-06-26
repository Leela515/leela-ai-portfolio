import json
from dataclasses import dataclass

class AnswerParsingError(Exception):
    """Raised when the LLM output cannot be parsed as a valid answer."""

@dataclass(frozen=True)
class ParsedAnswer:
    answer: str
    used_sources: list[str]

class AnswerParser:
    def parse(self, raw_output: str) -> ParsedAnswer:
        try:
            data = json.loads(raw_output)
        except json.JSONDecodeError as error:
            raise AnswerParsingError("LLM output was not valid JSON.") from error

        answer = data.get("answer")
        used_sources = data.get("used_sources", [])

        if not isinstance(answer, str) or not answer.strip():
            raise AnswerParsingError("Parsed answer is missing or empty.")

        if not isinstance(used_sources, list) or not all(
            isinstance(source, str) for source in used_sources
        ):
            raise AnswerParsingError("used_sources must be a list of strings.")

        return ParsedAnswer(
            answer=answer.strip(),
            used_sources=used_sources,
        )