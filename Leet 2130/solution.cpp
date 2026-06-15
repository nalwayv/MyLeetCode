class Solution {
public:
    int pairSum(ListNode* head) {
        std::vector<ListNode*> nodes;
        for (auto current = head; current != nullptr; current = current->next) {
            nodes.push_back(current);
        }

        int maxPair = -1;
        int p1 = 0;
        int p2 = nodes.size() - 1;
        while (p1 < p2)
        {
            int val1 = nodes.at(p1++)->val;
            int val2 = nodes.at(p2--)->val;
            if (val1 + val2 > maxPair) {
                maxPair = val1 + val2;
            }
        }
        return maxPair;
    }
};