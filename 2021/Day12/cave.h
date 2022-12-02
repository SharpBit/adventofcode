#pragma once
#include <iostream>
#include <vector>

class Cave {
public:
	std::string id;
	bool isSmall;
	bool visited;
	std::vector<std::string> linkedCaves;

	Cave();
	Cave(std::string caveID);
	void addLink(std::string caveID);
};