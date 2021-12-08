#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

int rangeSum(int n) {
	return n * (n + 1) / 2;
}

int min(int a, int b) {
	return a < b ? a : b;
}

int main() {
	std::string line;
	std::ifstream input("input.txt");
	std::vector<int> crabs;

	while (std::getline(input, line, ',')) {
		crabs.push_back(std::stoi(line));
	}
	std::sort(crabs.begin(), crabs.end());
	int med;
	if (crabs.size() % 2 == 0) {
		med = (crabs.at(crabs.size() / 2) + crabs.at(crabs.size() / 2 - 1)) / 2;
	} else {
		med = crabs.at(crabs.size() / 2);
	}

	int fuelCost = 0;
	for (int i = 0; i < crabs.size(); i++) {
		fuelCost += std::abs(med - crabs.at(i));
	}

	std::cout << "Part 1: " << fuelCost << std::endl;

	int sum = 0;
	for (int i = 0; i < crabs.size(); i++) {
		sum += crabs.at(i);
	}

	// The inputs are weird, for the sample input you need to round the mean, for the actual input I needed to floor it
	// I just do both and check to see which one results in a lower fuel cost and use that fuel cost.
	int meanFloor = (double) sum / crabs.size();
	int meanRound = (double)sum / crabs.size() + 0.5;

	int fuelCostF = 0;
	int fuelCostR = 0;
	for (int i = 0; i < crabs.size(); i++) {
		fuelCostF += rangeSum(std::abs(meanFloor - crabs.at(i)));
		fuelCostR += rangeSum(std::abs(meanRound - crabs.at(i)));
	}
	std::cout << "Part 2: " << min(fuelCostF, fuelCostR) << std::endl;
	return 0;
}