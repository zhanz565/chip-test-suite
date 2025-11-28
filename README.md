    # Chip Test Suite (Built on ES-TDK)

    This project extends the open-source **ES-TDK (Embedded Software Test Development Kit)**  
    to provide a clean, beginner-friendly, and demo-ready embedded testing environment.

    It is designed so students and developers can:
    - Quickly write tests for embedded C code  
    - Run them using ES-TDK’s existing test engine  
    - See real pass/fail outputs  
    - Build testable firmware modules  
    - Eventually extend to physical microcontrollers

    This repository adds:
    - A simple **Hello World example**  
    - A **minimal Makefile** for building and running tests  
    - A **Python test runner** that displays clean results  
    - Beginner-friendly documentation explaining how to add new tests  

    ---

    ## 📁 Project Layout

    ```
    my-chip-test-suite/
        README.md          → this file
        examples/
            hello/         → a simple “hello world” test project
                src/       → firmware/application code
                tests/     → test specifications
                Makefile   → build script
                run_tests.py → test runner
    ```

    ---

    ## ▶️ Running the Example (Hello Test)

    ### **Linux / WSL / macOS**
    ```
    cd examples/hello
    make
    python3 run_tests.py
    ```

    ### **Windows (PowerShell)**
    ```
    cd examples\hello
    make
    python run_tests.py
    ```

    You should see ES-TDK produce:
    ```
    Running tests...
    [PASS] test_addition
    [PASS] test_blink_stub
    All tests passed ✔
    ```

    ---

    ## 🧪 About the Test System

    The tests are written using **ETSpec**, the ES-TDK test specification language.

    This demo keeps it simple:
    - Runs tests against basic C functions
    - Uses ES-TDK engine to evaluate results
    - Prints human-readable pass/fail output

    Later you can extend it to real microcontrollers (e.g., STM32, Raspberry Pi Pico).

    ---

    ## 🌱 How to Add Your Own Tests

    1. Add a function to `src/main.c`
    2. Write a matching test in `tests/test_spec.et`
    3. Run `python3 run_tests.py`

    ---

    ## ⭐ Why This Project Exists

    This is a student-friendly, improved extension of the ES-TDK framework.  
    It makes the system **easier to understand**, **easier to run**, and **more résumé-ready** by including:

    - Examples  
    - Build scripts  
    - Documentation  
    - Test runner  
    - Demonstration workflows  

    ---

    ## 📜 License

    Base framework: ES-TDK (EPL-1.0)  
    Your additions: MIT License (optional)