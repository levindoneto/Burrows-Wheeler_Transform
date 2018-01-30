import Utils
import sys

def main(args):
    print(
        Utils.showRotations(
            Utils.bwm(args[1])
        )
    )
    ranks, tots = Utils.rankBwt(Utils.getLastColumn(args[1]))
    print (dict(Utils.getLastColumn(args[1]), ranks))
if __name__ == '__main__':
    main(sys.argv)
