import streamlit as st
import pandas as pd
import altair as alt

st.write('''

# DNA Neuclotide Count

Simple DNA nucleotide composition counter fomr DNA sequence

***
''')

st.header("Enter your DNA sequence")
default_sequence_input = '''> DNA Query \n
CGGGCGGCTGACGAGGGACTCACACCGAGAAACTAGACAGTTGCGCGCTGGAAGTAGCGCCGGCTAAGAAAGACGCCTGGTACAGCAGGACTATGAAACCCGTACAAAGGCAACATCCTCACTTCGGTGAATCGAAACGCGGCATCAAGGTTACTTTTTGGATACCTGAAACAAAACCCATCGTAGTCCTTAGACTTGGGACACTTTCACCCCTAGGGCCCATATCTGGAAATAGACGCCAAGTTCAATCCGTACTCCGACGTACGATGGAACAGTGTGGATGTGACGAGCTTCATTTATACCCTTCGCGCGCCGGACCGGGGTCCGCAAGGCGCGGCGGTGCACAAGCAATTGACAACTAACCACCGTGTATTCGTTATGGCACCAGGGAGTTTAAGCCGAGTCAATGGAGCTCGCAATACAGAGTTTACCGCATCTTGCCCTAACTGACAAACTGTGATCGACCACAAGCCAAGCCATTGCCTCTTAGACACGCCGTTACAGTGATTATGAAAACTTTGCGGGGCATGGCTACGACTTGTTCAGCCACGTCCGAGGGCAGAAACCTATCCCCATTTGTATGTTCAGCTATCTTCTACCCATCCCCGGAGGTTAAGTAGGTTGTGAGATGCGGAAGAGGCTCTCGATCATCCCGTGGGACATCAACCTTTCCCTTGATAAAGCACCCCGCTCGGGTATGGCAGAGAGAACGCCTTCTGAATTGTGCTATCCTTCGACCTTATCAAAGCTTGCTACCAATAATTAGGATTATTGCCTTGCGACAGACCTCCTACTCACACTGCCTCACATTGAGCTAGTCAGTGAGCGATTAGCTTGACCCGCTCTCTAGGGTCGCGAGTACGTGAGCTAGGGCTCCGGACTGGGCTATATAGTCGAGTCTGATCTCGCCCCGACAACTGCAAACCTCAACTTTTTTAGATAACATGGTTAGCCGAAGTTGCACGAGGTGCCGACCGCGGACTGCTCCCCGGGTGTGGCT

'''
sequence = st.text_area("Sequence", default_sequence_input, height=520)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write('''***''')

st.header("Output Nucleotide Count")
st.subheader('''1. ATGC count''')


def dna_nucleotide_count(dna_sequence):
    d = dict([
        ('A', dna_sequence.count('A')),
        ('T', dna_sequence.count('T')),
        ('G', dna_sequence.count('G')),
        ('C', dna_sequence.count('C'))
    ])

    return d


X = dna_nucleotide_count(sequence)

X

st.subheader('''2. ATGC Details''')

st.write(f"There are**", str(X['A']), '**adenine(A)')
st.write(f"There are**", str(X['T']), '**thymine(T)')
st.write(f"There are**", str(X['G']), '**adenine(G)')
st.write(f"There are**", str(X['C']), '**adenine(C)')

st.subheader('''3. Visualization''')

df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})

p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(
    width=alt.Step(100)
)
st.write(p)
