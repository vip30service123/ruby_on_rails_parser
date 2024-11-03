# ruby_on_rails_parser

# Tasks
Create data (dummy_project), should cover these cases:
- V1::ClassName
- Module -> ClassName
- Class in Class (super urgly, I don't want to cover this)
- Module ref module
Parse code
- Parse from tree
- Find parents
Parse all codes:
- /app
- /db
- /lib


# Stage and expected output
### Parse code
Logics:
    Parse code

Output:
    Class
        Full name
        Code
        Start code, end code
        Start line
    Function
        Name
        Called Classes
        Code
        Start code, end code
        Start line
    Module
        Full name
        Extend module
        Code
        Start code, end code
        Start line
Example:

### Find Parents and create full path
Logics:
    Find Parent

Output:
    Class
    Function
    Module

Example:

### Parse References
Logics
    /app
        Search in other place using it's post name (like controller or service)
        Search in its folder (if that file is a service, search in service first)
        Search in /model (I dunno if only controller use this folder or not)
    /db
        Use t.reference in code
    /lib
        No idea

Output:
    Class
    Function
    Module

Example:

### Change into Jedi like

# Questions
How many files that have inner class?
Do method only child "assignment"