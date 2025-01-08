#Function To Display Med list
def medlist():
    for x in range(len(Meds)): 
        print(x+1,':',Meds[x],'------Rs.:',Med_Price[x])
        x+=1

#Function To Make Med list
def Med_List():
    Med_Choice.append(Meds[Med_Input])
    Quantity=int(input('Enter Quantity:'))
    for a in range(Quantity):
        y.append(Med_input)

#Function To Make Final Order
def order():
        for z in range(len(y)):
            m.append(y[z]-1)
            Crocin=m.count(0)
            ml.append(Crocin)
            Diclofenac=m.count(1)
            ml.append(Diclofenac)
            Telmikind=m.count(2)
            ml.append(Telmikind)
            Azithromxcin=m.count(3)
            ml.append(Azithromxcin)
            Cisplatin=m.count(4)
            ml.append(Cisplatin)
            Ibuprofen=m.count(5)
            ml.append(Ibuprofen)
            Omprezole=m.count(6)
            ml.append(Omprezole)
            Ors=m.count(7)
            ml.append(Ors)
            Glucose=m.count(8)
            ml.append(Glucose)
            Paracetamol=m.count(9)
            ml.append(Paracetamol)
            Morphine_Sulfate=m.count(10)
            ml.append(Morphine_Sulfate)
            Aspirin=m.count(11)
            ml.append(Aspirin)
            Insulin=m.count(12)
            ml.append(Insulin)
            MultiVitamin=m.count(13)
            ml.append(MultiVitamin)
        if Crocin>0:
            print(Meds[0],'X',(Crocin),'=',Med_Price[0]*(Crocin))
        if Diclofenac>0:
            print(Meds[1],'X',(Diclofenac),'=',Med_Price[1]*(Diclofenac))
        if Telmikind>0:
            print(Meds[2],'X',(Telmikind),'=',Med_Price[2]*(Telmikind))
        if Azithromxcin>0:
            print(Meds[3],'X',(Azithromxcin),'=',Med_Price[3]*(Azithromxcin))
        if Cisplatin>0:
            print(Meds[4],'X',(Cisplatin),'=',Med_Price[4]*(Cisplatin))
        if Ibuprofen>0:
            print(Meds[5],'X',(Ibuprofen),'=',Med_Price[5]*(Ibuprofen))
        if Omprezole>0:
            print(Meds[6],'X',(Omprezole),'=',Med_Price[6]*(Omprezole))
        if Ors>0:
            print(Meds[7],'X',(Ors),'=',Med_Price[7]*(Ors))
        if Glucose>0:
            print(Meds[8],'X',(Glucose),'=',Med_Price[8]*(Glucose))
        if Paracetamol>0:
            print(Meds[9],'X',(Paracetamol),'=',Med_Price[9]*(Paracetamol))
        if Morphine_Sulfate>0:
            print(Meds[10],'X',(Morphine_Sulfate),'=',Med_Price[10]*(Morphine_Sulfate))
        if Aspirin>0:
            print(Meds[11],'X',(Aspirin),'=',Med_Price[11]*(Aspirin))
        if Insulin>0:
            print(Meds[12],'X',(Insulin),'=',Med_Price[12]*(Insulin))
        if MultiVitamin>0:
            print(Meds[13],'X',(MultiVitamin),'=',Med_Price[13]*(MultiVitamin))

#Function To Reset Med Count
def reset():
    if m.count(0)>0:
        while m.count(0)>0:
            m.remove(0)
    if m.count(1)>0:
        while m.count(1)>0:
            m.remove(1)
    if m.count(2)>0:
        while m.count(2)>0:
            m.remove(2)
    if m.count(3)>0:
        while m.count(3)>0:
            m.remove(3)
    if m.count(4)>0:
        while m.count(4)>0:
            m.remove(4)
    if m.count(5)>0:
        while m.count(5)>0:
            m.remove(5)
    if m.count(6)>0:
        while m.count(6)>0:
            m.remove(6)
    if m.count(7)>0:
        while m.count(7)>0:
            m.remove(7)
    if m.count(8)>0:
        while m.count(8)>0:
            m.remove(8)
    if m.count(9)>0:
        while m.count(9)>0:
            m.remove(9)
    if m.count(10)>0:
        while m.count(10)>0:
            m.remove(10)
    if m.count(11)>0:
        while m.count(11)>0:
            m.remove(11)
    if m.count(12)>0:
        while m.count(12)>0:
            m.remove(12)
    if m.count(13)>0:
        while m.count(13)>0:
            m.remove(13)

