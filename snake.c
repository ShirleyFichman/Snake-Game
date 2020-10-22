#include "functions.h"

int main()
{
	char check = RIGHT;//this is saving the last "move"
	char chTemp;// this input is for checking the user's input;
	char move = RIGHT;//once we save the relevant char
	int count = 0;//count the number of steps
	float speed = 1;//restart at 1 second
	init();//starts the screen
	drawFrame();//draw the frame to the screen
	//reset the snake
	SNAKE* snake = NULL;
	snake = (SNAKE*)malloc(sizeof(SNAKE*));
	snake->head = (NODE*)malloc(sizeof(NODE*));
	snake->head->x = (ROWS / 2) + 1;
	snake->head->y = (COLS / 2) + 1;
	snake->tail = snake->head;
	snake->tail->next = NULL;
	//reset the snake
	//reset the apple
	APPLE* apple = NULL;
	apple = (APPLE*)malloc(sizeof(APPLE*));
	apple->head = (NODE*)malloc(sizeof(NODE*));
	apple->head->x = 10;
	apple->head->y = 10;
	apple->head->next = NULL;
	gotoxy(apple->head->x, apple->head->y);
	printf("A");
	//
	gotoxy(snake->head->x, snake->head->y);
	printf("~");
	bool continueGame = true;
	
	while (continueGame)
	{
			if (_kbhit())//the player clicked the keyboard
			{
				chTemp = _getch();
				if (check == RIGHT && chTemp == LEFT)
					continueGame = false;
				else if (check == LEFT && chTemp == RIGHT)
					continueGame = false;
				else if (check == UP && chTemp == DOWN)
					continueGame = false;
				else if (check == DOWN && chTemp == UP)
					continueGame = false;
				if (checkChar(chTemp))//relevant move
				{
					move = chTemp;
					check = move;
				}//if
			}//if
			if (isDisqualification(move, snake, count) || isCrash(snake, count))//if the new move ends the game
				continueGame = false;
			else
			{
				moveSnake(move, snake, count, apple);
				count++;
				if ((count % 5 == 0) && (count != 0) && (speed > 0.1))//after 5 steps
				{
					speed = speed - (float)0.03;
				}//if
				sleep(speed);
			}//else
	}//while
	init();
	drawFrame();
	gotoxy(ROWS / 2, COLS / 2);
	printf("GAME OVER");
	gotoxy(ROWS, COLS);
	freeSnake(snake);
	freeApple(apple);
}

// Turn escape codes ON.
void init(void)
{
	system("cls");
}

// Moves the cursor to position (x,y) on screen.
// Parameters:
//     x: the row of the posiiton.
//     y: the column of the posiiton.
void gotoxy(int x, int y)
{
	printf("\x1b[%d;%df", x, y);
}

// Delays the execution of the program.
// Parameters:
//     secs: the length of the delay in seconds. 
void sleep(float secs)
{
	clock_t clocks_start = clock();

	while (clock() - clocks_start < secs*CLOCKS_PER_SEC)
		;
}

void drawFrame(void)
{
	int i;

	for (i = 1; i <= 75; i++)
	{
		gotoxy(1, i);
		printf("*");
	}//for

	for (i = 1; i <= 25; i++)
	{
		gotoxy(i, 1);
		printf("*");
	}//for

	for (i = 1; i <= 25; i++)
	{
		gotoxy(i, 75);
		printf("*");
	}//for

	for (i = 1; i <= 75; i++)
	{
		gotoxy(25, i);
		printf("*");
	}//for
}

bool checkChar(char chtemp)
{
	if (chtemp == 'a' || chtemp == 'd' || chtemp == 's' || chtemp == 'w')
		return true;
	else
		return false;
}

bool isDisqualification(char move, SNAKE* snake, int count)
{
	//checkes if the snake is touching the lines
	if (move == UP)
	{
		if (snake->head->x - 1 == 1) 
			return true;
		else
			return false;
	}//UP
	else if (move == DOWN)
	{
		if (snake->head->x + 1 == ROWS) 
			return true;
		else
			return false;
	}//DOWN
	else if (move == RIGHT)
	{
		if (snake->head->y + 1 == COLS)
			return true;
		else
			return false;
	}//RIGHT
	else if (move == LEFT)
	{
		if (snake->head->y - 1 == 0)
			return true;
		else
			return false;
	}//LEFT
}

bool isCrash(SNAKE * snake, int count)
{
	NODE* temp;
	temp = snake->head->next;
	if (count >= 5)
	{
		while (temp != NULL)
		{
			if ((temp->x == snake->head->x) && (temp->y == snake->head->y))
				return true;
			temp = temp->next;
		}//while
		return false;
	}//if
	free(temp);
}

void freeSnake(SNAKE * snake)
{
	if (snake == NULL)
		return;
	freeSnake(snake->head->next);
	free(snake);
}

void freeApple(APPLE * apple)
{
	if (apple == NULL)
		return;
	freeApple(apple->head->next);
	free(apple);
}

void moveSnake(char move, SNAKE* snake, int count, APPLE* apple)
{
	NODE* link;
	link = (NODE*)malloc(sizeof(NODE));
	link->next = snake->head;
	link->x = snake->head->x;
	link->y = snake->head->y;
	switch (move)
	{
	case RIGHT:
		link->y = snake->head->y + 1;
		break;

	case LEFT:
		link->y = snake->head->y - 1;
		break;

	case UP:
		link->x = snake->head->x - 1;
		break;

	case DOWN:
		link->x = snake->head->x + 1;
		break;
	default:
		break;
	}//switch
	snake->head = link;
	link = NULL;
	gotoxy(snake->head->x, snake->head->y);
	printf("~");
	if (isApple(snake, apple))//if the snake eats an apple
		return;
	else if ((count % 5 != 0) || count == 0 || isApple(snake, apple))//if it's not the 5th step
	{
		gotoxy(snake->tail->x, snake->tail->y);
		printf(" ");
		NODE* temp;
		temp = snake->head;
		while (temp->next->next != NULL)
		{
			temp = temp->next;
		}//while
		snake->tail = temp;
		snake->tail->next = NULL;
		free(temp->next);
	}//free the tail unless it's the 5th step 
}

bool isApple(SNAKE* snake, APPLE* apple)
{
	if ((apple->head->x == snake->head->x) && (apple->head->y == snake->head->y))//if the snake is touching the apple
	{
		apple->head->x = random(2, 25);
		apple->head->y = random(2, 75);
		gotoxy(apple->head->x, apple->head->y);
		printf("A");
		return true;
	}
	else
		return false;
}

int random(int min, int max) 
{
	return min + rand() / (RAND_MAX / (max - min + 1) + 1);
}