# trusted-linked-data
Awesomeness

## Requirements

You need a local IPFS daemon running. [Install IPFS on your platform](https://ipfs.io/docs/install/), then just run `ipfs daemon` from your terminal.

## Usage

Clone anywhere, cd in there, and

<pre>
virtualenv .
source bin/activate
pip install -r requirements.txt
cd src
python tld.py rdf input file> -d|-t
</pre>

**-d** will upload the whole RDF document to IPFS
**-t** will upload individual RDF triples to IPFS

## Random notes

- [IPFS](https://en.wikipedia.org/wiki/InterPlanetary_File_System) + Tobias TrustyURI blah = TRUSTED LINKED DATA (this will be a seal of approval)
- Embed trust in HTTP headers of request and response. You can ask for verification and get a status code that tells you if it’s verified!
- Eval: measure performance, threshold of how much you need to put into the IPFS to have “enough” trust
- Consider: protocol of requests, you don't want the last one coming from the server

So need the following:
- 2 use cases: publish Linked Data on ipfs, and retrieve *trusted* Linked Data from ipfs
- Publishing
  - You can publish a URI, a triple, or an RDF document
  - When you do, you get an IPFS link (hash) identifying the URI? Triple? Document?
  - Mapping between ipfs links and http links?
- Retrieving

## TODO
- [] Read on conceptual, basic functioning of [IPFS](https://en.wikipedia.org/wiki/InterPlanetary_File_System)
- [] Check out the [Python](https://github.com/ipfs/py-ipfs), [JS](https://github.com/ipfs/js-ipfs) and [Go](https://github.com/ipfs/go-ipfs) (most mature) implementations
- [] Idea is to build either a wrapper around [rdflib](https://github.com/RDFLib/rdflib), or use the JSON helper functions to get JSON-LD into IPFS
