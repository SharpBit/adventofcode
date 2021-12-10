#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include "point.h"


struct PointCompare {
	bool operator() (const Point& p1, const Point& p2) const {
		if (p1.x != p2.x) {
			return p1.x < p2.x;
		}
		else {
			return p1.y < p2.y;
		}
	}
};

int getValue(const std::vector<std::vector<int>> &heightmap, int x, int y) {
	if (x < 0 || y < 0 || x >= heightmap.size() || y >= heightmap[0].size()) return 9;
	return heightmap.at(x).at(y);
}

// Use BFS to get the basin
int basinSize(const std::vector<std::vector<int>> &heightmap, Point lowPoint) {
	std::queue<Point> queue;
	std::map<Point, bool, PointCompare> visited;
	queue.push(lowPoint);

	while (!queue.empty()) {
		Point p = queue.front();
		queue.pop();
		if (p.x < 0 || p.y < 0 || p.x >= heightmap.size() || p.y >= heightmap.at(0).size() ||
			getValue(heightmap, p.x, p.y) == 9 || visited[p]) continue;  // have to check if it is a 9 first otherwise visited[p] will add that point to the map with default value of false

		visited[p] = true;
		std::vector<Point> adjPoints = p.adjPoints();
		for (const Point &point : adjPoints) {
			queue.push(point);
		}
	}

	return visited.size();
}

bool isLowPoint(const std::vector<std::vector<int>> &heightmap, int x, int y) {
	if (getValue(heightmap, x - 1, y) <= getValue(heightmap, x, y)) return false;
	if (getValue(heightmap, x, y - 1) <= getValue(heightmap, x, y)) return false;
	if (getValue(heightmap, x + 1, y) <= getValue(heightmap, x, y)) return false;
	if (getValue(heightmap, x, y + 1) <= getValue(heightmap, x, y)) return false;
	return true;
}

int main() {
	const int numLargest = 3;  // For part 2

	std::ifstream input("input.txt");
	std::vector<std::vector<int>> heightmap;
	std::string line;
	while (input >> line) {
		std::vector<int> row;
		for (int i = 0; i < line.length(); i++) {
			row.push_back(line[i] - '0');  // converts the char to an int
		}
		heightmap.push_back(row);
	}

	int riskLvl = 0;
	std::vector<int> basinSizes;
	for (int i = 0; i < heightmap.size(); i++) {
		for (int j = 0; j < heightmap.at(0).size(); j++) {
			if (isLowPoint(heightmap, i, j)) {
				riskLvl += 1 + heightmap.at(i).at(j);

				Point p(i, j);
				basinSizes.push_back(basinSize(heightmap, p));
			}
		}
	}

	std::sort(basinSizes.begin(), basinSizes.end(), std::greater<int>());
	int prodLargest = 1;
	for (int i = 0; i < numLargest; i++) {
		prodLargest *= basinSizes[i];
	}

	std::cout << "Part 1: " << riskLvl << std::endl;
	std::cout << "Part 2: " << prodLargest << std::endl;
	return 0;
}