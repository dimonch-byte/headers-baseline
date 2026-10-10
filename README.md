# headers-baseline
One GET to **your own** site, prints which baseline security headers are present (HSTS, nosniff, Referrer-Policy, Permissions-Policy, frame protection, CSP or CSP-Report-Only). stdlib Python, no deps.
```
python3 headers_baseline.py https://your-site.com/          # report
python3 headers_baseline.py https://staging.your-site.com/ --fail   # CI gate
```
Not a pentest or a grade: headers are one layer, and adding CSP blindly can break your site. Start with Report-Only.

*Disclosure: I build [HeaderKit](https://headerkit.adjudi.com/?utm_source=github&utm_medium=readme&utm_campaign=headerkit-intent-w2&utm_content=headers-baseline) ($29), which writes host-specific header baselines for Vercel/Netlify/Cloudflare/nginx. This script is free (MIT) and standalone.*
