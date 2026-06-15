class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        if (head == nullptr || head.next == nullptr) {
            return nullptr;
        }

        auto mid = head;
        auto prev = head;
        auto size = 1;

        for (auto current = head; current->next != nullptr; current = current->next) {
            if(++size % 2 == 0) {
                prev = mid;
                mid = mid->next;
            }
        }

        prev->next = mid->next;
        
        return head;
    }
};