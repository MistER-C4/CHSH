#Create the qubit states from IBM

from qiskit import QuantumCircuit

def create_chsh_circuit(angle_a, angle_b):
    """
    Returns a 2-qubit circuit for CHSH measurement.
    
    Args:
        angle_a (float): rotation angle for Alice
        angle_b (float): rotation angle for Bob
    """
    qc = QuantumCircuit(2, 2)
    # Prepare singlet |ψ-> state
    qc.h(0)
    qc.cx(0, 1)
    qc.z(0)  # Optional: adjust to get |ψ->

    # Apply rotations for Alice and Bob
    qc.ry(angle_a, 0)
    qc.ry(angle_b, 1)

    # Measure
    qc.measure([0, 1], [0, 1])
    return qc