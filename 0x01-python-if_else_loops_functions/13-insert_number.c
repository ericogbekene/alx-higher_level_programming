#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	int idx = 0;
	listint_t *new_node;
	listint_t *current;

	current = *head;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
		*head = new_node;

	while (current != NULL)
	{
		if (idx == 4)
		{
			new_node->next = current->next;
			current->next = new_node;
			/*new_node */
		}
		current = current->next;
		idx++;
	}

	return (new_node);

}
