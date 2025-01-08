#include <bits/stdc++.h>
using namespace std;

void print(int *x,int size) {
    for (int i=0;i<=size-1;i++) {
        cout<<x[i] << " ";
    }
    cout<<endl;
}
void insert(int *x,int size){
    for (int i=0;i<=size-1;i++) {
        cout<<"Enter Value of Element "<<i+1<<" : ";
        cin>>x[i];
    }
    cout<<endl;
}
void b_sort(int *x,int size){
    for(int s=0;s<=size;s++)    
        for (int i=0;i<size-1;i++)
            if (x[i]>x[i+1]){
                int temp=x[i];
                x[i]=x[i+1];
                x[i+1]=temp;
                print(x,size);
            }
}
void s_sort(int *x, int size) {
    for(int i=0;i<size-1;i++){
        int lowest = INT_MAX;
        int index = i;
        for(int k=i+1;k<size;k++)
            if(x[k] < lowest) {
                lowest = x[k];
                index = k;
            }
        if(x[i] > lowest) {
            int temp = x[index];
            x[index] = x[i];
            x[i] = temp;
        }
    print(x, size);
    }
}

int main() {
    int size;
    cout<<"Enter Size of List :";
    cin>>size;
    int *x=new int[size];
    insert(x,size);
    print(x,size);
    int choice;
    cout<<"Select Method : "<<endl<<"1.Bubble Sort"<<endl<<"2.Selection Sort"<<endl<<" > ";
    cin>>choice;
    switch(choice){
        case(1):
            b_sort(x,size);
        case(2):
            s_sort(x,size);    
    }    
    delete(x);
}