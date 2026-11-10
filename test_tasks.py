import os
import tempfile
import unittest

import tasks


class TaskTests(unittest.TestCase):
    def test_add_and_complete(self):
        items = []
        tasks.add_task(items, "Buy milk")
        tasks.add_task(items, "Read")
        tasks.complete_task(items, 1)
        self.assertTrue(items[0]["done"])
        self.assertEqual(items[1]["id"], 2)

    def test_delete_unknown_id(self):
        with self.assertRaises(ValueError):
            tasks.delete_task([], 3)

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
                f.write("{not json")
            self.assertEqual(tasks.load_tasks(path), [])


if __name__ == "__main__":
    unittest.main()
