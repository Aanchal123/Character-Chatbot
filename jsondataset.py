def load_conversations():
  # dictionary of line id to text


  import glob
  
  list_of_paths=glob.glob("E:/Final Yr Poject/archive/*.txt")
  
  #print(list_of_paths)
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
  last_hist = []
  last_candidate = None



  u_list=[{'candidates':['my name is joey'],'history':['what is your name?']},{'candidates':['i am an actor'],'history':['what is your profession?']},{'candidates':['i live in new york city'],'history':['where do you live?']},{'candidates':['chandler, ross, rachel, monica and phoebe'],'history':['who is your best friend?']},{'candidates':['yankees'],'history':['which is your favourite baseball team?']}]

  while (True):
    u=dict()
    diag = list_of_dialogues[s]
    if (diag.split()[0]=="Joey:"):
      p=diag.find(':')
      j_diag=diag[p+2:].lower().replace("."," .").replace('!',' !').replace('?',' ?').replace(',', ' ,')
      u['candidates']=[j_diag]
      
      
      s=s-1
      pdiag = list_of_dialogues[s]
      np=pdiag.find(':')
      new_pdiag=pdiag[np+2:].lower().replace("."," .").replace('!',' !').replace('?',' ?').replace(',', ' ,')
      hist=[]
      
      for h in last_hist:     # {'candidate': ["Joey: C'mon, you're going out with the guy! There's gotta be something wrong with him!"],
        hist.append(h)         # 'history': ["Monica: There's nothing to tell! He's just some guy I work with!"]
     
      
      hist.append(new_pdiag)

      u['history']=hist

      last_hist.append(new_pdiag)
      last_hist.append(j_diag)
      last_candidate=j_diag
      



      s=s+1

      #print(u)
      u_list.append(u)

     
    s=s+1
      
    if (s >=900):
      break
  #print(len(list_of_dialogues))
  return u_list
  
u_list=load_conversations()
#print(u_list)



dataset=[{"personality":['i am joey','my name is joey','i am an actor','i am italian','i love the yankees','i live in new york','i like sandwiches','my profession is acting','i have seven sisters','chandler is my roommate']
          }]
dataset[0]['utterances']=u_list
#print(dataset)




import json

json_dataset = json.dumps(dataset)

with open("sample.json", "w") as outfile:
    outfile.write(json_dataset)
#print(json_dataset)
