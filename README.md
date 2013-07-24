To update the wikidata item for a particular Entrez ids:

    :::python
	from pygenewiki import proteinboxbot
	pbb = proteinboxbot.ProteinBoxBot()
	#updates wikidata gene page with Entrez id 1017 
	pbb.run([1017])
