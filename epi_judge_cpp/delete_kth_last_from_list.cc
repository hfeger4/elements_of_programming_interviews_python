#include <memory>

#include "list_node.h"

using std::shared_ptr;

// Assumes L has at least k nodes, deletes the k-th last node in L.
shared_ptr<ListNode<int>> RemoveKthLast(const shared_ptr<ListNode<int>>& L,
                                        int k) {
  // Implement this placeholder.
  return nullptr;
}

#include "test_framework/test_utils_generic_main.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> param_names{"L", "k"};
  generic_test_main(argc, argv, param_names, "delete_kth_last_from_list.tsv",
                    &RemoveKthLast);
  return 0;
}
