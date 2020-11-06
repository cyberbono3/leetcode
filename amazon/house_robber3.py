class Solution:
    	def rob(self, root):

        def solve(node, rob, memo):
            if not node:
                    return 0
            elif (rob, node) in memo:
                return memo[(rob, node)]
            # rob this - can't rob next 2
            robbed = (node.val if rob else 0) + solve(node.left, not rob, mem) + solve(node.right, not rob, mem)
            # don't rob - can rob next 2
            not_robbed = solve(node.left, True, mem) + solve(node.right, True, mem)

            result = max(robbed, not_robbed)
            memo[(rob, node)] = result
            return result
        
        return solve(root, True, {})