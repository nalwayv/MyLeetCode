
#include <iostream>
#include <queue>
#include <limits>

namespace leet
{
	struct TreeNode
	{
		int val;
		TreeNode* left;
		TreeNode* right;
		TreeNode() :
			val(0), left(nullptr), right(nullptr) {
		}
		TreeNode(int x) :
			val(x), left(nullptr), right(nullptr) {
		}
		TreeNode(int x, TreeNode* left, TreeNode* right)
			: val(x), left(left), right(right) {
		}
	};

	class Solution
	{
	public:
		int maxLevelSum(TreeNode* root)
		{
			if (!root)
			{
				return 0;
			}

			std::queue<TreeNode*> que;
			que.push(root);

			int maxLevel = 0;
			int maxSum = std::numeric_limits<int>::min();
			int currentLevel = 1;

			while (!que.empty())
			{
				int currentSum = 0;
				int currentLevelSize = que.size();

				for (int _ = 0; _ < currentLevelSize; _++)
				{
					auto currentNode = que.front();
					que.pop();

					currentSum += currentNode->val;

					if (currentNode->left)
					{
						que.push(currentNode->left);
					}
					if (currentNode->right)
					{
						que.push(currentNode->right);
					}
				}

				if (currentSum > maxSum)
				{
					maxSum = currentSum;
					maxLevel = currentLevel;
				}

				currentLevel++;
			}

			return maxLevel;
		}
	};
}


static void cleanupTree(leet::TreeNode* node)
{
	if (!node)
	{
		return;
	}

	cleanupTree(node->left);
	cleanupTree(node->right);

	delete node;
}


int main()
{
	std::cout << "1161. Maximum Level Sum of a Binary Tree" << std::endl;

	auto root = new leet::TreeNode(1);
	root->left = new leet::TreeNode(7);
	root->right = new leet::TreeNode(0);
	root->left->left = new leet::TreeNode(7);
	root->left->right = new leet::TreeNode(-8);

	leet::Solution solution;
	std::cout << "Case1: " << solution.maxLevelSum(root) << std::endl;

	//cleanupTree(root);

	return 0;
}

