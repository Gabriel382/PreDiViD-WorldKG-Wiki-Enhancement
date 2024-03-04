## OpenStreetMap Knowledge Graph

This project aims to build a Knowledge Graph (KG) based on OpenStreetMap (OSM) data,
 leveraging the principles, ontology and data from the World Knowledge Graph project (https://www.worldkg.org/). By utilizing the planet_osm.ttl dataset 
from osm2rdf.cs.uni-freiburg.de, we create a comprehensive graph representing entities and their relationships 
within OpenStreetMap.


## Dataset

The primary input for this project is the planet_osm.ttl file, which contains RDF triples representing OSM data.
 This file serves as the foundation for constructing the knowledge graph.
Processing

The pytranslate.py script is employed to filter entities from planet_osm.ttl and convert them into a new RDF file, 
nplanet_osm.ttl. This step ensures that only relevant entities are considered for inclusion in the knowledge graph.

## Enrichment with WikiData

To enhance the knowledge graph further, the WikiDataLink.ipynb Jupyter notebook is utilized. This notebook incorporates WikiData links between entities extracted from nplanet_osm.ttl, augmenting the graph's richness and context.
Outputs

Upon processing, the project generates two crucial outputs:

    Nodes CSV: This file contains information about the nodes within the knowledge graph, including their identifiers, types, and additional attributes.
    Edges CSV: The edges CSV file represents the relationships between nodes in the knowledge graph, specifying the source, target, and type of each edge.

Usage

To replicate this project, follow these steps:

    Download the planet ttl file from https://osm2rdf.cs.uni-freiburg.de/
    Run pytranslate.py to filter and convert the OSM entities into nplanet_osm.ttl.
    Execute WikiDataLink.ipynb to enrich nplanet_osm.ttl with WikiData links and generate the nodes and edges CSV files.

Contribution

Contributions to this project are welcome! Feel free to submit pull requests, report issues, or suggest enhancements to improve the functionality and usability of the OpenStreetMap Knowledge Graph.
License

This project is licensed under the MIT License. See the LICENSE file for details.

