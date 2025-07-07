# Fuzzing Results – crashme.c

## Date: 2025-07-07
## Target Binary: ./crashme
## Fuzzer: AFL++ (afl-fuzz)

### Command Used:
```bash
afl-fuzz -i fuzz_inputs -o logs -- ./crashme @@
