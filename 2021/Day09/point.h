#pragma once
#include <vector>

class Point {
public:
	int x;
	int y;
	Point(int x1, int y1);
	std::vector<Point> adjPoints();
};