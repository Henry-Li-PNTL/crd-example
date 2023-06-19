from typing import List
import markdown
import pytest


@pytest.mark.parametrize(
    "source, result",
    [
        ("# H1", "<h1>H1</h1>"),
        ("## H1", "<h2>H1</h2>"),
        ("### H1", "<h3>H1</h3>"),
        ("#### H1", "<h4>H1</h4>"),
    ],
)
def test_markdown_to_html(source: str, result: str) -> None:
    assert markdown.markdown(source) == result


