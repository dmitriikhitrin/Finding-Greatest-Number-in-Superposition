# Finding-Greatest-Number-in-Superposition

The goal of this project is to find a unitary matrix that can collapse the superposition of basis states $\frac{1}{\sqrt{N}}\sum_i\ket{i}$ into the state representing the greatest number. For example, if $\ket{\psi}=\frac{1}{\sqrt{2}}(\ket{01}+\ket{10})$, we want to find $U$ such that $U\ket{\psi} \mapsto \ket{10}$ (because 2>1🤯).

## Theory 
Because the columns of unitaries form the orthonormal set, it is impossible to find the perfect mapping. So, the application of $U$ (which I call mtrx in the examples notebook) will create some additional states that were not initially in the superposition.

## Examples

See the attached Examples notebook to see such a transformation for a 2-qubit case. According to our goal, mtrx should ideally perform the following mappings: <br />

$MTRX\frac{1}{\sqrt{2}}(\ket{00}+\ket{01}) \mapsto \ket{01}$ <br />
$MTRX\frac{1}{\sqrt{2}}(\ket{00}+\ket{10}) \mapsto \ket{10}$ <br />
$MTRX\frac{1}{\sqrt{2}}(\ket{00}+\ket{11}) \mapsto \ket{11}$ <br />
$MTRX\frac{1}{\sqrt{3}}(\ket{00}+\ket{01} +\ket{10}) \mapsto \ket{10}$ <br />
... I hope you got the idea ... <br />
$MTRX\frac{1}{2}(\ket{00}+\ket{01}+\ket{10}+\ket{11}) \mapsto \ket{11}$ <br />

I found MTRX through gradient decent starting from a random 4x4 matrix (see Getting-Unitary.py)
