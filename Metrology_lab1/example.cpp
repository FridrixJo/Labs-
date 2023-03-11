#include <iostream>

struct Book {
	std::string id;
	std::string author;
	std::string name;
	std::string year;
	std::string company;
	std::string pages;
};

std::string Alpha() {
	std::string s;
	std::cin >> s;
	bool status = true;
	std::string example = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
	while (status) {
		if (s.find_first_not_of(example) > s.size()) {
			return s;
		}
		else {
			std::cout << "!!!WRONG INPUT!!!\tTRY AGAIN\n";
			s = Alpha();
		}
	}
}

std::string Digit() {
	std::string s;
	std::cin >> s;
	bool status = true;
	std::string example = "-0123456789";
	while (status) {
		if (s.find_first_not_of(example) > s.size()) {
			return s;
		}
		else {
			std::cout << "!!!WRONG INPUT!!!\tTRY AGAIN\n";
			s = Digit();
		}
	}
}

int CurrentInput() {
	int a;
	while (!(std::cin >> a) || a < 0) {
		std::cin.clear();
		std::cin.ignore(std::numeric_limits < std::streamsize > ::max(), '\n');
		std::cout << "!!!WRONG INPUT!!!\tTRY AGAIN\n";
	}
	return a;
}


void addStruct((Book*)& arr, int& size, Book& item) {
    Book* newArr = new Book[size + 1];
	for (int i = 0; i < size; i++) {
		newArr[i].id = arr[i].id;
		newArr[i].author = arr[i].author;
		newArr[i].name = arr[i].name;
		newArr[i].year = arr[i].year;
		newArr[i].company = arr[i].company;
		newArr[i].pages = arr[i].pages;
	}
	newArr[size].id = item.id;
	newArr[size].author = item.author;
	newArr[size].name = item.name;
	newArr[size].year = item.year;
	newArr[size].company = item.company;
	newArr[size].pages = item.pages;
	size++;
	delete[] arr;
	arr = newArr;
}

void showData(Book* arr, int& size) {
	for (int i = 0; i < size; i++) {
		std::cout << "\n";
		std::cout << "ID: " << arr[i].id << "\t";
		std::cout << "Author: " << arr[i].author << "\t";
		std::cout << "Name: " << arr[i].name << "\t";
		std::cout << "Year: " << arr[i].year << "\t";
		std::cout << "Company: " << arr[i].company << "\t";
		std::cout << "Pages: " << arr[i].pages << "\t";
		std::cout << "\n\n";
	}
}

void showData(Book** arr, int& size, const int& start) {
	for (int i = start; i < size; i++) {
		std::cout << "\n";
		std::cout << "ID: " << arr[i]->id << "\t";
		std::cout << "Author: " << arr[i]->author << "\t";
		std::cout << "Name: " << arr[i]->name << "\t";
		std::cout << "Year: " << arr[i]->year << "\t";
		std::cout << "Company: " << arr[i]->company << "\t";
		std::cout << "Pages: " << arr[i]->pages << "\t";
		std::cout << "\n\n";
	}
}

Book createNewStruct() {
	Book item;
	std::cout << "\n";
	std::cout << "ID\t";
	item.id = Digit();

	std::cout << "Author\t";
    item.author = Alpha();

	std::cout << "Name\t";
	item.name = Alpha();

	std::cout << "Year\t";
	item.year = Digit();

	std::cout << "Company\t";
	item.company = Alpha();

	std::cout << "Pages\t";
	item.pages = Digit();
	std::cout << "\n";

	return item;
}

std::string Str(int b) {
	int a = abs(b);
	std::string s = "";
	int arr[10];
	int n = 0;
	while (a) {
		int b = 0;
		b = a % 10;
		arr[n] = b;
		a /= 10;
		n++;
	}
	std::string s1 = "";
	if (b < 0) {
		s1.push_back('-');
	}
	for (int i = n - 1; i > - 1; i--) {
		char var = static_cast<char>(arr[i] + 48);
		s1.push_back(var);
	}
	return s1;
}

int Num(std::string s) {
	int a = 0;
	int k = 0;
	if (s[0] == '-') {
		for (int i = s.size() - 1; i > 0; i--) {
			int b = static_cast<int>(s[i] - 48) * pow(10, k);
			a += b;
			k++;
		}
	}
	else {
		for (int i = s.size() - 1; i > -1; i--) {
			int b = static_cast<int>(s[i] - 48) * pow(10, k);
			a += b;
			k++;
		}
	}
	return a;
}

void Search(Book** arr, const int& size) {
	std::cout << "Write element of your structure to search\n";
	std::string element;
	std::cin >> element;
	bool status = false;
	for (int i = 0; i < size; i++) {
		if (arr[i]->id == element || arr[i]->author == element || arr[i]->name == element || arr[i]->year == element || arr[i]->company == element || arr[i]->pages == element) {
			std::cout << "\n";
			std::cout << "ID: " << arr[i]->id << "\t";
			std::cout << "Author: " << arr[i]->author << "\t";
			std::cout << "Name: " << arr[i]->name << "\t";
			std::cout << "Year: " << arr[i]->year << "\t";
			std::cout << "Company: " << arr[i]->company << "\t";
			std::cout << "Pages: " << arr[i]->pages << "\t";
			std::cout << "\n\n";
			status = true;
		}
	}
	if (status == false) {
		std::cout << "There is no such element\n";
	}
}

bool isThere(Book* arr, const int& size, std::string break_element) {
	for (int i = 0; i < size; i++) {
		if (arr[i].id == break_element || arr[i].author == break_element || arr[i].name == break_element || arr[i].year == break_element || arr[i].company == break_element || arr[i].pages == break_element) {
			return true;
		}
	}
	return false;
}

