# 0x00. AirBnB clone - The console
`Group project` `Python` `OOP`

|**By Guillaume**									       |
|:--											       |
|**Weight:** 5										       |
|Project to be done in teams of 2 people **olumide adeyanju**, **Olumide Micheal** 	       |
|**Ongoing project** - started Aug 1, 2022, must end by Aug 8, 2022			       |
|Checker will be released at Aug 6, 2022 12:00 PM				       	       |
|**Manual QA review must be done** (request it when you are done with the project)	       |
|An auto review will be launched at the deadline    				       	       |

# Concepts
For this project, we are expected to look at these concepts:

- [Python packages](https://alx-intranet.hbtn.io/concepts/66)
- [AirBnB clone](https://alx-intranet.hbtn.io/concepts/74)

![HBNB LOGO](https://camo.githubusercontent.com/dd07bdb5f1d850f43898037ed8f72e1d53af03841b08cabf09303f5902c3509f/68747470733a2f2f692e6962622e636f2f64354e38354e682f68626e622e706e67)

## First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the **AirBnB** clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:
- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

# Resources
**Read or watch:**

- [cmd module](https://docs.python.org/3.8/library/cmd.html)
- **packages** concept page
- [uuid module](https://docs.python.org/3.8/library/uuid.html)
- [datetime](https://docs.python.org/3.8/library/datetime.html)
- [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

