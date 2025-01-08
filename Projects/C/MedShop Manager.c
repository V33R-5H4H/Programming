#include <stdio.h>
#include <string.h>

#define MAX_MEDS 14
char *Meds[MAX_MEDS] = {"Crocin", "Diclofenac", "Telmikind", "Azithromxcin", "Cisplatin", "Ibuprofen", "Omprezole", "ORS", "Glucose", "Paracetamol", "Morphine Sulfate", "Aspirin", "Insulin", "MultiVitamin"};
int Med_Price[MAX_MEDS] = {120, 130, 150, 70, 99, 124, 146, 150, 180, 165, 177, 200, 133, 55};
int n,total = 0;
int m[MAX_MEDS] = {0};

void medlist() {
    printf("Medicine List:\n");
    for (int i = 0; i < MAX_MEDS; ++i) {
        printf("%d: %s ------ Rs. %d\n", i + 1, Meds[i], Med_Price[i]);
    }
}

void Med_List(int medInput) {
    printf("Enter Quantity : ");
    scanf("%d",&n);
    for (int p=1;p<=n;p++){
        m[medInput - 1]++;
    }
}

void order() {
    printf("Order:\n");
    for (int i = 0; i < MAX_MEDS; ++i) {
        if (m[i] > 0) {
            printf("%s X %d = Rs. %d\n", Meds[i], m[i], m[i] * Med_Price[i]);
        }
    }
}

void reset() {
    for (int i = 0; i < MAX_MEDS; ++i) {
        m[i] = 0;
    }
}

void displayTotal() {
    
    for (int i = 0; i < MAX_MEDS; ++i) {
        total += m[i] * Med_Price[i];
    }
    printf("Total = Rs. %d\n", total);
}

void createReceiptFile(char *userName, char *userPhone) {
    FILE *file;
    char fileName[50];
    sprintf(fileName, "%s_receipt.txt", userName);

    file = fopen(fileName, "w");

    if (file == NULL) {
        printf("Error creating receipt file.\n");
        return;
    }

    fprintf(file, "Receipt:\n");
    fprintf(file, "Customer Name: %s\n", userName);
    fprintf(file, "Customer Phone: %s\n", userPhone);

    for (int i = 0; i < MAX_MEDS; ++i) {
        if (m[i] > 0) {
            fprintf(file, "%s X %d = Rs. %d\n", Meds[i], m[i], m[i] * Med_Price[i]);
        }
    }

    fprintf(file, "Total = Rs. %d\n", total);
    fprintf(file, "\nThank you for shopping with MedShop!\n");

    fclose(file);
}

void main() {
    int medInput;
    char choice;
    char userName[50], userPhone[15];

    printf("Welcome to MedShop!\n");

    printf("Enter your First Name: ");
    scanf("%s", userName);

    printf("Enter your Phone Number: ");
    scanf("%s", userPhone);

    while (1) {
        medlist();

        printf("Enter medicine number: ");
        scanf("%d", &medInput);

        if (medInput < 1 || medInput > MAX_MEDS) {
            printf("Invalid medicine number. Please try again.\n");
            continue;
        }

        Med_List(medInput);
        order();

        printf("Do you want to add more medicines? (Y/N): ");
        scanf(" %c", &choice);

        if (choice != 'Y' && choice != 'y') {
            break;
        }
    }

    displayTotal();
    createReceiptFile(userName, userPhone);
    reset();
}
/*This is a program that simulates a simple medication shop called "MedShop". The user can view the list of available medications, choose a medicine, specify the quantity, and then view their order along with the total cost. After that, the program generates a receipt for the user and resets the order.

Here is a brief overview of the code:

Global variables and arrays are declared at the beginning. MAX_MEDS is a constant representing the maximum number of medications that can be handled. Meds[] and Med_Price[] are arrays containing the names and prices of the medications, respectively. m[] is an array that stores the quantities of each medicine in the order.

medlist() function: This function displays the list of available medications to the user. It iterates through the Meds[] array and prints the name, price, and stock quantity of each medicine.

Med_List(int medInput) function: This function takes a user input (the number of the medicine they want to add to their order) and adds the corresponding quantity of the medicine to the m[] array.

order() function: This function displays the user's current order, showing the name, quantity, and total price of each medicine in the order.

reset() function: This function resets the m[] array, clearing the current order.

displayTotal() function: This function calculates and displays the total cost of the user's order.

createReceiptFile(char *userName, char *userPhone) function: This function creates a text file named <userName>_receipt.txt, which contains the details of the user's order (medicine names, quantities, total prices, and the total cost).

main() function: This is the main function of the program. It prompts the user to enter their name and phone number, and then allows them to choose medications, specify quantities, and view their orders. The user can also choose to add more medications to their order. Once the user is satisfied with their order, the program generates a receipt for them and resets the order.

This program provides a simple simulation of a medication shop. However, it is important to note that it does not include features like handling payment transactions, user authentication, or a proper database to store the list of medications. These features would be necessary for a real-world application.*/