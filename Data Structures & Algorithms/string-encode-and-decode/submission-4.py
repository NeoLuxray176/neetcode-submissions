class Solution:

    def encode(self, strs: List[str]) -> str:
        # "neet" "code"
        # \"neet\"\"code\"
        enc_output = ""
        for single_str in strs:
            enc_output += "\""
            for char in single_str:
                if char == "\"": # checking for " in string
                    enc_output += "\\\"" # this is the literal \"
                elif char == "\\": # checking for \ in string
                    enc_output += "\\\\" # this is the literal \\
                else:
                    enc_output += char
            enc_output += "\""
        # print(f"{enc_output}")
        return enc_output

    def decode(self, s: str) -> List[str]:
        output = []
        curr_string = None
        for i in range(len(s)-1):
            print(f"{i} Processing {s[i]} or {s[i:i+1]}")
            if s[i:i+1] == "\\\"": # checking for the literal \"
                curr_string += "\"" # adding the literal "
            elif s[i:i+1] == "\\\\": # checking for the literal \\
                curr_string += "\\"
            elif s[i] == "\"": # this denotes the start or end of an item in the original strs array
                # print(f"We have a boundry character")
                if curr_string == None:
                    # print(f"Start of the string, initialize curr_string")
                    curr_string = ""
                else:
                    # print(f"End of the string, append to output and reset curr_str {curr_string}")
                    output.append(curr_string)
                    curr_string = None
            else:
                # print(f"{i} Adding {s[i]} to curr_string {curr_string}")
                curr_string += s[i]
        if curr_string is not None:
            output.append(curr_string)
        return output

