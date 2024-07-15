import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, student_id, certificate_id, course_name, grade, hash, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.student_id = student_id
        self.certificate_id = certificate_id
        self.course_name = course_name
        self.grade = grade
        self.hash = hash
        self.nonce = nonce

class CertificateBlockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Create the first block (genesis block)
        genesis_block = Block(
            0, "0", int(time.time()), "GenesisStudent", "GenesisCertificate", "GenesisCourse", "A",
            self.calculate_hash(0, "0", int(time.time()), "GenesisStudent", "GenesisCertificate", "GenesisCourse", "A", 0), 0
        )
        self.chain.append(genesis_block)

    def add_certificate(self, student_id, certificate_id, course_name, grade):
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = int(time.time())
        previous_hash = previous_block.hash
        nonce = self.proof_of_work(index, previous_hash, timestamp, student_id, certificate_id, course_name, grade)
        new_hash = self.calculate_hash(index, previous_hash, timestamp, student_id, certificate_id, course_name, grade, nonce)
        new_block = Block(index, previous_hash, timestamp, student_id, certificate_id, course_name, grade, new_hash, nonce)
        self.chain.append(new_block)

    def proof_of_work(self, index, previous_hash, timestamp, student_id, certificate_id, course_name, grade):
        nonce = 0
        while True:
            new_hash = self.calculate_hash(index, previous_hash, timestamp, student_id, certificate_id, course_name, grade, nonce)
            if new_hash[:4] == "0000":
                return nonce
            nonce += 1

    def calculate_hash(self, index, previous_hash, timestamp, student_id, certificate_id, course_name, grade, nonce):
        value = str(index) + str(previous_hash) + str(timestamp) + str(student_id) + str(certificate_id) + str(course_name) + str(grade) + str(nonce)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def print_chain(self):
        for block in self.chain:
            print(vars(block))

if __name__ == '__main__':
    certificate_blockchain = CertificateBlockchain()
    certificate_blockchain.add_certificate("Student_1", "Cert_1", "Math 101", "A")
    certificate_blockchain.add_certificate("Student_2", "Cert_2", "Physics 101", "B+")
    certificate_blockchain.add_certificate("Student_3", "Cert_3", "Chemistry 101", "A-")
    certificate_blockchain.print_chain()
