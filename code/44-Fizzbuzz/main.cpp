// author : gamingdy

#include <iostream>


int main(){
	int user_nb{20}; // Put the max number of number range for FizzBuzz
	
	for (int i=1; i<= user_nb; i++){
		std::cout << i << std::endl;
		if (i%3 == 0 && i%5==0){
			std::cout << "Fizzbuzz \n";
		}
		else if (i%5 == 0){
			std::cout<< "Buzz \n";
		}
		else if (i%3 == 0){
			std::cout << "Fizz \n";
		}


	}
	return 0;
}