# Contributing to telegram bot

<details>
  <summary>Table of Contents</summary>

- [1 Requirements](#1-requirements)
- [2 Github](#2-github)
- [3 Project goals](#3-project-goals)
    * [3.1 Brief description](#3.1-brief-description)
    * [3.2 Function Explorer features](#3.2-function-explorer)
    * [3.3 Bot and core](#3.3-bot-and-core)
    * [3.4 Repository](#3.4-repository)
- [4 Naming](#4-naming)
    * [4.1 Github](#4.1-github)
    * [4.2 Code](#4.2-code)

</details>

<a id="1-requirements"></a>

## 1 Requirements

* `Python 3.10` or greater
* `MiKTeX` as a TeX distribution to display text in TeX format, for example, [MiKTeX](https://miktex.org/download)
  or [TeX Live](https://www.tug.org/texlive/)
* `Pylint` as a static code analysis tool. It is necessary to fix all Pylint warnings. Specific rules for linter are
  prescribed in `.pylintrc`. To can use requirements-dev to install if. Alternatively, type in the terminal:

```shell
pip install pylint
```

<a id="2-github"></a>

## 2 Github

We use feature branch workflow to make working with the repository easier. It means that you should push your changes to
the topic branches and then a make pull request to commit the changes to the main branch. The request must include
description of what was done. The request must be reviewed by code reviewer or team leader, approved and then merged
into main.

<a id="3-project-goals"></a>

## 3 Project goals

<a id="3.1-brief-description"></a>

### 3.1 Brief description

The Telegram bot must analyse the function data (Function Explorer). The interface must be user-friendly. Optional: the
bot must analyse sample data and be able to build functions and charts based on it (Stats Explorer).

<a id="3.2-function-explorer"></a>

### 3.2 Function Explorer features

_with `Sympy` and `Matplotlib` as backend_<br>

1) **Drawing graphs in a single coordinate system**<br>
   The user specifies the functions by comma, semicolon or new line, and has the option of specifying the domain of all
   the functions. It is desirable to add additional possible parameters, e.g. range of the functions, scale, appearance
   of graphs (through configurations). Due to the peculiarities of the graphs it is not possible to implement these
   additional options at once. There is also a need to improve the stability of the plotting process and increase
   performance. This is especially true for implicit functions that take a very long time to render.

- Graph drawing _[DONE]_
- Function domain _[DONE]_
- Function range _[DONE]_
- Aspect ratio _[DONE]_
- Scale
- Appearance, stylesheet
- Performance and stability _[IN PROGRESS ALWAYS]_

2) **Functional analysis**<br>
   We need to create a functional for the study of mathematical functions and organize a convenient interface for
   interaction with it. Information about the study function can be taken from the Internet, for example respected
   source: [Mathprofi](https://vk.com/away.php?to=http%3A%2F%2Fmathprofi.ru%2Fpolnoe_issledovanie_funkcii_i_postroenie_grafika.html&cc_key=) <br><br>

   The main functions are as follows:

- Derivative _[DONE]_
- Domain _[DONE]_
- Range _[DONE]_
- Zeros _[DONE]_
- Axes intersection _[DONE]_
- Periodicity _[DONE]_
- Convexity _[DONE]_
- Concavity _[DONE]_
- Asymptotes (vertical, horizontal and slant) _[DONE]_
- Evenness and oddness _[DONE]_
- Maximum value _[DONE]_
- Minimum value _[DONE]_
- Stationary points _[DONE]_
- Constant sign intervals
- Monotonic intervals

Not all the listed functions are mandatory, some of them may be too complex to implement. In addition, not all
attributes can be found for a particular function. The functionality can be implemented with `Sympy`.

3) Optional: sample analysis and charting _[not important now]_

<a id="3.3-bot-and-core"></a>

### 3.3 Bot and core

1) **Interface** _[IN PROGRESS]_ <br>
   The bot must have a clear system of interaction with the user. For example, through buttons and commands.<br><br>
   A rough set of commands is as follows:

- `Start` To tell the bot about the user. You will be written in database. Use it if bot doesn't answer on your requests
- `Graph` Draw charts mode
- `Analyse` Function analysis mode
- `Examples` Contains examples of commands (functions that is). Can be combined with 'help'.
- `Help`: Help information about commands and bot. Should explain command syntax and tell what's expected of the user
  and what work the bot will do
- `Stats` _[not important now]_
- On `unknown` commands bot should respond adequately
- To `text`, `pictures`, `files` etc. bot should react adequately in any state

2) **Configuration** _[DONE]_ <br>
   I really need a class implemented as a singleton that can parse a json file with settings and apply the changes. In
   case of an error opening or reading the file, exception should be thrown.

3) **Logging** _[DONE]_ <br>
   Every user action should be logged in terminal or file.

<a id="3.4-repository"></a>

### 3.4 Repository

1) **Readme** _[IN PROGRESS]_ <br>
   The following points should be written and formatted in it:

- The main purpose of the bot (what it should ideally do, an abstraction)
- What is implemented
- How to use (essentially, a summary of the help command)
- What is planned to be implemented (TBD) (?)
- Some meme

2) **Requirements** _[DONE]_ <br>
   We need to generate an adequate fact. PyCharm knows how to generate it itself (click on the project, create a new
   file - requirements.txt).

3) **Contributing information file** _[DONE]_ <br>
   I assume the rules are prescribed in CONTRIBUTING.md. It's worth writing naming rules for anything and everything,
   how to commit and push.

<a id="4-naming"></a>

## 4 Naming

<a id="4.1-github"></a>

### 4.1 Github

* `Branch` Dash-naming e.g. _some-exciting-feature_, _another-broken-functionality-fix_
* `Commit` Write a detailed description of what has been done. List the changes point by point. For example:

> _-_ Added "Draw graph" button in GUI\
> _-_ Rocket launching works now\
> _-_ Fixed issues in handling messages in Japanese

<a id="4.2-code"></a>

### 4.2 Code

<table>

  <tr>
    <th>Type</th>
    <th>Naming</th>
  </tr>

  <tr>
    <td>Packages</td>
    <td><code>package_name</code></td>
  </tr>

  <tr>
    <td>Modules</td>
    <td><code>module_name</code></td>
  </tr>

  <tr>
    <td>Classes</td>
    <td><code>ClassName</code></td>
  </tr>

  <tr>
    <td>Exceptions</td>
    <td><code>ExceptionName</code></td>
  </tr>

  <tr>
    <td>Functions</td>
    <td><code>function_name()</code></td>
  </tr>

  <tr>
    <td>Global/Class Constants</td>
    <td><code>GLOBAL_CONSTANT_NAME</code></td>
  </tr>

  <tr>
    <td>Global/Class Variables</td>
    <td><code>global_variable_name</code></td>
  </tr>

  <tr>
    <td>Private Variable</td>
    <td><code>_private_variable</code></td>
  </tr>

  <tr>
    <td>Private Function</td>
    <td><code>_private_function</code></td>
  </tr>

  <tr>
    <td>Instance Variables</td>
    <td><code>instance_variable_name</code></td>
  </tr>

  <tr>
    <td>Function/Method Parameters</td>
    <td><code>function_param_name</code></td>
  </tr>

  <tr>
    <td>Local Variables</td>
    <td><code>local_variable_name</code></td>
  </tr>

  <tr>
    <td>Python</td>
    <td><code>SLOW_CRAP</code></td>
  </tr>

</table>
