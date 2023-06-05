#include "lists.h"
#include <stdio.h>
/**
* check_cycle - checks  is a singly linked list has a cycle in it
* @list: point er to the list
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint _t * fast = list;
	listint _t * slow = list;
	if (!list)
	{
		return (0);
	}
	while (1)
	{
		if (fast->next != NULL && fast->next->next != NULL)
		{
			fast = fast->next->next;
			slow = slow->next;
			if (fast == slow)
			{
				return (1);
			}
		}
		else
		{
			return (0);
		}
	}
}
