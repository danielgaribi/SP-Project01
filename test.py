import subprocess

TESTS = {
    './prog 3 600 < tests/input_1.txt': 'tests/output_1.txt',
    'python3 kmeans.py 3 600 < tests/input_1.txt': 'tests/output_1.txt',
    './prog 7 < tests/input_2.txt': 'tests/output_2.txt',
    'python3 kmeans.py 7 < tests/input_2.txt': 'tests/output_2.txt',
    './prog 15 300 < tests/input_3.txt': 'tests/output_3.txt',
    'python3 kmeans.py 15 300 < tests/input_3.txt': 'tests/output_3.txt'
}


def _run_process(cmd):
    print('> Running \'{}\'... '.format(cmd), end='')
    proc = subprocess.run(cmd, shell=True, capture_output=True)
    print('done')

    if proc.returncode != 0:
        raise RuntimeError('Invalid return code for command line \'{}\': {}'.format(
            cmd, proc.returncode))
    return proc.stdout.decode('utf8')


def _read_file(path):
    with open(path, 'r') as fd:
        return fd.read()


def main():
    success = True
    for cmd, expected_output_file in TESTS.items():
        output = _run_process(cmd)
        expected_output = _read_file(expected_output_file)
        if output != expected_output:
            success = False
            print('\nMismatching outputs for command line \'{}\':'.format(cmd))
            print('Expected:\n{}'.format(expected_output))
            print('Got:\n{}'.format(output))
    print('>>> {} <<<'.format('Success' if success else 'Failure'))


if __name__ == '__main__':
    main()
