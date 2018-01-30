import Utils
import sys

def main(args):
    print(
        Utils.showRotations(
            Utils.bwm(args[1])
        )
    )
    print("Last bwm column:", Utils.getLastColumn(args[1]))

if __name__ == '__main__':
    main(sys.argv)
