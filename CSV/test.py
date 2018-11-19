import json
import requests
import mwparserfromhell

"""sample code"""

base_url = 'https://bots.snpedia.com/api.php'
sesh = requests.session()

def query(search):
    params = {
        'format':'json',
        'action':'query',
        'prop':'revisions',
        'rvprop':'content',
        'titles':search
    }
    res = sesh.get(base_url, params=params).json()

    pages = res["query"]["pages"]
    text = list(pages.values())[0]["revisions"][0]["*"]

    wikicode = mwparserfromhell.parse(text)
    return wikicode

def get_genos(rsid):
    wikicode = query(rsid)
    genos = ['geno1', 'geno2', 'geno3']
    template = wikicode.filter_templates()[0]

    genes_list = []
    for geno in genos:
        gene = template.get(geno).value.strip()
        genes_list.append(gene)
        print (query(rsid+gene))

    return genes_list

# """end sample code"""
#
#
# """instructions: """
#
# 1. query base page with specified rsid as title var (ex: https://bots.snpedia.com/api.php?format=json&action=query&prop=revisions&rvprop=content&titles=rs144848)
# 2. find all genos in page (ex: (A;A) within geno1, geno2, etc.)
# 3. new query with each geno (https://bots.snpedia.com/api.php?format=json&action=query&prop=revisions&rvprop=content&titles=rs144848(A;A))
# 4. the function (or class) should create a new json with all geno variations appended with these keys:
#
# {
# 	"gene": "BRCA1",
# 	"rsid": "rs144848",
#     "CLNDBN":"Breast-ovarian cancer, familial 1 not provided Hereditary breast and ovarian cancer syndrome not specified Hereditary cancer-predisposing syndrome Familial cancer of breast",
# 	"genes": [{
# 			"gene": "(A;A)",
# 			"magnitude": 1,
# 			"repute": "Good",
#             "summary": "lorem"
# 		},
# 		{
# 			"gene": "(A;B)",
# 			"magnitude": 2,
# 			"repute": "Bad",
#             "summary": "lorem"
# 		}
# 	]
# }