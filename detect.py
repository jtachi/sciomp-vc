
import pandas

def detect_problems(filename):
    data = pandas.read_table(filename, header=None)
    data.columns = ['chrom','chromStart','chromEnd','name','score','strand','level','signif','score2']
    if data['score2'].min() < 1 and data['score'].min() > 0:
        print 'Suspicious data!'
<<<<<<< HEAD
    elif data.loc[data['chrom'] == 'chrM']['score'].mean() > 50:
=======
    elif data.loc[data['chrom'] == 'chrM']['score'].mean() > 200:
>>>>>>> parent of ab728af... I have made a changes in the files0
        print 'High scores on chrM!'
    else:
        print 'Seems OK!'
        
import glob
filenames = glob.glob('*.bed')
for f in filenames[:3]:
    print f
    detect_problems(f)