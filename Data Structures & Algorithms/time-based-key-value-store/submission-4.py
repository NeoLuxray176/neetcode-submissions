class TimeMap:

    def __init__(self):
        self.dictionary = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dictionary:
            self.dictionary[key].append((timestamp, value))
        else:
            self.dictionary[key] = [((timestamp, value))]
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.dictionary:
            return ""
        arr = self.dictionary[key]

        left = 0
        right = len(arr) - 1
        last_val = ""

        while left <= right:
            middle = (left + right) // 2
            if arr[middle][0] <= timestamp:
                left = middle + 1
                last_val = arr[middle][1]
            else:
                right = middle - 1
        
        return last_val

