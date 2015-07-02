from Cheetah.Template import Template
import yaml

data = yaml.load(open("modules.yml", "r"))
 
modulerefs = []
modulep2repos = []

for name, info in data.items():
    print "Generating for " + name

    deps = info.get("dependencies", [])
    repositories = []
    repositories.append("${" + name + ".p2repo.url}") # not sure why a module needs itself as dependency. dgolovin ?
    for d in deps:
        repositories.append("${" + d + ".p2repo.url}")
        if d not in data:
            print "dependency " + d + " not available."

    modulename = info.get("module", "jbosstools-" + name)
    modulerefs.append(modulename + ".setup#/")
    if info.get("type", "eclipse") == "eclipse":
    	modulep2repos.append(
    	     { "modulename": name, 
    	       "modulep2repo" : info.get("p2repo", "${snapshot.url.prefix}/" + modulename + "_${scope.project.stream.name}/latest/all/repo/")
    	     }) 
    
    t = Template(file="module-setup.tmpl", searchList =
             [
                 { "modulename" : modulename,
                   "modulelabel" : modulename,
                   "modulesimplename" : name,
                   "modulegiturl" : info.get('giturl', "https://github.com/jbosstools/" + modulename + ".git"),
                   "moduledescription" : info.get("description", modulename),
                   "modulegitlocation" : "${git.clone." + name + ".location}",
                   "repositories" : repositories,
                   "type" : info.get("type", "eclipse")
                 }
             ])
    out = open("setup/" + modulename + ".setup", "w")
    out.write(str(t))
    out.close()

print "Generating jbosstools.setup"
t = Template(file="jbosstools.setup.tmpl", searchList = [
     { "moduleref": modulerefs,
       "modulep2repo": modulep2repos }
  ])
out = open("setup/jbosstools.setup", "w")
out.write(str(t))
out.close()

