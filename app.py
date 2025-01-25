import streamlit as st
from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs

# Título de la aplicación
st.title("Comparador de Moléculas usando el Índice de Tanimoto")
st.markdown(
    """
    Ingrese dos moléculas en formato **SMILES** para calcular el índice de similitud de Tanimoto.
    Este índice mide la similitud estructural entre las dos moléculas.
    """
)

# Entrada: SMILES para la primera molécula
smiles1 = st.text_input("Ingrese el SMILES de la primera molécula", value="CCO")
# Entrada: SMILES para la segunda molécula
smiles2 = st.text_input("Ingrese el SMILES de la segunda molécula", value="CCN")

# Verificar que ambos SMILES sean válidos
if st.button("Calcular Índice de Tanimoto"):
    try:
        # Convertir SMILES a moléculas RDKit
        mol1 = Chem.MolFromSmiles(smiles1)
        mol2 = Chem.MolFromSmiles(smiles2)

        if mol1 is None or mol2 is None:
            st.error("Uno o ambos SMILES ingresados no son válidos.")
        else:
            # Calcular huellas moleculares (fingerprints)
            fp1 = AllChem.GetMorganFingerprintAsBitVect(mol1, radius=2, nBits=2048)
            fp2 = AllChem.GetMorganFingerprintAsBitVect(mol2, radius=2, nBits=2048)

            # Calcular índice de Tanimoto
            tanimoto_index = DataStructs.TanimotoSimilarity(fp1, fp2)

            # Mostrar el resultado
            st.success(f"Índice de Tanimoto: {tanimoto_index:.4f}")

    except Exception as e:
        st.error(f"Error procesando las moléculas: {e}")
