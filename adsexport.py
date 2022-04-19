import datetime
import html
import json
import os
import time

import requests


def get_secrets():
    secrets = {}
    with open("secrets.txt") as fp:
        for line in fp:
            if line.count("=") != 1:
                continue
            k, v = line.strip().split("=")
            secrets[k] = v
    return secrets


def make_adsexport_json() -> None:
    try:
        secrets = get_secrets()
    except FileNotFoundError:
        raise SystemExit(
            "Please create 'secrets.txt' containing ADS_API_TOKEN=...your.ads.api.token..."
        )
    token = secrets["ADS_API_TOKEN"]

    lib_url = 'https://api.adsabs.harvard.edu/v1/biblib/libraries/VoJI-I0hQmeylc72urzhUw'
    headers = {'Authorization': 'Bearer ' + token}
    with requests.get(lib_url, headers=headers) as r:
        lib_json = r.json()
    debugbase = "adsexport-debug-%s-" % datetime.datetime.now().strftime("%Y-%m-%d_%H%m%s")
    with open(debugbase + "library.json", "w") as fp:
        fp.write(json.dumps(lib_json, indent=2))
    bibcodes = lib_json["documents"]
    bigquery_data = "bibcode\n%s" % "\n".join(bibcodes)
    headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'big-query/csv'}
    bigquery_params = {"q":"*:*", "fl": "bibcode,title,author,date,pubdate,pub,issue,volume,doi", "rows":len(bibcodes)}
    bq_url = "https://api.adsabs.harvard.edu/v1/search/bigquery"
    with requests.post(bq_url, params=bigquery_params, headers=headers, data=bigquery_data) as r:
        bq_json = r.json()
    with open(debugbase + "bigquery.json", "w") as fp:
        fp.write(json.dumps(bq_json, indent=2))
    docs = bq_json["response"]["docs"]
    with open("adsexport.json", "w") as fp:
        fp.write(json.dumps(docs, indent=2))


def main(noofpubs=5) -> None:
    try:
        mtime = os.stat("adsexport.json").st_mtime
    except FileNotFoundError:
        rerun_export = True
    else:
        if time.time() - mtime < 300:
            rerun_export = False
        else:
            rerun_export = True
    if rerun_export:
        print("Extract ADS library into adsexport.json...")
        make_adsexport_json()
    else:
        print("Reuse ADS library from adsexport.json")
    with open("adsexport.json") as fp:
        adsexport = json.load(fp)
    adsexport.sort(key=lambda pub: pub["pubdate"])
    adsexport.reverse()
    f = "_includes/publications_ads.html"
    with open(f + "_", "w") as fp:
        fp.write("<ul>\n")
        for pub in adsexport[0:noofpubs]:
            link = "https://ui.adsabs.harvard.edu/abs/%s/abstract" % pub["bibcode"]
            fp.write('<li><a href="%s" target="_blank">\n' % html.escape(link))
            fp.write('%s</a>\n' % html.escape(pub["title"][0]))
            fp.write('<br>\n')
            for i, a in enumerate(pub["author"]):
                if i == 0:
                    fp.write('\n')
                if i >= 4:
                    fp.write(' et al.\n')
                    break
                fp.write('%s ' % html.escape(a.split(',')[1]))
                fp.write('%s' % html.escape(a.split(',')[0]))
                if i < 2:
                    fp.write(', ')
            fp.write('<br>\n')
            fp.write('Published %s\n' % pub["pubdate"][:7])
            fp.write('in %s\n' % pub["pub"])
            fp.write('</li>\n')
        fp.write('</ul>\n')
    os.rename(f + "_", f)
    print("Wrote %s" % f)


if __name__ == "__main__":
    main()
