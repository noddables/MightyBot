import csv, sys
filedir = 'C:\\Python27\\'  # put read file here, or pick a different dir and change filedir
readfilename = 'TestyBotMapping'   # copy of readfile included in package, for reference
readfilepath = filedir + readfilename + '.csv'  
readfieldnames = [
        'SOURCE_COLUMN','TARGET_COLUMN','RULE_DESCRIPTION','RULE_EXPRESSION','TARGET_COLUMN_SEQ'
                    ]
consoleprint = sys.stdout
def test_nulls(tgt):
            print ', sum(case when tgt.' + tgt[tgt.rindex('.')+1:] + ' is null then 1 else 0 end) as ' + tgt[tgt.rindex('.')+1:] + '_pass_count'
            print ', sum(case when tgt.' + tgt[tgt.rindex('.')+1:] + ' is null then 0 else 1 end) as ' + tgt[tgt.rindex('.')+1:] + '_fail_count\n--'
def test_straight_moves(src,tgt):
            print ', sum(case when src.' + src[src.rindex('.')+1:] + ' = tgt.' + tgt[tgt.rindex('.')+1:] + ' then 1 else 0 end) as ' + tgt[tgt.rindex('.')+1:] + '_pass_count'
            print ', sum(case when src.' + src[src.rindex('.')+1:] + ' = tgt.' + tgt[tgt.rindex('.')+1:] + ' then 0 else 1 end) as ' + tgt[tgt.rindex('.')+1:] + '_fail_count\n--'
def test_hardcodes(tgt,xfm):
            print ', sum(case when tgt.' + tgt[tgt.rindex('.')+1:] + ' = ' + xfm[xfm.index("'"):] + ' then 1 else 0 end) as ' + tgt[tgt.rindex('.')+1:] + '_pass_count'
            print ', sum(case when tgt.' + tgt[tgt.rindex('.')+1:] + ' = ' + xfm[xfm.index("'"):] + ' then 0 else 1 end) as ' + tgt[tgt.rindex('.')+1:] + '_fail_count\n--'
def test_conversions(src,tgt,xfm):
            print ', sum(case when cast(src.' + src[src.rindex('.')+1:] + ' as ' + xfm[xfm.rindex(' ')+1:] + ') = tgt.' + tgt[tgt.rindex('.')+1:] + ' then 1 else 0 end) as ' + tgt[tgt.rindex('.')+1:] + '_pass_count'
            print ', sum(case when cast(src.' + src[src.rindex('.')+1:] + ' as ' + xfm[xfm.rindex(' ')+1:] + ') = tgt.' + tgt[tgt.rindex('.')+1:] + ' then 0 else 1 end) as ' + tgt[tgt.rindex('.')+1:] + '_fail_count\n--'
with open(readfilepath,'r') as f1:
    reader = csv.DictReader(f1,fieldnames=readfieldnames)
    writefilepath = filedir + readfilename + '_conversions_tests.sql'
    sys.stdout = open(writefilepath,'w')
    print '--start datatype conversion tests\nSELECT COUNT(*) AS total_rows\n--'
    for row in reader:
        source = row['SOURCE_COLUMN']
        target = row['TARGET_COLUMN']
        transformation = row['RULE_DESCRIPTION']
        #transformation = row['Rule Expression']
        transformation = transformation.lower()
        if transformation.startswith("convert to "):
            test_conversions(source,target,transformation)
    print 'FROM ' + target[:target.rindex('.')] + ' tgt \n--\n--'
    print  'JOIN ' + target[:target.rindex('.')] + ' tgt ON src.load_id = tgt.load_id\n--replace pseudocode w/real joins\nAND tgt.keys = src.keys\n--'
    print 'WHERE tgt.LOAD_ID = :LOAD_ID;\n--stop datatype conversion tests\n--\n--'
with open(readfilepath,'r') as f2:
    reader = csv.DictReader(f2,fieldnames=readfieldnames)
    writefilepath = filedir + readfilename + '_nulls_tests.sql'
    sys.stdout = open(writefilepath,'w')
    print '--start nulls tests\nSELECT COUNT(*) AS total_rows\n--'
    for row in reader: 
        source = row['SOURCE_COLUMN']
        target = row['TARGET_COLUMN']
        transformation = row['RULE_DESCRIPTION']
        #transformation = row['Rule Expression']
        transformation = transformation.lower()
        if transformation.startswith('set to null'):
            test_nulls(target)
    print 'FROM ' + target[:target.rindex('.')] + ' tgt '
    print 'WHERE tgt.LOAD_ID = :LOAD_ID;\n--stop nulls tests\n--\n--'
#stop nulls tests
#start straight moves tests
with open(readfilepath,'r') as f3:
    reader = csv.DictReader(f3,fieldnames=readfieldnames)
    writefilepath = filedir + readfilename + '_straight_moves_tests.sql'
    sys.stdout = open(writefilepath,'w')
    print '--start straight moves tests\nSELECT COUNT(*) AS total_rows\n--'
    for row in reader: 
        source = row['SOURCE_COLUMN']
        target = row['TARGET_COLUMN']
        transformation = row['RULE_DESCRIPTION']
        #transformation = row['Rule Expression']
        transformation = transformation.lower()
        if transformation.startswith('straight move'):
            test_straight_moves(source,target)
    print 'FROM ' + source + ' src'
    print 'JOIN ' + target[:target.rindex('.')] + ' tgt ON src.load_id = tgt.load_id\n--replace pseudocode w/real joins\nAND tgt.keys = src.keys'
    print 'WHERE tgt.LOAD_ID = :LOAD_ID;\n--stop straight moves tests\n--\n--'
#stop straight moves tests
#start hardcoded tests
with open(readfilepath,'r') as f4:
    reader = csv.DictReader(f4,fieldnames=readfieldnames)
    writefilepath = filedir + readfilename + '_hardcoded_tests.sql'
    sys.stdout = open(writefilepath,'w')
    print '--start hardcoded tests\nSELECT COUNT(*) AS total_rows\n--'
    for row in reader:
        source = row['SOURCE_COLUMN']
        target = row['TARGET_COLUMN']
        transformation = row['RULE_DESCRIPTION']
        #transformation = row['Rule Expression']
        transformation = transformation.lower()
        if transformation.startswith("set to \'") and "null" not in transformation:
            test_hardcodes(target,transformation)
    print 'FROM ' + target[:target.rindex('.')] + ' tgt \n--\nWHERE tgt.LOAD_ID = :LOAD_ID;\n--stop hardcoded tests\n--\n--'
#stop hardcoded tests
sys.stdout = consoleprint
print "\n\nFinished!\n\nCheck your file directory for automated tests!"