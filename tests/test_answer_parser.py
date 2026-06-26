import pytest

from backend.app.rag.answer_parser import AnswerParser, AnswerParsingError


def test_answer_parser_parses_valid_json():
    parser = AnswerParser()

    parsed = parser.parse(
        '{"answer": "Leela used PyTorch. [Source 1]", "used_sources": ["Source 1"]}'
    )

    assert parsed.answer == "Leela used PyTorch. [Source 1]"
    assert parsed.used_sources == ["Source 1"]


def test_answer_parser_raises_error_for_invalid_json():
    parser = AnswerParser()

    with pytest.raises(AnswerParsingError):
        parser.parse("This is not JSON")


def test_answer_parser_raises_error_for_missing_answer():
    parser = AnswerParser()

    with pytest.raises(AnswerParsingError):
        parser.parse('{"used_sources": ["Source 1"]}')


def test_answer_parser_raises_error_for_invalid_sources():
    parser = AnswerParser()

    with pytest.raises(AnswerParsingError):
        parser.parse('{"answer": "Hello", "used_sources": "Source 1"}')