import os


base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

scree_dir = os.path.join(base_dir, 'outfile\\screenshot')

log_dir = os.path.join(base_dir, 'outfile\\log')

test_case_dir = os.path.join(base_dir, 'testcase')
# print(scree_dir)
# print(log_dir)

