from treelib import Tree
import xml.etree.ElementTree as ET
from xml.dom import minidom

from treelib import Tree

tree = Tree()

# root
tree.create_node("cell", "cell")

# ========== Level 1: Main branches. ==========
#tree.create_node("Progenitor cells", "Progenitor cells", parent="cell")
#tree.create_node("Cycling/proliferating cells (non-lymphoid)", "Cycling/proliferating cells (non-lymphoid)", parent="cell")
#tree.create_node("Erythro-megakaryocytic lineage", "Erythro-megakaryocytic lineage", parent="cell")
tree.create_node("Myeloid lineage", "Myeloid lineage", parent="cell")
tree.create_node("Lymphoid lineage", "Lymphoid lineage", parent="cell")
tree.create_node("Doublets / multiplets", "Doublets / multiplets", parent="cell")

# ========== Progenitor cells ==========
#tree.create_node("Progenitor", "Progenitor", parent="Progenitor cells")

# ========== Cycling/proliferating cells (non-lymphoid) ==========
#tree.create_node("Cycling", "Cycling", parent="Cycling/proliferating cells (non-lymphoid)")

# ========== Erythro-megakaryocytic lineage ==========
#tree.create_node("Erythroid", "Erythroid", parent="Erythro-megakaryocytic lineage")
#tree.create_node("Megakaryocytes", "Megakaryocytes", parent="Erythro-megakaryocytic lineage")

# ========== Myeloid lineage ==========
tree.create_node("Monocytes", "Monocytes", parent="Myeloid lineage")
tree.create_node("Classical monocytes", "Classical monocytes", parent="Monocytes")
tree.create_node("Nonclassical monocytes", "Nonclassical monocytes", parent="Monocytes")

tree.create_node("Macrophages", "Macrophages", parent="Myeloid lineage")
tree.create_node("Intermediate macrophages", "Intermediate macrophages", parent="Macrophages")
tree.create_node("Alveolar macrophages", "Alveolar macrophages", parent="Macrophages")
tree.create_node("Intestinal macrophages", "Intestinal macrophages", parent="Macrophages")
tree.create_node("Erythrophagocytic macrophages", "Erythrophagocytic macrophages", parent="Macrophages")

# tree.create_node("Dendritic cells", "Dendritic cells", parent="Myeloid lineage")
# tree.create_node("DC1", "DC1", parent="Dendritic cells")
# tree.create_node("DC2", "DC2", parent="Dendritic cells")
# tree.create_node("pDC", "pDC", parent="Dendritic cells")
# tree.create_node("migDC", "migDC", parent="Dendritic cells")

tree.create_node("Mast cells", "Mast cells", parent="Myeloid lineage")

# ========== Lymphoid lineage ==========
tree.create_node("B cell lineage", "B cell lineage", parent="Lymphoid lineage")
#tree.create_node("Pro-B", "Pro-B", parent="B cell lineage")
#tree.create_node("Pre-B", "Pre-B", parent="B cell lineage")
tree.create_node("Naive B cells", "Naive B cells", parent="B cell lineage")
#tree.create_node("GC_B (I)", "GC_B (I)", parent="B cell lineage")
#tree.create_node("GC_B (II)", "GC_B (II)", parent="B cell lineage")
tree.create_node("Memory B cells", "Memory B cells", parent="B cell lineage")
tree.create_node("Plasmablasts", "Plasmablasts", parent="B cell lineage")
tree.create_node("Plasma cells", "Plasma cells", parent="B cell lineage")
tree.create_node("ABCs", "ABCs", parent="B cell lineage")

tree.create_node("T cell lineage", "T cell lineage", parent="Lymphoid lineage")
tree.create_node("T_CD4/CD8", "T_CD4/CD8", parent="T cell lineage")

tree.create_node("CD4+ T cells", "CD4+ T cells", parent="T cell lineage")
tree.create_node("Tnaive/CM_CD4", "Tnaive/CM_CD4", parent="CD4+ T cells")
tree.create_node("Tnaive/CM_CD4_activated", "Tnaive/CM_CD4_activated", parent="CD4+ T cells")
tree.create_node("Teffector/EM_CD4", "Teffector/EM_CD4", parent="CD4+ T cells")
tree.create_node("Trm_Th1/Th17", "Trm_Th1/Th17", parent="CD4+ T cells")
tree.create_node("Tregs", "Tregs", parent="CD4+ T cells")
tree.create_node("Tfh", "Tfh", parent="CD4+ T cells")

tree.create_node("CD8+ T cells", "CD8+ T cells", parent="T cell lineage")
tree.create_node("Tnaive/CM_CD8", "Tnaive/CM_CD8", parent="CD8+ T cells")
tree.create_node("Tem/emra_CD8", "Tem/emra_CD8", parent="CD8+ T cells")
tree.create_node("Trm/em_CD8", "Trm/em_CD8", parent="CD8+ T cells")
tree.create_node("Trm_gut_CD8", "Trm_gut_CD8", parent="CD8+ T cells")

