<!-- ©︎ BBQ大好き All Rights Reserved. -->

# BBQ UGC creator documentation

Static, localized documentation for creating, building, testing, and sharing BBQ Player UGC. UI
packages have a dedicated section within the broader creator workflow. The generated site is
configured for `ugc.bbqdaisuki.moe` and contains four complete locales:

- `en` at `/`;
- `ja` at `/ja/`;
- `zhs` at `/zhs/`;
- `zht` at `/zht/`.

## Update a page

1. Edit the English Markdown file under `content/en/`.
2. Increase its `<!-- source-revision: N -->` value.
3. Apply the same change and revision to the matching file under `ja`, `zhs`, and `zht`.
4. Run the build. It fails when a locale, page, or revision is missing.

Navigation labels, locale paths, and the custom domain live in `config/site.yml`. Shared visual
styles live in `assets/stylesheets/extra.css`.

## Build locally

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --requirement requirements.txt
.\.venv\Scripts\python.exe scripts\build_site.py
```

The output is a static `site/` directory. Preview it with:

```powershell
python -m http.server 8765 --directory site
```

Then open `http://127.0.0.1:8765/`.

## Future deployment

Push `main` to GitHub and select **GitHub Actions** as the repository's Pages source. In the Pages
settings, set the custom domain to `ugc.bbqdaisuki.moe`, then point that subdomain's DNS CNAME record
to the repository owner's GitHub Pages hostname. The included workflow builds and deploys only the
static artifact.

The repository-wide public-content check runs before every build and rejects unrelated or private
authoring material.
