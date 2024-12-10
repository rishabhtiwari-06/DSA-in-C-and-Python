#include <stdio.h>
#include <stdbool.h>

char stack[20];
int top = -1;

int isEmpty() {
    return top == -1;
}

void push(char c) {
    top++;
    stack[top] = c;
}

char pop() {
    if (!isEmpty()) {
        char c = stack[top];
        top--;
        return c;
    }
    return '\0';  // Return null character if stack is empty
}

bool isValid(char* s) {
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            push(s[i]);
        } else {
            if (isEmpty()) {
                return false;  
            }
            char c = pop();
            if ((s[i] == ')' && c != '(') ||
                (s[i] == '}' && c != '{') ||
                (s[i] == ']' && c != '[')) {
                return false;  
            }
        }
    }
    return isEmpty();  
}

int main() {
    char s[] = "{[]}";
    if (isValid(s)) {
        printf("True\n");
    } else {
        printf("False\n");
    }

    return 0;
}

// #include<stdio.h>
// #include<stdbool.h>
// #include<string.h>

// char stack[20];
// int top=-1;

// int isEmpty (char* s){
//     int l;
//     l = strlen(&s);
//     if (l==0)
//     {
//         printf("Stack is empty");
//         return 1;
//     }   
// }


// void push (char c)
// {
// 	top++;
// 	stack[top]=c;
// }

// char pop()
// {
// 	char c;
// 	c=stack[top];
// 	top--;
// 	return c;
// }

// bool isValid(char* s) {
//    char c;
//    for (int i = 0; s[i] != '\0'; i++)
//    {
//       if (s[i]=="(" || s[i]=="{" || s[i]=="[")
//       {
//         push(s[i]);
//       }
//       else{
//         if (isEmpty(s))
//         {
//             return false;
//         }
//         else{
//             char c = s[top];
//             pop(s);
//         }
//       }
//       if ((s[i]==")" && c =="(") || (s[i]=="}" && c =="{") || (s[i] =="]" && c=="["))
//       {
//         return true;
//       }
      
//    }
   
// }
// int main()
// {
// 	char s[] = "()[]{}";	
//     if (isValid(s))
//     {
//         printf("True");
//     }
//     else{
//         printf("False");
//     }
    
// 	return 0;
// }


// #include<stdio.h>
// #include<stdbool.h>
// #include<string.h>

// char stack[20];
// int top=-1;
// int isEmpty (char* s){
//     if (/* condition */)
//     {
//         /* code */
//     }
    
// }
// void push (char c)
// {
// 	top++;
// 	stack[top]=c;
// }

// char pop()
// {
// 	char c;
// 	c=stack[top];
// 	top--;
// 	return c;
// }

// bool isValid(char* s) {
   
// }
// int main()
// {
// 	char s[] = "()[]{})";	
//     bool a = isValid(s);
//     printf("%d\n",a);
// 	return 0;
// }

