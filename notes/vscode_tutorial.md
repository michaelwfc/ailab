# Reference:

[tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

# Install python extension in vscode

1. conda install
2. extensions 中搜索 python
3. 使用虚拟环境 右下角

# Setting

新版的 vscode 设置默认为 UI 的设置，而非之前的 json 设置。如果你想复制我上面这段代码进行配置，可以进行下面的修改:
文件>首选项>设置 > 搜索 workbench.settings.editor ，选中 json 即可改成 json 设置,vs 会自动生成 settings.json

```json
{
 "workbench.settings.editor": "json",
 //   "terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe",
 "#terminal.integrated.defaultProfile.windows#": "C:\\Program Files\\Git\\bin\\bash.exe",
 "terminal.integrated.defaultProfile.windows": "Git Bash",
 "terminal.integrated.cwd": "${workspaceFolder}",
 "terminal.integrated.env.windows": {"PYTHONPATH":"${workspaceFolder}\\src"},
//   terminal setting to git bash setting >  terminal.integrated.profiles.windows > settings.json
{
 "terminal.integrated.automationProfile.windows": {
 "GitBash":{
 "path": "C:\\Program Files\\Git\\bin\\bash.exe"
        }
    },

}

 "terminal.integrated.fontSize": 10,
 //主题颜色
 "workbench.colorTheme": "Monokai", // "Visual Studio Dark",
 "python.defaultInterpreterPath": "C:\\Users\\e691464\\Anaconda\\envs\\sec_master\\python.exe",
 "python.envFile": "${workspaceFolder}/dev.env",


 "editor.fontSize": 10,
 "window.zoomLevel": 2,
 "editor.wordWrap": "on",
 "editor.detectIndentation": false,

 "files.associations": {
 "*.vue": "vue",
 "*.wpy": "vue",
 "*.wxml": "html",
 "*.wxss": "css"
  },
 // 重新设定tabsize
 "editor.tabSize": 2,
 //失去焦点后自动保存
 "files.autoSave": "onFocusChange",
 // #值设置为true时，每次保存的时候自动格式化；
 "editor.formatOnSave": false,
 //每120行就显示一条线
 "editor.rulers": [
  ],
 // 在使用搜索功能时，将这些文件夹/文件排除在外
 "search.exclude": {
 "**/node_modules": true,
 "**/bower_components": true,
 "**/target": true,
 "**/logs": true,
  },
 // 这些文件将不会显示在工作空间中
 "files.exclude": {
 "**/.git": true,
 "**/.svn": true,
 "**/.hg": true,
 "**/CVS": true,
 "**/.DS_Store": true,
 "**/*.js": {
 "when": "$(basename).ts" //ts编译后生成的js文件将不会显示在工作空中
      },
 "**/node_modules": true
  }
}
multi-root-workspaces File > Add Folder to Workspace  save to ***.code-workspace in .vscode https://code.visualstudio.com/docs/editor/multi-root-workspaces
{
 "folders": [
        {
 "name":"Project",
 "path": ".."
        },
        {
 "name":"Source",
 "path": "../src"
        }
    ],
}

// show frame of py 左下角 OUTLINE git setting in vs code
// To configure Python to search for modules in the src-folder we alter the default search path. In PyCharm this is done by selecting a source folder. In Visual Studio Code, this is done by setting the PYTHONPATH variable.
// Add source folder to PYTHONPATH
// Modify settings.json to include the source folder “src” in the integrated terminal:
{
 "terminal.integrated.env.osx": {
 "PYTHONPATH": "${env:PYTHONPATH}:${workspaceFolder}/src",
  },
 "terminal.integrated.env.linux": {
 "PYTHONPATH": "${env:PYTHONPATH}:${workspaceFolder}/src",
  },
 "terminal.integrated.env.windows": {
 "PYTHONPATH": "${env:PYTHONPATH};${workspaceFolder}/src",
  }
}
```

PYTHONPATH=${PYTHONPATH}:./src # Use path separator ';' on Windows.

Note that the PYTHONPATH must be set for both the editors’ Python environment and the integrated terminal.
The editors’ Python environment is used by extensions and provides linting and testing functionality.
The integrated terminal is used when debugging to activate a new python environment.
Environment variable
python.envFile Absolute path to a file containing environment variable definitions. "${workspaceFolder}/dev.env"
dev.env
no_proxy=azure.net,windows.net,management.azure.com,documents.azure.com,azmk8s.io,azurecr.io,windowsazure.com,azure-automation.net,database.azure.com,art.it.statestr.com,snowflakecomputing.com

# Shortcuts

[shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)

| command          | decs                         | Note |
| ---------------- | ---------------------------- | ---- |
| Ctrl + `         | show 集成终端                |
| Ctrl+Shift+P     | 格式化代码 vscode 设置成中文 |
| Ctrl+P           | 快速打开最近打开的文件       |
| Ctrl+Shift+N     | 打开新的编辑器窗口           |
| Ctrl+Shift+W     | 关闭编辑器                   |
| Home             | 光标跳转到行头               |
| End              | 光标跳转到行尾               |
| Ctrl + Home      | 跳转到页头                   |
| Ctrl + End       | 跳转到页尾                   |
| Ctrl + Shift + [ | 折叠区域代码                 |
| Ctrl + Shift + ] | 展开区域代码                 |
| Ctrl + /         | 添加关闭行注释               |
| Shift + Alt +A   | 块区域注释                   |

## add shortcuts

1. Open Visual Studio Code.
2. Press CTRL+SHIFT+P.
3. Type: Open keyboard shortcuts (json)
4. Select An editor will appear with keybindings.json file. Place the following JSON in there and save:

```json
[
  {
    "key": "ctrl+shift+u",
    "command": "editor.action.transformToUppercase",
    "when": "editorTextFocus"
  },
  {
    "key": "ctrl+shift+l",
    "command": "editor.action.transformToLowercase",
    "when": "editorTextFocus"
  },
  {
    // Navigate to Top of Call Stack
    "key": "alt+f10",
    "command": "workbench.action.debug.callStackTop"
  }
]
```

Now CTRL+SHIFT+U will capitalise selected text, even if multi line. In the same way, CTRL+SHIFT+L will make selected text lowercase.
These commands are built into VS Code and no extensions are required to make them work.

# 代码模板

1. In vscode, File -> Preferences -> Configure User Snippets. Type python and choose python. A json file will open
2. Copy-paste all or the specific snippets you want in the file and save
3. Ctrl+Shift+P then Reload Window to activate the changes This is the default main snippet:
   https://code.visualstudio.com/docs/editor/userdefinedsnippets#_snippet-syntax
   https://adamtheautomator.com/vs-code-snippets/#Creating_a_Custom_Python_Snippet
   "if(main)": {
   "prefix": "main",
   "body": ["if __name__ == \"__main__\":", " ${1:pass}"],
   "description": "Code snippet for a `if __name__ == \"__main__\": ...` block"
   },
   If you want to change or tweak which text triggers the snippet, modify the prefix field. The prefix field can be a string as shown above or a list if you want more triggers:
   "prefix": ["__main__", "ifmain", "main", "ifm", "if m"],

