from collections.abc import MutableSequence
from typing import Iterator, Any, Iterable, Optional

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self._len = 0
        self._head: Optional[Node] = None
        self._tail = self._head

        if data is not None:
            for value in data:
                self.append(value)

    def __len__(self):
        return self._len

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self._len:  # для for
            raise IndexError()

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __delitem__(self, index: int) -> None:
        """ Метод удаляет значение узла по указанному индексу. """
        if not isinstance(index, int):
            raise TypeError()
        else:
            current_index = 1
            right_node = self._head
            left_node = None

            while right_node is not None:
                if current_index == index:
                    if left_node is not None:
                        left_node.next = right_node.next
                    else:
                        self._head = right_node.next
                        return

                left_node = right_node
                right_node = right_node.next
                current_index += 1

            return

    def insert(self, index: int, value: Any) -> Any:
        next_node = self.step_by_step_on_nodes(index + 1)
        self.step_by_step_on_nodes(index).next = Node(value)
        self.step_by_step_on_nodes(index + 1).next = next_node
        self._len += 1

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def nodes_iterator(self) -> Iterator[Node]:
        current_node = self._head
        for _ in range(self._len):
            yield current_node
            current_node = current_node.next


class DoubleLinkedList(LinkedList):
    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        """Метод связывает узлы двусвязного списка"""
        left_node.next = right_node
        right_node.prev = left_node


def append(self, value: Any):
    """ Добавление элемента в конец связного списка. """
    append_node = DoubleLinkedNode(value)

    if self._head is None:
        self._head = self._tail = append_node
    else:
        self.linked_nodes(self._tail, append_node)
        self._tail = append_node

    self._len += 1


def __delitem__(self, index: int) -> Any:
    """ Метод удаляет значение узла по указанному индексу. """
    if not isinstance(index, int):
        raise TypeError()
    else:
        current_index = 1
        right_node = self._head
        left_node = None

        while right_node is not None:
            if current_index == index:
                if left_node is not None:
                    left_node.next = right_node.next
                    right_node.next.prev = left_node
                else:
                    self.head = right_node.next
                    return

            left_node = right_node
            right_node = right_node.next
            current_index += 1
        self._len = self._len - 1
        return


def insert(self, index: int, value: Any) -> None:
    """Метод устанавливает узел по указанному индексу """
    inserted_node = DoubleLinkedNode(value)
    next_node = self.step_by_step_on_nodes(index + 1)
    self.step_by_step_on_nodes(index).next = inserted_node
    self.step_by_step_on_nodes(index + 1).next = next_node
    self.step_by_step_on_nodes(index + 2).prev = inserted_node
    self._len += 1


if __name__ == "__main__":
    ...
