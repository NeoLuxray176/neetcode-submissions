class TimeMap:

    def __init__(self):
        self.dictionary = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dictionary:
            self.dictionary[key].append([timestamp, value])
        else:
            self.dictionary[key] = [[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dictionary:
            arr = self.dictionary[key]
            left, right = 0, len(arr) - 1

            while left <= right:
                middle = (left + right) // 2

                if arr[middle][0] < timestamp:
                    left = middle + 1
                else:
                    right = middle - 1

            return arr[middle][1]
        else:
            return ""
        
