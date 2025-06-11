class Element:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

class MaxHeapQueue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].priority > self.data[parent].priority:
                self._swap(index, parent)
                index = parent
            else:
                break

    def _sink_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.data[left].priority > self.data[largest].priority:
                largest = left
            if right < size and self.data[right].priority > self.data[largest].priority:
                largest = right

            if largest == index:
                break

            self._swap(index, largest)
            index = largest

    def insert(self, name, priority):
        new_element = Element(name, priority)
        self.data.append(new_element)
        self._bubble_up(len(self.data) - 1)

    def remove_max(self):
        if self.is_empty():
            return None
        self._swap(0, len(self.data) - 1)
        max_element = self.data.pop()
        self._sink_down(0)
        return max_element

    def peek_max(self):
        if self.is_empty():
            return None
        return self.data[0]

    def __str__(self):
        return str([(e.name, e.priority) for e in self.data])

queue = MaxHeapQueue()
queue.insert("Завдання 1", 3)
queue.insert("Завдання 2", 5)
queue.insert("Завдання 3", 1)
queue.insert("Завдання 4", 4)

print("Поточна черга:", queue)
print("Видалено елемент з найвищим пріоритетом:", queue.remove_max().name)
print("Поточна черга після видалення:", queue)

