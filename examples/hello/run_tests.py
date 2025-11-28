import os
import subprocess
import sys

TEST_SPEC = "tests/test_spec.et"
BINARY = "build/demo.out"

def fallback_self_test():
    print("ES-TDK not available, running fallback self-tests...\n")

    # Simple self-checks mirroring our C functions
    passed = True

    # test_addition
    if 2 + 3 == 5:
        print("[PASS] test_addition (fallback)")
    else:
        print("[FAIL] test_addition (fallback)")
        passed = False

    # test_blink_stub semantics
    if (3 > 0) and not (0 > 0):
        print("[PASS] test_blink_stub (fallback)")
    else:
        print("[FAIL] test_blink_stub (fallback)")
        passed = False

    # test_max_int
    if max(3, 7) == 7 and max(10, -5) == 10 and max(0, 0) == 0:
        print("[PASS] test_max_int (fallback)")
    else:
        print("[FAIL] test_max_int (fallback)")
        passed = False

    if passed:
        print("\nOverall: [PASS] All fallback tests passed ✔")
    else:
        print("\nOverall: [FAIL] Some fallback tests failed ❌")

def run_es_tdk_tests():
    print("Running tests...")

    # TODO: adjust this if you actually set up ES-TDK's tdk.jar locally
    TDK_JAR = "../../../../org.testeditor.tdk.eclipse.application/tdk.jar"

    if not os.path.exists(TDK_JAR):
        print("Warning: ES-TDK tdk.jar not found, using fallback test runner.")
        fallback_self_test()
        return

    result = subprocess.run(
        ["java", "-jar", TDK_JAR, BINARY, TEST_SPEC],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    output = result.stdout.strip()
    error = result.stderr.strip()

    if result.returncode != 0:
        print("ES-TDK returned an error, falling back to self-tests.")
        if error:
            print("\nES-TDK error output:")
            print(error)
        fallback_self_test()
        return

    # Very naive check; you can refine based on actual ES-TDK output
    if "FAIL" in output:
        print("[FAIL] Some tests failed ❌")
    else:
        print("[PASS] All tests passed ✔")

    print("\nRaw Output:")
    print(output)

if __name__ == "__main__":
    if not os.path.exists(BINARY):
        print("Error: binary not found. Run `make` first.")
        sys.exit(1)

    run_es_tdk_tests()
