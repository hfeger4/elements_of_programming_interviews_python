package epi;

import epi.test_framework.EpiTest;
import epi.test_framework.GenericTestHandler;

public class CollatzChecker {
  @EpiTest(testfile = "collatz_checker.tsv")

  public static boolean testCollatzConjecture(int n) {
    // Implement this placeholder.
    return true;
  }

  public static void main(String[] args) {
    GenericTestHandler.executeTestsByAnnotation(
        new Object() {}.getClass().getEnclosingClass(), args);
  }
}
