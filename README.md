# Path of Exile Campaign Routes

A community-maintained collection of Path of Exile campaign route and layout guides. Guides live in `_guides/` as Markdown, with images stored in `assets/guides/`.

## Preview locally

Install Ruby and Bundler, then run:

```sh
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve
```

Open the local address printed by Jekyll. Changes will rebuild as you edit files.

### Windows setup

1. Install Git for Windows if it is not already installed.
2. Download and install the latest **Ruby+Devkit x64** package from [RubyInstaller](https://rubyinstaller.org/downloads/). When the installer asks to run `ridk install`, choose option `3` to install the MSYS2 and development toolchain.
3. Open PowerShell in the repository folder and install Bundler:

   ```powershell
   gem install bundler
   ```

4. Install the project dependencies and start the preview:

   ```powershell
   bundle config set --local path vendor/bundle
   bundle install
   bundle exec jekyll serve
   ```

5. Open the local address printed in PowerShell. Leave that window running while you edit; the preview rebuilds when files change.

For editing instructions, see [CONTRIBUTING.md](CONTRIBUTING.md). Copy [templates/guide.md](templates/guide.md) to start a guide.

## Publishing

The site builds and deploys from the `main` branch with GitHub Actions. In the repository settings, open **Pages → Build and deployment** and set **Source** to **GitHub Actions**. The workflow builds with the dependencies in `Gemfile.lock` and publishes the generated site; the custom domain remains configured separately under **Pages**.
