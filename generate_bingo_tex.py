import argparse
import random


# read fields from file
def read_fields(filename: str):
    fields = []
    f = open(filename, "r")
    for line in f:
        fields.append(line.rstrip("\n"))

    return fields

def get_args():
    parser = argparse.ArgumentParser(
                    prog='GenerateBingo',
                    description='generate latex code for a bingo sheet')
    parser.add_argument('--fields_file')
    parser.add_argument('--template_file')
    return parser.parse_args()


def main():
    # parse args
    args = get_args()
    
    # read all possible fields
    all_fields = read_fields(args.fields_file)
    
    # randomly sample 25 fields
    subset_fields = random.sample(all_fields, 25)
    
    # generate latex lines
    field_idx = ['A', 'B', 'C', 'D', 'E',]
    commands = ''
    for row in range(5):
        for col in range(5):
            commands += '\\newcommand{\\Node' + field_idx[row] + field_idx[col] + '}{' + subset_fields[row + col * 5] + '}%\n'

    # template latex lines via jinja   
    with open(args.template_file) as f:
        bingo = f.read().replace('{{ commands }}', commands)

    print(bingo)

if __name__ == '__main__':
    main()
