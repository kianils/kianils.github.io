# Local Jekyll setup

This site requires **Ruby 3.3+** (GitHub Pages and gems like `ffi` need it). The built-in Mac Ruby (2.6) is too old.

## 1. Install Ruby 3.3.10

**Option A: rbenv (recommended on Mac)**

```bash
# Install rbenv + ruby-build (if needed)
brew install rbenv ruby-build

# Install Ruby 3.3.10 and use it in this project
# On Apple Silicon, YJIT often causes build failures; disable it:
RUBY_CONFIGURE_OPTS="--disable-yjit" rbenv install 3.3.10
rbenv local 3.3.10

# Make rbenv active in this shell (required before bundle/jekyll):
eval "$(rbenv init -)"

# Optional: add to ~/.zshrc so it runs in every new terminal:
# echo 'eval "$(rbenv init -)"' >> ~/.zshrc
```

**Option B: Homebrew Ruby**

```bash
brew install ruby
# Add Homebrew Ruby to your PATH (see `brew info ruby`).
# Then ensure you're using it: `which ruby` → /opt/homebrew/opt/ruby/...
```

## 2. Use rbenv’s Ruby (important)

If you use rbenv, your shell must load it **before** running bundle/jekyll:

```bash
eval "$(rbenv init -)"
```

Then check you’re on 3.3.x:

```bash
ruby -v    # should show 3.3.10, not 2.6.x
which ruby # should be ~/.rbenv/shims/ruby, not /usr/bin/ruby
```

If you still see 2.6, add `eval "$(rbenv init -)"` to `~/.zshrc`, **above** any conda initialization, then open a new terminal.

## 3. Install gems and run Jekyll

```bash
cd /path/to/kianils.github.io   # your repo path
bundle install
bundle exec jekyll serve
```

Open http://localhost:4000.

## 4. Fetch GitHub repos (contributions section)

The “GitHub contributions” block on the CS Projects page reads from `_data/github_repos.json`. To populate it **locally**:

```bash
./bin/fetch-repos
```

Then restart Jekyll (or let it regenerate). Uses **public** repos only. For **private** repos:

```bash
GH_PAT=ghp_yourToken ./bin/fetch-repos
```

Optional: `GITHUB_USERNAME=youruser ./bin/fetch-repos` if different from `kianils`.

## Tokens (optional)

### Jekyll / GitHub Metadata (`JEKYLL_GITHUB_TOKEN`)

Removes the “No GitHub API authentication could be found” warning and lets the theme use GitHub API data.

**Where to add it:** as an **environment variable** when you run Jekyll. Never put the token in `_config.yml` or commit it.

**Option A – one-off when starting the server:**

```bash
JEKYLL_GITHUB_TOKEN=ghp_yourTokenHere bundle exec jekyll serve
```

**Option B – export in the same terminal, then run Jekyll:**

```bash
export JEKYLL_GITHUB_TOKEN=ghp_yourTokenHere
bundle exec jekyll serve
```

**Option C – in your shell profile (e.g. `~/.zshrc`):**

```bash
export JEKYLL_GITHUB_TOKEN=ghp_yourTokenHere
```

Restart the terminal, then run `bundle exec jekyll serve` as usual. Don’t commit `~/.zshrc` if it contains the token.

Create a token at [GitHub → Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens). For public repos only, no scope is needed; for private repo metadata, use the `repo` scope.

---

### GitHub Contributions / private repos (`GH_PAT`)

Used by the **Fetch GitHub repos** workflow to include **private** repos in the “GitHub contributions” section.

**Where to add it:** as a **GitHub Actions secret** in your repo.

1. Open your repo on GitHub → **Settings** → **Secrets and variables** → **Actions**.
2. Click **New repository secret**.
3. Name: `GH_PAT`, Value: your Personal Access Token (scope `repo`).
4. Save. The workflow will use it automatically on the next run.

## Troubleshooting

- **`ffi requires ruby version >= 3.0`** or **`bundler: command not found: jekyll`** → You’re still on system Ruby 2.6. Run `eval "$(rbenv init -)"`, then `ruby -v`. Only after it shows 3.3.10, run `bundle install` and `bundle exec jekyll serve`.
- **`(base)` in prompt** → Conda can override PATH. Run `conda deactivate`, then `eval "$(rbenv init -)"`, then retry.
