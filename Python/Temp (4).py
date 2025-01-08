class MedicineShop:
    def __init__(self):
        self.meds = ['Crocin', 'Diclofenac', 'Telmikind', 'Azithromxcin', 'Cisplatin', 'Ibuprofen', 'Omprezole', 'ORS', 'Glucose', 'Paracetamol', 'Morphine Sulfate', 'Aspirin', 'Insulin', 'MultiVitamin']
        self.med_prices = [120, 130, 150, 70, 99, 124, 146, 150, 180, 165, 177, 200, 133, 55]
        self.med_choice = []
        self.quantity = []
        self.payment_methods = {'1': 'Cash', '2': 'Net Banking', '3': 'Paytm', '4': 'Credit Card'}
        self.customer_name = ""
        self.customer_phone = ""

    def display_med_list(self):
        for i, (med, price) in enumerate(zip(self.meds, self.med_prices), start=1):
            print(f'{i}: {med} ------ Rs. {price}')

    def take_customer_details(self):
        self.customer_name = input('Enter Your Name: ')
        self.customer_phone = input('Enter Your Phone No: ')

    def add_to_cart(self):
        while True:
            med_input = int(input('Enter Medicine Number: '))
            quantity = int(input('Enter Quantity: '))
            self.med_choice.extend([med_input] * quantity)
            more_meds = input('Do You Want To Add More Medicines? (Y/N): ').lower()
            if more_meds != 'y':
                break

    def display_order(self):
        total_amount = 0
        for med_num in set(self.med_choice):
            quantity = self.med_choice.count(med_num)
            total_amount += self.med_prices[med_num - 1] * quantity
            print(f'{self.meds[med_num - 1]} X {quantity} = Rs. {self.med_prices[med_num - 1] * quantity}')
        print(f'Total Amount: Rs. {total_amount}')

    def confirm_order(self):
        confirm = input('Confirm Order? (Y/N): ').lower()
        if confirm == 'y':
            self.display_payment_options()

    def display_payment_options(self):
        print('\nPayment Methods:')
        for key, value in self.payment_methods.items():
            print(f'{key}: {value}')
        while True:
            payment_choice = input('Select Payment Method (1/2/3/4): ')
            if payment_choice in self.payment_methods:
                print(f'Please proceed with payment using {self.payment_methods[payment_choice]}')
                confirm_payment = input('Confirm Payment? (Y/N): ').lower()
                if confirm_payment == 'y':
                    self.generate_bill()
                    break
                elif confirm_payment == 'n':
                    print('Program Ended')
                    break
            else:
                print('Invalid Input')

    def generate_bill(self):
        print(f'\nMedishop\nPlease Visit Again\nCustomer Name: {self.customer_name}\nCustomer Phone: {self.customer_phone}\nOrder:')
        self.display_order()
        print(f'Total Amount: Rs. {sum([self.med_prices[med - 1] * self.med_choice.count(med) for med in set(self.med_choice)])}\nThank you\nContact No.: 9825439633\nEmail Id: veer3.shah@gmail.com')


if __name__ == "__main__":
    med_shop = MedicineShop()

    while True:
        begin = input('Do You Want To Begin? (Y/N): ').lower()
        if begin == 'y':
            med_shop.take_customer_details()
            med_shop.display_med_list()
            med_shop.add_to_cart()
            med_shop.confirm_order()
        elif begin == 'n':
            break
