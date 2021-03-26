#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: singly linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
**/
int check_cycle(listint_t *list)
{
	listint_t *a, *b;

	a = b = list;

	while (a && b && a->next)
	{
		a = a->next->next;
		b = b->next;

		if (b == a)
			return (1);
	}

	return (0);
}
