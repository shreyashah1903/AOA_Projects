import os
import subprocess

# Set the directories
input_dir = 'input'
output_dir = 'output'
gen_dir = 'gen'

# Get a list of all the input files
input_files = os.listdir(input_dir)

def checkFiles(file_regex, task_list):
    # Loop through each input file

    fail_count = 0
    total_count = 0
    for taskFile in task_list:
        for filename in input_files:
            total_count += 1
            # Construct the input and output file paths
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            gen_path = os.path.join(gen_dir, filename)

            # Run p1.py on the input file and save the output to the gen directory
            with open(input_path, 'r') as f_in, open(gen_path, 'w') as f_gen:
                subprocess.run(['python3', taskFile], stdin=f_in, stdout=f_gen)

            # Compare the generated output to the expected output
            with open(output_path, 'r') as f_out, open(gen_path, 'r') as f_gen:
                expected_output = f_out.read()
                generated_output = f_gen.read()
                if expected_output == generated_output:
                    print(f'{filename} - {taskFile}: PASS')
                else:
                    print(f'{filename} - {taskFile}: FAIL')
                    fail_count += 1

    print(f'{fail_count} failed out of {total_count}')
