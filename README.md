# Star Classification

A tool to organize your starred Github projects. It creats a directory of tagged markdown files that you can add to your [Obsidian⤴](https://obsidian.md/) vault.

## Usage

```
export GITHUB_TOKEN=''
python run.py
```

1. It requires a Github Token to access your user profile. You can generate one in your Github settings.
2. It will create a directory of markdown files based on the template file `output.md`.

## Query

Once you add the directory to your Obsidian vault, you can query these notes:

```
tag:#repo tag:#nlp line:(/(^# )/
```
The above query will show all the project titles containing the tag `repo` and `nlp`.

Or if you are using [obsidian-dataview plugin⤴](https://github.com/blacksmithgu/obsidian-dataview), you can have a nice table with the following query:

```dataview
table title, reference, tags
from #repo and (#nlp or #natural-language-processing)
```

## Contribute
PRs and Issues are welcome!

## Disclaimer
This project is not affiliated with [Obsidian⤴](https://obsidian.md/) or any its plugins.