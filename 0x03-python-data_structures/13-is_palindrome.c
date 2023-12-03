#include "lists.h"
#include <stddef.h>

/**
 * is_palind - identify if the list is palindrome
 * @head: the head of the list
 * @end:the end of the list
 * Return: 0 if not or 1 if it is a palindrome
 */
int is_palind(listint_t **head, listint_t *end)
{
	if (!end)
		return (1);
	if (is_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - identify if the list is palindrome
 * @head: the head of the list
 * Return: 0 if not or 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (is_palind(head, *head));
}	
