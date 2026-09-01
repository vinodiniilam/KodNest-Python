class Developer:
    def work(self):
        print("developer is working")
    def attend(self):
        print("attend meeting")
class JDeveloper(Developer):
    def work(self):
        print("Java developer working on the java project")
    def do_project(self):
        print("doing the java project")
class PyDeveloper(Developer):
    def work(self):
        print("Python developer working on the python project")
    def do_project(self):
        print("doing the python project")
dev=Developer()
dev.work()
dev.attend()
javadev=JDeveloper()
javadev.work()
javadev.attend()
javadev.do_project()
pyddev=PyDeveloper()
pyddev.work()
pyddev.attend()
pyddev.do_project()