#Function Confirm Order And Payment Method
def Confirm():
        confirmation=input('confirm Order?(Y/N)')
        confirmation=confirmation.lower() 
        if confirmation=='y':
            print('''    
            1: Cash 
            2: Net Banking
            3: Paytm
            4: Credit Card''')
            while True:
                Mode_Pay=input('Pls Select Method of Payment(1/2/3/4)')
                if Mode_Pay in ('1','2','3','4'):
                    if Mode_Pay=='1':
                        print('Pls Provide The Cashier With Rs:',c)
                    if Mode_Pay=='2':
                        print('Pls Send Rs:',c,'On UPI Id v33r_h4h@paytm')
                    if Mode_Pay=='3':
                        print('Pls Send Rs:',c,'On 9825439633 via Paytm')
                    if Mode_Pay=='4':
                        print('Pls Insert Your Credit/Debit Card In The Card Reader')
                        print('Ammount To Be Paid is Rs:',c)
                    input_2=input('Confirm Payment?(Y/N):')
                    input_2=input_2.lower()
                    if input_2 =='y':
                        break
                    if input_2 =='n':
                        print('Program Ended')
                        continue   
                else:
                    print('Invalid Input')
        else:
            breakpoint

#Function To Create The Bill
def Bill():
    Bill=input('Do You Want A Reciept?(Y/N)')
    Bill=Bill.lower() 
    if Bill=='y':
        print('''               
                Medishop
            Please Visit Again           
        Customer Name:''',u_name,'''
        Customer Phone:''',u_phone,'''
        Order:
                ''')
        order()
        print('''           
            Total Amount:''',c,'''
                Thank you
        Contact No.:9825439633
        Email Id:veer3.shah@gmail.com
                ''')
    else: 
        print('Thank you For Shopping With MedShop')
        print('Have A Nice Day')

#Function To Create Txt File Of Bill
def file():
    fname=u_name
    file=fname+'_Data'+'.txt'
    fileout=open(file,'w+')
    list1.append('Customer Name:'+str(u_name)+'\n')
    list1.append('Customer Phone:'+str(u_phone)+'\n')
    list1.append('Total Amount:'+'Rs'+str(c)+'\n')
    if Mode_pay=='1':
        list1.append('Mode Of Payment'+' : '+'Cash')
    if Mode_pay=='2':
        list1.append('Mode Of Payment'+' : '+'Net Banking')
    if Mode_pay=='3':
        list1.append('Mode Of Payment'+' : '+'Paytm')
    if Mode_pay=='4':
        list1.append('Mode Of Payment'+' : '+'Credit Card')
    list1.append('\n')
    if m.count(0)>0:
        list1.append('Crocin x '+str(m.count(0))+' = '+str(m.count(0)*Med_Price[0])+'\n')
    if m.count(1)>0:
        list1.append('Diclofenac x '+str(m.count(1))+' = '+str(m.count(1)*Med_Price[1])+'\n')
    if m.count(2)>0:
        list1.append('Telmikind x '+str(m.count(2))+' = '+str(m.count(2)*Med_Price[2])+'\n')
    if m.count(3)>0:
        list1.append('Azithromixcin x '+str(m.count(3))+' = '+str(m.count(3)*Med_Price[3])+'\n')
    if m.count(4)>0:
        list1.append('Cisplatin x '+str(m.count(4))+' = '+str(m.count(4)*Med_Price[4])+'\n')
    if m.count(5)>0:
        list1.append('Ibuprofen x '+str(m.count(5))+' = '+str(m.count(5)*Med_Price[5])+'\n')
    if m.count(6)>0:
        list1.append('Omprezole x '+str(m.count(6))+' = '+str(m.count(6)*Med_Price[6])+'\n')
    if m.count(7)>0:
        list1.append('Ors x '+str(m.count(7))+' = '+str(m.count(7)*Med_Price[7])+'\n')
    if m.count(8)>0:
        list1.append('Glucose x '+str(m.count(8))+' = '+str(m.count(8)*Med_Price[8])+'\n')
    if m.count(9)>0:
        list1.append('Paracetamol x '+str(m.count(9))+' = '+str(m.count(9)*Med_Price[9])+'\n')
    if m.count(10)>0:
        list1.append('Morphine Sulphate x '+str(m.count(10))+' = '+str(m.count(10)*Med_Price[10])+'\n')
    if m.count(11)>0:
        list1.append('Aspirin x '+str(m.count(11))+' = '+str(m.count(11)*Med_Price[11])+'\n')
    if m.count(12)>0:
        list1.append('Insulin x '+str(m.count(12))+' = '+str(m.count(12)*Med_Price[12])+'\n')
    if m.count(13)>0:
        list1.append('Multivitamin x '+str(m.count(13))+' = '+str(m.count(13)*Med_Price[13])+'\n')
    list1.append('\n')
    list1.append('Total'+' = '+' Rs'+str(c)+'\n')
    fileout.writelines(list1)
    fileout.close()

