import subprocess
import time

parse = lambda x: "".join(x.split()) # Remove Whitespaces.
SEPERATOR = "-" * 7
PYTHON_IMPL = "python3 kmeans.py"
C_IMPL = "./prog"
tests = ["3 600 < tests/input_1.txt", "7 < tests/input_2.txt", "15 300 < tests/input_3.txt"]
outputs = ["tests/output_1.txt", "tests/output_2.txt", "tests/output_3.txt"]
for output, test in zip(outputs, tests):
	python_start = time.time()
	python_output = subprocess.check_output(f"{PYTHON_IMPL} {test}", shell=True).decode()
	python_end = time.time()

	c_start = time.time()
	c_output = subprocess.check_output(f"{C_IMPL} {test}", shell=True).decode()
	c_end = time.time()

	with open(output, "r") as f:
		real_output = f.read()

	if parse(python_output) != parse(real_output):
		print(f"Python Output Differs from Real Output!")
		print(f"{SEPERATOR}PYTHON{SEPERATOR}\n{python_output}\n{SEPERATOR}{len('PYTHON') * '-'}{SEPERATOR}")
		print(f"{SEPERATOR}REAL{SEPERATOR}\n{python_output}\n{SEPERATOR}{len('REAL') * '-'}{SEPERATOR}")

	if parse(c_output) != parse(real_output):
		print(f"C Output Differs from Real Output!")
		print(f"{SEPERATOR}C{SEPERATOR}\n{python_output}\n{SEPERATOR}{len('C') * '-'}{SEPERATOR}")
		print(f"{SEPERATOR}REAL{SEPERATOR}\n{python_output}\n{SEPERATOR}{len('REAL') * '-'}{SEPERATOR}")

	print(f"Python Runtime was: {python_end - python_start}")
	print(f"C Runtime was: {c_end - c_start}")
