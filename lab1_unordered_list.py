class Node:
    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self): return self._data
    def set_data(self, node_data): self._data = node_data
    data = property(get_data, set_data)

    def get_next(self): return self._next
    def set_next(self, node_next): self._next = node_next
    next = property(get_next, set_next)

    def __str__(self):
        return str(self._data)


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item):
        current = self.head
        previous = None
        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError(f"{item} is not in the list")
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def __str__(self):
        elements = []
        current = self.head

        while current is not None:
            elements.append(str(current.data))
            current = current.next
        
        return "["+", ".join(elements) + "]" 
        
    def append(self, item):
        temp = Node(item)

        if self.head is None:
            self.head = temp
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = temp
        
def run_tests_lab1():
    print("เริ่มการทดสอบ Lab 1...")
    ul = UnorderedList()
    
    # ทดสอบภารกิจที่ 1
    ul.add(30)
    ul.add(20)
    ul.add(10)
    assert str(ul) == "[10, 20, 30]", f"ภารกิจที่ 1 ล้มเหลว: ค่าที่ได้คือ {str(ul)}"
    print("✅ ภารกิจที่ 1: __str__ ทำงานถูกต้อง")

    # ทดสอบภารกิจที่ 2
    ul.append(40)
    ul.append(50)
    assert str(ul) == "[10, 20, 30, 40, 50]", f"ภารกิจที่ 2 ล้มเหลว: ค่าที่ได้คือ {str(ul)}"
    print("✅ ภารกิจที่ 2: append ทำงานถูกต้อง")
    print("🎉 ผ่าน Lab 1 ยอดเยี่ยมมาก!\n")

if __name__ == "__main__":
    run_tests_lab1()