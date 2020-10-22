#ifndef functions_h
#define functions_h
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

//Shirley Fichman
//ID 207021502
//PROJECT 2: SNAKE

typedef struct node
{
	int x;
	int y;
	struct node* next;
} NODE;

typedef struct snake
{
	NODE* head;
	NODE* tail;
} SNAKE;

typedef struct apple
{
	NODE* head;
} APPLE;

// Turn escape codes ON.
void init(void);

// Moves the cursor to position (x,y) on screen.
// Parameters:
//     x: the row of the posiiton.
//     y: the column of the posiiton.
void gotoxy(int x, int y);

// Delays the execution of the program.
// Parameters:
//     secs: the length of the delay in seconds. 
void sleep(float secs);

//Draws the lines of (*) to the screen
void drawFrame(void);

//this function checkes if the char entered by the player is relevant to the game
bool checkChar(char chtemp);

//prints the snake to the screen+lengthen it every 5 steps
void moveSnake(char move, SNAKE* snake, int count, APPLE* apple);

//this function will check if the move of the player causes disqualification by crashing into the lines
bool isDisqualification(char move, SNAKE* snake, int count);

//checkes if the snake is "crashing" with itself
bool isCrash(SNAKE* snake, int count);

//at the end of the game- frees the snake
void freeSnake(SNAKE* snake);

//at the end of the game- frees the apple
void freeApple(APPLE * apple);

//checkes if touches an apple
bool isApple(SNAKE* snake, APPLE* apple);

//generate a randong number
int random(int min, int max);

#define COLS 75 //y
#define ROWS 25 //x
#define LEFT 'a'
#define RIGHT 'd'
#define UP 'w'
#define DOWN 's'

#endif
