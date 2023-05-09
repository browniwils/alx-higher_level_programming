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

	while (s != NULL && s->next != NULL)
	{
		list = list->next;
		s = s->next->next;
		if (list == s)
		{
			list = f;
			f = s;
			while (1)
			{
				s = f;
				while (s->next != list && s->next != f)
				{
					s = s->next;
				}
				if (s->next == list)
				{
					break;
				}
				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
