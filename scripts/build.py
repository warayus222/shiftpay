#!/usr/bin/env python3
"""Wrap src/page.html (a bare fragment, also what is published as the artifact)
into a full standalone document -> index.html."""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
frag = (root / "src" / "page.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0b4f52">
<meta name="color-scheme" content="light dark">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="ตารางเวร">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/svg+xml" href="icons/icon.svg">
<link rel="icon" type="image/png" sizes="64x64" href="icons/favicon.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
"""
# the fragment's own <title>/<meta>/<link>/<style>/<script> go into <head> as-is; body markup follows
i = frag.index("<header")
top, body = frag[:i], frag[i:]
html = head + top + "</head>\n<body>\n" + body.rstrip() + "\n</body>\n</html>\n"
(root / "index.html").write_text(html, encoding="utf-8")
print("wrote index.html", len(html), "bytes")
