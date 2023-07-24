# positional args
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('Staff_Number')
parser.add_argument('Name')
parser.add_argument('Engineering_Branch')
parser.add_argument('AIR')
parser.add_argument('Age')


args = parser.parse_args()
print(f'My name is {args.Name} and I am {args.Age} years old')
print(f'My Staff Number is {args.Staff_Number} and I had my BE in {args.Engineering_Branch} branch')
print(f'My All India Rank is {args.AIR} ')
