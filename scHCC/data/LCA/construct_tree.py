from treelib import Tree
import xml.etree.ElementTree as ET
from xml.dom import minidom

# 1. Build tree
tree = Tree()

# Root node
tree.create_node("cell", "cell")

# First-level children
tree.create_node("eukaryotic cell", "eukaryotic cell", parent="cell")

# Children of eukaryotic cell
tree.create_node("epithelial cell", "epithelial cell", parent="eukaryotic cell")
tree.create_node("endothelial cell", "endothelial cell", parent="eukaryotic cell")
tree.create_node("mesenchymal cell", "mesenchymal cell", parent="eukaryotic cell")
tree.create_node("hematopoietic cell", "hematopoietic cell", parent="eukaryotic cell")

# Children of epithelial cell
tree.create_node("basal cell", "basal cell", parent="epithelial cell")
tree.create_node("lung multiciliated epithelial cell", "lung multiciliated epithelial cell", parent="epithelial cell")
tree.create_node("ciliated cell", "ciliated cell", parent="epithelial cell")
tree.create_node("club cell", "club cell", parent="epithelial cell")
tree.create_node("lung goblet cell", "lung goblet cell", parent="epithelial cell")
tree.create_node("pulmonary ionocyte", "pulmonary ionocyte", parent="epithelial cell")
tree.create_node("tracheobronchial serous cell", "tracheobronchial serous cell", parent="epithelial cell")
tree.create_node("pulmonary alveolar epithelial cell", "pulmonary alveolar epithelial cell", parent="epithelial cell")
tree.create_node("mesothelial cell of pleura", "mesothelial cell of pleura", parent="epithelial cell")

# Children of pulmonary alveolar epithelial cell
tree.create_node("pulmonary alveolar type 1 cell", "pulmonary alveolar type 1 cell", parent="pulmonary alveolar epithelial cell")
tree.create_node("pulmonary alveolar type 2 cell", "pulmonary alveolar type 2 cell", parent="pulmonary alveolar epithelial cell")

# Children of endothelial cell
tree.create_node("endothelial cell of artery", "endothelial cell of artery", parent="endothelial cell")
tree.create_node("vein endothelial cell", "vein endothelial cell", parent="endothelial cell")
tree.create_node("capillary endothelial cell", "capillary endothelial cell", parent="endothelial cell")
tree.create_node("endothelial cell of lymphatic vessel", "endothelial cell of lymphatic vessel", parent="endothelial cell")

# Children of mesenchymal cell
tree.create_node("fibroblast", "fibroblast", parent="mesenchymal cell")
tree.create_node("pericyte", "pericyte", parent="mesenchymal cell")
tree.create_node("smooth muscle cell", "smooth muscle cell", parent="mesenchymal cell")

# Children of fibroblast
#tree.create_node("myofibroblast cell", "myofibroblast cell", parent="fibroblast")

# Children of smooth muscle cell
tree.create_node("bronchial smooth muscle cell", "bronchial smooth muscle cell", parent="smooth muscle cell")
tree.create_node("vascular associated smooth muscle cell", "vascular associated smooth muscle cell", parent="smooth muscle cell")

# Children of hematopoietic cell
tree.create_node("lymphoid lineage", "lymphoid lineage", parent="hematopoietic cell")
tree.create_node("myeloid lineage", "myeloid lineage", parent="hematopoietic cell")

# Children of lymphoid lineage
tree.create_node("T cell", "T cell", parent="lymphoid lineage")
tree.create_node("B cell", "B cell", parent="lymphoid lineage")
tree.create_node("plasma cell", "plasma cell", parent="lymphoid lineage")
tree.create_node("natural killer cell", "natural killer cell", parent="lymphoid lineage")
tree.create_node("mature NK T cell", "mature NK T cell", parent="lymphoid lineage")

# Children of T cell
tree.create_node("CD4_positive_ alpha_beta T cell", "CD4_positive_ alpha_beta T cell", parent="T cell")
tree.create_node("CD8_positive_ alpha_beta T cell", "CD8_positive_ alpha_beta T cell", parent="T cell")

# Children of CD4_positive_ alpha_beta T cell
#tree.create_node("naive thymus_derived CD4_positive_ alpha_beta T cell", "naive thymus_derived CD4_positive_ alpha_beta T cell", parent="CD4_positive_ alpha_beta T cell")
tree.create_node("effector memory CD4_positive_ alpha_beta T cell", "effector memory CD4_positive_ alpha_beta T cell", parent="CD4_positive_ alpha_beta T cell")

# Children of CD8_positive_ alpha_beta T cell
tree.create_node("naive thymus_derived CD8_positive_ alpha_beta T cell", "naive thymus_derived CD8_positive_ alpha_beta T cell", parent="CD8_positive_ alpha_beta T cell")
tree.create_node("effector memory CD8_positive_ alpha_beta T cell", "effector memory CD8_positive_ alpha_beta T cell", parent="CD8_positive_ alpha_beta T cell")

# Children of myeloid lineage
tree.create_node("monocyte", "monocyte", parent="myeloid lineage")
tree.create_node("macrophage", "macrophage", parent="myeloid lineage")
tree.create_node("dendritic cell", "dendritic cell", parent="myeloid lineage")
tree.create_node("megakaryocyte", "megakaryocyte", parent="myeloid lineage")
tree.create_node("myeloid leukocyte", "myeloid leukocyte", parent="myeloid lineage")

# Children of monocyte
tree.create_node("classical monocyte", "classical monocyte", parent="monocyte")
tree.create_node("intermediate monocyte", "intermediate monocyte", parent="monocyte")
tree.create_node("non_classical monocyte", "non_classical monocyte", parent="monocyte")

