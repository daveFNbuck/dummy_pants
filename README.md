# dummy_pants
For demonstrating a pants/pex bug

pkgutil.walk_packages doesn't do its proper nested traversal in a pex file. We
can demonstrate it with this repo by running bin:load_pkg to display the output
of `pkgutil.walk_packages(mod.__path__, 'mod.')` as follows:

```sh
$ ./pants run bin:load_pkg -q
modules:
  - mod.submod
  - mod.submod.subsubmod
```

we see that mod.submod and mod.submod.subsubmod are both loaded. However, if
we first compile with `./pants binary bin:load_pkg`, then run that we get a
different output:

```sh
$ dist/load_pkg.pex
modules:
  - submod
```

notice that this loses both the nested `subsubmod` and the `mod.` prefix that
`pkgutil.walk_packages(mod.__path__, 'mod.')` is supposed to prepend.
