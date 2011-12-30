import re
import sys,math
import linecache
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
			line = line.replace("  "," ").strip()
			correct_cccs=re.split("[_]",line)
			split_line = re.split(" ",line)
			print correct_cccs[0]
			try:
				re.match("^\d",correct_cccs[1])
				value=int(correct_cccs[1])
				var=split_line[5].split("_")
				newline=split_line[0]+"  " + split_line[-3] + " " + split_line[-2]  + " " + var[0]+ " " + var[1]+"\n"
			except:
			#else:
				if (len(split_line)==6):
					if ((split_line[1]=="1")or(split_line[1]=="3")):
						newline=split_line[0] + "  " + "3 " + "4 " + "1 " + "2 " + split_line[5] + "\n"
		if (newline.strip()!= ".end"):
			output.write(newline)
	output.close()
	fw.close()
	ask_for_models=raw_input("Enter models(y/n) ? ").strip()
	if (ask_for_models=="y"):
		database_fp=open("database.txt","r")
		i=1
		type_model=[""]
		for line in database_fp:
			if ((line.strip()!="1>>") and (line.strip()!="")):
				print str(i) + str(line) 
				type_model.insert(i-1,str(line.strip()))
				i+=1
			else:
				break
		model_number = input("Enter model numeber :")
		selected_model_name=type_model[model_number-1]
		model_name = raw_input("Enter model name ").strip()

		start_line=1
		database_fp.close()
		database_fp=open("database.txt","r")
		for line in database_fp:
			if(line.strip()==(str(model_number)+">>")):
				break
			else:
				#print line
				start_line+=1
		database_fp.close()
		model_content=""
		start_line+=1
		print start_line
		is_read= True
		while is_read:
			line = linecache.getline("database.txt",start_line)
			start_line+=1
			if (line.strip()==(str(model_number+1)+">>")):
				is_read= False
			else:
				model_content = model_content+line.strip()+"\n"
		model_content=model_content.replace(selected_model_name,model_name)
		 
		print model_content
		with open("netlist_output.cir","a") as myfile:
			myfile.write(model_content)
			myfile.write("\n\n")



	#else:
		#sys.exit(0)
	resp=raw_input("Enter simulation data(y/n)? ")
	if (resp=="y"):
		analysis_type= raw_input("Type of Analysis(AC[a]/Trans[t]): ")
		if (analysis_type=="a"):
			ac_scale=raw_input("Type of Scale : lin/dec/oct: ").strip()
			number_of_data_points=input("Number of Data Points: ")
			start_frequency= raw_input("Enter frequency: ").strip()
			end_frequency = raw_input("Enter end frequency: ").strip()
			appendline_ac_or_trans = ".ac " + str(ac_scale) + " " + str(number_of_data_points)+" " + str(start_frequency) + " " + str(end_frequency) + "\n" 
		elif(analysis_type=="t"):
			print "Enter data input for Transition analysis"
			start_time = raw_input("Start Time: ").strip()
			end_time = raw_input("End Time: ").strip()
			appendline_ac_or_trans = ".trans" + " " + str(start_time) + " " + str(end_time) + "\n"
		else:
			sys.exit(0)
		appendline_end = ".end\n"
		appendline_control=".control\n" + "run\n" + ".endc\n"
		with open("netlist_output.cir","a") as myfile:
			myfile.write("\n")
			myfile.write(appendline_ac_or_trans)
			myfile.write("\n\n")
			myfile.write(appendline_end)
			myfile.write("\n\n\n")
			myfile.write(appendline_control)
	else:
		with open("netlist_output.cir","a") as myfile:
			myfile.write("\n.end\n")
