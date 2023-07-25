"""
Prompt to run qa (English). Replace the text and question and play around!
"""
prompt = """### Instruction:
What type of star is HR 7484? If there's no answer, say "NO_ANSWER_IN_TEXT". 

### Input:
Text: HR 7484 is a detached eclipsing binary, which means the orbital plane is aligned close to the line-of-sight from the Earth, causing the components to eclipse twice per orbit. The system is undergoing apsidal motion, with a rate greater than that predicted by general relativity. Both components are ordinary F-type main-sequence stars with similar physical properties. The star normally has an apparent magnitude of 5.89, but every 7.64 days (7 days, 15 hours, and 22 minutes) its brightness decreases to magnitude 6.37, approximately two thirds as bright.  Five days and 17 hours after each primary eclipse, there is a secondary eclipse when the brightness drops to magnitude 6.06, about 85% of the normal brightness. Each eclipse lasts for 220 minutes.  Both eclipses are partial.

Question: What type of star is HR 7484?

### Response:"""

settings = {
    "maximum_tokens": 128
}

model = "luminous-supreme-control"