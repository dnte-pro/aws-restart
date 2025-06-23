#store the human prepoinsulin sequence in a a variable called preproinsulin
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
                "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
                
#store the remaining sequence elements of human insulin in variables

IsInsulin = "malwmrllpllallalwgpdpaaa"

bInsulin = 	"fvnqhlcgshlvealylvcgergffytpkt"

aInsulin = "giveqcctsicslyqlenycn"

cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin

#Printing "the sequence of human insulin" to console using successive print() commands:

print("The sequenceof human preproinsulin:")
print(preproInsulin)

#Printing to console using concatenated strings inside the print function (one-liner)
print("The sequence of huan insulin, chain a:" + aInsulin)