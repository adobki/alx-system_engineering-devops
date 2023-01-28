#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - Keeps process running in memory indefinitely.
 *
 * Return: Always 0 (Success).
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
 * createZombie - Creates a zombie process by duplicating current process as a
 *                child process using fork(), then returns the child's PID.
 *                If PID == 0, current process is fork() duplicate, so exit it
 *                [without handling its exit code in parent] to turn it into a
 *                zombie process.
 *                If PID != 0, current process is original/parent process.
 *
 * Return: Process ID (PID) of created zombie process.
 */
int createZombie(void)
{
	int PID = 1;

	PID = fork();
	if (PID == 0)
		exit(EXIT_SUCCESS);

	return (PID);
}

/**
 * main - Creates 5 zombie processes in Ubuntu/Linux.
 *
 * Return: Always EXIT_SUCCESS (0).
 */
int main(void)
{
	int count = 5;

	while (count--)
		printf("Zombie process created, PID: %d\n", createZombie());

	infinite_while();

	return (EXIT_SUCCESS);
}
