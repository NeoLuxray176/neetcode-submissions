class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append([value, timestamp])
        else:
            self.map[key] = [[value, timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        else:
            arr = self.map[key]

            left, right = 0, len(arr) - 1
            res = ""

            while left <= right:
                middle = (left + right) // 2

                if arr[middle][1] <= timestamp:
                    res = arr[middle][0]
                    left = middle + 1
                else:
                    right = middle - 1

            return res

        
