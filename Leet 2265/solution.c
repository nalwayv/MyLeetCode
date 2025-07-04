/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct AverageResult {
    int sum;
    int length;
};

struct AverageResult get_result(struct TreeNode* root, int* count) {
    if (!root) {
        return (struct AverageResult){0, 0};
    }

    struct AverageResult left = get_result(root->left, count);
    struct AverageResult right = get_result(root->right, count);

    int sum = left.sum + right.sum + root->val;
    int length = left.length + right.length + 1;

    if (root->val == sum / length) {
        *count += 1;
    }

    return (struct AverageResult){sum, length};
}

int averageOfSubtree(struct TreeNode* root) {
    int count = 0;
    get_result(root, &count);
    return count;
}