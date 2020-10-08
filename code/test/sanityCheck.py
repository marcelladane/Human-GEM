# -*- coding: utf-8 -*-

"""Test functions"""

import json
import cobra


def load_yml(yml_file):
    """
    import yml model file, and output rxn and met lists
    """
    model = cobra.io.load_yaml_model(yml_file)

    # get lists of rxns, mets and genes
    modelRxns  = list(map(lambda element : element.id, model.reactions))
    modelMets  = list(map(lambda element : element.id, model.metabolites))
    modelGenes = list(map(lambda element : element.id, model.genes))

    return modelRxns, modelMets, modelGenes


def checkRxnAnnotation(rxns):
    """
    check consistency of rxn lists between model and annoation file
    """
    rxnJsonFile = "data/annotation/humanGEMRxnAssoc.JSON"
    with open(rxnJsonFile) as rxnJson:
        rxnAssoc = json.load(rxnJson)
    rxnList = rxnAssoc.get('rxns', None)
    assert rxnList == rxns, "Reaction annoation mismatch!"


def checkMetAnnotation(mets):
    """
    check consistency of met lists between model and annoation file
    """
    metJsonFile = "data/annotation/humanGEMMetAssoc.JSON"
    with open(metJsonFile) as metJson:
        metAssoc = json.load(metJson)
    metList = metAssoc.get('mets', None)
    assert metList == mets, "Metabolite annoation mismatch!"


def checkGeneAnnotation(genes):
    """
    check consistency of gene lists between model and annoation file
    """
    geneJsonFile = "data/annotation/humanGEMGeneAssoc.JSON"
    with open(geneJsonFile) as geneJson:
        geneAssoc = json.load(geneJson)
    geneList = geneAssoc.get('genes', None)
    assert geneList == genes, "Gene annoation mismatch!"


if __name__ == "__main__":
    rxns, mets, genes = load_yml("model/Human-GEM.yml")
    checkRxnAnnotation(rxns)
    checkMetAnnotation(mets)
    checkGeneAnnotation(genes)
    print("Everything passed")
