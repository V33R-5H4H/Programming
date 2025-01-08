/* Write a program to construct binary search tree.Write a program to traverse binary search tree.*/
#include<iostream>
using namespace std;

struct node
{
    struct node *left;
    int data;
    struct node *right;
};

class bst
{
    node *newnode, *temp, *prev, *head = nullptr;
public:
    void insert(int n)
    {
        node *prev = nullptr;
        newnode = new node;
        newnode->data = n;
        newnode->left = nullptr;
        newnode->right = nullptr;
        if(head == nullptr)
        {
            head = newnode;
            return;
        }
        temp = head;
        while(temp != nullptr)
        {
            prev = temp;
            if(n == temp->data)
                return;
            else if(n < temp->data)
                temp = temp->left;
            else if(n > temp->data)
                temp = temp->right;
        }
        if(n<prev->data)
            prev->left = newnode;
        else if(n>prev->data)
            prev->right = newnode;
        return;
    }
    void inorder(node *h)
    {
        if(h != nullptr)
        {
            inorder(h->left);
            cout<<h->data<<", ";
            inorder(h->right);
        }
        return;
    }
    void preorder(node *h)
    {
        if(h != nullptr)
        {
            cout<<h->data<<", ";
            preorder(h->left);
            preorder(h->right);
        }
        return;
    }
    void postorder(node *h)
    {
        if(h != nullptr)
        {
            postorder(h->left);
            postorder(h->right);
            cout<<h->data<<", ";
        }
        return;
    }
    void display()
    {
        cout<<endl<<"Inorder traversal of BST is : ";
        inorder(head);
        cout<<endl<<"Preorder traversal of BST is : ";
        preorder(head);
        cout<<endl<<"Postorder traversal of BST is : ";
        postorder(head);
    }

    // to delete desired node from binary tree
    void remove(int n)
    {
        temp = head;
        while(temp->data != n || temp == nullptr)                // find node with data n
        {
            prev = temp;
            if(temp->data < n)
                temp = temp->right;
            else if(temp->data > n)
                temp = temp->left;
        }
        if(temp==nullptr)
            return;                  // n does'nt exist

        if(temp->left == nullptr && temp->right == nullptr)          // n has no roots
        {
            if(prev->left == temp)
                prev->left = nullptr;
            else
                prev->right = nullptr;
        }
        else if(temp->left != nullptr && temp->right != nullptr)    // n has 2 roots
        {
            if(prev->left == temp)
            {
                prev->left = findnext(temp->right);
                prev->left->left = temp->left;
                prev->left->right = temp->right;
                remove(findnext(temp->right)->data);
            }
        }
        else
        {
            if(temp->left != nullptr)
            {
                if(prev->left == temp)
                    prev->left = temp->left;
                else
                    prev->right = temp->left;
            }
            else
            {
                if(prev->left == temp)
                    prev->left = temp->right;
                else
                    prev->right = temp->right;
            }
        }
    }
    node* findnext(node *n)
    {
        // inorder predecessor will be the minimum element of the right sub tree
        while(n->left != nullptr)
            n = n->left;
        return n;
    }
};

int main()
{
    bst o1;
    int n;
    cout<<"Enter number of nodes : ";
    cin>>n;
    int num[n];
    cout<<"Enter data of nodes : ";
    for(int i=0; i<n; i++)
        cin>>num[i];

    for(int i=0; i<n; i++)
        o1.insert(num[i]);

    int ch=0;
    while(ch!=3)
    {
        cout<<endl<<"Enter 1 to remove element, 2 to display, 3 to end : ";
        cin>>ch;
        switch(ch)
        {
        case 1:
            int x;
            cout<<"Enter node to be deleted : ";
            cin>>x;
            o1.remove(x);
            break;
        case 2:
            o1.display();
            break;
        }
    }
    return 0;
}
