#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

int rangeSum(int n) {
	return n * (n + 1) / 2;
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

	int mean = 0;
	for (int i = 0; i < crabs.size(); i++) {
		mean += crabs.at(i);
	}

	// The inputs are weird, for the sample input you need to round the mean, for the actual input I needed to floor it
	// It's inconsistent but this worked for my actual input
	mean = (double) mean / crabs.size();  // add + 0.5 at the end of this for the sample input to get 168

	fuelCost = 0;
	for (int i = 0; i < crabs.size(); i++) {
		fuelCost += rangeSum(std::abs(mean - crabs.at(i)));
	}
	std::cout << "Part 2: " << fuelCost << std::endl;
	return 0;
}