<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">
    <html lang="en">
      <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title><xsl:value-of select="rss/channel/title"/></title>
        <style>
          :root{color-scheme:light;--ink:#21183d;--muted:#6d6690;--violet:#6c3fc5;--line:#e7e3f3;--paper:#faf9fe}
          *{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 Arial,Helvetica,sans-serif}
          header{padding:48px 24px 36px;background:linear-gradient(135deg,#32136e,#6c3fc5);color:#fff}
          main{max-width:900px;margin:0 auto;padding:28px 20px 60px}.brand{font-size:14px;text-transform:uppercase;letter-spacing:.12em;opacity:.8}
          h1{margin:8px 0 4px;font-size:clamp(28px,5vw,46px);line-height:1.1}header p{margin:0;max-width:650px;color:#eee8ff}
          article{background:#fff;border:1px solid var(--line);border-radius:16px;padding:22px 24px;margin:16px 0;box-shadow:0 8px 24px #2612500d}
          h2{font-size:21px;line-height:1.25;margin:0 0 8px}a{color:var(--violet);font-weight:700;text-decoration:none}a:hover{text-decoration:underline}
          .meta{color:var(--muted);font-size:13px;margin-bottom:10px}.tag{display:inline-block;background:#f0eaff;color:var(--violet);border-radius:999px;padding:2px 9px;margin-left:8px}
          footer{max-width:900px;margin:0 auto;padding:0 20px 36px;color:var(--muted);font-size:13px}
        </style>
      </head>
      <body>
        <header>
          <div class="brand">FinPath RSS feed</div>
          <h1><xsl:value-of select="rss/channel/title"/></h1>
          <p><xsl:value-of select="rss/channel/description"/></p>
        </header>
        <main>
          <xsl:for-each select="rss/channel/item">
            <article>
              <h2><a href="{link}"><xsl:value-of select="title"/></a></h2>
              <div class="meta"><xsl:value-of select="pubDate"/><span class="tag"><xsl:value-of select="category"/></span></div>
              <div><xsl:value-of select="description"/></div>
            </article>
          </xsl:for-each>
        </main>
        <footer>Use this page in a browser, or subscribe to the feed URL in an RSS reader.</footer>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
