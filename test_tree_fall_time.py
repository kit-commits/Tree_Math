from __future__ import annotations

import io
import unittest
from contextlib import redirect_stderr
from datetime import datetime
from unittest.mock import patch

from tree_fall_time import estimate_tree_fall_time, main


class TreeFallTimeTests(unittest.TestCase):
    def test_estimate_tree_fall_time_subtracts_sound_delay(self) -> None:
        heard_time = datetime.fromisoformat("2026-06-08T10:00:00")
        result = estimate_tree_fall_time(heard_time, 686)
        self.assertEqual(result.replace(microsecond=0), datetime(2026, 6, 8, 9, 59, 58))

    def test_main_rejects_invalid_timestamp(self) -> None:
        stderr = io.StringIO()
        with patch(
            "sys.argv",
            [
                "tree_fall_time.py",
                "--heard-time",
                "invalid",
                "--distance-meters",
                "10",
            ],
        ), redirect_stderr(stderr), self.assertRaises(SystemExit) as exit_context:
            main()

        self.assertEqual(exit_context.exception.code, 2)
        self.assertIn("must be a valid ISO 8601 timestamp", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
