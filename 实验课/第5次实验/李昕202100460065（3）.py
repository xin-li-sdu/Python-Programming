import fileinput
import glob
for line in fileinput.input(glob.glob(r"C:\Users\waldeinsamkeit\Desktop\test*.txt")):
    if fileinput.isfirstline():
        print( '-'*20, 'Reading %s...' % fileinput.filename(), '-'*20)
    print( '#' + str(fileinput.filelineno()) + line.upper());
