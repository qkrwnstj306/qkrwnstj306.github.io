#!/usr/bin/env python3
"""Build https://qkrwnstj306.github.io/ from content.yml + pages/*.md into _site/.

    python scripts/build.py          # build into _site/
    python scripts/build.py serve    # build, then serve at http://127.0.0.1:8000
"""
import functools
import http.server
import os
import re
import shutil
import sys

import jinja2
import markdown
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
OUT = '_site'
SITE_URL = 'https://qkrwnstj306.github.io'
ME = 'Junseo Park'

MD_EXT = ['tables', 'fenced_code', 'attr_list', 'md_in_html', 'sane_lists', 'pymdownx.arithmatex']
MD_CFG = {'pymdownx.arithmatex': {'generic': True}}

# Old URLs of the previous site that should keep working.
REDIRECTS = {'about': '/#about', 'blog': '/#publications', 'proj': '/#projects', 'contact': '/#contact'}


def md(text):
    return markdown.markdown(text, extensions=MD_EXT, extension_configs=MD_CFG)


def md_inline(text):
    return re.sub(r'^<p>(.*)</p>$', r'\1', md(text).strip(), flags=re.S)


def bold_me(authors):
    return authors.replace(ME, f'<strong>{ME}</strong>')


def read_page(path):
    text = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', text, re.S)
    return (yaml.safe_load(m.group(1)), m.group(2)) if m else ({}, text)


def write(path, html):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(html)


def build():
    c = yaml.safe_load(open('content.yml', encoding='utf-8'))
    p = c['profile']
    p['bio_html'] = jinja2.utils.markupsafe.Markup(md(p['bio']))
    for n in c['news']:
        n['html'] = jinja2.utils.markupsafe.Markup(md_inline(n['text']))
    for pub in c['publications']:
        pub['authors_html'] = jinja2.utils.markupsafe.Markup(bold_me(pub['authors']))

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'), autoescape=True)
    common = {'p': p, 'site_url': SITE_URL}

    shutil.rmtree(OUT, ignore_errors=True)
    shutil.copytree('assets', f'{OUT}/assets', dirs_exist_ok=True)  # rmtree may leave dirs locked by OneDrive

    home = env.get_template('home.html').render(
        **common, path='/', math=False,
        title=f"{p['name']} — {p['role']}",
        description=f"{p['name']}, {p['role']} at {p['affiliation']}. {p['headline']}",
        og_image=p['photo'],
        highlights=c['highlights'], news=c['news'], publications=c['publications'],
        under_review=c.get('under_review', []),
        under_review_total=sum(u['count'] for u in c.get('under_review', [])),
        projects=c['projects'], education=c['education'], skills=c['skills'])
    write(f'{OUT}/index.html', home)

    # detail pages: pages/<slug>.md, matched to a content.yml entry by `page`
    entries = {e['page']: ('Publication', e) for e in c['publications']}
    entries.update({e['page']: ('Project', e) for e in c['projects']})
    built = set()
    for name in sorted(os.listdir('pages')):
        meta, body = read_page(f'pages/{name}')
        url = meta['url'].strip('/')
        if url not in entries:
            sys.exit(f'pages/{name}: url "{url}" is not referenced by any entry in content.yml')
        kind, item = entries[url]
        authors = item.get('authors') or meta.get('contributors')
        html = env.get_template('page.html').render(
            **common, path=f'/{url}/', math='$' in body,
            title=f"{item['title']} — {p['name']}",
            description=item.get('tldr') or item.get('summary') or meta.get('tagline', ''),
            og_image=item['thumbnail'], kind=kind, item=item,
            authors_html=jinja2.utils.markupsafe.Markup(bold_me(authors)) if authors else '',
            tagline=meta.get('tagline'), body=jinja2.utils.markupsafe.Markup(md(body)))
        write(f'{OUT}/{url}/index.html', html)
        built.add(url)
    missing = set(entries) - built
    if missing:
        sys.exit(f'content.yml links to pages without a pages/*.md file: {sorted(missing)}')

    for old, target in REDIRECTS.items():
        write(f'{OUT}/{old}/index.html',
              f'<!doctype html><meta charset="utf-8"><title>Redirecting…</title>'
              f'<meta http-equiv="refresh" content="0; url={target}"><link rel="canonical" href="{target}">'
              f'<a href="{target}">Continue</a>')

    write(f'{OUT}/404.html', env.from_string(
        '{% extends "base.html" %}{% block main %}<section class="wrap section contact">'
        '<h2>Page not found</h2><p>The page you are looking for does not exist.</p>'
        '<a class="btn btn-primary" href="/">Back to home</a></section>{% endblock %}').render(
        **common, path='/404.html', math=False, title=f"Not found — {p['name']}",
        description=p['headline'], og_image=p['photo']))

    urls = ['/'] + [f'/{u}/' for u in sorted(built)]
    write(f'{OUT}/sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + ''.join(f'  <url><loc>{SITE_URL}{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    write(f'{OUT}/robots.txt', f'User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n')
    print(f'built {len(urls)} pages into {OUT}/')


def serve():
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=OUT)
    print('serving http://127.0.0.1:8000  (Ctrl+C to stop)')
    http.server.ThreadingHTTPServer(('127.0.0.1', 8000), handler).serve_forever()


if __name__ == '__main__':
    build()
    if len(sys.argv) > 1 and sys.argv[1] == 'serve':
        serve()