void removeItem(Book** arr, const int& size) {
	std::cout << "Write element of your structure you want to delete or change\n";
	std::string element;
	std::cin >> element;
	std::cout << "1. delete / 2. change\n";
	int choice = CurrentInput();
	std::string newStr = "";
	bool status = false;
	for (int i = 0; i < size; i++) {
		bool isChanged = false;
		if (arr[i]->id == element) {
			if (choice == 2) {
				std::cout << "Your new ID element\n";
				newStr = Digit();
				arr[i]->id = newStr;
				isChanged = true;
			}
			else {
				arr[i]->id = "-1";
				isChanged = true;
			}
		}
		if (arr[i]->author == element) {
			if (choice == 2) {
				std::cout << "Your new Author element\n";
				newStr = Alpha();
				arr[i]->author = newStr;
				isChanged = true;
			}
			else {
				arr[i]->author = "---";
				isChanged = true;
			}
		}
		if (arr[i]->name == element) {
			if (choice == 2) {
				std::cout << "Your new Name element\n";
				newStr = Alpha();
				arr[i]->name = newStr;
				isChanged = true;
			}
			else {
				arr[i]->name = "---";
				isChanged = true;
			}
		}
		if (arr[i]->year == element) {
			if (choice == 2) {
				std::cout << "Your new Year element\n";
				newStr = Digit();
				arr[i]->year = newStr;
				isChanged = true;
			}
			else {
				arr[i]->year = "-1";
				isChanged = true;
			}
		}
		if (arr[i]->company == element) {
			if (choice == 2) {
				std::cout << "Your new Company element\n";
				newStr = Alpha();
				arr[i]->company = newStr;
				isChanged = true;
			}
			else {
				arr[i]->company = "---";
				isChanged = true;
			}
		}
		if (arr[i]->pages == element) {
			if (choice == 2) {
				std::cout << "Your new Pages element\n";
				newStr = Digit();
				arr[i]->pages = newStr;
				isChanged = true;
			}
			else {
				arr[i]->pages = "-1";
				isChanged = true;
			}
		}
		if (isChanged) {
			status = true;
		}
	}
	if (status == false) {
		std::cout << "There is no such element\n";
	}
}

void shell_sort_up(Book** arr, const int& size, int& counter) {
	std::cout << "Write year for sorting\n";
	int year = CurrentInput();
	int i, j, temp;
	for (int step = size / 2; step > 0; step /= 2) {
		for (i = step; i < size; i++) {
			Book* temp = arr[i];
			int tmp = Num(arr[i]->year);
			for (j = i; j >= step; j -= step) {
				if (tmp >= Num(arr[j - step]->year)) {
					break;
				}
				arr[j] = arr[j - step];
			}
			arr[j] = temp;
		}
	}
	for (int i = 0; i < size; i++) {
		if (Num(arr[i]->year) <= year)
			counter++;
	}
}


int main()
{
	std::cout << "Enter size\t";
	int size = CurrentInput();
	std::cout << "Enter break element\t";
	std::string break_element;
	std::cin >> break_element;
	Book* arr = new Book[size]{};

	for (int i = 0; i < size; i++) {
		std::cout << "\n";
		std::cout << "ID\t";
		arr[i].id = Digit();

		std::cout << "Author\t";
		arr[i].author = Alpha();

		std::cout << "Name\t";
		arr[i].name = Alpha();

		std::cout << "Year\t";
		arr[i].year = Digit();

		std::cout << "Company\t";
		arr[i].company = Alpha();

		std::cout << "Pages\t";
		arr[i].pages = Digit();
		std::cout << "\n";

		if (isThere(arr, size, break_element)) {
			size = i + 1;
			break;
		}
	}

	std::cout << "Do you want to add one more struct?\n1 (yes) / 2 (no)\n";
	int k = CurrentInput();
	Book item;
	switch (k) {
	case 1:
		item = createNewStruct();
		addStruct(arr, size, item);
		showData(arr, size);
		std::cout << "One more?\n 1 (yes) / 2 (no)\n";
		int q;
		std::cin >> q;
		if (q == 1) {
			int n = 1;
			for (int i = 0; i < n; i++) {
				Book item;
				item = createNewStruct();
				addStruct(arr, size, item);
				showData(arr, size);
				std::cout << "One more?\n 1 (yes) / 2 (no)\n";
				int condition = CurrentInput();
				if (condition == 1) {
					n++;
				}
				else {
					break;
				}
			}
		}
		break;
	case 2:
		showData(arr, size);
		break;
	default:
		showData(arr, size);
		break;
	}

	Book** array = new Book * [size];
	for (int i = 0; i < size; i++) {
		array[i] = &arr[i];
	}

	Search(array, size);
	removeItem(array, size);
	showData(array, size, 0);
	std::cout << "Do you want to change or delete more elements\n";
	std::cout << "1. yes / 2. no\n";
	int answer = CurrentInput();
	if (answer == 1) {
		int t = 1;
		removeItem(array, size);
		showData(array, size, 0);
		for (int i = 0; i < t; i++) {
			std::cout << "more?\n";
			std::cout << "1. yes / 2. no\n";
			int l = CurrentInput();
			if (l == 1) {
				removeItem(array, size);
				showData(array, size, 0);
				t++;
			}
			else {
				break;
			}
		}

	}

	int counter = 0;
	shell_sort_up(array, size, counter);
	showData(array, size, counter);
	delete[] arr;
	delete[] array;
	return 0;
}