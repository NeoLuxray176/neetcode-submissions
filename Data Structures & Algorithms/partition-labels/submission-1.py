class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 1. Only need end_dict (last occurrence of each char)
        end_dict = {c: i for i, c in enumerate(s)}
        
        output = []
        j = 0          # The furthest index we need to reach for the current partition
        anchor = 0     # The starting index of the current partition
        
        # 2. Iterate through every character, don't skip
        for i, c in enumerate(s):
            # Update the furthest point this partition must reach
            j = max(j, end_dict[c])
            
            # 3. If we have reached the furthest point required
            if i == j:
                # Calculate length: current_index - start_index + 1
                output.append(i - anchor + 1)
                # Move anchor to the start of the next partition
                anchor = i + 1
                
        return output