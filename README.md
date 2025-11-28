 # 🔧 Chip Test Suite  
    ### An Embedded C Test Harness Built on ES-TDK  
    **By: zhanz565**  

    ![Build](https://img.shields.io/badge/build-passing-brightgreen)
    ![Language](https://img.shields.io/badge/language-C-blue)
    ![Python](https://img.shields.io/badge/python-3.10+-yellow)
    ![License](https://img.shields.io/badge/license-EPL_1.0-lightgrey)

    ---
    ## 🚀 Overview

    **Chip Test Suite** is a lightweight, beginner-friendly test harness built on top of  
    the open-source **ES-TDK (Embedded Software Test Development Kit)** framework.

    This project makes it easy to:

    - Write small **embedded-style C functions**
    - Test them using both **ETSpec test files** and a **Python fallback test engine**
    - Build everything with a simple **Makefile**
    - Run tests with one command (`python3 run_tests.py`)
    - Use GitHub Actions CI to automatically test the code on each push

    This project acts as a **personal learning environment for embedded testing**,  
    and a polished demo for hiring managers evaluating embedded or software engineering skills.

    ---
    ## 📁 Project Structure

    ```
    my-chip-test-suite/
    │
    ├── README.md
    ├── examples/
    │   └── hello/
    │       ├── src/
    │       │   └── main.c
    │       ├── tests/
    │       │   └── test_spec.et
    │       ├── Makefile
    │       └── run_tests.py
    ```

    ---
    ## ▶️ How to Run the Example

    **Build:**
    ```
    cd examples/hello
    make
    ```

    **Run tests:**
    ```
    python3 run_tests.py
    ```

    Expected output:
    ```
    Running tests...
    [PASS] test_addition
    [PASS] test_blink_stub
    [PASS] test_max_int
    Overall: [PASS] All fallback tests passed ✔
    ```

    If ES-TDK’s `tdk.jar` is detected locally, the script automatically switches  
    to the real ES-TDK engine. Otherwise, the lightweight fallback engine runs.

    ---
    ## 🧪 Tests Included

    - ✔ **test_addition** – verifies arithmetic  
    - ✔ **test_blink_stub** – simulates embedded HAL behavior  
    - ✔ **test_max_int** – example of embedded-style branching logic  

    ---
    ## 🛠 Technologies Used

    | Type | Tools |
    |------|-------|
    | Language | C, Python |
    | Build | GCC, Make |
    | Testing | ETSpec (ES-TDK), Python fallback |
    | OS | WSL / Linux |
    | CI | GitHub Actions |

    ---
    ## 📦 Installing Dependencies

    ```
    sudo apt update
    sudo apt install build-essential python3
    ```

    ---
    ## 🔁 Continuous Integration (CI)

    A GitHub Actions workflow automatically:

    - Builds the C example  
    - Runs the Python test engine  
    - Reports pass/fail status  

    Workflow file is at:
    ```
    .github/workflows/chip-test-suite-ci.yml
    ```

    ---
    ## 🌱 Future Improvements

    - Full ES-TDK integration
    - Real MCU backend (STM32 / Pico)
    - More complex test modules  
    - GUI dashboard for test visualization  

    ---
    ## 📜 License

    Base framework: **EPL-1.0**  
    Your additions: **MIT License** (optional)
