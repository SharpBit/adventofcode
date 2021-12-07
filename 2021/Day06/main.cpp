#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>

unsigned long long int simFish(std::vector<int> &timers, int days) {
	std::unordered_map<int, unsigned long long int> offspringDays;
	for (int i = 0; i < timers.size(); i++) {
		offspringDays[timers.at(i)]++;
	}

	unsigned long long int numFish = timers.size();
	for (int i = 0; i < days; i++) {
		if (offspringDays.find(i) != offspringDays.end()) {
			offspringDays[i + 7] += offspringDays[i];
			offspringDays[i + 9] += offspringDays[i];
			numFish += offspringDays[i];
			offspringDays.erase(i);
		}
	}
	return numFish;
}

int main()  {
	const int days1 = 80;
	const int days2 = 256;

	std::string agestr;
	std::vector<int> timers;
	std::ifstream input("input.txt");
	while (std::getline(input, agestr, ',')) {
		timers.push_back(std::stoi(agestr));
	}

	std::cout << "Part 1: " << simFish(timers, 80) << std::endl;
	std::cout << "Part 2: " << simFish(timers, 256) << std::endl;
	return 0;
}