# Debugging

## launch.json

is the standard name for a file containing debugging configurations. https://code.visualstudio.com/docs/python/python-tutorial#_configure-and-run-the-debugger
关于 VSCode 的 Debug 问题,大家参考一下这个文档,看看有没有帮助: https://code.visualstudio.com/docs/python/debugging
run and debug button > lauch.json lanuch.json 是 debug 相关的配置文件

```json
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: 当前文件",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": false,
      // add the src to PYTHONPATH when run or debug
      "env": { "PYTHONPATH": "${workspaceFolder}${pathSeparator}src" }
    },

    {
      "name": "Python: Current File",
      "type": "python",
      //request: "launch" or "attach": start the debugger on the file specified in program
      "request": "launch",
      //
      "program": "${file}",
      // when debugging tests in VS Code,important to setting when do unit test
      "purpose": ["debug-test"],
      //Specifies how program output is displayed
      "console": "integratedTerminal",
      "justMyCode": false,
      //When set to true, breaks the debugger at the first line of the program being debugged.
      "stopOnEntry": true
      // with the arguments --port 1593 when you start the debugger
      //"args" : ["--port", "1593"]
    },
    {
      "name": "Python: main entry point",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/model/executor.py"
    }
  ]
}
```

## Unit Test

[vscode-testing](https://code.visualstudio.com/docs/python/testing#_intellisense-for-pytest)
https://www.youtube.com/watch?v=ucjRpS7WCPA
https://blog.thenets.org/how-to-create-a-modern-pytest-dev-environment-with-vscode/
conda install pytest

<!-- laungh.json -->

```json
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      // import to setting when do unit test
      "purpose": ["debug-test"],
      "console": "integratedTerminal",
      "justMyCode": false
    }
  ]
}
```

```json
{
  // 单元测试
  "python.testing.autoTestDiscoverOnSaveEnabled": true,
  "python.testing.pytestEnabled": true,
  "python.testing.pytestPath": "C:\\Users\\e691464\\Anaconda\\envs\\sec_master\\Scripts\\pytest.exe",
  "python.testing.pytestArgs": ["--no-cov", "-s"]
}
```

pytest.ini in Project directory
[pytest]
log_cli = true

<!-- supress the DeprecationWarning when debug pytest -->

filterwarnings =
ignore::DeprecationWarning

# 插件

## autoDocstring

函数和方法的注释文档 docstring，其重要性不需要再强调了，安装了 autoDocstring 插件后， 通过快捷键：“ctrl+shift+2”，可以自动生成 Google 或 Numpy 风格的注释文档。 autoDocstring 的配置方法：从“File”菜单->Preferences->Settings，打开“Settings”界面，在搜索栏中键入：“autoDocstring”，根据自己的风格喜好，Docstring 风格，本文选择 numpy 风格 https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring

```json
{
  // 文档注釋工具
  "autoDocstring.docstringFormat": "google",
  "autoDocstring.customTemplatePath": "C:\\Users\\e691464\\AppData\\Roaming\\Code\\User\\google.mustache"
}
```

## pylint

conda install pylint
Python 代码错误检查通常用 pylint ,前提是必须把 settings.json 文件中的"python.linting.enabled"值设为“true”，否则即使安装了这些工具，也起不到代码的错误提醒。

```json
{
  //自动检查代码
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true
  // "python.linting.pylintArgs": [
  //     "--disable=wrong-import-order,wrong-import-position,unused-import,ungrouped-imports,line-too-long,logging-fstring-interpolation"
  // ],
}
```

## utopep8

Python 自动格式化代码通常用

````json
{
 "[python]": {
 "editor.defaultFormatter": "ms-python.autopep8",
 "editor.formatOnSave": true
  }
  }

## GitLens

## koroFileHeader
自动添加 头部注释 和 函数注释 的插件。支持自定义内容，需要在 settings.json 中进行自定义配置。

## Better Comments
这个插件通过不同的彩色把不同功能的注释信息区分开来。能区分的功能有：Alerts、Queries、TODOs、Highlights和用户自定义，如下图所示。
Better Comments的使用方法：Better Comments安装好后，"!"表示警告、"?"表示询问，"TODOs"表示待办事项，"*"表示高亮内容
## vscode-icons
这是一个美化VS Code图标的插件，提升在VS Code中开发的美好感受。安装前和安装后的对比如下图所示。 Kite
Python自动代码补全工具。从Kite官网中下载Kite安装文件，按提示安装完毕即可使用。例如，最常用的语句，import numpy as np, 只需要键入import n，就能自动补全了，大大提高开发效率。
## AZ AL Dev Tools/AL Code Outline
用来梳理代码结构的插件，安装完后在文件图标里就会多出一个 AL OUTLINE 的选项。 Add TODO highlight add extension to .vscode/extensions.json

```json
{"recommendations": [
 "gruntfuggly.todo-tree",
 "wayou.vscode-todo-highlight"
  ],
}
add to settings.json {
"todohighlight.isEnable": true,
 "todohighlight.isCaseSensitive": true,
 "todohighlight.keywords": [
 "DEBUG:",
 "REVIEW:",
        {
 "text": "NOTE:",
 "color": "#ff0000",
 "backgroundColor": "yellow",
 "overviewRulerColor": "grey"
        },
        {
 "text": "HACK:",
 "color": "#000",
 "isWholeLine": false,
        },
        {
 "text": "TODO:",
 "color": "red",
 "border": "1px solid red",
 "borderRadius": "2px", //NOTE: using borderRadius along with `border` or you will see nothing change
 "backgroundColor": "rgba(0,0,0,.2)",
 //other styling properties goes here ...
        }
    ],
 "todohighlight.keywordsPattern": "TODO:|FIXME:)", //highlight `TODO:`,`FIXME:` or content between parentheses
 "todohighlight.defaultStyle": {
 "color": "red",
 "backgroundColor": "#ffab00",
 "overviewRulerColor": "#ffab00",
 "cursor": "pointer",
 "border": "1px solid #eee",
 "borderRadius": "2px",
 "isWholeLine": true,
 //other styling properties goes here ...
    },
 "todohighlight.include": [
 "**/*.js",
 "**/*.jsx",
 "**/*.ts",
 "**/*.tsx",
 "**/*.html",
 "**/*.php",
 "**/*.css",
 "**/*.scss",
 "**/*.py",
 "**/*.c",
    ],
 "todohighlight.exclude": [
 "**/node_modules/**",
 "**/bower_components/**",
 "**/dist/**",
 "**/build/**",
 "**/.vscode/**",
 "**/.github/**",
 "**/_output/**",
 "**/*.min.*",
 "**/*.map",
 "**/.next/**"
    ],
 "todohighlight.maxFilesForSearch": 5120,
 "todohighlight.toggleURI": false
}
````

## ESLint

## Prettier

javascript 代码检语法测工具，可以配置每次保存时格式化 js● 每次保存时只格式化部分代码，需要连续按住 Ctrl+S 多次才能格式化完成
Code formatter ● 只关注格式化，并不具有 eslint 检查语法等能力， ● 支持 JavaScript · Flow · TypeScript · CSS · SCSS · Less · JSX · Vue · GraphQL · JSON · Markdown
https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight
