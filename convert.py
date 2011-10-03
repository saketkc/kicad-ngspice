import re
import sys,math

if (len(sys.argv)<= 1):
	print "Incorrect number of parameters"
else :
	filename = sys.argv[1]
	fw = open(filename, 'r')
	output = open ('netlist_output.cir','w')
	for line in fw:

		cc = re.search("\w\d_\w\d_\w\d",line)
		newline=line
		if cc:
			nline = re.split("[_]", line)
			newline = ""
			for i in range(0,len(nline)):
				if (i==0):
					newline=newline+nline[i] + "  "
				else :
					if (i==(len(nline)-1)):
						newline=newline+nline[i].replace("  "," ")
					else:
						newline=newline+nline[i]+" "
		else:
			newline = line
			line = line.replace("  "," ")
			correct_cccs=re.split("_",line)
			split_line = re.split(" ",line)
			try:
				value=int(correct_cccs[1])
				var=split_line[5].split("_")
				newline=split_line[0]+"  " + split_line[1] + " " + split_line[2]  + " " + var[0]+ " " + var[1]
				
			except:
				if (len(split_line)==6):
					if ((split_line[1]=="1")or(split_line[1]=="3")):
						newline=split_line[0] + "  " + "3 " + "4 " + "1 " + "2 " + split_line[5]




		output.write(newline)
	output.close()
	fw.close()
