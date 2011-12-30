#!/usr/bin/python
# This program converts Pspice netlist to ngspice netlist
import sys
import os.path

def readNetlist(filename):
  """Read Pspice netList"""
# Open file if it exists
  if os.path.exists(filename):
    try:
      f = open(filename)
    except :
      print("Error in opening file")
      sys.exit()
  else:
    print filename + " does not exist"
    sys.exit()
  
# Read the data from file
  data=f.read()
  
# Close the file
  f.close()
  return data.splitlines()

def readParamInfo(data):
  """Read Parameter information and store it into dictionary"""
  param={}
  for eachline in lines:
    eachline=eachline.strip()
    if len(eachline)>1:
      words=eachline.split();
      option=words[0].lower()
      if option=='.param':
        for i in range(1, len(words), 1):
  	  paramList=words[i].split('=')
  	  param[paramList[0]]=paramList[1]
  return param

def preprocessNetlist(lines,param):
  """Preprocess netlist (replace parameters)"""
  netlist=[]
  for eachline in lines:
  # Remove leading and trailing blanks spaces from line 
    eachline=eachline.strip()
  # Remove special character $
    eachline=eachline.replace('$','')
  # Replace parameter with values
    for subParam in eachline.split():
      if '}' in subParam:
        key=subParam.split()[0]
	key=key.strip('{')
	key=key.strip('}')
	if key in param:
	  eachline=eachline.replace('{'+key+'}',param[key])
        else:
	  print "Parameter " + key +" does not exists"
	  value=raw_input('Enter parameter value: ')
	  eachline=eachline.replace('{'+key+'}',value)
   # Convert netlist into lower case letter	
    eachline=eachline.lower()
   # Construct netlist
    if len(eachline)>1:
      if eachline[0]=='+':
	netlist.append(netlist.pop()+eachline.replace('+',' '))
      else:
        netlist.append(eachline) 
 # Copy information line
  infoline=netlist[0]
  netlist.remove(netlist[0])	
  return netlist,infoline

def separateNetlistInfo(netlist):
  optionInfo=[]
  schematicInfo=[]
  
  for eachline in netlist:
    if eachline[0]=='*':
      continue
    elif eachline[0]=='.':
      optionInfo.append(eachline)
    else:
      schematicInfo.append(eachline)
  return optionInfo,schematicInfo

def findCurrent(schematicInfo,outputOption):
  """Find current through component by placing voltage source series with the component"""
  i=0
  for eachline in outputOption:
    words=eachline.split()
    option=words[0]
  # Add voltage sources in series with component to find current 
    if option=="print" or option=="plot":
      words.remove(option)
      updatedline=eachline
      for outputVar in words:
      # Find component name if output variable is current
        if outputVar[0]=='i':
          outputVar=outputVar.strip('i')
          outputVar=outputVar.strip('(')
          compName=outputVar.strip(')')
	 # If component is voltage source, skip
          if compName[0]=='v':
            continue
         # Find the component from the circuit
          for compline in schematicInfo:
            compInfo=compline.split()
            if compInfo[0]==compName:
	    # Construct dummy node 
              dummyNode='dummy_'+str(i)
              i+=1
	    # Break the one node component and place zero value voltage source in between.
              index=schematicInfo.index(compline)
              schematicInfo.remove(compline)
              compline=compline.replace(compInfo[2],dummyNode)
              schematicInfo.insert(index,compline)
              schematicInfo.append('v'+compName+' '+dummyNode+' '+compInfo[2]+' 0')
    # Update option information
          updatedline=updatedline.replace('i('+compName+')','i(v'+compName+')')
      index=outputOption.index(eachline)
      outputOption.remove(eachline)
      outputOption.insert(index,updatedline) 
  return schematicInfo, outputOption

# Accept input file name from user if not provided
if len(sys.argv) != 2:
  filename=raw_input('Enter file name: ')
else:
  filename=sys.argv[1]

# Read the netlist
lines=readNetlist(filename)

# Construct parameter information
param=readParamInfo(lines)

# Replace parameter with values
netlist, infoline=preprocessNetlist(lines,param)

# Separate option and schematic information
optionInfo, schematicInfo=separateNetlistInfo(netlist)

# Find the analysis option
analysisOption=[]
outputOption=[]
initialCondOption=[]
simulatorOption=[]
includeOption=[]
model=[]

for eachline in optionInfo:
  words=eachline.split()
  option=words[0]
  if (option=='.ac' or option=='.dc' or 
      option=='.disto' or option=='.noise' or
      option=='.op' or option=='.pz' or
      option=='.sens' or option=='.tf' or
      option=='.tran'):
    analysisOption.append(eachline+'\n')
  elif (option=='.save' or option=='.print' or 
      option=='.plot' or option=='.four'):
    eachline=eachline.strip('.')
    outputOption.append(eachline+'\n')
  elif (option=='.nodeset' or option=='.ic'):  
    initialCondOption.append(eachline+'\n')
  elif option=='.option':  
    simulatorOption.append(eachline+'\n')
  elif (option=='.include' or option=='.lib'):
    includeOption.append(eachline+'\n')
  elif (option=='.model'):
    model.append(eachline+'\n')
  elif option=='.end':
    break;

# Find the various model library required
modelList=[]
for eachline in schematicInfo:
  words=eachline.split()
  if eachline[0]=='d':
    modelName=words[3]
    if modelName in modelList:
      continue
    modelList.append(modelName)
  elif eachline[0]=='q':
    modelName=words[4]
    if modelName in modelList:
      continue
    modelList.append(modelName)

# Find current through components
schematicInfo,outputOption=findCurrent(schematicInfo,outputOption)

# Add newline in the schematic information
for i in range(len(schematicInfo),0,-1):
  schematicInfo.insert(i,'\n')

outfile=filename+".out"
out=open(outfile,"w")
out.writelines(infoline)
out.writelines('\n')

for modelName in modelList:
  out.writelines('.include '+modelName+'.lib\n')

sections=[simulatorOption, initialCondOption, schematicInfo, analysisOption]
for section in sections:
  if len(section) == 0:
    continue
  else:
   out.writelines('\n') 
   out.writelines(section)

out.writelines('\n* Control Statements \n')
out.writelines('.control\n')
out.writelines('run\n')
out.writelines(outputOption)
out.writelines('.endc\n')
out.writelines('.end\n')

out.close()

