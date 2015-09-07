import argparse

def parse_input():
    parser = argparse.ArgumentParser(prog='Say hallo world')
    parser.add_argument('name', type=str, help='your name')
    args = parser.parse_args()
    return args.name

def get_greetings(name=''):
    return 'Nice to meet you {}!'.format(name) 
    
if __name__ == '__main__':
    name = parse_input()
    print(get_greetings(name))
