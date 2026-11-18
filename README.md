# qkrwnstj306.github.io

Source of my portfolio, **https://qkrwnstj306.github.io/**.

## How it works

| What | Where |
|:--|:--|
| Profile, news, publications, projects, education, skills | `content.yml` |
| Detail page of a publication / project | `pages/<slug>.md` |
| Images (thumbnails, figures) | `assets/img/`, `assets/img/posts/` |
| Layout and style | `templates/`, `assets/site.css` |
| Build script | `scripts/build.py` |

Pushing to `main` builds the site and deploys it with GitHub Actions (`.github/workflows/pages.yml`).

## Common edits

**Add a news item** — add to the top of `news:` in `content.yml`:

```yaml
- date: 2026.03
  text: Our paper **XYZ** was accepted to **CVPR 2026**.
```

**Add a publication**

1. Put a thumbnail in `assets/img/posts/`.
2. Add an entry to `publications:` in `content.yml` (title, authors, venue, thumbnail, tldr, `page: blog/<slug>`, links).
3. Create `pages/<slug>.md`:

   ```markdown
   ---
   url: blog/<slug>
   tagline: One sentence that sums up the paper
   ---

   ## Context
   ...
   ```

Projects work the same way with `projects:` and `page: proj/<slug>`.

## Preview locally

```bash
pip install -r requirements.txt
python scripts/build.py serve    # http://127.0.0.1:8000
```
