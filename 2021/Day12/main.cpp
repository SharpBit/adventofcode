#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <map>
#include <stack>
#include "cave.h"

int main()
{
    std::ifstream input("input.txt");
    std::string connection;
    std::string cave1, cave2;

    std::map<std::string, Cave> caves;
    while (input >> connection) {
        std::replace(connection.begin(), connection.end(), '-', ' ');
        std::stringstream lineStream(connection);
        lineStream >> cave1;
        lineStream >> cave2;
        if (caves.find(cave1) == caves.end()) {  // Cave not found
            caves[cave1] = Cave(cave1);
        }
        caves[cave1].addLink(cave2);

        if (caves.find(cave2) == caves.end()) {
            caves[cave2] = Cave(cave2);
        }
        caves[cave2].addLink(cave1);
    }

    std::stack<Cave*> stack;
    stack.push(&caves["start"]);

    int paths = 0;
    while (!stack.empty()) {
        Cave* c = stack.top();
        stack.pop();
        if (c->id == "end") {
            paths++;
            continue;
        }
        if (c->visited && c->isSmall) continue;
        c->visited = true;
        for (std::string& caveID : c->linkedCaves) {
            
            if (caves[caveID].id != "start" && (!caves[caveID].isSmall || !caves[caveID].visited)) {
                stack.push(&caves[caveID]);
            }
        }
    }


    std::cout << "Part 1: " << paths << std::endl;
}
