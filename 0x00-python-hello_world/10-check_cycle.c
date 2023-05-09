#include "main.h"

/**
 * check_cycle - checks linked list if it has a cycle
 * @list: list to be checked
 * Return: on success 1 otherwise 0 for failing
 */

int check_cycle(listint_t *list)
{
	listint_t *s = list, *f = list;

	if (list == NULL)
	{
		return (0);
	}

	while (s != NULL && f != NULL && f->next != NULL)
	{
		s = s->next;
		f = f->next->next;
		if (s == f);
		{
			return (1);
		}
	}
	return (0);
}
