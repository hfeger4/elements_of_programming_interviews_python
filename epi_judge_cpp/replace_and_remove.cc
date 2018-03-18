#include <iterator>
#include <string>
#include <vector>

#include "test_framework/test_timer.h"

using std::string;
using std::vector;

int ReplaceAndRemove(int size, char s[]) {
  // Implement this placeholder.
  return 0;
}

vector<string> ReplaceAndRemoveWrapper(TestTimer& timer, int size,
                                       const vector<string>& s) {
  std::vector<char> s_copy(s.size(), '\0');
  for (int i = 0; i < s.size(); ++i) {
    if (!s[i].empty()) {
      s_copy[i] = s[i][0];
    }
  }

  timer.Start();
  int res_size = ReplaceAndRemove(size, s_copy.data());
  timer.Stop();

  vector<string> result;
  for (int i = 0; i < res_size; ++i) {
    result.emplace_back(string(1, s_copy[i]));
  }
  return result;
}

#include "test_framework/test_utils_generic_main.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> param_names{"timer", "size", "s"};
  generic_test_main(argc, argv, param_names, "replace_and_remove.tsv",
                    &ReplaceAndRemoveWrapper);
  return 0;
}
