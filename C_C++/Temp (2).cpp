#include <iostream>
#include <vector>

using namespace std;

struct Node {
    int key;
    int value;

    Node(int key, int value) {
        this->key = key;
        this->value = value;
    }
};

class HashMap {
public:
    HashMap(int size) {
        table = vector<Node>(size, Node(-1, -1));
    }

    void put(int key, int value) {
        int index = hashFunction(key);
        int probe = 0;

        while (table[index].key != -1 && probe < table.size()) {
            if (table[index].key == key) {
                table[index].value = value;
                return;
            }
            index = (index + probe) % table.size();
            probe++;
        }

        table[index] = Node(key, value);
    }

    int get(int key) {
        int index = hashFunction(key);
        int probe = 0;

        while (table[index].key != -1 && probe < table.size()) {
            if (table[index].key == key) {
                return table[index].value;
            }
            index = (index + probe) % table.size();
            probe++;
        }

        return -1; // Key not found
    }

private:
    vector<Node> table;

    int hashFunction(int key) {
        // Simple hash function (replace with a more suitable one)
        return key % table.size();
    }
};

int main() {
    HashMap hashTable(10);

    hashTable.put(1, 10);
    hashTable.put(2, 20);
    hashTable.put(3, 30);
    hashTable.put(4, 40);
    hashTable.put(5, 50);
    hashTable.put(6, 60);
    hashTable.put(7, 70);
    hashTable.put(8, 80);
    hashTable.put(9, 90);
    hashTable.put(10, 100);
    hashTable.put(11, 110); // Collision with key 1

    cout << hashTable.get(5) << endl;
    cout << hashTable.get(11) << endl;

    return 0;
}