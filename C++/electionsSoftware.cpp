#include <iostream>
using namespace std;

int main(){

	//Variables//
	int age = 0;
	char name[80] = "";
	
	//Getting the data//
	cout << "Please enter your name: ";
	cin >> name;
	cout << "Please enter your age: ";
	cin >> age;

	//Execution//
	if(age >= 18 && age <= 60){
		cout << "You are abel to vote, " << name << endl;
	}
	else{
		cout << "Sorry " << name << ", you are not abel to vote" << endl;
	}

	return 0;
}

