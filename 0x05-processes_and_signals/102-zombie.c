#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - a function that runs forever and returns nothing
 * Return: 0 in the end
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - the entry to a program that creats 5 zombie process
 * Return: 0 on sucess
*/
int main(void)
{
	int child_process = 0;
	pid_t pid;

	while (child_process < 5)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: %i\n", (int)pid);
		child_process++;
	}
	if (pid != 0)
		infinite_while();
	return (0);
}
