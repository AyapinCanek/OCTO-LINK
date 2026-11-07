import unittest
from src.simulator import MISSIONS, Mission, shortest_path


class TestMissions(unittest.TestCase):
    def test_exit_reachable(self):
        self.assertIsNotNone(shortest_path(MISSIONS[0]))

    def test_detour_needs_more_than_manhattan_distance(self):
        m = MISSIONS[1]
        path = shortest_path(m)
        self.assertIsNotNone(path)
        self.assertGreater(len(path) - 1, abs(m.goal[0] - m.start[0]) + abs(m.goal[1] - m.start[1]))

    def test_unreachable(self):
        self.assertIsNone(shortest_path(MISSIONS[2]))

    def test_no_wall_crossing(self):
        for m in MISSIONS:
            path = shortest_path(m)
            if path is None:
                continue
            self.assertEqual(path[0], m.start)
            self.assertEqual(path[-1], m.goal)
            for point in path:
                self.assertNotEqual(m.grid[point[1]][point[0]], '#')
            for a, b in zip(path, path[1:]):
                self.assertEqual(abs(a[0] - b[0]) + abs(a[1] - b[1]), 1)

    def test_bad_map(self):
        with self.assertRaises(ValueError):
            shortest_path(Mission("error", ("##", "#"), (0, 0), (1, 0)))


if __name__ == "__main__":
    unittest.main()
