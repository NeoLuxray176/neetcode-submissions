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
        # print(f"arr is {arr}")

        last_val = ""
        # for (t, v) in arr:
        #     if t > timestamp:
        #         return last_val
        #     last_val = v

        left = 0
        right = len(arr) - 1
        while left <= right:
            print(f"last_val is {last_val}")
            middle = (left + right) // 2
            if arr[middle][0] <= timestamp:
                left = middle + 1
                last_val = arr[middle][1]
            else:
                right = middle - 1
        
        return last_val

        
