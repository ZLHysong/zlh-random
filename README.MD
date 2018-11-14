# Zachery Hysong - Personal Repo

> This repo contains programming and other tech information that I want to save for easy access.
> This repo will also serve as a test repo for ZSH and other shell functionality within Debian, VS Code, Etc.

## Table of Contents
<!-- TOC -->

- [Zachery Hysong - Personal Repo](#zachery-hysong---personal-repo)
    - [Table of Contents](#table-of-contents)
    - [PHP](#php)
    - [Git](#git)
        - [Resources](#resources)
        - [`.gitignore`](#gitignore)
        - [Useful options for `git log --pretty=format`](#useful-options-for-git-log---prettyformat)
        - [Common options to git log](#common-options-to-git-log)
        - [Options to limit the output of git log](#options-to-limit-the-output-of-git-log)
        - [Amending a `git commit`](#amending-a-git-commit)
        - [Git Tags](#git-tags)
            - [Creating Tags](#creating-tags)
            - [Annotated Tags](#annotated-tags)
            - [Lightweight Tags](#lightweight-tags)
            - [Tagging Later](#tagging-later)
            - [Sharing Tags](#sharing-tags)
            - [Deleting Tags](#deleting-tags)

<!-- /TOC -->
## PHP

When checking php errors, we can add `ini_set('display_errors', '1');` to force errors to show.

## Git

### Resources 

> NOTE: Quotes and code below taken from [Pro Git Book (Free)](https://git-scm.com/book/en/v2)
> 
### `.gitignore`

> A repository might have a single .gitignore file in its root directory, which applies recursively to the entire repository. However, it is also possible to have additional .gitignore files in subdirectories. The rules in these nested .gitignore files apply only to the files under the directory where they are located. (The Linux kernel source repository has 206 .gitignore files.)


Code           | Description
---            | ---
`*.a`          | Ignore all .a files
`!lib.a`       | But do track lib.a, even though you're ignoring .a files above
`/TODO`        | Only ignore the TODO file in the current directory, not subdir/TODO
`build/`       | Ignore all files in any directory named build
`doc/*.txt`    | Ignore doc/notes.txt, but not doc/server/arch.txt
`doc/**/*.pdf` | Ignore all .pdf files in the doc/ directory and any of its subdirectories



### Useful options for `git log --pretty=format`

Option   | Description of Output
---      | ---
`%H`     | Commit hash
`%h`     | Abbreviated commit hash
`%T`     | Tree hash
`%t`     | Abbreviated tree hash
`%P`     | Parent hashes
`%p`     | Abbreviated parent hashes
`%an`    | Author name
`%ae`    | Author email
`%ad`    | Author date (format respects the --date=option)
`%ar`    | Author date, relative
`%cn`    | Committer name
`%ce`    | Committer email
`%cd`    | Committer date
`%cr`    | Committer date, relative
`%s`     | Subject

> The author is the person who originally wrote the work, whereas the committer is the person who last applied the work. So, if you send in a patch to a project and one of the core members applies the patch, both of you get credit — you as the author, and the core member as the committer.

### Common options to git log

Option           | Description
---              | ---
`-p`             | Show the patch introduced with each commit.
`--stat`         | Show statistics for files modified in each commit.
`--shortstat`    | Display only the changed/insertions/deletions line from the --stat command.
`--nameonly`     | Show the list of files modified after the commit information.
`--namestatus`   | Show the list of files affected with added/modified/deleted information as well.
`--abbrevcommit` | Show only the first few characters of the SHA-1 checksum instead of all 40.
`--relativedate` | Display the date in a relative format (for example, “2 weeks ago”) instead of using the full date format.
`--graph`        | Display an ASCII graph of the branch and merge history beside the log output.
`--pretty`       | Show commits in an alternate format. Options include oneline, short, full, fuller, and format (where you specify your own format).
`--oneline`      | Shorthand for --pretty=oneline --abbrev-commit used together.

### Options to limit the output of git log

Option              | Description
---                 | ---
`-<n>`              | Show only the last n commits
`--since, --after ` | Limit the commits to those made after the specified date.
`--until, --before` | Limit the commits to those made before the specified date.
`--author`          | Only show commits in which the author entry matches the specified string.
`--committer`       | Only show commits in which the committer entry matches the specified string.
`--grep`            | Only show commits with a commit message containing the string
`-S`                | Only show commits adding or removing code matching the string


### Amending a `git commit`

One of the common undos takes place when you commit too early and possibly forget to add some files, or you mess up your commit message. If you want to redo that commit, make the additional changes you forgot, stage them, and commit again using the --amend option:

```bash
$ git commit --amend
```

This command takes your staging area and uses it for the commit. If you’ve made no changes since your last commit (for instance, you run this command immediately after your previous commit), then your snapshot will look exactly the same, and all you’ll change is your commit message.

The same commit-message editor fires up, but it already contains the message of your previous commit. You can edit the message the same as always, but it overwrites your previous commit. As an example, if you commit and then realize you forgot to stage the changes in a file you wanted to add to this commit, you can do something like this:

```bash
$ git commit -m 'initial commit'
$ git add forgotten_file
$ git commit --amend
```

You end up with a single commit - the second commit replaces the results of the first.

> It’s important to understand that when you’re amending your last commit, you’re not so much fixing it as replacing it entirely with a new, improved commit that pushes the old commit out of the way and puts the new commit in its place. Effectively, it’s as if the previous commit never happened, and it won’t show up in your repository history.  
The obvious value to amending commits is to make minor improvements to your last commit, without cluttering your repository history with commit messages of the form, “Oops, forgot to add a file” or “Darn, fixing a typo in last commit”.

### Git Tags

> NOTE: This section is copied in it's entirety from the [Pro Git](https://git-scm.com/book/en/v2) so I can read over it more later. It will then be pruned to just the necessities.

#### Creating Tags

Git supports two types of tags: *lightweight* and *annotated*.

A lightweight tag is very much like a branch that doesn’t change — it’s just a pointer to a specific commit.

Annotated tags, however, are stored as full objects in the Git database. They’re checksummed; contain the tagger name, email, and date; have a tagging message; and can be signed and verified with GNU Privacy Guard (GPG). It’s generally recommended that you create annotated tags so you can have all this information; but if you want a temporary tag or for some reason don’t want to keep the other information, lightweight tags are available too.

#### Annotated Tags

Creating an annotated tag in Git is simple. The easiest way is to specify `-a` when you run the tag command:

```bash
$ git tag -a v1.4 -m "my version 1.4"
$ git tag
v0.1
v1.3
v1.4
```

The `-m` specifies a tagging message, which is stored with the tag. If you don’t specify a message for an annotated tag, Git launches your editor so you can type it in.

You can see the tag data along with the commit that was tagged by using the `git show` command:

```bash
$ git show v1.4
tag v1.4
Tagger: Ben Straub <ben@straub.cc>
Date: Sat May 3 20:19:12 2014 -0700
my version 1.4
commit ca82a6dff817ec66f44342007202690a93763949
Author: Scott Chacon <schacon@gee-mail.com>
Date: Mon Mar 17 21:52:11 2008 -0700
    changed the version number
```

That shows the tagger information, the date the commit was tagged, and the annotation message before showing the commit information.

#### Lightweight Tags

Another way to tag commits is with a lightweight tag. This is basically the commit checksum stored in a file — no other information is kept. To create a lightweight tag, don’t supply any of the `-a`, `-s`, or `-m` options, just provide a tag name:

```bash
$ git tag v1.4-lw
$ git tag
v0.1
v1.3
v1.4
v1.4-lw
v1.5
```

This time, if you run `git show` on the tag, you don’t see the extra tag information. The command just shows the commit:

```bash
$ git show v1.4-lw
commit ca82a6dff817ec66f44342007202690a93763949
Author: Scott Chacon <schacon@gee-mail.com>
Date: Mon Mar 17 21:52:11 2008 -0700
    changed the version number
```

#### Tagging Later

You can also tag commits after you’ve moved past them. Suppose your commit history looks like this:

```bash
$ git log --pretty=oneline
15027957951b64cf874c3557a0f3547bd83b3ff6 Merge branch 'experiment'
a6b4c97498bd301d84096da251c98a07c7723e65 beginning write support
0d52aaab4479697da7686c15f77a3d64d9165190 one more thing
6d52a271eda8725415634dd79daabbc4d9b6008e Merge branch 'experiment'
0b7434d86859cc7b8c3d5e1dddfed66ff742fcbc added a commit function
4682c3261057305bdd616e23b64b0857d832627b added a todo file
166ae0c4d3f420721acbb115cc33848dfcc2121a started write support
9fceb02d0ae598e95dc970b74767f19372d61af8 updated rakefile
964f16d36dfccde844893cac5b347e7b3d44abbc commit the todo
8a5cbc430f1a9c3d00faaeffd07798508422908a updated readme
```

Now, suppose you forgot to tag the project at v1.2, which was at the “updated rakefile” commit. You can add it after the fact. To tag that commit, you specify the commit checksum (or part of it) at the end of the command:

```bash
$ git tag -a v1.2 9fceb02
```
You can see that you’ve tagged the commit:

```bash
$ git tag
v0.1
v1.2
v1.3
v1.4
v1.4-lw
v1.5

$ git show v1.2
tag v1.2
Tagger: Scott Chacon <schacon@gee-mail.com>
Date:   Mon Feb 9 15:32:16 2009 -0800

version 1.2
commit 9fceb02d0ae598e95dc970b74767f19372d61af8
Author: Magnus Chacon <mchacon@gee-mail.com>
Date:   Sun Apr 27 20:43:35 2008 -0700

    updated rakefile
...
```

#### Sharing Tags

By default, the `git push` command doesn’t transfer tags to remote servers. You will have to explicitly push tags to a shared server after you have created them. This process is just like sharing remote branches — you can run `git push` origin `<tagname>`.

```bash
$ git push origin v1.5
Counting objects: 14, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (12/12), done.
Writing objects: 100% (14/14), 2.05 KiB | 0 bytes/s, done.
Total 14 (delta 3), reused 0 (delta 0)
To git@github.com:schacon/simplegit.git
* [new tag]          v1.5 -> v1.5
```

If you have a lot of tags that you want to push up at once, you can also use the `--tags` option to the `git push` command. This will transfer all of your tags to the remote server that are not already there.

```bash
$ git push origin --tags
Counting objects: 1, done.
Writing objects: 100% (1/1), 160 bytes | 0 bytes/s, done.
Total 1 (delta 0), reused 0 (delta 0)
To git@github.com:schacon/simplegit.git
* [new tag]          v1.4 -> v1.4
* [new tag]          v1.4-lw -> v1.4-lw
```

Now, when someone else clones or pulls from your repository, they will get all your tags as well.

#### Deleting Tags

To delete a tag on your local repository, you can use `git tag -d <tagname>`. For example, we could remove our lightweight tag above as follows:

```bash
$ git tag -d v1.4-lw
Deleted tag 'v1.4-lw' (was e7d5add)
```

Note that this does not remove the tag from any remote servers. In order to update any remotes, you must use `git push <remote> :refs/tags/<tagname>:`

```bash
$ git push origin :refs/tags/v1.4-lw
To /git@github.com:schacon/simplegit.git
- [deleted]          v1.4-lw
```

Checking out Tags

If you want to view the versions of files a tag is pointing to, you can do a git checkout, though this puts your repository in “detached HEAD” state, which has some ill side effects:

```bash
$ git checkout 2.0.0
Note: checking out '2.0.0'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

    git checkout -b <new-branch>

HEAD is now at 99ada87... Merge pull request #89 from schacon/appendix-final

$ git checkout 2.0-beta-0.1
Previous HEAD position was 99ada87... Merge pull request #89 from
schacon/appendix-final
HEAD is now at df3f601... add atlas.json and cover image
```

In “detached HEAD” state, if you make changes and then create a commit, the tag will stay the same, but your new commit won’t belong to any branch and will be unreachable, except by the exact commit hash. Thus, if you need to make changes — say you’re fixing a bug on an older version, for instance — you will generally want to create a branch:

```bash
$ git checkout -b version2 v2.0.0
Switched to a new branch 'version2'
```

If you do this and make a commit, your version2 branch will be slightly different than your `v2.0.0` tag since it will move forward with your new changes, so do be careful.