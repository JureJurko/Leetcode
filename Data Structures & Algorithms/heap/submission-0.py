class MinHeap:
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        idx = len(self.heap) - 1
        i = idx // 2
        
        while i >= 1:
            if self.heap[i] > self.heap[idx]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[idx]
                self.heap[idx] = tmp
            
            idx = i
            i //= 2

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        
        ret_val = self.heap[1]
        self.heap[1] = self.heap.pop()

        i = 1

        while i * 2 < len(self.heap):
            if (i * 2 + 1 < len(self.heap) and
                self.heap[i * 2 + 1] < self.heap[i * 2] and
                self.heap[i * 2 + 1] < self.heap[i]):
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2 + 1]
                self.heap[i * 2 + 1] = tmp
                i = i * 2 +1
            elif self.heap[i * 2] < self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2]
                self.heap[i * 2] = tmp
                i = i * 2
            else:
                break

        return ret_val

    def top(self) -> int:
        if len(self.heap) <= 1:
            return -1
        
        return self.heap[1]
        
    def heapify(self, nums: List[int]) -> None:
        self.heap.extend(nums)

        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            i = cur
            while 2 * i < len(self.heap):
                if (2 * i + 1 < len(self.heap) and
                    self.heap[2 * i + 1] < self.heap[2 * i] and
                    self.heap[2 * i + 1] < self.heap[i]):
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[2 * i] < self.heap[i]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i 
                else:
                    break
            cur -= 1

        