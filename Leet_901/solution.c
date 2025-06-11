#include <stdio.h>
#include <stdlib.h>


typedef struct Span {
    int price;
    int amount;
} Span;


typedef struct Node {
    Span data;
    struct Node* next;
} Node;


typedef struct StockSpanner {
    Node* top;
} StockSpanner;


void stockPush(StockSpanner* self, Span value) {
    Node* node = malloc(sizeof(Node));
    node->data = value;
    node->next = self->top;
    self->top = node;
}


Span stockPop(StockSpanner* self) {
    Node* temp = self->top;
    Span value = temp->data;
    self->top = temp->next;
    
    free(temp);

    return value;
}


Span stockPeek(StockSpanner* self){ 
    return self->top->data;
}


int stockIsEmpty(StockSpanner* self) {
    return self->top == NULL;
}


void stockSpannerFree(StockSpanner* self) {
    while(!stockIsEmpty(self)) {
        stockPop(self);
    }

    free(self);
}


StockSpanner* stockSpannerCreate() {
    StockSpanner* stock = malloc(sizeof(StockSpanner));
    stock->top = NULL;
    return stock;
}


int stockSpannerNext(StockSpanner *self, int price) {
    int span = 1;
    while (!stockIsEmpty(self) && stockPeek(self).price <= price) {
        span += stockPop(self).amount;
    }

    stockPush(self, (Span){.price= price, .amount= span});
    return span;
}


int main() {
    StockSpanner *stock= stockSpannerCreate();

    printf("StockSpanner(100) = %d\n", stockSpannerNext(stock, 100));
    printf("StockSpanner(80) = %d\n", stockSpannerNext(stock, 80));
    printf("StockSpanner(60) = %d\n", stockSpannerNext(stock, 60));
    printf("StockSpanner(70) = %d\n", stockSpannerNext(stock, 70));
    printf("StockSpanner(60) = %d\n", stockSpannerNext(stock, 60));
    printf("StockSpanner(75) = %d\n", stockSpannerNext(stock, 75));
    printf("StockSpanner(85) = %d\n", stockSpannerNext(stock, 85));
    
    stockSpannerFree(stock);
    
    return 0;
}