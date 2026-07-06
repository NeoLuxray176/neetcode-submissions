class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start_dict = {}
        end_dict = {}

        for i, c in enumerate(s):
            if not c in start_dict:
                start_dict[c] = i
            end_dict[c] = i

        print(f"Character {s[0]} from {start_dict[s[0]]} to {end_dict[s[0]]}")
        output = [end_dict[s[0]]]
        j = 1

        while j < len(s):
            c = s[j]
            c_start = start_dict[c]
            c_end = end_dict[c]

            print(f"Previous range is until {output[len(output) - 1]}")
            print(f"Character {c} from {c_start} to {c_end}")

            if c_start > output[len(output) - 1]:
                print(f"New character {c} with no overlaps at {j}")
                output.append(1)
                j += 1
            else:
                print(f"At character {c} Increase previous range {c_start} {output[len(output) - 1]}")
                output[len(output) - 1] = output[len(output) - 1] + (c_end - c_start)
                print(f"Next character to look at is {1 + (c_end - c_start)}")
                j += 1 + (c_end - c_start)

        return output