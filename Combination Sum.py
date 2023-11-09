from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # Visualize the current state before diving deeper
            print(f"dfs called with i={i}, cur={cur}, total={total}")

            if total == target:
                res.append(cur.copy())
                print(f"Found combination: {cur}")  # Visualize when we find a combination
                return
            if i >= len(candidates) or total > target:
                print("No valid continuation found, returning back up.")  # Visualize the dead end
                return

            # Choose the current candidate
            cur.append(candidates[i])
            print(f"Choose {candidates[i]}, new cur={cur}, new total={total + candidates[i]}")
            dfs(i, cur, total + candidates[i])

            # Backtrack: Unchoose the last candidate
            cur.pop()
            print(f"Backtrack, new cur={cur}, new total={total}")

            # Choose to skip the current candidate
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

# Create a Solution object
sol = Solution()

# Call the combinationSum method with the provided input and target
result = sol.combinationSum([2, 3, 6, 7], 7)

# Print the result
print("Combinations that sum to the target are:", result)
