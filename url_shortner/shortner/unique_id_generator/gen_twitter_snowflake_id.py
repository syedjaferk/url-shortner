import time

class Snowflake:
    def __init__(self, worker_id, epoch=0):
        """        Initialize a Snowflake ID generator.

        Args:
            worker_id (int): The unique identifier for the worker.
            epoch (int?): The epoch timestamp. Defaults to 0.
        """

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
        """        Generate a timestamp based on the current time and epoch.

        Returns:
            int: The generated timestamp.
        """

        return int((time.time() * 100) - self.epoch)

    def generate_id(self):
        """        Generate a unique ID based on the current timestamp and worker ID.

        It first generates a timestamp using the _generate_timestamp method. If the generated timestamp is less than the last timestamp, it raises a ValueError indicating that the clock has moved backwards. If the timestamp is equal to the last timestamp, it increments the sequence number and waits until the next millisecond if the sequence number reaches its maximum value. If the timestamp is different from the last timestamp, it resets the sequence number to 0. Finally, it calculates the snowflake ID using bitwise operations and returns it.

        Returns:
            int: The unique snowflake ID generated based on the current timestamp and worker ID.

        Raises:
            ValueError: If the clock moves backwards.
        """

        timestamp = self._generate_timestamp()

        if timestamp < self.last_timestamp:
            raise ValueError("Clock moved backwards. Refusing to generate ID.")

        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & self.max_sequence
            if self.sequence == 0:
                timestamp = self._wait_til_next_millis(self.last_timestamp)
        else:
            self.sequence = 0

        self.last_timestamp = timestamp

        snowflake_id = ((timestamp - self.epoch) << self.timestamp_shift) | (self.worker_id << self.worker_id_shift) | self.sequence
        return snowflake_id

    def _wait_til_next_millis(self, last_timestamp):
        """        Waits until the next millisecond and returns the timestamp.

        This method generates a new timestamp and compares it with the last timestamp. If the new timestamp is less than or equal to the last timestamp, it continues generating new timestamps until it finds one greater than the last timestamp.

        Args:
            last_timestamp (int): The last timestamp obtained.

        Returns:
            int: The new timestamp that is greater than the last timestamp.
        """

        timestamp = self._generate_timestamp()
        while timestamp <= last_timestamp:
            timestamp = self._generate_timestamp()
        return timestamp


