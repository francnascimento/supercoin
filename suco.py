import argparse
import Node

parser = argparse.ArgumentParser(description="SuperCoin CLI")

parser.add_argument("--init", help="Initialize de SuperCoin CLI. Requires one argument, which is going to be your address.")
parser.add_argument("-t", "--transaction", help="-t VALUE ADDRESS", nargs=2)

args = parser.parse_args()

if __name__ == "__main__":
    if args.init:
        node = Node.Node(address=args.init)
        node.initPeer()
    
    