tree.create_node("Other T cells", "Other T cells", parent="T cell lineage")
tree.create_node("MAIT", "MAIT", parent="Other T cells")
tree.create_node("Tgd_CRTAM+", "Tgd_CRTAM+", parent="Other T cells")
tree.create_node("Trm_Tgd", "Trm_Tgd", parent="Other T cells")

tree.create_node("Natural Killer cells", "Natural Killer cells", parent="Lymphoid lineage")
tree.create_node("NK_CD16+", "NK_CD16+", parent="Natural Killer cells")
tree.create_node("NK_CD56bright_CD16-", "NK_CD56bright_CD16-", parent="Natural Killer cells")

#tree.create_node("Innate lymphoid cells (non-NK)", "Innate lymphoid cells (non-NK)", parent="Lymphoid lineage")
#tree.create_node("ILC3", "ILC3", parent="Innate lymphoid cells (non-NK)")

#tree.create_node("Proliferating lymphoid cells", "Proliferating lymphoid cells", parent="Lymphoid lineage")
#tree.create_node("Cycling T&NK", "Cycling T&NK", parent="Proliferating lymphoid cells")

# ========== Doublets / multiplets ==========
tree.create_node("MNP/B doublets", "MNP/B doublets", parent="Doublets / multiplets")
tree.create_node("MNP/T doublets", "MNP/T doublets", parent="Doublets / multiplets")
tree.create_node("T/B doublets", "T/B doublets", parent="Doublets / multiplets")


leaves = sorted([x.tag for x in tree.leaves()])
print(f"Number of leaves: {len(leaves)}")
print("Leaves:", leaves)
with open("leaves.txt", "w", encoding="utf-8") as f:
    for leaf in leaves:
        f.write("'"+leaf+"',")
print("LEAVES file: leaves.txt")    
    
print(tree.show(stdout=False))

with open("tree.txt", "w", encoding="utf-8") as f:
    f.write(tree.show(stdout=False))

print("TREE file: tree.txt")

template = '    "CICA-en-{}-synset-0-n": "{}"'
with open("CICA_id_to_label.json", "w", encoding="utf-8") as f:
    f.write("{\n")
    for i, celltype in enumerate(leaves):
        line = template.format(celltype, celltype)
        if i < len(leaves) - 1:
            line += ","
        f.write(line + "\n")
    f.write("}")
    
print("JSON file: CICA_id_to_label.json")


nodes_info = {}
for node in tree.all_nodes():
    base_name = node.tag
    lexical_id = f"CICA-en-{base_name}-n"
    sense_id = f"CICA-en-{base_name}-sense-0-n"
    synset_id = f"CICA-en-{base_name}-synset-0-n"
    parent_node = tree.parent(node.identifier)
    nodes_info[node.identifier] = {
        'base_name': base_name,
        'lexical_id': lexical_id,
        'sense_id': sense_id,
        'synset_id': synset_id,
        'parent': parent_node,
        'tag': node.tag
    }


root_elem = ET.Element("LexicalResource", {"xmlns:dc": "https://globalwordnet.github.io/schemas/dc/"})
lexicon = ET.SubElement(root_elem, "Lexicon",
    id="CICA-en",
    label="Wordnet for the CICA dataset",
    language="en",
    email="email@email",
    license="https://creativecommons.org/licenses/by/4.0/",
    version="1.0"
)


for node in tree.all_nodes():
    info = nodes_info[node.identifier]
    lex_entry = ET.SubElement(lexicon, "LexicalEntry", id=info['lexical_id'])
    ET.SubElement(lex_entry, "Lemma", writtenForm=info['base_name'], partOfSpeech="n")
    ET.SubElement(lex_entry, "Sense", id=info['sense_id'], synset=info['synset_id'])

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

for node in tree.all_nodes():
    node_id = node.identifier
    info = nodes_info[node_id]
    parent_obj = info['parent']

    if parent_obj is not None:
        parent_info = nodes_info[parent_obj.identifier]
        ET.SubElement(synset_elements[node_id], "SynsetRelation",
            relType="hypernym",
            target=parent_info['synset_id']
        )

    children = tree.children(node_id)
    for child in children:
        child_info = nodes_info[child.identifier]
        ET.SubElement(synset_elements[node_id], "SynsetRelation",
            relType="hyponym",
            target=child_info['synset_id']
        )

def prettify(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="    ")
    lines = pretty_xml.split('\n')
    lines = [line for line in lines if not line.strip().startswith('<?xml')]
    xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'
    doctype = '<!DOCTYPE LexicalResource SYSTEM "http://globalwordnet.github.io/schemas/WN-LMF-1.1.dtd">'
    for i, line in enumerate(lines):
        if line.strip().startswith('<LexicalResource'):
            lines.insert(i, xml_declaration)
            lines.insert(i+1, doctype)
            break
    return '\n'.join(lines)

output = prettify(root_elem)
with open("CICA_tree.xml", "w", encoding="utf-8") as f:
    f.write(output)

print("XML file: CICA_tree.xml")