#Fuction To Create Txt File of Customer Bill
def cfile():
    fname=u_name
    file=fname+'.txt'
    fileout=open(file,'w+')
    list2.append('''Customer Name:'''+str(u_name)+'\n')
    list2.append('''Customer Phone:'''+str(u_phone)+'\n')
    if Mode_pay=='1':
        list2.append('Mode Of Payment'+' : '+'Cash')
    if Mode_pay=='2':
        list2.append('Mode Of Payment'+' : '+'Net Banking')
    if Mode_pay=='3':
        list2.append('Mode Of Payment'+' : '+'Paytm')
    if Mode_pay=='4':
        list2.append('Mode Of Payment'+' : '+'Credit Card')
    list2.append('\n')
    if m.count(0)>0:
        list2.append('Crocin x '+str(m.count(0))+' = '+str(m.count(0)*Med_Price[0])+'\n')
    if m.count(1)>0:
        list2.append('Diclofenac x '+str(m.count(1))+' = '+str(m.count(1)*Med_Price[1])+'\n')
    if m.count(2)>0:
        list2.append('Telmikind x '+str(m.count(2))+' = '+str(m.count(2)*Med_Price[2])+'\n')
    if m.count(3)>0:
        list2.append('Azithromixcin x '+str(m.count(3))+' = '+str(m.count(3)*Med_Price[3])+'\n')
    if m.count(4)>0:
        list2.append('Cisplatin x '+str(m.count(4))+' = '+str(m.count(4)*Med_Price[4])+'\n')
    if m.count(5)>0:
        list2.append('Ibuprofen x '+str(m.count(5))+' = '+str(m.count(5)*Med_Price[5])+'\n')
    if m.count(6)>0:
        list2.append('Omprezole x '+str(m.count(6))+' = '+str(m.count(6)*Med_Price[6])+'\n')
    if m.count(7)>0:
        list2.append('Ors x '+str(m.count(7))+' = '+str(m.count(7)*Med_Price[7])+'\n')
    if m.count(8)>0:
        list2.append('Glucose x '+str(m.count(8))+' = '+str(m.count(8)*Med_Price[8])+'\n')
    if m.count(9)>0:
        list2.append('Paracetamol x '+str(m.count(9))+' = '+str(m.count(9)*Med_Price[9])+'\n')
    if m.count(10)>0:
        list2.append('Morphine Sulphate x '+str(m.count(10))+' = '+str(m.count(10)*Med_Price[10])+'\n')
    if m.count(11)>0:
        list2.append('Aspirin x '+str(m.count(11))+' = '+str(m.count(11)*Med_Price[11])+'\n')
    if m.count(12)>0:
        list2.append('Insulin x '+str(m.count(12))+' = '+str(m.count(12)*Med_Price[12])+'\n')
    if m.count(13)>0:
        list2.append('Multivitamin x '+str(m.count(13))+' = '+str(m.count(13)*Med_Price[13])+'\n')
    list2.append('\n')
    list2.append('''Total Amount:'''+' Rs '+str(c)+'\n')
    list2.append('''
                Thank you
        Contact No.:9825439633
        Email Id:veer3.shah@gmail.com
                ''')
    fileout.writelines(list2)
    fileout.close()

