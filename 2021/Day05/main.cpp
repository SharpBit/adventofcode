#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <tuple>
#include <vector>
#include <algorithm>
#include <regex>

struct Point {
    int x;
    int y;
};

// Necessary for Point to be a map key
inline bool operator<(const Point &p1, const Point &p2) {
    if (p1.x != p2.x) {
        return p1.x < p2.x;
    }
    else {
        return p1.y < p2.y;
    }
}

int min(int x, int y) {
    return x < y ? x : y;
}

int max(int x, int y) {
    return x > y ? x : y;
}

int main()
{
    std::string line;
    std::ifstream input("input.txt");

    std::vector<std::pair<Point, Point>> vents;
    while (std::getline(input, line)) {
        line = std::regex_replace(line, std::regex(" -> "), ",");
        std::replace(line.begin(), line.end(), ',', ' ');
        std::stringstream lineStream(line);
        Point p1, p2;
        lineStream >> p1.x;
        lineStream >> p1.y;
        lineStream >> p2.x;
        lineStream >> p2.y;
        vents.push_back(std::make_pair(p1, p2));
    }

    std::map<Point, int> dangerZones;
    for (const auto &v : vents)
    {
        if (v.first.x == v.second.x) {
            for (int y = min(v.first.y, v.second.y); y <= max(v.first.y, v.second.y); y++)
            {
                Point p;
                p.x = v.first.x;
                p.y = y;
                if (dangerZones.find(p) == dangerZones.end()) {
                    dangerZones[p] = 1;
                }
                else {
                    dangerZones[p]++;
                }
            }
        } else if (v.first.y == v.second.y) {
            for (int x = min(v.first.x, v.second.x); x <= max(v.first.x, v.second.x); x++)
            {
                Point p;
                p.x = x;
                p.y = v.first.y;
                if (dangerZones.find(p) == dangerZones.end()) {
                    dangerZones[p] = 1;
                }
                else {
                    dangerZones[p]++;
                }
            }
        }
    }

    int numDanger = 0;
    for (const auto &p : dangerZones) {
        if (p.second >= 2) {
            numDanger++;
        }
    }

    std::cout << "Part 1: " << numDanger << std::endl;

    for (const auto& v : vents) {
        if (v.first.x != v.second.x && v.first.y != v.second.y) {
            int x = min(v.first.x, v.second.x);
            int y, yinc;
            if (x == v.first.x) {
                y = v.first.y;
                yinc = y < v.second.y ? 1 : -1;
            } else{
                y = v.second.y;
                yinc = y < v.first.y ? 1 : -1;
            }
            while (x <= max(v.first.x, v.second.x)) {
                Point p;
                p.x = x;
                p.y = y;
                if (dangerZones.find(p) == dangerZones.end()) {
                    dangerZones[p] = 1;
                }
                else {
                    dangerZones[p]++;
                }
                x++;
                y += yinc;
            }
        }
    }

    int numDanger2 = 0;
    for (const auto &p : dangerZones) {
        if (p.second >= 2) {
            numDanger2++;
        }
    }

    std::cout << "Part 2: " << numDanger2 << std::endl;
}
