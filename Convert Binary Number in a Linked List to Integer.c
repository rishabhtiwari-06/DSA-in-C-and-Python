#include<stdio.h>
#include<stdlib.h>

struct Node
{
    int data;
    struct Node * next;
};

int getDecimalValue(struct Node* head){
    struct Node * temp = head;
    int a = 0;
    int n = 0;

    while (temp !=NULL)
    {
        n++;
        temp = temp->next;
    }
    while (head !=NULL)
    {
        a = (head->data) * pow(2,n-1) + a;
        n--;
        head = head->next;
    }
    printf("%d",a);
    return a;
}

// void linkedListTraversal(struct Node* ptr){
//     while (ptr !=NULL)
//     {
//         printf("%d\n", ptr->data);
//         ptr = ptr->next;
//     }
    
// }

int main(){
    struct Node * head = (struct Node *)malloc(sizeof(struct Node));
    struct Node * one = (struct Node *)malloc(sizeof(struct Node));
    struct Node * two = (struct Node *)malloc(sizeof(struct Node));
    struct Node * three = (struct Node *)malloc(sizeof(struct Node));

    head->data = 1;
    head->next = one;
    one->data = 0;
    one->next = two;
    two->data = 1;
    two->next = three;
    three->data = 0;
    three->next = NULL;

    getDecimalValue(head);

    return 0;
}