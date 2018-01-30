import Utils
import sys

def main(args):
    print("BWT Matrix:")
    print(
        Utils.showRotations(
            Utils.bwm(args[1])
        )
    )
    ranks, tots = Utils.rankBwt(Utils.getLastColumn(args[1]))
    #print (map(Utils.getLastColumn(args[1]), ranks))
    print ("\n", Utils.firstColumn(tots))
    print("\nInput:", Utils.reverseBwt(Utils.getLastColumn(args[1])))
    
if __name__ == '__main__':
    main(sys.argv)
