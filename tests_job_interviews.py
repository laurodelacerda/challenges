import job_interviews
import pytest

replacements = [
  {
    "start": 0,
    "before": "hello",
    "after": "bye"
  },
  {
    "start": 6,
    "before": "new",
    "after": "old"
  }
]
def test_replace_substring():
  assert google.replace("hello new world", replacements) == "bye old world"




