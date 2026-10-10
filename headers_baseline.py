#!/usr/bin/env python3
"""headers-baseline: which baseline security headers does your own site send? stdlib only, one GET, no probing."""
import sys, urllib.request, urllib.parse, argparse
CHECKS=[("strict-transport-security","HSTS"),("x-content-type-options","nosniff"),("referrer-policy","Referrer-Policy"),
        ("permissions-policy","Permissions-Policy"),("x-frame-options","clickjacking (or CSP frame-ancestors)"),
        ("content-security-policy","CSP (or Report-Only)")]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("url"); ap.add_argument("--fail",action="store_true",help="exit 1 if anything missing (CI)")
    a=ap.parse_args()
    r=urllib.request.urlopen(urllib.request.Request(a.url,headers={"User-Agent":"headers-baseline/1.0"}),timeout=20)
    h={k.lower():v for k,v in r.headers.items()}; miss=[]
    srv=h.get("server","?"); print(f"{a.url} -> HTTP {r.status}  server={srv}")
    for k,lab in CHECKS:
        ok = k in h or (k=="content-security-policy" and "content-security-policy-report-only" in h) or (k=="x-frame-options" and "frame-ancestors" in h.get("content-security-policy",""))
        print(f"  {'OK ' if ok else 'MISSING'} {lab}"); ok or miss.append(lab)
    if miss:
        print(f"\n{len(miss)} baseline header(s) missing. Not a security audit; headers are one layer.")
        print("Host-specific config (vercel.json / netlify _headers / Cloudflare / nginx), free check first: https://headerkit.adjudi.com/?url="+urllib.parse.quote(a.url,safe="")+"&utm_source=github&utm_medium=cli&utm_campaign=headerkit-intent-w2&utm_content=headers-baseline")
    sys.exit(1 if miss and a.fail else 0)
if __name__=="__main__": main()
