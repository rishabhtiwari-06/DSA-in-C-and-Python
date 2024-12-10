#include<stdio.h>
#include<stdlib.h>

struct Node
{
    int data;
    struct Node * next;
};

struct Node* removeNthFromEnd(struct Node* head, int n) {
    struct Node* ptr = head->next; // start ptr at head
    int l = 0; // should start with 0 because it's a length counter
    int i = 0;
    struct Node* q = head; // pointer to move with ptr

    
    struct Node* temp = head; 
    while (temp != NULL) {
        l++;               
        temp = temp->next;  
    }

    
    if (n == l) {
        struct Node* toDelete = head;
        head = head->next;
        free(toDelete);
        return head;
    }
    // if(n==1){
    //     head = NULL;
    //     return head;
    // }

    
    while (i < (l - n - 1)) { 
        ptr = ptr->next;
        q = q->next;
        i++;
    }

    
    q->next = ptr->next;
    free(ptr); 
    return head;
}



void linkedListTraversal(struct Node* ptr){
    while (ptr !=NULL)
    {
        printf(" Haha The Data is %d\n", ptr->data);
        ptr = ptr->next;
    }
    
}

int main(){
    struct Node * head = (struct Node *)malloc(sizeof(struct Node));
    // struct Node * one = (struct Node *)malloc(sizeof(struct Node));
    // struct Node * two = (struct Node *)malloc(sizeof(struct Node));
    // struct Node * three = (struct Node *)malloc(sizeof(struct Node));
    // struct Node * four = (struct Node *)malloc(sizeof(struct Node));

    head->data = 1;
    head->next = NULL;
    // one->data = 2;
    // one->next = two;
    // two->data = 3;
    // two->next = three;
    // three->data = 4;
    // three->next = four;
    // four ->data = 5;
    // four ->next = NULL;
    head = removeNthFromEnd(head , 1);
    linkedListTraversal(head);

    return 0;
}
// struct Node* removeNthFromStart(struct Node* head, int n) {
//     struct Node * ptr = head;
//     struct Node * temp = head;
//     int l =0;
//     int i =0;
//     struct Node * q = head;
//     while (temp!=NULL)
//     {
//         l++;
//         temp = temp->next;
//     }
     
//     while (i <(l-n-1))
//     {
//         ptr = ptr->next;
//         q = q->next;
//         i++;
//     }
//     q->next = ptr->next;
//     free(ptr); 
//     return head;
// }
// struct Node* removeNthFromStart(struct Node* head, int n) {
//     struct Node * ptr = head->next;
//     struct Node * q = head;
    
//     while (q->next->data != n)
//     {
//         ptr = ptr->next;
//         q = q->next;
//     }
//     q->next = ptr->next;
//     free(ptr); 
//     return head;
// }