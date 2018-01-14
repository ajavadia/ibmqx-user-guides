# use QISKit.org
from qiskit import QuantumProgram

# Define the QProgram and the Quantum and Classical Registers
qp = QuantumProgram()
q = qp.create_quantum_register('q', 1)
c = qp.create_classical_register('c', 1)

# Build the circuit
single_q_measurement = qp.create_circuit('single_q_measurement', [q], [c])
single_q_measurement.measure(q, c)
 
# Execute the circuit
result = qp.execute(['single_q_measurement'], backend = 'local_qasm_simulator')

# Print result
print(result.get_counts('single_q_measurement'))