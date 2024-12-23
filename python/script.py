import argparse
import sys

def main(args_dict):
    # Print arguments
    print("Arguments:")
    for arg in args_dict.keys():
        print(f"  {arg} = {args_dict[arg]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--input_file", type=str, help="Path to input file")
    args = parser.parse_args()

    print("Starting...")

    args_dict = vars(args) # Make args into a dictionary
    main(args_dict) 

    print("Done!")

    sys.exit(0)
