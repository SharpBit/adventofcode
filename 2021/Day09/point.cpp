#include "point.h"

Point::Point(int x1, int y1) {
	x = x1;
	y = y1;
}

std::vector<Point> Point::adjPoints() {
	std::vector<Point> adj;
	adj.push_back(Point(x - 1, y));
	adj.push_back(Point(x, y - 1));
	adj.push_back(Point(x + 1, y));
	adj.push_back(Point(x, y + 1));
	return adj;
}
