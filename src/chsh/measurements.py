#Code for measuring in different base
from qiskit_aer import Aer
from qiskit import execute

def run_circuit(qc, shots=1024, backend_name="qasm_simulator"):
    backend = Aer.get_backend(backend_name)
    result = execute(qc, backend, shots=shots).result()
    counts = result.get_counts()
    return counts