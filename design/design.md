# Design for AutoPy App @Mova801 (early stage dev - 2022.06.28)

[github]: ../app/src/icons/github.png "GitHub link"

!["Author's GitHub"][github]

- Authors: [Mova](https://github.com/Mova801)

___

- [Design for AutoPy App @Mova801 (early stage dev - 2022.06.28)](#design-for-autopy-app-mova801-early-stage-dev---20220628)
  - [1. About](#1-about)
  - [2. User Interface](#2-user-interface)
  - [3. Technical Specification](#3-technical-specification)
  - [4. Testing and Security (WIP)](#4-testing-and-security-wip)
  - [5. Deployment](#5-deployment)
  - [6. Planning](#6-planning)
  - [7. Broader Context](#7-broader-context)

___

## 1. About  

- What is the software application or feature?
  - AutoPy is an application that
- Who’s it intended for?
  - The main purpose of AutoPy is to generate executables from python files.
- What problem does the software solve?
  - Simplify the process of creating executables which may be frustrating for a beginner or an employee which has other work to do.
- How is it going to work?
  - You select the files needed (the app checks them) and then generate the file.
- What are the main concepts that are involved and how are they related?
  - Reading files from memory, external libraries.
  
___

## 2. User Interface

- What are the main user stories (happy flows + alternative flows)?
  - . . .

___

## 3. Technical Specification

- What technical details need developers to know to develop the software or new feature?
  - Python3 general knowledge and the following:
    - Basic UI design and development.
    - Event handling.
    - File handling.
    - Executable generation concepts.
- Are there new tables to add to the database? What fields?
  - There is currently no DB type involved in the project.
- How will the software technically work? Are there particular algorithms or libraries that are important?
  - There is no particular algorithm involved, there's anyway a python3 library called pyinstaller. This is used to finally generate the executables.
  
- What will be the overall design? Which classes are needed? What design patterns are used to
model the concepts and relationships?
  - Class needed:
    - PyInstaller
    - Configuration
    - EventHandler
  - Design patterns:
    - . . .
- What third-party software is needed to build the software or feature?
  - Any kind of IDE (currently used [Visual Studio Code](https://code.visualstudio.com))

___

## 4. Testing and Security (WIP)

- Are there specific coverage goals for the unit tests?
  - . . .
- What kinds of tests are needed (unit, regression, end-to-end, etc)?
  - . . .

___

## 5. Deployment

- Are there any architectural or DevOps changes needed (e.g. adding an extra microservice,
changes in deployment pipelines, adding secrets to services)?
  - No changes needed at the moments.
- Are there any migration scripts that need to be written?
  - Not clear at the moment (EARLY PROJECT STAGE - 28/06/2022)

___

## 6. Planning

- How much time will developing the software or feature cost?
- What are the steps and how much time does step take?
- What are the developmental milestones and in what order?
- What are the main risk factors and are there any alternative routes to take if you find out
something isn’t feasible?
- What parts are absolutely required, and what parts can optionally be done at a later stage? (i.e. the Definition of Done)

___

## 7. Broader Context

- What are limitations of the current design?
- What are possible extensions to think about for the future?
- Any other considerations?

___
