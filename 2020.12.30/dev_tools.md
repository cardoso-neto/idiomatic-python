
# tools to enhance development

## EditorConfig on VSCode

- `code --install-extension editorconfig.editorconfig`
- Right click on a folder (repo root) on the sidebar > Generate .editorconfig
- Set `trim_trailing_whitespace` and `insert_final_newline` to true.

See ../.editorconfig
and check their website for more tips.

## isort

Sort import automagically.

- `pip install isort`
- `.isort.cfg` file. Should be compatible with black.
There are other files in which you could specify the settings
e.g., pyproject.toml, setup.cfg, tox.ini, .editorconfig
- `isort . --check-only`
- `isort $file_or_folder`

VSCode has it bundled on the Microsoft Python extension:
F1 > Python Refactor: Sort Imports

## black

Code auto-formatting.
- `pip install black`
- `pyproject.toml` file.
- `black $file_or_folder`

VSCode: F1 > Format Document
`"python.formatting.provider": "black",`

Careful: black operates on whole files. If you only want a snippet, save it on a
new file, format it, and copypaste.

## docstrings

PEP 257 told us how to do it.

### docstring generator

`code --install-extension njpwerner.autodocstring`

```json
"autoDocstring.docstringFormat": "sphinx",
"autoDocstring.generateDocstringOnEnter": true,
"autoDocstring.includeExtendedSummary": false,
"autoDocstring.includeName": false,
"autoDocstring.startOnNewLine": true,
"autoDocstring.guessTypes": true,
"autoDocstring.quoteStyle": "\"\"\"",
```
Whenever you type `"""` and press `enter`, it'll auto-create a docstring
template for you.

### docstring linter

`pip install pydocstyle`
`pydocsstyle $file`

`pip install flake8-docstrings`
`flake8 --docstring-convention numpy $file`

## Language server and syntax highlighting

`code --install-extension ms-python.vscode-pylance`

`"python.languageServer": "Pylance",`

`"python.analysis.typeCheckingMode": "basic"`

##

`"vsintellicode.features.python.deepLearning": "enabled",`

# sources:

isort config files:
https://pycqa.github.io/isort/docs/configuration/config_files/

isort intro and multi line output modes examplified:
https://pycqa.github.io/isort/

https://github.com/PyCQA/pydocstyle
