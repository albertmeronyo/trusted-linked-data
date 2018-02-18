#!/usr/bin/env python

# tld.py: Trusted Linked Data (via IPFS)

import ipfsapi
import rdflib
import sys
import logging

# Local modules
import static

# Set logging format
logging.basicConfig(level=logging.DEBUG, format=static.LOG_FORMAT)
tldlogger = logging.getLogger(__name__)

class IPFSLDPub(object):

    def __init__(self, filename):
        # Connects to local IPFS API
        self._ipfs_api = ipfsapi.connect('127.0.0.1', 5001)

        # Loads rdflib.Graph, chunks, uploads
        self._g = rdflib.Graph()
        self._g.parse(filename, format=rdflib.util.guess_format(filename))
        tldlogger.debug("Loaded document with {} triples".format(len(self._g)))

    def upload_doc(self):
        '''
        Uploads the whole document to IPFS
        Returns the hash of the document
        '''
        return self.upload_graph(self._g)

    def upload_triples(self):
        '''
        Uploads the document by triples to IPFS
        Returns a list of hashes per triple
        '''
        tripleids = []
        for s,p,o in self._g:
            self._f = rdflib.Graph()
            self._f.add((s,p,o))
            print s,p,o
            print len(self._f)
            tripleids.append(self.upload_graph(self._f))

        return tripleids

    def upload_graph(self, graph):
        '''
        Uploads rdflib.Graph to IPFS, returns hash
        '''
        with open('test.nt', 'w') as graphfile:
            graphfile.write(graph.serialize(format='ntriples'))
            res = self._ipfs_api.add('test.n3')
            tldlogger.debug("Added file to IPFS with id {}".format(res['Hash']))

        return res['Hash']

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: {0} <rdf input file> -d|-t".format(sys.argv[0])
        print "-d will upload the whole RDF document to IPFS"
        print "-t will upload individual RDF triples to IPFS"
        exit(2)

    filename = sys.argv[1]
    option = sys.argv[2]
    pub = IPFSLDPub(filename)
    if option == '-d':
        pub.upload_doc()
    elif option == '-t':
        pub.upload_triples()
    else:
        print "Unrecognized option {}".format(option)

    exit(0)
