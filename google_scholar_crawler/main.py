import json
import os
import sys
from datetime import datetime, timezone
from urllib.parse import parse_qs, urlparse

import requests
from bs4 import BeautifulSoup


SCHOLAR_PROFILE_URL = "https://scholar.google.com/citations"


def citation_count(text):
    text = (text or "").replace(",", "").strip()
    return int(text) if text.isdigit() else 0


def publication_id_from_href(href):
    if not href:
        return None

    query = parse_qs(urlparse(href).query)
    return query.get("citation_for_view", [None])[0]


def fetch_with_requests(scholar_id):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/126.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }
    params = {
        "user": scholar_id,
        "hl": "en",
        "cstart": "0",
        "pagesize": "100",
    }

    response = requests.get(
        SCHOLAR_PROFILE_URL,
        params=params,
        headers=headers,
        timeout=30,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    name_node = soup.select_one("#gsc_prf_in")
    citation_nodes = soup.select("td.gsc_rsb_std")

    if name_node is None or not citation_nodes:
        raise RuntimeError("Google Scholar profile page did not contain citation data.")

    publications = {}
    for row in soup.select("tr.gsc_a_tr"):
        title_node = row.select_one("a.gsc_a_at")
        cites_node = row.select_one("a.gsc_a_ac")
        if title_node is None:
            continue

        pub_id = publication_id_from_href(title_node.get("href"))
        if not pub_id:
            continue

        publications[pub_id] = {
            "bib": {"title": title_node.get_text(strip=True)},
            "num_citations": citation_count(cites_node.get_text(strip=True) if cites_node else "0"),
        }

    return {
        "name": name_node.get_text(strip=True),
        "citedby": citation_count(citation_nodes[0].get_text(strip=True)),
        "updated": datetime.now(timezone.utc).isoformat(),
        "publications": publications,
        "source": "google-scholar-html",
    }


def fetch_with_scholarly(scholar_id):
    from scholarly import scholarly

    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
    author["updated"] = datetime.now(timezone.utc).isoformat()
    author["publications"] = {
        publication["author_pub_id"]: publication
        for publication in author.get("publications", [])
    }
    author["source"] = "scholarly"
    return author


def write_results(author):
    os.makedirs("results", exist_ok=True)

    with open("results/gs_data.json", "w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False, indent=2)

    shields_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author["citedby"]),
    }
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as outfile:
        json.dump(shields_data, outfile, ensure_ascii=False, indent=2)


def main():
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID")
    if not scholar_id:
        raise RuntimeError("GOOGLE_SCHOLAR_ID is not set.")

    errors = []
    for fetcher in (fetch_with_requests, fetch_with_scholarly):
        try:
            author = fetcher(scholar_id)
            write_results(author)
            print(json.dumps(author, indent=2, ensure_ascii=False))
            return
        except Exception as error:
            errors.append(f"{fetcher.__name__}: {error}")
            print(f"WARNING: {fetcher.__name__} failed: {error}", file=sys.stderr)

    raise RuntimeError("All Google Scholar fetch methods failed. " + " | ".join(errors))


if __name__ == "__main__":
    main()
