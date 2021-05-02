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

struct node_double
{
    double value;
    struct node_double *next;
};

struct linked_list_double
{
    struct node_double *head;
    struct node_double *tail;
};

typedef struct node node;
typedef struct linked_list linked_list;
typedef struct node_double node_double;
typedef struct linked_list_double linked_list_double;

void kmean(int **pointsArray, int k, int max_iter);
int readArgs(int argc, char *argv[], int* k, int* max_iter);
void readPointsArray();
void stringToPoint(char *str);
void addToList(linked_list* list, double* point);
void addToListDouble(linked_list_double* list, double value);
double* convertDoubleListToArray(linked_list_double* list, int d);
void freeList(linked_list* list);
void freeListDouble(linked_list_double* list);
void freeNode(node* n);
void freeNodeDouble(node_double* n);

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
    int d = 0, i = 0;
    double value;
    char c;
    linked_list_double *pointA = (linked_list_double*)malloc(sizeof(linked_list));
    while(scanf("%lf%c", &value, &c) == 2) {
        d++;
        addToListDouble(pointA, value);
        if(c == '\n') {
            break;
        }
    }
    double *point = (double*)calloc(d, sizeof(double));
    linked_list *pointsList = (linked_list*)malloc(sizeof(linked_list));
    addToList(pointsList, convertDoubleListToArray(pointA, d));
    freeListDouble(pointA);

    while (scanf("%lf%c", &value, &c) > 0) {
        point[i] = value;
        i++;
        if(i == d) {
            i = 0;
            addToList(pointsList, point);
            point = (double*)calloc(d, sizeof(double));
        }
    } 

    #ifdef DEBUG_INPUT
    int index = 0;
    for (node *n = pointsList -> head; n != NULL; n = n -> next) {
        printf("Point %d: ", index);
        for (int j = 0; j < d; j++) {
            printf("%lf, ", (n -> point)[j]);
        }
        printf("\n");
        index++;
    }
    #endif
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
    if(list -> head == NULL) {
        list -> head = n;
        list -> tail = n;
    } else {
        list -> tail -> next = n;
        list -> tail = n;
    }
}

void addToListDouble(linked_list_double* list, double value) {
    node_double *n = (node_double*)malloc(sizeof(node_double));
    n -> value = value;
    n -> next = NULL;
    if(list -> head == NULL) {
        list -> head = n;
        list -> tail = n;
    } else {
        list -> tail -> next = n;
        list -> tail = n;
    }
}

double* convertDoubleListToArray(linked_list_double* list, int d) {
    double *point = (double*)calloc(d, sizeof(double));
    node_double *n = list -> head;
    for(int i = 0; n != NULL; n = n -> next, i++) {
        point[i] = n -> value;
    }
    return point;
}

void freeList(linked_list* list) { 
    freeNode(list -> head);
    free(list);
}

void freeNode(node* n) {
    if (n != NULL) {
        freeNode(n -> next);
        free(n);
    }
}

void freeListDouble(linked_list_double* list) {
    freeNodeDouble(list -> head);
    free(list);
}

void freeNodeDouble(node_double* n) {
    if (n != NULL) {
        freeNodeDouble(n -> next);
        free(n);
    }
}