fin = open("config.txt", "rt")
# Output file to write the result to
fout = open("C:\ebyn\BTP.bat", "wt")
# For each line in the input file
for line in fin:
	# Read replace the string and write to output file
	fout.write(line.replace('C:\\j2sdk1.4.2_08\\bin\\', ''))
# Close input and output files
fin.close()
fout.close()
