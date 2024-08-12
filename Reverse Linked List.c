#include<stdio.h>
#include<stdlib.h>

struct ListNode
{
    int data;
    struct ListNode * next;
};

struct ListNode * linkedListTraversal(struct ListNode* head){
    struct ListNode * prev =  NULL;
    struct ListNode * curr = head;
    struct ListNode * forward = NULL;
    while (curr !=NULL)
    {
        forward = curr->next;
        curr->next = prev;
        prev = curr;
        curr = forward;
    }
    head = prev;
    return head;
    
}
void linkedListTreversal(struct ListNode * ptr){
    while (ptr !=NULL)
    {
        printf("%d",ptr->data);
        ptr = ptr->next;    
    }
    
}

int main(){
    struct ListNode * head = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode * one = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode * two = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode * three = (struct ListNode *)malloc(sizeof(struct ListNode));

    head->data = 1;
    head->next = one;
    one->data = 2;
    one->next = two;
    two->data = 3;
    two->next = three;
    three->data = 4;
    three->next = NULL;
    linkedListTreversal(head);
    head = linkedListTraversal(head);
    linkedListTreversal(head);

    return 0;
}

// int main(){
//     struct Node * head = (struct Node *)malloc(sizeof(struct Node));
//     struct Node * one = (struct Node *)malloc(sizeof(struct Node));
//     struct Node * two = (struct Node *)malloc(sizeof(struct Node));
//     struct Node * three = (struct Node *)malloc(sizeof(struct Node));
//     head->prev = NULL;
//     head->data = 1;
//     head->next = one;

//     one->prev = head;
//     one->data = 2;
//     one->next = two;
//     two->prev = one;
//     two->data = 3;
//     two->next = three;
//     three->prev = two;
//     three->data = 4;
//     three->next = NULL;
    
//     linkedListTraversal(three);
//     // printf("\nOlaa\n");
//     // linkedListTraversal(head);

//     return 0;
// }