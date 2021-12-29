// author : gamingdy

#include <iostream>

int main(){
	std::string user_string {"This is an string exemple"}; // Put your string here

	char user_char {'a'}; // Put the char you want to count the occurence in the given string


	int occurence_char {};
	for (char element : user_string){
		if (element == user_char){
			occurence_char ++;
		}
	}

	std::cout << "There are " << occurence_char << " "<<user_char << " in given string: " << user_string;

	return 0;
}