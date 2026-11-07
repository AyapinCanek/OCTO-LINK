"""Grid-world reference missions: navigation, detour, impossible target.

This simulator is not a model of real neuronal activity or animal behavior.
"""
from collections import deque
from dataclasses import dataclass

Point = tuple[int, int]


@dataclass(frozen=True)
class Mission:
    name: str
    grid: tuple[str, ...]
    start: Point
    goal: Point


def shortest_path(mission: Mission) -> list[Point] | None:
    """Return a collision-free shortest route or None if the goal is unreachable."""
    grid = mission.grid
    height = len(grid)
    if height == 0 or not all(len(row) == len(grid[0]) for row in grid):
        raise ValueError("The map must be non-empty and rectangular")
    width = len(grid[0])

    def valid(p: Point) -> bool:
        x, y = p
        return 0 <= x < width and 0 <= y < height and grid[y][x] != '#'

    if not valid(mission.start) or not valid(mission.goal):
        raise ValueError("Start and goal must be inside accessible cells")
    queue = deque([mission.start])
    previous: dict[Point, Point | None] = {mission.start: None}
    while queue:
        current = queue.popleft()
        if current == mission.goal:
            path: list[Point] = []
            while current is not None:
                path.append(current)
                current = previous[current]
            return list(reversed(path))
        x, y = current
        for nxt in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)):
            if valid(nxt) and nxt not in previous:
                previous[nxt] = current
                queue.append(nxt)
    return None


MISSIONS = (
    Mission("salida", ("#######", "#.....#", "#.###.#", "#.....#", "#######"), (1, 1), (5, 3)),
    Mission("barrera", ("#########", "#...#...#", "#...#...#", "#.......#", "#########"), (1, 1), (7, 1)),
    Mission("imposible", ("#########", "#...#...#", "#...#...#", "#...#...#", "#########"), (1, 1), (7, 1)),
)


def run() -> None:
    for mission in MISSIONS:
        path = shortest_path(mission)
        if path is None:
            print(f"{mission.name}: SIN RUTA (objetivo físicamente inaccesible en este mapa)")
        else:
            print(f"{mission.name}: RUTA ENCONTRADA; movimientos={len(path) - 1}; trayectoria={path}")


if __name__ == "__main__":
    run()
