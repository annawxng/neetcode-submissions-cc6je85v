class TimeMap:

    # key("alice") - should be a string
    # value - {timestamp : str} - exactly one string per timestamp




    def __init__(self):
        self.timeMp = defaultdict((list))

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMp or not self.timeMp[key]:
            return ""
        best = ""
        pairs = self.timeMp[key]
        left = 0
        right = len(pairs) - 1

        while left <= right:
            mid = (left + right) // 2
            if self.timeMp[key][mid][0] <= timestamp:
                left = mid + 1
                best = self.timeMp[key][mid][1]
            # mid > timestamp
            else:
                right = mid - 1
        return best


# timeMp:
# "alice": (1, "happy"), (3, "sad")

# TimeMap timeMap = new TimeMap();
# timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
# timeMap.get("alice", 1);           // return "happy"
# timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
# timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
# timeMap.get("alice", 3);           // return "sad"
# timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.


        