#Start
while True: 
    Begin=input('Do You Want To Begin?(Y/N)')
    Begin=Begin.lower()
    if Begin=='y':

#Lists         
        Meds=['Crocin','Diclofenac','Telmikind','Azithromxcin','Cisplatin','Ibuprofen','Omprezole','ORS','Glucose','Paracetamol','Morphine Sulfate','Aspirin','Insulin','MultiVitamin'] 
        Med_Price=[120,130,150,70,99,124,146,150,180,165,177,200,133,55]
        Crocin=Diclofenac=Telmikind=Azithromxcin=Cisplatin=Ibuprofen=Omprezole=Ors=Glucose=Paracetamol=Morphine_Sulfate=Aspirin=Insulin=MultiVitamin=0        
        Mode_pay=0
        Med_Choice=[]
        list1=[]
        list2=[]
        y=[]
        b=[]
        m=[]
        p=[]
        ml=[]
        lm=[]

#Welcome Title
        print('Welcome To MedShop') 

#Code To Collect Customer Name
        while True: 
            u_fname=str(input('Enter Your First Name:'))
            u_sname=str(input('Enter Your Last Name:'))
            u_name=u_fname+'_'+u_sname
            if u_fname.isalpha()==False and u_sname.isalpha()==False:   
                print('Enter Valid Name')
                continue
            elif u_fname.isalpha()==True and u_sname.isalpha()==False:
                print('Enter Valid Name')
                continue
            elif u_fname.isalpha()==False and u_sname.isalpha()==True:
                print('Enter Valid Name')
                continue
            else:
                break

#Code To Collect Phone Number
        while True: 
            u_phone=(input('Enter Your Phone No:'))
            u_phonestring=str(u_phone)
            if len(u_phonestring)>10 and u_phonestring.isdigit()==False:    
                print('Enter Valid Number')
                continue
            if len(u_phonestring)>10:
                print('Enter Valid Number')
                continue
            if len(u_phonestring)<10:
                print('Enter Valid Number')
                continue
            if len(u_phonestring)<10 and u_phonestring.isdigit()==False:
                print('Enter Valid Number')
                continue
            if u_phonestring.isdigit()==False:
                print('Enter Valid Number')
                continue
            if len(u_phonestring)==10 and u_phonestring.isdigit()==True:
                break

#Code To Display  Med List        
        medlist()     

#Code To Make Medicine List        
        while True:  
            Med_input=int(input("Enter Medicine Number:"))
            Med_Input=0
            Med_Input=Med_input-1
            if Med_input in range(len(Meds)+1):
                if Med_input == 1: 
                    Med_List()
                if Med_input == 2: 
                    Med_List()
                if Med_input == 3: 
                    Med_List()
                if Med_input == 4: 
                    Med_List()
                if Med_input == 5: 
                    Med_List()
                if Med_input == 6: 
                    Med_List()      
                if Med_input == 7: 
                    Med_List()
                if Med_input == 8: 
                    Med_List()
                if Med_input == 9: 
                    Med_List()
                if Med_input == 10: 
                    Med_List()
                if Med_input == 11: 
                    Med_List()
                if Med_input == 12: 
                    Med_List()
                if Med_input == 13: 
                    Med_List()
                if Med_input == 14: 
                    Med_List()   
                choice=input('Do You Want To Add More Medicines(Y/N):')
                choice=choice.lower()
                if choice =='y':
                    print('Selected Medicines:',Med_Choice)
                    continue
                elif choice=='n':
                    print('Selected Medicines:',Med_Choice)
                    break
                else:
                    break
            else:
                print('Enter valid Medicine Number')

#Code To Display Meds With Price
        order()
        lm=list(ml)
        reset()

#Code To Display Total Ammount        
        for a in range(len(y)): 
            if a>=0:
                b.append((Med_Price[y[a]-1]))
                c=sum(b)
        print('Total=',c)

#Code To Confirm Order and Payment Method        
        Confirm()

#Code To Print Reciept
        Bill()

#Code To Create Txt file for Bill
        file()
        cfile()
    elif Begin =='n':
        break
#End