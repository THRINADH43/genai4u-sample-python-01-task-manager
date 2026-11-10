import os
import tempfile
import unittest

import tasks


class TaskTests(unittest.TestCase):
    def test_add_and_complete(self):
        items = []
        tasks.add_task(items, "Buy milk")
        tasks.add_task(items, "Read")
        tasks.complete_task(items, 0)
        self.assertTrue(items[0]["done"])
        self.assertFalse(items[1]["done"])

    def test_delete_closes_up_numbers(self):
        items = []
        for title in ("a", "b", "c"):
            tasks.add_task(items, title)
        tasks.delete_task(items, 0)
        self.assertEqual([t["title"] for t in items], ["b", "c"])

    def test_number_out_of_range(self):
        with self.assertRaises(ValueError):
            tasks.delete_task([], 3)
        with self.assertRaises(ValueError):
            tasks.complete_task([{"title": "x", "done": False}], -1)

    def test_empty_title(self):
        with self.assertRaises(ValueError):
            tasks.add_task([], "   ")

    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "t.json")
            self.assertEqual(tasks.load_tasks(path), [])  # missing file
            items = []
            tasks.add_task(items, "Walk")
            tasks.save_tasks(items, path)
            self.assertEqual(tasks.load_tasks(path), items)

    def test_broken_file(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "t.json")
            with open(path, "w") as f:
                f.write("{oops")
            self.assertEqual(tasks.load_tasks(path), [])


if __name__ == "__main__":
    unittest.main()
