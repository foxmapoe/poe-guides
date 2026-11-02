# Path of Exile Campaign Routes

A community-maintained collection of Path of Exile campaign route and layout guides. Guides live in `_guides/` as Markdown, with images stored in `assets/guides/`.

## Preview locally

Install Ruby and Bundler, then run:

```sh
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve
```

The local Bundler setting keeps gems inside this repository instead of trying to write to Arch's system gem directory. It is stored in `.bundle/` and excluded from Git along with the installed gems.

Open the local address printed by Jekyll. Changes will rebuild as you edit files.

For editing instructions, see [CONTRIBUTING.md](CONTRIBUTING.md). Copy [templates/guide.md](templates/guide.md) to start a guide.
