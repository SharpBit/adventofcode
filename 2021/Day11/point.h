#pragma once
#include <vector>

class Point {
public:
	int x;
	int y;
	int energy;
	bool isFlashed = false;
	Point(int x1, int y1, int energyLvl);
};