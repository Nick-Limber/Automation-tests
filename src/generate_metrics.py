import os
import subprocess
import sys

# ENVIRONMENT VARIABLE EXTRACTION WITH DEFAULTS
duration = os.getenv("DURATION", "60s")
cpu_max_load = os.getenv("CPU_MAX_LOAD", "100")
num_cores = os.getenv("num_cores", "2")
memrate_bytes = os.getenv("memrate_bytes", "")
memrate_flush = os.getenv("memrate_flush", "on")
cpu_method = os.getenv("cpu_method", "all")


def stress_cpu():

    stress_args = [
        "stress-ng",
        "--cpu", (num_cores),
        "--cpu-method", (cpu_method),
        "--cpu-load", (cpu_max_load),
        "-t", (duration)
    ]

    cmd = ["perf", "stat", "-x,", "-o ../output.csv"] + stress_args

    res = subprocess.run(cmd, check=True)
    print(res.returncode)

def stress_mem():

    stress_args = [
            "stress-ng",
            "--memrate", num_cores,
            "-t", duration
            ]

    if memrate_bytes:
        stress_args.extend(["--memrate-bytes", memrate_bytes])
    if memrate_flush == "on":
        stress_args.extend(["--memrate-flush"])

    cmd =  ["perf", "stat", "-x,"] + stress_args

    res = subprocess.run(cmd, check=True)
    print(res.returncode)


if __name__ == "__main__":

    stress_cpu()
    stress_mem()
