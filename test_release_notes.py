"""
Tests for the pure, non-API parts of release_notes.py.

These don't call the Gemini API, so they run without a real API key.
"""

import os
import tempfile
import unittest

import release_notes


class BuildPromptTests(unittest.TestCase):
    def test_includes_raw_text(self):
        prompt = release_notes.build_prompt("Added dark mode toggle")
        self.assertIn("Added dark mode toggle", prompt)

    def test_includes_required_headings(self):
        prompt = release_notes.build_prompt("some entry")
        for heading in ("Features", "Fixes", "Improvements", "Other"):
            self.assertIn(heading, prompt)

    def test_includes_human_review_instruction(self):
        prompt = release_notes.build_prompt("some entry")
        self.assertIn("Needs Human Review", prompt)

    def test_wraps_raw_text_in_delimiters(self):
        prompt = release_notes.build_prompt("some entry")
        self.assertIn("<raw_notes>", prompt)
        self.assertIn("</raw_notes>", prompt)


class LogResultTests(unittest.TestCase):
    def test_appends_timestamped_entry(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            log_path = os.path.join(tmp_dir, "log.md")
            original_log_file = release_notes.LOG_FILE
            release_notes.LOG_FILE = log_path
            try:
                release_notes.log_result("**Features**\n* Example entry")
                with open(log_path, encoding="utf-8") as f:
                    contents = f.read()
                self.assertIn("## ", contents)
                self.assertIn("Example entry", contents)
            finally:
                release_notes.LOG_FILE = original_log_file


if __name__ == "__main__":
    unittest.main()
