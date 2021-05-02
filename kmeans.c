#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <stdlib.h>

#define true 1
#define false 0
#define DEFAULT_MAX_ITER 200
#define DEBUG_INPUT

struct node
{
    double* point;
    struct node *next;
};

struct linked_list
{
    struct node *head;
    struct node *tail;
};

typedef struct node node;
typedef struct linked_list linked_list;

void kmean(int **pointsArray, int k, int max_iter);
int readArgs(int argc, char *argv[], int* k, int* max_iter);
void readPointsArray();
void stringToPoint(char *str);
void addToList(linked_list* list, double* point);

int main(int argc, char *argv[]) {
    assert(2 <= argc && argc <= 3);
    int k, max_iter;
    int res = readArgs(argc, argv, &k, &max_iter);
    if(res == false) {
        return 0;
    }

    readPointsArray();

    return 0;
}

int readArgs(int argc, char *argv[], int* k, int* max_iter) {
    *k = atoi(argv[1]); /////////////////////////////////////////////////////////////////////
    if (*k <= 0) {
        printf("K is not a valid integer, exits...\n");
        return false;
    }

    *max_iter = argc == 3 ? atoi(argv[2]) : DEFAULT_MAX_ITER;
    if (*max_iter <= 0) {
        printf("max_iter is not a valid integer, exits...\n");
        return false;
    }

    #ifdef DEBUG_INPUT
    printf("K: %d \nmax_iter: %d\n", *k, *max_iter);
    #endif

    return true;
}

void readPointsArray() {
    int d = 0;
    double value;
    char c;
    while(scanf("%lf%c", &value, &c) == 2) {
        d++;
        if(c == '\n') {
            break;
        }
    }
    
    int i;

    while(scanf("%lf%c", &value, &c) == 2) {
        
    }

    for (int i =0; i< 9; i++)
    {
        printf("\n");
        scanf("%s", str);
         
        stringToPoint(str);

    }    
}

void stringToPoint(char *str){
    int init_size = strlen(str);
    char delim[] = ",";
    char *ptr = strtok(str, delim);
    double value;
    while(ptr != NULL)
	{ 
        sscanf(ptr, "%lf", &value);
		printf("'%lf'\n", value);
		ptr = strtok(NULL, delim);
	}
}

void kmean(int **pointsArray, int k, int max_iter) {
    int **centroids;
}




void addToList(linked_list* list, double* point) {
    node *n = (node*)malloc(sizeof(node));
    n -> point = point;
    n -> next = NULL;
    list -> tail -> next = n
}