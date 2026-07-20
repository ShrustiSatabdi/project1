class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        path = []
        def dfs(index, total):
            if total == target:
                ans.append(path.copy())
                return
            if total > target:
                return
            if index == n:
                return
            path.append(candidates[index])
            dfs(index, total+candidates[index])
            path.pop()
            dfs(index+1, total)
        dfs(0,0)
        return ans


        