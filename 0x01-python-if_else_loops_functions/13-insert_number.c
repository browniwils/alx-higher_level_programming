#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a new node in list
 * @head: points to list head
 * @number: position in list were node to be inserted
 * Return: pointer to the first node of list otherwise NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *p_head, *o_head = *head;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
	{
		return (NULL);
	}
	while (o_head != NULL)
	{
		if (o_head->n > number)
		{
			break;
		}
		p_head = o_head;
		o_head = o_head->next;
	}
	node->n = number;
	if (*head == NULL)
	{
		node->next = NULL;
		*head = node;
	}
	else
	{
		node->next = o_head;
		if (o_head == *head)
		{
			*head = node;
		}
		else
		{
			p_head->next = node;
		}
	}
	return (node);
}
