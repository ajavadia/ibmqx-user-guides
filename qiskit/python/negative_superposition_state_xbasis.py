# use QISKit.org
from qiskit import QuantumProgram

# Define the QProgram and the Quantum and Classical Registers
qp = QuantumProgram()
q = qp.create_quantum_register('q', 1)
c = qp.create_classical_register('c', 1)

# Build the circuit
negative_superposition_state_xbasis = qp.create_circuit('negative_superposition_state_xbasis', [q], [c])
negative_superposition_state_xbasis.x(q)
negative_superposition_state_xbasis.h(q)
negative_superposition_state_xbasis.barrier()
negative_superposition_state_xbasis.h(q)
negative_superposition_state_xbasis.measure(q, c)

# Execute the circuit
result = qp.execute(['negative_superposition_state_xbasis'], backend = 'local_qasm_simulator')

# Print result
print(result.get_counts('negative_superposition_state_xbasis'))