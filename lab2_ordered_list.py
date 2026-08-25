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


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        # มีให้พร้อมใช้งานแล้ว อ้างอิงจาก Lab 1
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return "[" + ", ".join(elements) + "]"

    def add(self, item):
         current - self.head
         previous = None 
         stop = False

        while current is not None and not stop:
            if current._data > item:
                stop = True
            else:
                previous = current
                current = current.next

        temp = Node(item)
        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

    def search(self, item):
        current = self.head

         while current is not None:
            if current.data == item:
                return True

            if current.data > item:
                return False
                
        current = current.next

        return False


def run_tests_lab2():
    print("เริ่มการทดสอบ Lab 2...")
    ol = OrderedList()
    
    # ทดสอบภารกิจที่ 1
    ol.add(31)
    ol.add(77)
    ol.add(17)
    ol.add(93)
    ol.add(26)
    ol.add(54)
    
    expected = "[17, 26, 31, 54, 77, 93]"
    assert str(ol) == expected, f"ภารกิจที่ 1 ล้มเหลว: ลำดับไม่ถูกต้อง ได้ {str(ol)}"
    assert ol.size() == 6, "ภารกิจที่ 1 ล้มเหลว: จำนวนโหนดไม่ถูกต้อง"
    print("✅ ภารกิจที่ 1: add ทำงานและเรียงลำดับถูกต้อง")

    # ทดสอบภารกิจที่ 2
    assert ol.search(54) is True, "ภารกิจที่ 2 ล้มเหลว: ค้นหา 54 ที่มีอยู่ไม่พบ"
    assert ol.search(100) is False, "ภารกิจที่ 2 ล้มเหลว: ค้นหา 100 ไม่ควรพบ"
    assert ol.search(10) is False, "ภารกิจที่ 2 ล้มเหลว: ค้นหา 10 ไม่ควรพบ"
    assert ol.search(50) is False, "ภารกิจที่ 2 ล้มเหลว: ค้นหา 50 ไม่ควรพบ"
    print("✅ ภารกิจที่ 2: search ทำงานถูกต้อง (อย่าลืมตรวจลอจิก Early Exit ในโค้ดด้วยตัวเองอีกครั้ง)")
    print("🎉 ผ่าน Lab 2 ยอดเยี่ยมมาก!")

if __name__ == "__main__":
    run_tests_lab2()