import csv, itertools, graphviz
filedir = 'C:\\Python27\\'  # put read file here, or pick a different dir and change filedir
readfilename = 'TestyBotMapping.csv'        # copy of readfile included in package, for reference
readfilepath = filedir + readfilename
writefilepath = filedir + 'MappingViz'      # copy of writefile included in package, for reference
maxlength = 100
g1 = graphviz.Digraph(format='png')
with open(readfilepath,'r') as f2:
    readfieldnames = [
        'SOURCE_COLUMN','TARGET_COLUMN','RULE_DESCRIPTION','RULE_EXPRESSION','TARGET_COLUMN_SEQ'
                    ]
    reader = csv.DictReader(f2,fieldnames=readfieldnames)
    for row in itertools.islice(reader,1,maxlength):
        source = row['SOURCE_COLUMN']
        target = row['TARGET_COLUMN']
        transformation = row['RULE_EXPRESSION']
        if source and len(source) <= maxlength and len(transformation) <= maxlength:
            g1.node(source)
            g1.node(target)
            g1.node(transformation)
            g1.edge(source,transformation)
            g1.edge(transformation,target)
g1.graph_attr['rankdir'] = 'LR'
print(g1.source)
filename = g1.render(filename=writefilepath, view=True)