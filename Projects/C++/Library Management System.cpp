#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Book {
private:
    string title;
    string author;
    string isbn;

public:
    Book(string t, string a, string i) : title(t), author(a), isbn(i) {}

    void display() const {
        cout << "Title: " << title << ", Author: " << author << ", ISBN: " << isbn << endl;
    }

    string getTitle() const {
        return title;
    }
};

class User {
private:
    string username;
    vector<Book> readingList;
    vector<Book> savedBooks;
    vector<string> history;
    string lockerContents;

public:
    User(string u) : username(u) {}

    string getUsername() const { return username; }

    void addToReadingList(const Book& b) {
        readingList.push_back(b);
    }

    void addToSavedBooks(const Book& b) {
        savedBooks.push_back(b);
    }

    void addToHistory(const string& action) {
        history.push_back(action);
    }

    void displayReadingList() const {
        cout << "Reading List:" << endl;
        for (const auto& book : readingList) {
            book.display();
        }
    }

    void displaySavedBooks() const {
        cout << "Saved Books:" << endl;
        for (const auto& book : savedBooks) {
            book.display();
        }
    }

    void displayHistory() const {
        cout << "History:" << endl;
        for (const auto& action : history) {
            cout << action << endl;
        }
    }

    void removeFromReadingList(const string& title) {
        auto it = find_if(readingList.begin(), readingList.end(), [&](const Book& book) {
            return book.getTitle() == title;
        });
        if (it != readingList.end()) {
            readingList.erase(it);
        }
    }

    bool hasBookInReadingList(const string& title) const {
        return find_if(readingList.begin(), readingList.end(), [&](const Book& book) {
            return book.getTitle() == title;
        }) != readingList.end();
    }

    void removeFromSavedBooks(const string& title) {
        auto it = find_if(savedBooks.begin(), savedBooks.end(), [&](const Book& book) {
            return book.getTitle() == title;
        });
        if (it != savedBooks.end()) {
            savedBooks.erase(it);
        }
    }

    bool hasBookInSavedBooks(const string& title) const {
        return find_if(savedBooks.begin(), savedBooks.end(), [&](const Book& book) {
            return book.getTitle() == title;
        }) != savedBooks.end();
    }

    void setLockerContents(const string& contents) {
        lockerContents = contents;
    }

    string getLockerContents() const {
        return lockerContents;
    }

    bool hasLocker() const {
        return !lockerContents.empty();
    }
};

class Library {
private:
    vector<Book> books;

public:
    void addBook(const Book& b) {
        books.push_back(b);
    }

    void displayBooks() const {
        cout << "Library Contents:" << endl;
        for (const auto& book : books) {
            book.display();
        }
    }

    vector<Book>& getBooks() {
        return books;
    }
};

void displayMenu() {
    cout << "\nMenu:\n";
    cout << "1. Display Library Contents\n";
    cout << "2. Display Reading List\n";
    cout << "3. Display Saved Books\n";
    cout << "4. Display History\n";
    cout << "5. Check Locker\n";
    cout << "6. Exit\n";
    cout << "Enter your choice: ";
}

int main() {
    Library library;

    // Adding some books to the library
    library.addBook(Book("Book 1", "Author 1", "ISBN1"));
    library.addBook(Book("Book 2", "Author 2", "ISBN2"));
    library.addBook(Book("Book 3", "Author 3", "ISBN3"));

    string username;
    cout << "Enter your name: ";
    cin >> username;

    User currentUser(username);

    char choice;
    bool exit = false;
    while (!exit) {
        displayMenu();
        cin >> choice;

        switch (choice) {
            case '1':
                library.displayBooks();
                break;
            case '2':
                currentUser.displayReadingList();
                break;
            case '3':
                currentUser.displaySavedBooks();
                break;
            case '4':
                currentUser.displayHistory();
                break;
            case '5':
                if (currentUser.hasLocker()) {
                    cout << "Locker Contents: " << currentUser.getLockerContents() << endl;
                } else {
                    string contents;
                    cout << "No locker exists for this user. Enter locker contents: ";
                    cin.ignore();
                    getline(cin, contents);
                    currentUser.setLockerContents(contents);
                    cout << "Locker created!" << endl;
                }
                break;
            case '6':
                exit = true;
                break;
            default:
                cout << "Invalid choice!" << endl;
                continue;
        }

        if (choice == '2') {
            string addBookChoice;
            cout << "Do you want to add a book from the library to your reading list? (yes/no): ";
            cin >> addBookChoice;
            if (addBookChoice == "yes") {
                string bookTitle;
                cout << "Enter the title of the book you want to add: ";
                cin.ignore();
                getline(cin, bookTitle);

                auto& libraryBooks = library.getBooks();
                auto it = find_if(libraryBooks.begin(), libraryBooks.end(), [&](const Book& book) {
                    return book.getTitle() == bookTitle;
                });

                if (it != libraryBooks.end()) {
                    currentUser.addToReadingList(*it);
                    libraryBooks.erase(it);
                    cout << "Book added to your reading list successfully." << endl;
                } else {
                    cout << "Book not found in the library." << endl;
                }
            }
        } else if (choice == '3') {
            string saveBookChoice;
            cout << "Do you want to save a book from your reading list? (yes/no): ";
            cin >> saveBookChoice;
            if (saveBookChoice == "yes") {
                string bookTitle;
                cout << "Enter the title of the book you want to save: ";
                cin.ignore();
                getline(cin, bookTitle);

                if (currentUser.hasBookInReadingList(bookTitle)) {
                    currentUser.removeFromReadingList(bookTitle);
                    currentUser.addToSavedBooks(Book(bookTitle, "Author", "ISBN")); // Creating a dummy book entry
                    cout << "Book saved successfully." << endl;
                } else {
                    cout << "Book not found in your reading list." << endl;
                }
            }
        } else if (choice == '4') {
            string removeSavedBookChoice;
            cout << "Do you want to remove any saved books? (yes/no): ";
            cin >> removeSavedBookChoice;
            if (removeSavedBookChoice == "yes") {
                string bookTitle;
                cout << "Enter the title of the book you want to remove: ";
                cin.ignore();
                getline(cin, bookTitle);

                if (currentUser.hasBookInSavedBooks(bookTitle)) {
                    currentUser.removeFromSavedBooks(bookTitle);
                    currentUser.addToHistory("Removed book from saved books: " + bookTitle);
                    cout << "Book removed from saved books and added to history." << endl;
                } else {
                    cout << "Book not found in your saved books." << endl;
                }
            }
        }
    }

    cout << "Goodbye!" << endl;

    return 0;
}
