#include "cave.h"
#include <algorithm>

Cave::Cave() {
	id = "";
	isSmall = false;
	visited = false;
}

Cave::Cave(std::string caveID) {
	id = caveID;
	isSmall = std::all_of(caveID.begin(), caveID.end(), [](unsigned char c) { return std::islower(c); });
	visited = false;
}

void Cave::addLink(std::string caveID) {
	linkedCaves.push_back(caveID);
}