# Children of macrophage
#tree.create_node("alveolar macrophage", "alveolar macrophage", parent="macrophage")

# Children of dendritic cell
#tree.create_node("myeloid dendritic cell", "myeloid dendritic cell", parent="dendritic cell")
#tree.create_node("plasmacytoid dendritic cell_ human", "plasmacytoid dendritic cell_ human", parent="dendritic cell")

# Children of myeloid dendritic cell
#tree.create_node("CD1c_positive myeloid dendritic cell", "CD1c_positive myeloid dendritic cell", parent="myeloid dendritic cell")


leaves = sorted([x.tag for x in tree.leaves()])
print(f"Number of leaf nodes: {len(leaves)}")
print("Leaf nodes:", leaves)
with open("leaves.txt", "w", encoding="utf-8") as f:
    for leaf in leaves:
        f.write("'"+leaf+"',")
print("LEAVES file generated: leaves.txt")    
    
print(tree.show(stdout=False))

with open("tree.txt", "w", encoding="utf-8") as f:
    f.write(tree.show(stdout=False))

print("TREE file generated: tree.txt")

template = '    "LCA_wo_CD4-en-{}-synset-0-n": "{}"'
with open("LCA_wo_CD4_id_to_label.json", "w", encoding="utf-8") as f:
    f.write("{\n")
    for i, celltype in enumerate(leaves):
        line = template.format(celltype, celltype)
        if i < len(leaves) - 1:
            line += ","
        f.write(line + "\n")
    f.write("}")
    
print("JSON file generated: LCA_wo_CD4_id_to_label.json")

# 2. Traverse all nodes and store related information for each node (keyed by node identifier)
nodes_info = {}
for node in tree.all_nodes():
    base_name = node.tag
    lexical_id = f"LCA_wo_CD4-en-{base_name}-n"
    sense_id = f"LCA_wo_CD4-en-{base_name}-sense-0-n"
    synset_id = f"LCA_wo_CD4-en-{base_name}-synset-0-n"
    # Store parent node object (None if root)
    parent_node = tree.parent(node.identifier)
    nodes_info[node.identifier] = {
        'base_name': base_name,
        'lexical_id': lexical_id,
        'sense_id': sense_id,
        'synset_id': synset_id,
        'parent': parent_node,          # parent node object (or None)
        'tag': node.tag
    }

# 3. Build XML
# Root element LexicalResource, add namespace attribute
root_elem = ET.Element("LexicalResource", {"xmlns:dc": "https://globalwordnet.github.io/schemas/dc/"})

# Lexicon element
lexicon = ET.SubElement(root_elem, "Lexicon",
    id="LCA_wo_CD4-en",
    label="Wordnet for the LCA_wo_CD4 dataset",
    language="en",
    email="email@email",
    license="https://creativecommons.org/licenses/by/4.0/",
    version="1.0"
)

# First add all LexicalEntry in the order of node list
for node in tree.all_nodes():
    info = nodes_info[node.identifier]
    lex_entry = ET.SubElement(lexicon, "LexicalEntry", id=info['lexical_id'])
    ET.SubElement(lex_entry, "Lemma", writtenForm=info['base_name'], partOfSpeech="n")
    ET.SubElement(lex_entry, "Sense", id=info['sense_id'], synset=info['synset_id'])

# Then add all Synset in the same order (first create all Synset elements)
synset_elements = {}
for node in tree.all_nodes():
    info = nodes_info[node.identifier]
    syn = ET.SubElement(lexicon, "Synset",
        id=info['synset_id'],
        ili="in",
        partOfSpeech="n",
        members=info['sense_id']
    )
    synset_elements[node.identifier] = syn

# Add SynsetRelation for each node
for node in tree.all_nodes():
    node_id = node.identifier
    info = nodes_info[node_id]
    parent_obj = info['parent']
    
    # If parent exists, add hypernym relation
    if parent_obj is not None:
        parent_info = nodes_info[parent_obj.identifier]
        ET.SubElement(synset_elements[node_id], "SynsetRelation",
            relType="hypernym",
            target=parent_info['synset_id']
        )
    
    # Get children, add hyponym relation
    children = tree.children(node_id)
    for child in children:
        child_info = nodes_info[child.identifier]
        ET.SubElement(synset_elements[node_id], "SynsetRelation",
            relType="hyponym",
            target=child_info['synset_id']
        )

# 4. Format output XML (add DOCTYPE and indentation)
def prettify(elem):
    """Convert an ElementTree element to a formatted string and add DOCTYPE"""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    # Do not specify encoding, return unicode string, usually without XML declaration
    pretty_xml = reparsed.toprettyxml(indent="    ")
    lines = pretty_xml.split('\n')
    # Remove any lines starting with '<?xml' (to avoid auto-generated declaration)
    lines = [line for line in lines if not line.strip().startswith('<?xml')]
    # Custom declaration and DOCTYPE
    xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'
    doctype = '<!DOCTYPE LexicalResource SYSTEM "http://globalwordnet.github.io/schemas/WN-LMF-1.1.dtd">'
    # Find root element position and insert declaration and DOCTYPE
    for i, line in enumerate(lines):
        if line.strip().startswith('<LexicalResource'):
            lines.insert(i, xml_declaration)
            lines.insert(i+1, doctype)
            break
    return '\n'.join(lines)

# Output to file
output = prettify(root_elem)
with open("LCA_wo_CD4_tree.xml", "w", encoding="utf-8") as f:
    f.write(output)

print("XML file generated: LCA_wo_CD4_tree.xml")