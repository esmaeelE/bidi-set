# autodir
# vs
# noautodir

output_format = u'\u202B{}\n'.format
with open('a') as fin, open('output', 'w') as fout:
    fout.writelines( output_format(line.strip()) for line in fin )