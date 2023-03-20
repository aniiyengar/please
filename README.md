
# `please`: Ask your computer nicely

`please` is a command-line tool that accepts natural language
input, then uses an LLM to generate + run a Bash script.

### Installation

```bash
pip install git+https://github.com/aniiyengar/please.git
```

### Usage

> **NOTE:** You need to pass your OpenAI API key in your environment as `OPENAI_API_KEY`.

Type your prompt in natural language starting with the word "please".

```bash
$ please <prompt>
```

For example:

```
$ please create a standard gitignore for a python package in the current directory

echo "# Byte-compiled / optimized / DLL files" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.py[cod]" >> .gitignore
echo "*$py.class" >> .gitignore
echo "*.so" >> .gitignore
echo "*.egg-info/" >> .gitignore
echo "dist/" >> .gitignore
echo "build/" >> .gitignore
echo "pip-wheel-metadata/" >> .gitignore
echo "*.egg" >> .gitignore
echo "*.egg-info" >> .gitignore
echo ".eggs/" >> .gitignore


Creating a .gitignore file and adding rules to ignore various types of files and directories.
```

### Features

* If a script fails, `please` pipes stderr back into the LLM
to create a revised script. This is especially useful when a file
or dependency doesn't exist, etc.

* If the prompt isn't specific enough, `please` prompts the user for
extra information, which gets inserted into the script before it's run.

* `please` will print the command(s) being executed, and summarizes
the command(s) of the script in natural language after execution.

### Demo

Some capabilities are shown in [this Twitter thread](https://twitter.com/aniiyengar/status/1637480917194223619).

### Roadmap

I'm open-sourcing this in the interest of collaboration and openness,
but I don't plan on maintaining it a lot. There are a few improvements
that can be made though:

* Better prompts
* Run an LLM locally instead of relying on OpenAI
* Caution the user before making destructive actions
