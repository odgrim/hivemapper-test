#!/usr/bin/env python3
import argparse
import json
import multiprocessing
import os
import subprocess
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print("%s does not exist"% args.input_file)
        sys.exit(1)
    return args

def execute_string(args_tuple):
    command_to_run, timeout = args_tuple
    try:
        job_run = subprocess.run([command_to_run], timeout=timeout, capture_output=True)
        output = job_run.stdout
    except subprocess.TimeoutExpired:
        output = "Timeout Expired"
    return output

def main(args):
    with open(args.input_file, 'r') as f:
        jobs = json.load(f)
    pool = multiprocessing.Pool(len(jobs['run_these']))
    
    job_args = []
    for job in jobs['run_these']:
       job_args.append(tuple(job.values()))

    results = pool.map_async(execute_string, job_args, callback=print)
    results.wait()
    results.get()

if __name__ == "__main__":
    args = parse_args()
    main(args)

