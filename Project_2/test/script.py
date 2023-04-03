import os
import subprocess

# Set the directories
input_dir = 'input'
output_dir = 'output'
gen_dir = 'gen'

# Get a list of all the input files
input_files = os.listdir(input_dir)

tasks = {'p1': ['../task1.py', '../task2.py', '../task3.py'], 'p2': ['../task4.py', '../task5A.py', '../task5B.py'],
         'p3': ['../task6.py', '../task7A.py', '../task7B.py']}


def checkFiles():
    cleanup()
    total_count = 0
    fail_count = 0
    for filename in input_files:
        # Construct the input and output file paths
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        gen_path = os.path.join(gen_dir, filename)

        if 'p1' in filename:
            task_list = tasks['p1']
        elif 'p2' in filename:
            task_list = tasks['p2']
        else:
            task_list = tasks['p3']

        for taskFile in task_list:
            total_count += 1

            # Run p1.py on the input file and save the output to the gen directory
            with open(input_path, 'r') as f_in, open(gen_path, 'w') as f_gen:
                subprocess.run(['python3', taskFile], stdin=f_in, stdout=f_gen)

            # Compare the generated output to the expected output
            with open(output_path, 'r') as f_out, open(gen_path, 'r') as f_gen:
                expected_output = f_out.read()
                generated_output = f_gen.read().strip()
                if expected_output == generated_output:
                    print(f'{filename} - {taskFile}: PASS')
                else:
                    print(f'{filename} - {taskFile}: FAIL')
                    fail_count += 1

    print(f'{fail_count} failed out of {total_count}')


def cleanup():
    dir = 'gen'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


if __name__ == '__main__':
    checkFiles()
