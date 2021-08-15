from chembl_webresource_client.new_client import new_client
with Chem.SDMolSupplier('aspirin.sdf') as suppl:
  ms = [x for x in suppl if x is not None]
 for m in ms: tmp=AllChem.Compute2DCoords(m)
 from rdkit.Chem import Draw
 Draw.MolToFile(ms[0],'images/aspirin_mol1.o.png')
 Draw.MolToFile(ms[1],'images/aspirin_mol2.o.png')