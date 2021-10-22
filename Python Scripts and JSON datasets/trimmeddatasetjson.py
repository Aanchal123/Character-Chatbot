def load():
  # dictionary of line id to text


  import glob
  list_of_paths=glob.glob("E:/Final Yr Poject/archive/*.txt")
 # print(list_of_paths)
  list_of_paths.sort()


  list_of_dialogues= []
  for ep in list_of_paths:
    path_to_file = ep
    fi = open(path_to_file,encoding="utf8")
    for line in fi:
      l=[]
      stripped_line = line.strip()
      if (stripped_line=="" or stripped_line=="\n"):

        pass

      else:
        name=stripped_line.split()
        if(name[0][-1]==":" or name[0]=="End" or stripped_line== "THE END" ):
          #l.append(stripped_line)
          list_of_dialogues.append(stripped_line)
  #print(list_of_dialogues[:15])
  #print(list_of_dialogues[0])

  s=0
# last_hist = []
#  last_candidates = None



  u_list=[{'candidates':['my name is joey'],'history':['what is your name?']},{'candidates':['i am an actor'],'history':['what is your profession?']},{'candidates':['i live in new york city'],'history':['where do you live?']},{'candidates':['chandler, ross, rachel, monica and phoebe'],'history':['who is your best friend?']},{'candidates':['yankees'],'history':['which is your favourite baseball team?']}]
  jd = 1
  while (True):
    
    diag = list_of_dialogues[s]
    if(jd ==1):
      u=dict()
      u['candidates']=[]
      u['history']=[]
      

    if (diag.split()[0] != "Joey:"):
      jd=0
      #print("hiii")
      p=diag.find(':')
      nj_diag=diag[p+2:].lower().replace("."," .").replace('!',' !').replace('?',' ?').replace(',', ' ,')
      u['history'].append(nj_diag)
        
    else:
      jd=1
      po=diag.find(':')
      j_diag=diag[po+2:].lower().replace("."," .").replace('!',' !').replace('?',' ?').replace(',', ' ,')
      u['candidates'].append(j_diag)
        
      #print(u)
      u_list.append(u)
    s=s+1

     

      
    if (s >= 1000):
      break
  #print(len(list_of_dialogues))
  return u_list
  
u_list=load()



dataset=[{"personality":['Joey','I am an actor','I am Italian','I love the Yankees','i live in new york','i like sandwiches','my profession is acting','i have seven sisters','chandler is my roommate']
          }]
dataset[0]['utterances']=u_list

import json

json_dataset = json.dumps(dataset)
#print(json_dataset)

with open("new.json", "w") as outfile:
  outfile.write(json_dataset)

  
