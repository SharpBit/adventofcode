#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include "point.h"


int main() {
    std::ifstream input("input.txt");
    std::string line;
    std::vector<Point> octopi;

    int x = 0;
    while (input >> line) {
        for (int y = 0; y < line.length(); y++) {
            octopi.push_back(Point(x, y, line[y] - '0'));
        }
        x++;
    }

    int flashes = 0;
    int syncStep = -1;
    int s = 1;
    while (s <= 100 || syncStep == -1) {
        int stepFlashes = 0;

        std::queue<Point*> queue;  // For some reason queue.front() makes a copy so I have to use pointers
        for (Point& p : octopi) {
            p.isFlashed = false;
            p.energy++;
            if (p.energy > 9) {
                queue.push(&p);
            }
        }

        while (!queue.empty()) {
            Point *point = queue.front();

            queue.pop();
            if (point->isFlashed) continue;
            point->isFlashed = true;
            point->energy = 0;

            for (int xdiff = -1; xdiff <= 1; xdiff++) {
                for (int ydiff = -1; ydiff <= 1; ydiff++) {
                    if (xdiff == 0 && ydiff == 0) continue;
                    for (Point& p : octopi) {
                        if (p.x == point->x + xdiff && p.y == point->y + ydiff && !p.isFlashed) {
                            p.energy++;
                            if (p.energy > 9) {
                                queue.push(&p);
                                break;
                            }
                        }
                    }
                }
            }
        }

        for (Point& p : octopi) {
            if (p.isFlashed) {
                stepFlashes++;
                if (s <= 100) {
                    flashes++;
                }
            }
        }
        if (stepFlashes == octopi.size() && syncStep == -1) {
            syncStep = s;
        }
        s++;
    }
    std::cout << "Part 1: " << flashes << std::endl;
    std::cout << "Part 2: " << syncStep << std::endl;

    return 0;
}
