import time

class Snowflake:
    def __init__(self, worker_id, epoch=0):
        self.worker_id = worker_id
        self.sequence = 0
        self.last_timestamp = -1
        self.epoch = epoch

        # Bits allocation
        self.timestamp_bits = 41
        self.worker_id_bits = 10
        self.sequence_bits = 12

        # Max values
        self.max_worker_id = -1 ^ (-1 << self.worker_id_bits)
        self.max_sequence = -1 ^ (-1 << self.sequence_bits)

        # Shifts
        self.timestamp_shift = self.worker_id_bits + self.sequence_bits
        self.worker_id_shift = self.sequence_bits

    def _generate_timestamp(self):
        return int((time.time() * 100) - self.epoch)

    def generate_id(self):
        timestamp = self._generate_timestamp()

        if timestamp < self.last_timestamp:
            raise ValueError("Clock moved backwards. Refusing to generate ID.")

        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & self.max_sequence
            if self.sequence == 0:
                timestamp = self.wait_til_next_millis(self.last_timestamp)
        else:
            self.sequence = 0

        self.last_timestamp = timestamp

        snowflake_id = ((timestamp - self.epoch) << self.timestamp_shift) | (self.worker_id << self.worker_id_shift) | self.sequence
        return snowflake_id

    def wait_til_next_millis(self, last_timestamp):
        timestamp = self._generate_timestamp()
        while timestamp <= last_timestamp:
            timestamp = self._generate_timestamp()
        return timestamp


