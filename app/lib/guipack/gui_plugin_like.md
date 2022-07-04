# GUI PLUGIN STRUCTURE

`GUI` `python3.10`

---

## GUI Package Structure

```HTML
gui_package
├── __init__.py
├── loader.py
├── modules.json
└── modules
    ├── __init__.py
    ├── module1
    |   ├── __init__.py
    |   ├── module1.py
    |   └── support_functions.py
    ├── module2
    |   ├── __init__.py
    |   ├── module2.py
    |   └── support_functions.py
    └── ...
```

`__init__.py:` initialize the package
`loader.py:` load all the modules
`modules:` contains all the modules

## modules.json Structure

```json
{
  "plugins": [],
  "modules": [
    {
      "__name__": "",
      "__builder__": "",
      "__dirname__": ""
    },
    {
      "__name__": "",
      "__builder__": "",
      "__dirname__": ""
    }
  ]
}
```

`__name__:` name of the module
`__builder__:` indicates the builder function (main function)
`__dirname__:` path to the module
